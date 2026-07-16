# Run Market Signal Pipeline For Codex

This file is the canonical source instruction for the Codex-run hourly market monitor.

## Goal

Collect fresh pain signals for an explainable ops console for low-volume and mid-volume email senders. The target problem space includes deliverability, reputation, blocklists, provider filtering, inbox placement, visibility gaps, and remediation workflows.

## Inputs

- `research/config/signal-sources.json`
- `research/config/write-rules.md`
- Existing files under `research/signals/`
- Existing files under `research/comments/`
- Existing files under `research/digests/daily/`
- Existing files under `research/mvp-iterations/`
- Existing files under `research/product-specs/`
- Current date and time at execution

## Source policy

- Community and official ecosystem threads are preferred.
- Windows and Microsoft ecosystem sources count as first-class sources for this project.
- Fresh 2025-2026 discussions have priority.
- Reddit is optional, not mandatory for MVP.
- Weak SEO pages should be skipped unless they contain a unique pain signal.
- Only new articles and useful comments should be added to the database.
- If comments are available for a source thread, parsing them is mandatory.
- On the first successful comment fetch, record how many comments are available and how many were actually parsed.
- If a prior run parsed only part of the available comments, the next run must retry.
- Only stop retrying when comments are explicitly disabled or structurally unsupported for that thread.

## Acceptance rules

Accept a signal when at least one of these is true:

- It contains a direct user complaint.
- It shows a repeated workaround.
- It reveals a visibility gap in provider dashboards.
- It shows authentication is fine but delivery is still bad.
- It exposes junk placement, quarantine, throttling, or silent drop.
- It shows confusion between blocklists and broader reputation issues.
- It shows remediation friction or lack of explainability.
- It appears in a useful comment that adds new operational detail, root cause evidence, or remediation context not already captured from the article or thread opener.

## Output rules

- Keep one canonical markdown file per signal in `research/signals/`.
- Keep one canonical comment artifact per source thread in `research/comments/` when comments are available or partially parsed.
- Use YAML frontmatter exactly as described in `research/config/signal-template.md`.
- Write a daily digest in `research/digests/daily/YYYY-MM-DD.md`.
- On Mondays and Fridays, write one incremental refined MVP synthesis in `research/mvp-iterations/`.
- On Tuesdays, write one versioned product specification in `research/product-specs/`.
- Write a run log in `research/logs/YYYY-MM-DD/run-HHmmss.md`.
- If useful runtime metadata appears, store it in `research/state/`.
- Track comment availability, available-count, parsed-count, artifact path, and recheck decisions in `research/state/comment-source-registry.yaml`.
- Track Monday/Friday MVP synthesis creation in `research/state/mvp-iteration-registry.yaml`.
- Track Tuesday product specification creation in `research/state/product-spec-registry.yaml`.

## Monday and Friday MVP synthesis

- This synthesis must live in the separate folder `research/mvp-iterations/`.
- It should be an incremented refined version, not a raw digest.
- Before writing, review the latest relevant MVP syntheses and the latest relevant Tuesday product specifications.
- Use the source-of-truth order from `research/config/write-rules.md`.
- It should be written as a senior business analyst and implementation planner with strong backend and ops judgment.
- It should identify all finalized decisions, changes, fixes, and requirements from the reviewed context.
- Keep it concise, specific, and optimized for token efficiency.
- It should synthesize the current sample into a potential MVP ops tool for low-volume and mid-volume senders.
- The tool description should explicitly cover reputation, blocklists, provider feedback, inbox placement, and remediation steps in one explainable console.
- It should also act as if written by an experienced venture investor and business consultant.
- The synthesis should describe:
  - what can be built now as the MVP
  - finalized decisions
  - changes
  - fixes
  - requirements
  - which majority needs from the current sample it would close
  - pros
  - cons
  - open questions
  - value and problem severity
  - business model and scalability
  - market sizing and competitors
  - likely acquisition and retention economics
  - 3 main business risks and mitigations
- Create at most one Monday synthesis and one Friday synthesis per calendar date unless there is a material need to revise the same day's file; if revised, update the existing file instead of creating duplicates.
- Use the template in `research/mvp-iterations/TEMPLATE.md`.

## Tuesday product specification

- This specification must live in the separate folder `research/product-specs/`.
- It must be based on the latest available MVP document from `research/mvp-iterations/`.
- It should be written from the perspective of an expert software architect, systems engineer, and business analyst.
- It should be a comprehensive pre-implementation blueprint.
- It should cover both the product specification and the MVP architecture.
- It should describe a simple product that can be built quickly, cheaply, and with a stack that is relatively easy to maintain and scale.
- The specification should explicitly cover:
  - a 2-word to 3-word executive summary
  - architectural advantages and performance or maintainability benefits
  - technical debt, limitations, security risks, and edge cases
  - recommended implementation approach
  - recommended stack and hosting choices
  - why the stack is fast to build with
  - why the stack is low cost
  - why the stack is relatively easy to support and scale
  - the MVP architecture and major components
- Prefer pragmatic choices over novelty. Bias toward boring, proven components with low operational overhead.
- The specification must use these exact top-level headers:
  - `Executive Summary`
  - `Pros & Benefits`
  - `Cons & Risks`
  - `Proposed Tech Stack & Tools`
- Under `Proposed Tech Stack & Tools`, use bullet points with specific technologies and the reason for each choice, and include the proposed MVP architecture.
- Create at most one Tuesday specification per calendar date unless the same day's file needs a material revision; if revised, update the existing file instead of creating duplicates.
- Use the template in `research/product-specs/TEMPLATE.md`.

## Deduplication

- Deduplicate by normalized canonical URL first.
- Then deduplicate by content fingerprint or obviously duplicated pain statement.
- Update the existing canonical signal file instead of creating near-duplicate follow-ups unless the new thread is materially distinct.
- Do not create a new signal file for a comment if it only repeats the same pain already captured from the article or thread.
- If a useful new comment materially extends an existing signal, update the existing canonical file instead of re-adding the article.

## Comment handling

- When comments are available, create or update the thread's comment artifact in `research/comments/`.
- Record `comments_available_count` and `comments_parsed_count` in the registry.
- If `comments_parsed_count < comments_available_count`, set the recheck policy to retry on the next run.
- If the count is unknown because parsing failed partway through, retry on the next run.
- Extract a concise summary of the most useful comments and use that summary as an artifact for future synthesis work.

## Git policy

- Always stage all changed files with `git add -A`.
- If the only staged changes are under `research/logs/`, do not commit and do not push.
- If there is a diff outside `research/logs/`, commit it with `research: hourly signal update YYYY-MM-DD HHmm`.
- Push the result to branch `main`.
- Do not create empty commits.

## Failure handling

- If one source fails, log it and continue.
- If search results are thin, prefer fewer high-confidence signals over filler.
- If Git push fails, leave files in place and report the exact blocker.
