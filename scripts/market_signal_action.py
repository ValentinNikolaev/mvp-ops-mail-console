#!/usr/bin/env python3
"""Python-only GitHub Actions collector for the market-signal monitor."""
from __future__ import annotations

import argparse
import html
import json
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "research/config/signal-sources.json"
INBOX = ROOT / "research/.automation"
CANDIDATES = ROOT / "research/candidates"
COMMENTS = ROOT / "research/comments"
COMMENT_REGISTRY = ROOT / "research/state/comment-source-registry.yaml"


def get(url: str, timeout: int = 30) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "OpsMailConsoleResearchBot/1.0"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def normalize_url(url: str) -> str:
    """Use one canonical comparison form for discovered and stored URLs."""
    parts = urllib.parse.urlsplit(html.unescape(url).strip())
    query = urllib.parse.parse_qsl(parts.query, keep_blank_values=True)
    query = [(key, value) for key, value in query if not key.lower().startswith("utm_")]
    return urllib.parse.urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"), urllib.parse.urlencode(sorted(query)), ""))


def matches_source_scope(url: str, source: dict) -> bool:
    """Bing occasionally returns an external result despite a `site:` query."""
    if source["kind"] != "bing-rss":
        return True
    match = re.search(r"site:([^/\s]+)", source.get("siteScope", ""))
    if not match:
        return False
    host = urllib.parse.urlsplit(url).netloc.lower()
    domain = match.group(1).lower()
    return host == domain or host.endswith("." + domain)


def meets_minimum_year(published: str, minimum_year: int) -> bool:
    match = re.search(r"\b(20\d{2})\b", published)
    return match is None or int(match.group(1)) >= minimum_year


def rss_items(source: dict, config: dict) -> list[dict]:
    items = []
    for cluster in config["global"]["keywordClusters"]:
        query = f'{source["siteScope"]} {cluster["terms"]}'
        feed = get("https://www.bing.com/search?format=rss&q=" + urllib.parse.quote_plus(query))
        root = ET.fromstring(feed)
        for item in root.findall(".//item")[:config["global"]["maxItemsPerQuery"]]:
            items.append({
                "title": item.findtext("title", default=""),
                "url": item.findtext("link", default=""),
                "published": item.findtext("pubDate", default=""),
                "snippet": item.findtext("description", default=""),
                "cluster": cluster["name"],
            })
    return items


def hn_items(config: dict) -> list[dict]:
    query = "email deliverability spam reputation"
    payload = json.loads(get("https://hn.algolia.com/api/v1/search_by_date?" + urllib.parse.urlencode({"query": query, "tags": "story", "hitsPerPage": 6})))
    return [{"title": h.get("title") or "", "url": f'https://news.ycombinator.com/item?id={h["objectID"]}', "published": h.get("created_at", ""), "snippet": h.get("story_text") or "", "cluster": "hacker-news"} for h in payload["hits"]]


def stackexchange_items(config: dict) -> list[dict]:
    url = "https://api.stackexchange.com/2.3/questions?" + urllib.parse.urlencode({"site": "serverfault", "order": "desc", "sort": "creation", "tagged": "email;spam", "pagesize": 6, "filter": "withbody"})
    payload = json.loads(get(url))
    return [{"title": h["title"], "url": h["link"], "published": datetime.fromtimestamp(h["creation_date"], timezone.utc).isoformat(), "snippet": h.get("body", ""), "cluster": "stackexchange"} for h in payload["items"]]


def flatten_hn(node: dict) -> list[str]:
    comments = [html.unescape(node.get("text") or "")]
    for child in node.get("children") or []:
        comments.extend(flatten_hn(child))
    return [re.sub(r"<[^>]+>", "", comment).strip() for comment in comments if comment.strip()]


def flatten_reddit(nodes: list[dict]) -> list[str]:
    comments = []
    for node in nodes:
        data = node.get("data", {})
        body = data.get("body")
        if body:
            comments.append(body.strip())
        replies = data.get("replies")
        if isinstance(replies, dict):
            comments.extend(flatten_reddit(replies.get("data", {}).get("children", [])))
    return comments


def fetch_comments(url: str) -> tuple[int | None, list[str], str]:
    """Return available count, parsed comments, and a deterministic status."""
    parts = urllib.parse.urlsplit(url)
    if parts.netloc == "news.ycombinator.com":
        item_id = urllib.parse.parse_qs(parts.query).get("id", [""])[0]
        thread = json.loads(get(f"https://hn.algolia.com/api/v1/items/{item_id}"))
        comments = [comment for child in thread.get("children") or [] for comment in flatten_hn(child)]
        return len(comments), comments, "complete"
    if "reddit.com" in parts.netloc:
        thread = json.loads(get(url.rstrip("/") + ".json"))
        comments = flatten_reddit(thread[1].get("data", {}).get("children", []))
        return len(comments), comments, "complete"
    if parts.netloc == "serverfault.com":
        match = re.search(r"/questions/(\d+)", parts.path)
        if not match:
            return None, [], "unsupported"
        question_id = match.group(1)
        data = json.loads(get("https://api.stackexchange.com/2.3/questions/" + question_id + "/comments?" + urllib.parse.urlencode({"site": "serverfault", "filter": "withbody", "pagesize": 100})))
        comments = [re.sub(r"<[^>]+>", "", item.get("body", "")).strip() for item in data.get("items", [])]
        return len(comments), comments, "complete"
    # This collector has no reliable parser for this source yet. Treat it as a
    # retriable retrieval gap, not as proof that comments are unsupported.
    return None, [], "retry"


def comment_id(item: dict, source_slug: str) -> str:
    date = re.search(r"\d{4}-\d{2}-\d{2}", item.get("published", ""))
    title = re.sub(r"[^a-z0-9]+", "-", item["title"].lower()).strip("-")[:60] or "thread"
    published_date = date.group(0) if date else datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return f"{published_date}-{source_slug}-{title}"


def comment_retry_allowed(url: str) -> bool:
    text = COMMENT_REGISTRY.read_text(encoding="utf-8")
    pattern = re.compile(rf'(?ms)^  - source: .*?^    url: "{re.escape(url)}".*?(?=^  - source:|\Z)')
    match = pattern.search(text)
    if not match:
        return True
    previous = match.group(0)
    return 'comments_recheck_policy: "retry-exhausted"' not in previous and f'comment_last_failure_date: "{datetime.now(timezone.utc):%Y-%m-%d}"' not in previous


def upsert_comment_registry(source: str, url: str, available: int | None, parsed: int, artifact: str | None, status: str) -> None:
    text = COMMENT_REGISTRY.read_text(encoding="utf-8")
    pattern = re.compile(rf'(?ms)^  - source: .*?^    url: "{re.escape(url)}".*?(?=^  - source:|\Z)')
    previous = pattern.search(text)
    previous_text = previous.group(0) if previous else ""
    today = f"{datetime.now(timezone.utc):%Y-%m-%d}"
    attempt_match = re.search(r"comment_failure_attempts: (\d+)", previous_text)
    attempts = int(attempt_match.group(1)) if attempt_match else 0
    if status == "retry":
        attempts += 1
    policy = "periodic-refresh" if status == "complete" else ("retry-exhausted" if attempts >= 3 else "retry-until-counted")
    fields = [f'  - source: "{source}"', f'    url: "{url}"', '    comments_supported: "yes"' if status == "complete" else '    comments_supported: "unknown"', f"    comments_available_count: {available if available is not None else 'null'}", f"    comments_parsed_count: {parsed}", f'    comments_artifact_file: "{artifact}"' if artifact else "    comments_artifact_file: null", f'    comments_last_checked_at: "{datetime.now(timezone.utc).isoformat()}"']
    if status == "retry":
        fields += [f"    comment_failure_attempts: {attempts}", f'    comment_last_failure_date: "{today}"']
    fields += [f'    comments_recheck_policy: "{policy}"', f'    note: "Python collector comment pass: {status}."']
    block = "\n".join(fields)
    COMMENT_REGISTRY.write_text(pattern.sub(block + "\n", text) if previous else text.rstrip() + "\n" + block + "\n", encoding="utf-8")


def process_comments(results: list[dict]) -> None:
    COMMENTS.mkdir(parents=True, exist_ok=True)
    for result in results:
        for item in result["items"]:
            if not comment_retry_allowed(item["url"]):
                continue
            try:
                available, comments, status = fetch_comments(item["url"])
            except Exception:
                available, comments, status = None, [], "retry"
            artifact = None
            if available is not None:
                canonical_id = comment_id(item, result["slug"])
                artifact = f"research/comments/{canonical_id}-comments.md"
                body = ["---", f'source: "{result["source"]}"', f'url: "{item["url"]}"', f'canonical_id: "{canonical_id}"', 'comments_supported: "yes"', f"comments_available_count: {available}", f"comments_parsed_count: {len(comments)}", f'parse_status: "{status}"', "---", "", "## Most Useful Comments Summary", "- Deterministic collector preserved the thread comments below for later review.", "", "## Useful Comment Artifacts"] + [f"- {comment}" for comment in comments[:25]]
                (ROOT / artifact).write_text("\n".join(body) + "\n", encoding="utf-8")
            upsert_comment_registry(result["source"], item["url"], available, len(comments), artifact, status)


def collect() -> Path:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    existing_urls = {normalize_url(url) for url in re.findall(r'^url:\s*"?([^"\n]+)', "\n".join(p.read_text(encoding="utf-8") for p in (ROOT / "research/signals").glob("*.md")), re.MULTILINE)}
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
                url = normalize_url(item["url"])
                text = f'{item["title"]} {item["snippet"]}'
                if not url or not meets_minimum_year(item["published"], config["global"]["minimumPublishedYear"]) or not matches_source_scope(url, source) or url in seen or url in existing_urls or excluded.search(text) or not positive.search(text):
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
    process_comments(results)
    write_ledger(now, results, failures)
    print(path.relative_to(ROOT))
    return path


def write_ledger(now: datetime, results: list[dict], failures: list[dict]) -> None:
    """Persist reviewable evidence without mislabelling it as an accepted signal."""
    CANDIDATES.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# Candidate evidence {now:%Y-%m-%d}",
        "",
        "This is a deterministic collection ledger, not accepted market-signal research.",
        "Each item still needs thread/comment verification before it can enter `research/signals/`.",
        "",
        f"## Run {now:%Y-%m-%d %H:%M:%SZ}",
        "",
        f"- Sources succeeded: {len(results)}",
        f"- Sources failed: {len(failures)}",
        f"- Unique rule-matched candidates: {sum(len(r['items']) for r in results)}",
        "",
    ]
    for result in results:
        if not result["items"]:
            continue
        lines += [f"### {result['source']}", ""]
        for item in result["items"]:
            terms = ", ".join(item["match_terms"])
            snippet = re.sub(r"\s+", " ", item["snippet"]).strip()
            lines += [f"- [{item['title']}]({item['url']})", f"  - Published: {item['published'] or 'unknown'}; matches: {terms}", f"  - Preview: {snippet[:500]}"]
        lines.append("")
    if failures:
        lines += ["## Failed sources", ""] + [f"- {f['source']}: {f['error']}" for f in failures] + [""]
    ledger = CANDIDATES / f"{now:%Y-%m-%d}.md"
    with ledger.open("a", encoding="utf-8") as stream:
        stream.write("\n".join(lines))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("collect",))
    args = parser.parse_args()
    collect()


if __name__ == "__main__":
    main()
