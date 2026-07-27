# Write Rules

This file is the canonical write-policy reference for unattended runs.

## Naming rules

- Signals: `YYYY-MM-DD-<source-slug>-<topic-slug>.md`
- Comment artifacts: `<canonical_id>-comments.md`
- Daily digests: `YYYY-MM-DD.md`
- Run logs: `YYYY-MM-DD/run-HHmmss.md`
- Monday/Friday MVP syntheses: `YYYY-MM-DD-mvp-iteration-NNN.md`
- Monday/Friday MVP council verdicts: `YYYY-MM-DD-mvp-iteration-NNN-council-verdict.md`
- Tuesday product specifications: `YYYY-MM-DD-product-spec-NNN.md`

## Versioning rules

- `NNN` is a zero-padded repository-wide sequence number from the relevant YAML registry.
- On the same calendar date, update the existing MVP synthesis or product spec file instead of inventing a second filename unless there is a materially different version requirement.
- Registry files are the source of truth for file reuse and next version ids.
- Council verdict files reuse the linked MVP iteration id and date. If the linked MVP synthesis is revised, update the matching verdict file instead of creating a second verdict.

## Commit gating

- Always stage all changes with `git add -A`.
- If the only staged changes are under `research/logs/`, do not commit and do not push.
- If any staged changes exist outside `research/logs/`, commit and push, and it is acceptable to include the corresponding log file in the same commit.
- If a run prepares both an MVP synthesis and its matching Council verdict, create or update the GitHub release only after the commit containing those artifacts has been pushed to `main`.

## Synthesis precedence

- Monday/Friday MVP and Tuesday product-spec outputs must use this source-of-truth order:
  1. `research/signals/` plus useful captured comments
  2. `research/config/` and YAML state registries
  3. latest Tuesday product specification
  4. older MVP syntheses
- When there is conflict, prefer the higher-ranked source and note the conflict briefly.

## MVP council verdict rules

- After a Monday/Friday MVP synthesis is created or materially updated, run `agent-plugins:council` from `valentin-agent-plugins` (requested alias: `valentin-agent-plugins::counsil`) to brainstorm and pressure-test the whole MVP.
- Use the current MVP synthesis, latest Tuesday product specification, and strongest signal/comment evidence as council context.
- Save only the final Council Verdict in `research/mvp-council-verdicts/` using `research/mvp-council-verdicts/TEMPLATE.md`.
- Do not store the full advisor transcript unless explicitly requested.
- Mention the verdict file path in the run log and final run summary.

## Release rules

- Releases are triggered by prepared artifacts, not by calendar assumptions or scheduler configuration.
- Whenever a run creates or materially updates both `research/mvp-iterations/YYYY-MM-DD-mvp-iteration-NNN.md` and `research/mvp-council-verdicts/YYYY-MM-DD-mvp-iteration-NNN-council-verdict.md`, create or update the GitHub release for that MVP iteration.
- Use tag `mvp-iteration-NNN` and title `MVP Iteration NNN - YYYY-MM-DD`.
- Release notes must summarize the MVP synthesis, the Council recommendation, the one thing to do first, and link the MVP synthesis and Council verdict paths.
- If the release already exists for the iteration, update it instead of creating a duplicate.
- If release creation or update fails, record the blocker in the run log and final summary.

## Comment parsing rules

- If comments are available for a source thread, parsing them is mandatory.
- On the first successful comment fetch, record:
  - `comments_available_count`
  - `comments_parsed_count`
  - `comments_artifact_file`
- Comment artifacts must live in `research/comments/`.
- Each comment artifact must contain:
  - source and thread metadata
  - available and parsed counts
  - parse status
  - concise summary of the most useful comments for the current request
  - a short list of comment-level artifacts or paraphrases worth preserving
- If `comments_parsed_count` is lower than `comments_available_count`, retry on the next eligible calendar day, not another hourly run that day.
- For a failed retrieval or parse, store `comment_failure_attempts` and `comment_last_failure_date`. Increment at most once per calendar day and make no more than one automatic attempt that day.
- At three failed daily attempts, set `comments_recheck_policy: retry-exhausted` and stop automatic retries. Reset this only after a material source/access change or a manual decision.
- Only use `skip` when comments are explicitly disabled or structurally unsupported for that source/thread.

## Candidate source discovery rules

- Treat relevant external URLs found in an accepted signal, accepted comment artifact, or high-value source thread as **candidate sources**, not automatic permanent sources.
- Normalise the candidate URL, deduplicate it by canonical URL/domain, and record it in `research/state/candidate-source-registry.yaml` with the referring canonical signal/thread, discovery date, relevance note, status, and next-review decision.
- A candidate is eligible for promotion to `research/config/signal-sources.json` only when either:
  - two distinct accepted signals or comment artifacts independently reference it; or
  - one high-confidence, current community thread clearly demonstrates a repeatable user-pain discussion and comments can be parsed.
- Before promotion, validate that the resource is public, searchable, materially in scope, and can yield primary user discussion or authoritative provider evidence. Apply the normal recency, deduplication, and comment policy on its first pass.
- Never promote a link that is only SEO, affiliate, a generic vendor landing page, a paid tool listing, a one-off support article without user evidence, or a destination that cannot be searched or read reliably.
- Keep unproven candidates in `candidate` or `rejected` state with a concise reason; do not repeatedly search rejected candidates unless new independent evidence appears.
- In every run log, report candidate sources discovered, promoted, deferred, or rejected. A candidate registry change is a substantive research change and follows the normal commit policy.

## Empty-run source-expansion rules

- `research/state/no-signal-run-registry.yaml` is the source of truth for consecutive runs with no created or materially updated accepted signal.
- Increment its counter once per completed empty source pass; reset it to zero whenever the pass creates or materially updates an accepted signal.
- At three consecutive empty runs, a source-expansion pass is mandatory in that same run. It must find and add at least one validated, in-scope community or issue-tracker source to `research/config/signal-sources.json`.
- This explicit maintenance trigger overrides the ordinary two-referrer promotion threshold, but not the quality safeguards: the source must be public, searchable, able to yield primary user evidence, and support comment/reply parsing where available.
- Log the validation query and rationale, update the candidate registry, and record `last_expansion_at` in the counter registry. If no eligible source is found, keep the counter at three and repeat the expansion pass on the next empty run.
