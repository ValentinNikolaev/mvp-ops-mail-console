#!/usr/bin/env python3
"""Python-only GitHub Actions collector for the market-signal monitor."""
from __future__ import annotations

import argparse
import json
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
    existing_urls = set(re.findall(r'^url:\s*"?([^"\n]+)', "\n".join(p.read_text(encoding="utf-8") for p in (ROOT / "research/signals").glob("*.md")), re.MULTILINE))
    positive = re.compile("|".join(re.escape(x) for x in config["global"]["positivePatterns"]), re.I)
    excluded = re.compile("|".join(re.escape(x) for x in config["global"]["excludePatterns"]), re.I)
    results, failures, seen = [], [], set()
    for source in config["sources"]:
        try:
            if source["kind"] == "hn-algolia":
                items = hn_items(config)
            elif source["kind"] == "stackexchange-api":
                items = stackexchange_items(config)
            else:
                items = rss_items(source, config)
            candidates = []
            for item in items:
                url = item["url"].split("#", 1)[0].rstrip("/")
                text = f'{item["title"]} {item["snippet"]}'
                if not url or url in seen or url in existing_urls or excluded.search(text) or not positive.search(text):
                    continue
                seen.add(url)
                item["url"] = url
                item["match_terms"] = sorted(set(m.group(0).lower() for m in positive.finditer(text)))
                candidates.append(item)
            results.append({"source": source["name"], "slug": source["slug"], "items": candidates})
        except Exception as exc:  # a source failure must not stop the pass
            failures.append({"source": source["name"], "error": str(exc)})
    INBOX.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    path = INBOX / f"candidates-{now:%Y%m%dT%H%M%SZ}.json"
    path.write_text(json.dumps({"generated_at": now.isoformat(), "results": results, "failures": failures, "automation": {"mode": "collection-only", "note": "Candidates are ranked/deduplicated by deterministic rules. They are not accepted signals until a reviewer verifies thread and comment evidence."}}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(path.relative_to(ROOT))
    return path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("collect",))
    args = parser.parse_args()
    collect()


if __name__ == "__main__":
    main()
