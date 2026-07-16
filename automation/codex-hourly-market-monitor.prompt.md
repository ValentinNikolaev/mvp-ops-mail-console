Run the hourly market-signal monitoring workflow for this repository.

Requirements:
- Read `scripts/run-market-signal-pipeline.codex.md` first.
- Read `research/config/signal-sources.json` first.
- Search the configured priority sources on the web for fresh user pain signals related to deliverability, reputation, provider filtering, blocklists, inbox placement, visibility gaps, and remediation workflows.
- Prefer 2025-2026 discussions. Ignore low-value SEO articles unless they contain a unique signal.
- Add only new articles and useful comments.
- For sources and threads where comments can be fetched, periodically revisit already parsed items to collect newly appeared useful comments.
- If comments are disabled, unavailable, or not fetchable for a parsed item, record that in `research/state/comment-source-registry.md` and do not re-fetch that article only to check comments again.
- For each accepted signal, normalize the URL, deduplicate against existing files in `research/signals/`, and keep one canonical `.md` file per signal.
- Use `research/config/signal-template.md` for each signal file.
- Use `research/config/digest-template.md` for the daily digest in `research/digests/daily/YYYY-MM-DD.md`.
- Write a human-readable run log under `research/logs/YYYY-MM-DD/run-HHmmss.md`.
- Continue if one source fails or rate-limits.
- Treat Windows-related ecosystem threads and Microsoft properties as valid first-class sources.
- Stage all changed files with `git add -A`.
- Commit and push only if there is a real diff after staging.
- Use commit message format `research: hourly signal update YYYY-MM-DD HHmm`.
- Push to branch `main`.
- Do not edit config or templates unless they are clearly broken.

After the run:
- Summarize how many sources succeeded, how many failed, and how many signals were created or updated.
- If push failed, report the exact blocker.
