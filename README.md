# MVP Ops Mail Console Research Monitor

This repository contains a Codex-native monitoring setup for collecting fresh market pain signals about deliverability, reputation, provider filtering, and remediation workflows.

## Structure

- `scripts/run-market-signal-pipeline.codex.md` - canonical pipeline instructions for Codex.
- `research/config/signal-sources.json` - source list, keyword clusters, and filtering rules.
- `research/config/write-rules.md` - canonical naming, versioning, and commit-gating rules.
- `research/config/signal-template.md` - canonical structure for one signal file.
- `research/config/digest-template.md` - canonical structure for daily digests.
- `research/signals/` - one markdown file per normalized signal.
- `research/comments/` - one comment artifact per source thread when comments are available or partially parsed.
- `research/state/candidate-source-registry.yaml` - evaluated third-party links that may become permanent sources after independent evidence.
- `research/digests/daily/` - daily digest files for new or updated signals.
- `research/mvp-iterations/` - Monday/Friday incremental MVP syntheses in a separate folder.
- `research/mvp-council-verdicts/` - separate Council verdicts that pressure-test Monday/Friday MVP syntheses.
- `research/product-specs/` - Tuesday versioned product specifications based on the latest MVP synthesis.
- `research/logs/` - per-run execution logs. Tracked in Git.
- `research/state/` - tracked run state and repo-side metadata when the pipeline needs them.
- `automation/codex-hourly-market-monitor.prompt.md` - prompt mirror for the Codex cron automation.

## Codex automation

Use the prompt from `automation/codex-hourly-market-monitor.prompt.md` when creating a recurring Codex automation for this project. The automation should run once every hour, inspect the configured sources, update the markdown database, and then always stage all changed files, commit if there is a diff, and push to `main`.

## GitHub Actions monitor

`.github/workflows/market-signal-monitor.yml` is a Python-only unattended collector. It runs hourly at minute 17, fast-forwards `main` before collection, searches every configured source, normalizes and deduplicates URLs against existing signals, filters configured exclusion terms, and uploads ranked candidate evidence as a 30-day GitHub Actions artifact. It also appends the same reviewable evidence to `research/candidates/YYYY-MM-DD.md` and commits that ledger with `GITHUB_TOKEN`. It uses no OpenAI API key. Candidate ledger entries are not accepted signals: source-thread/comment verification is still required before an item enters `research/signals/`.

## Git policy

- All generated and maintained files live in Git.
- The pipeline should use `git add -A`.
- If the only changed files are under `research/logs/`, do not commit or push.
- If there are staged non-log changes, commit them and push to branch `main`.
- If there are no file changes, do not create an empty commit.
- When an MVP synthesis and its matching Council verdict are both prepared, create or update the GitHub release for that MVP iteration after the commit has been pushed.

## Source Of Truth

- Use this precedence order when synthesizing Monday/Friday MVP documents and Tuesday product specifications:
  1. `research/signals/` and useful comments captured from source threads
  2. `research/config/` and tracked state registries
  3. latest Tuesday product specification
  4. older MVP syntheses
- If sources disagree, prefer the higher-precedence layer and note the conflict briefly instead of silently blending them.

## Comment policy

- Add only new articles and useful comments.
- If comments are available, parsing them is mandatory.
- On the initial comment pass, record both the total available comment count and the parsed comment count.
- Store comments as a first-class artifact in `research/comments/`.
- Each comment artifact should contain a concise summary of the most useful comments for the current problem space.
- Retry a failed comment retrieval once per calendar day, never multiple times in the same day.
- Stop automatic retries after three failed daily attempts by recording `retry-exhausted`; reset only after a material source/access change or a manual decision.
- Partial comment parsing without a retrieval failure is also retried at most once per day.
- Use `research/state/comment-source-registry.yaml` to remember whether comment rechecks are worth doing.

## Monday And Friday MVP Synthesis

- On Mondays and Fridays, create an incremental refined MVP synthesis in `research/mvp-iterations/`.
- Keep these MVP syntheses separate from raw signal files and daily digests.
- Each synthesis should describe a potential MVP ops tool for low-volume and mid-volume senders that combines reputation, blocklists, provider feedback, inbox placement, and remediation steps into one explainable console.
- Each synthesis should act as if written by a senior business analyst and implementation planner with strong backend and ops judgment.
- Each synthesis should always review the latest relevant MVP documents and the latest relevant product specification documents before writing.
- Each synthesis should identify all finalized decisions, changes, fixes, and requirements from the reviewed context.
- Keep the result concise, specific, and optimized for token efficiency.
- Each synthesis should also include a venture-style business assessment from the perspective of an experienced investor and business consultant.
- Each synthesis should include:
  - the proposed MVP
  - finalized decisions
  - changes
  - fixes
  - requirements
  - what majority needs from the sample it closes
  - pros
  - cons
  - open questions
  - value and problem severity
  - business model and scalability
  - market and competitors
  - marketing and sales channels
  - 3 main business risks with mitigations
- Use tracked state in `research/state/mvp-iteration-registry.yaml` so the automation does not create duplicate Monday/Friday syntheses during repeated hourly runs on the same day.
- After creating or materially updating an MVP synthesis, run `agent-plugins:council` from `valentin-agent-plugins` (requested alias: `valentin-agent-plugins::counsil`) to brainstorm and pressure-test the whole MVP.
- Save the final verdict separately in `research/mvp-council-verdicts/YYYY-MM-DD-mvp-iteration-NNN-council-verdict.md`.
- Update the matching verdict file when the same day's MVP synthesis is revised; do not append council output to the synthesis itself.
- Once both the MVP synthesis and matching Council verdict are prepared, publish or update the GitHub release for that iteration. This is based on the prepared artifacts, not on whether the task was started by the hourly scheduler.

## MVP Releases

- Release trigger: a run creates or materially updates both an MVP synthesis and its matching Council verdict.
- Tag format: `mvp-iteration-NNN`.
- Title format: `MVP Iteration NNN - YYYY-MM-DD`.
- Release notes should summarize the MVP, the Council recommendation, the one thing to do first, and link the two artifact files.
- Existing releases for the same iteration should be updated, not duplicated.

## Tuesday Product Specification

- On Tuesdays, create a versioned product specification in `research/product-specs/`.
- Base each Tuesday specification on the latest available MVP document from `research/mvp-iterations/`.
- Keep these product specifications separate from raw signals, digests, and MVP syntheses.
- Each Tuesday specification should be written from the perspective of an expert software architect, systems engineer, and business analyst.
- Each Tuesday specification should be a comprehensive pre-implementation blueprint.
- The Tuesday document should cover both product specification and MVP architecture.
- Each Tuesday specification should describe a simple product that can be built quickly, cheaply, and with a stack that is relatively easy to maintain and scale.
- Structure the Tuesday specification with these exact top-level headers:
  - `Executive Summary`
  - `Pros & Benefits`
  - `Cons & Risks`
  - `Proposed Tech Stack & Tools`
- `Executive Summary` should be only a 2-word to 3-word overview of the proposed solution.
- `Proposed Tech Stack & Tools` should be a bulleted list of specific technologies with reasons, and should also cover the proposed MVP architecture and major system components.
- Use `research/state/product-spec-registry.yaml` so repeated hourly runs on the same Tuesday update the same spec file instead of creating duplicates.

## Debugging

- Check the newest run log under `research/logs/YYYY-MM-DD/`.
- Read the latest digest under `research/digests/daily/` to confirm what changed.
- If a source is flaky, the automation should log the error and continue with the rest.

## Self-Expanding Source Discovery

The monitor extracts relevant external links from accepted signals and useful comments. It records them as candidates first, then promotes only sources with independent evidence or a validated high-confidence community-thread exception. SEO, affiliate, generic vendor, and unreadable destinations remain excluded. The authoritative promotion rules and candidate schema live in `research/config/write-rules.md` and `research/state/candidate-source-registry.yaml`.
- If Git push fails in unattended mode, confirm the remote, branch, and authentication are already configured on the host.
- If outputs start drifting, inspect `research/config/write-rules.md` and the YAML registries in `research/state/` first.

## Recovery

- To rebuild a signal manually, edit or remove only the affected markdown file in `research/signals/` and let the next automation run recreate it.
- To adjust source coverage, edit `research/config/signal-sources.json`.
- If the automation prompt needs to change, update `scripts/run-market-signal-pipeline.codex.md` and `automation/codex-hourly-market-monitor.prompt.md` together.
