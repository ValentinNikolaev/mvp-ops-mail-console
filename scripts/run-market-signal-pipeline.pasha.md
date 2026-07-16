# Run Market Signal Pipeline For Pasha

This file describes the same pipeline as the Codex version, but written separately for Pasha.

## Mission

Find fresh market pain around email deliverability and turn it into a compact markdown knowledge base that can guide product discovery for an explainable ops console.

## What to look for

- SPF, DKIM, and DMARC are configured but inbox placement is still bad.
- Low-volume or mid-volume senders cannot get enough data from Postmaster Tools, SNDS, or similar dashboards.
- New domain, warm-up, and re-warm issues.
- Gmail or Outlook junk placement.
- Silent drop, throttling, or quarantine without a clear root cause.
- Blocklist confusion versus actual reputation problems.
- Remediation steps that are fragmented, unclear, or provider-specific.
- Demand for combined monitoring and explainability.

## What counts as a source

- Priority sources from `research/config/signal-sources.json`.
- Official communities and technical forums.
- Windows and Microsoft ecosystem sources count as valid project sources.
- Fresh threads from 2025-2026 should be preferred over older material.

## What to write

- One canonical signal file per accepted signal in `research/signals/`.
- One daily digest in `research/digests/daily/YYYY-MM-DD.md`.
- One run log in `research/logs/YYYY-MM-DD/run-HHmmss.md`.
- Optional tracked runtime metadata in `research/state/`.

## Quality bar

- Prefer real user pain over generic advice.
- Prefer concrete operational ambiguity over broad marketing commentary.
- Mark confidence honestly.
- Keep summaries concise and useful for product discovery.

## Deduplication

- Normalize the URL.
- Check whether the same source or same pain signal already exists.
- Update the existing file when the new finding is not materially distinct.

## Git behavior

- Stage everything with `git add -A`.
- Commit only when there is a real diff.
- Use commit message `research: hourly signal update YYYY-MM-DD HHmm`.
- Push to `main`.

## Failure behavior

- Continue after source-level failures.
- Log partial failures clearly.
- If push fails, report the exact reason and keep the repo changes intact.
