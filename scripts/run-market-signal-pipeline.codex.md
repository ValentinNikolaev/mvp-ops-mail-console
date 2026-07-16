# Run Market Signal Pipeline For Codex

This file is the canonical source instruction for the Codex-run hourly market monitor.

## Goal

Collect fresh pain signals for an explainable ops console for low-volume and mid-volume email senders. The target problem space includes deliverability, reputation, blocklists, provider filtering, inbox placement, visibility gaps, and remediation workflows.

## Inputs

- `research/config/signal-sources.json`
- Existing files under `research/signals/`
- Existing files under `research/digests/daily/`
- Current date and time at execution

## Source policy

- Community and official ecosystem threads are preferred.
- Windows and Microsoft ecosystem sources count as first-class sources for this project.
- Fresh 2025-2026 discussions have priority.
- Reddit is optional, not mandatory for MVP.
- Weak SEO pages should be skipped unless they contain a unique pain signal.

## Acceptance rules

Accept a signal when at least one of these is true:

- It contains a direct user complaint.
- It shows a repeated workaround.
- It reveals a visibility gap in provider dashboards.
- It shows authentication is fine but delivery is still bad.
- It exposes junk placement, quarantine, throttling, or silent drop.
- It shows confusion between blocklists and broader reputation issues.
- It shows remediation friction or lack of explainability.

## Output rules

- Keep one canonical markdown file per signal in `research/signals/`.
- Use YAML frontmatter exactly as described in `research/config/signal-template.md`.
- Write a daily digest in `research/digests/daily/YYYY-MM-DD.md`.
- Write a run log in `research/logs/YYYY-MM-DD/run-HHmmss.md`.
- If useful runtime metadata appears, store it in `research/state/`.

## Deduplication

- Deduplicate by normalized canonical URL first.
- Then deduplicate by content fingerprint or obviously duplicated pain statement.
- Update the existing canonical signal file instead of creating near-duplicate follow-ups unless the new thread is materially distinct.

## Git policy

- Always stage all changed files with `git add -A`.
- If there is a diff, commit it with `research: hourly signal update YYYY-MM-DD HHmm`.
- Push the result to branch `main`.
- Do not create empty commits.

## Failure handling

- If one source fails, log it and continue.
- If search results are thin, prefer fewer high-confidence signals over filler.
- If Git push fails, leave files in place and report the exact blocker.
