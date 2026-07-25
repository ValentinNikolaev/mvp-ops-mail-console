#!/usr/bin/env python3
"""GitHub Actions runner for the market-signal monitor.

Collection is deterministic; acceptance and prose are delegated to the OpenAI
Responses API. The model can only write allowed research outputs and its JSON
payload is validated before it reaches the working tree.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "research/config/signal-sources.json"
INBOX = ROOT / "research/.automation"
ALLOWED = (
    "research/signals/", "research/comments/", "research/digests/daily/",
    "research/logs/", "research/state/", "research/mvp-iterations/",
    "research/product-specs/",
)


def get(url: str, timeout: int = 30) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "OpsMailConsoleResearchBot/1.0"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def rss_items(source: dict, config: dict) -> list[dict]:
    terms = config["global"]["keywordClusters"][0]["terms"]
    query = f'{source["siteScope"]} {terms}'
    feed = get("https://www.bing.com/search?format=rss&q=" + urllib.parse.quote_plus(query))
    root = ET.fromstring(feed)
    items = []
    for item in root.findall(".//item")[:config["global"]["maxItemsPerQuery"]]:
        items.append({
            "title": item.findtext("title", default=""),
            "url": item.findtext("link", default=""),
            "published": item.findtext("pubDate", default=""),
            "snippet": item.findtext("description", default=""),
        })
    return items


def hn_items(config: dict) -> list[dict]:
    query = "email deliverability spam reputation"
    payload = json.loads(get("https://hn.algolia.com/api/v1/search_by_date?" + urllib.parse.urlencode({"query": query, "tags": "story", "hitsPerPage": 6})))
    return [{"title": h.get("title") or "", "url": h.get("url") or f'https://news.ycombinator.com/item?id={h["objectID"]}', "published": h.get("created_at", ""), "snippet": h.get("story_text") or ""} for h in payload["hits"]]


def stackexchange_items(config: dict) -> list[dict]:
    url = "https://api.stackexchange.com/2.3/questions?" + urllib.parse.urlencode({"site": "serverfault", "order": "desc", "sort": "creation", "tagged": "email;spam", "pagesize": 6, "filter": "withbody"})
    payload = json.loads(get(url))
    return [{"title": h["title"], "url": h["link"], "published": datetime.fromtimestamp(h["creation_date"], timezone.utc).isoformat(), "snippet": h.get("body", "")} for h in payload["items"]]


def collect() -> Path:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    results, failures = [], []
    for source in config["sources"]:
        try:
            if source["kind"] == "hn-algolia":
                items = hn_items(config)
            elif source["kind"] == "stackexchange-api":
                items = stackexchange_items(config)
            else:
                items = rss_items(source, config)
            results.append({"source": source["name"], "slug": source["slug"], "items": items})
        except Exception as exc:  # a source failure must not stop the pass
            failures.append({"source": source["name"], "error": str(exc)})
    INBOX.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    path = INBOX / f"candidates-{now:%Y%m%dT%H%M%SZ}.json"
    path.write_text(json.dumps({"generated_at": now.isoformat(), "results": results, "failures": failures}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(path.relative_to(ROOT))
    return path


def read_context(candidates: Path) -> str:
    def read(path: str, limit: int = 60000) -> str:
        return (ROOT / path).read_text(encoding="utf-8")[:limit]
    signals = "\n".join(sorted(p.name + "\n" + p.read_text(encoding="utf-8")[:500] for p in (ROOT / "research/signals").glob("*.md")))
    return "\n\n".join([
        "PIPELINE:\n" + read("scripts/run-market-signal-pipeline.codex.md"),
        "WRITE RULES:\n" + read("research/config/write-rules.md"),
        "SIGNAL TEMPLATE:\n" + read("research/config/signal-template.md"),
        "DIGEST TEMPLATE:\n" + read("research/config/digest-template.md"),
        "EXISTING SIGNAL INDEX:\n" + signals[:60000],
        "COMMENT REGISTRY:\n" + read("research/state/comment-source-registry.yaml"),
        "CANDIDATES:\n" + candidates.read_text(encoding="utf-8")[:100000],
    ])


def output_text(response: dict) -> str:
    for item in response.get("output", []):
        for content in item.get("content", []):
            if content.get("type") == "output_text":
                return content["text"]
    raise RuntimeError("Responses API returned no output_text")


def review(candidates: Path) -> list[dict]:
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OPENAI_API_KEY is required for the review step")
    prompt = """Review the supplied market-signal research material. Return ONLY JSON with this schema:
{"files":[{"path":"research/...","content":"complete UTF-8 file content"}],"summary":"short run summary"}.
Apply every pipeline and write rule exactly. Preserve all existing content unless a material update is justified. Create a run log every run. Never edit configs/templates, source code, GitHub files, or any path outside the allowed research output folders. If comment text/counts were not actually available in candidates, record a retry state rather than inventing them. Write zero signal files when evidence is not distinct. JSON must be valid and contain no Markdown fence."""
    payload = {"model": os.environ.get("OPENAI_MODEL", "gpt-5.6-terra"), "input": [{"role": "system", "content": prompt}, {"role": "user", "content": read_context(candidates)}], "text": {"verbosity": "medium"}}
    request = urllib.request.Request("https://api.openai.com/v1/responses", data=json.dumps(payload).encode(), headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(request, timeout=240) as response:
        data = json.loads(response.read().decode())
    return json.loads(output_text(data))["files"]


def apply(files: list[dict]) -> None:
    for item in files:
        path, content = item.get("path", ""), item.get("content", "")
        if not isinstance(content, str) or not path.startswith(ALLOWED) or ".." in Path(path).parts:
            raise RuntimeError(f"refusing model output path: {path!r}")
        target = ROOT / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content.rstrip() + "\n", encoding="utf-8")
        print(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("collect", "review"))
    parser.add_argument("--candidates", type=Path)
    args = parser.parse_args()
    if args.command == "collect":
        collect()
        return
    if not args.candidates:
        raise SystemExit("review requires --candidates")
    apply(review(args.candidates))


if __name__ == "__main__":
    main()
