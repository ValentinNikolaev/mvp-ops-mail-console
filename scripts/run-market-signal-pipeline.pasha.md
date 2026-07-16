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
- Only new articles and useful comments should be added.
- If comments can be fetched for a source, previously parsed items may be revisited from time to time to collect new useful comments.
- If comments are disabled or unavailable, do not keep re-fetching that article for comment checks.

## What to write

- One canonical signal file per accepted signal in `research/signals/`.
- One daily digest in `research/digests/daily/YYYY-MM-DD.md`.
- On Mondays and Fridays, one incremental refined MVP synthesis in `research/mvp-iterations/`.
- On Tuesdays, one versioned product specification in `research/product-specs/`.
- One run log in `research/logs/YYYY-MM-DD/run-HHmmss.md`.
- Optional tracked runtime metadata in `research/state/`.
- Maintain `research/state/comment-source-registry.md` so future runs know which parsed items are worth comment rechecks.
- Maintain `research/state/mvp-iteration-registry.md` so repeated hourly runs do not create duplicate Monday/Friday MVP syntheses.
- Maintain `research/state/product-spec-registry.md` so repeated hourly runs do not create duplicate Tuesday product specifications.

## Monday and Friday synthesis

- Keep these files in the separate folder `research/mvp-iterations/`.
- Build an incremented refined MVP version for an ops tool for low-volume and mid-volume senders.
- The MVP must combine reputation, blocklists, provider feedback, inbox placement, and remediation steps into one explainable console.
- Explain:
  - what MVP can be built now
  - which needs from most of the sample it addresses
  - pros
  - cons
  - open questions
- If the same Monday or Friday run happens again later that day, update the existing file instead of creating a duplicate unless a new version is truly needed.

## Tuesday product specification

- Keep these files in the separate folder `research/product-specs/`.
- Build each Tuesday specification from the latest available MVP document.
- Describe a simple product that can be built quickly, cheaply, and with relatively easy maintenance and scaling.
- Explain:
  - recommended stack
  - architecture
  - product scope
  - MVP feature set
  - tradeoffs
  - support and scaling considerations
  - open questions
- Prefer practical and boring technology choices over fancy ones.
- If the same Tuesday run happens again later that day, update the existing file instead of creating a duplicate unless a new version is truly needed.

## Quality bar

- Prefer real user pain over generic advice.
- Prefer concrete operational ambiguity over broad marketing commentary.
- Mark confidence honestly.
- Keep summaries concise and useful for product discovery.
- Useful comments count only when they add new pain evidence, workaround detail, provider behavior, or remediation context.

## Deduplication

- Normalize the URL.
- Check whether the same source or same pain signal already exists.
- Update the existing file when the new finding is not materially distinct.
- Do not create another entry for a comment that only restates the same issue already captured.

## Git behavior

- Stage everything with `git add -A`.
- Commit only when there is a real diff.
- Use commit message `research: hourly signal update YYYY-MM-DD HHmm`.
- Push to `main`.

## Failure behavior

- Continue after source-level failures.
- Log partial failures clearly.
- If push fails, report the exact reason and keep the repo changes intact.
