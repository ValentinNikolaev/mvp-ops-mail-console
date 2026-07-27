Run the hourly market-signal monitoring workflow for this repository.

Before any processing—including reading prompts/configuration, collecting candidates, inspecting research, or parsing comments—refresh the local checkout from GitHub:

1. `git fetch --prune origin`
2. `git pull --ff-only origin main`

If either command fails, preserve all local work, report the exact blocker, and stop. Do not process potentially stale repository data.

All changes to this scheduled task prompt must be committed back to this source prompt file.

Requirements:
- Read `scripts/run-market-signal-pipeline.codex.md` first.
- Read `scripts/run-mvp-processing.codex.md` before creating or updating any MVP, Council verdict, product specification, or MVP release artifact.
- Read `research/config/signal-sources.json` first.
- Read `research/config/write-rules.md` first.
- Search the configured priority sources on the web for fresh user pain signals related to deliverability, reputation, provider filtering, blocklists, inbox placement, visibility gaps, and remediation workflows.
- Prefer 2025-2026 discussions. Ignore low-value SEO articles unless they contain a unique signal.
- Add only new articles and useful comments.
- If comments are available for a source thread, parsing them is mandatory.
- On the first successful comment pass for a thread, record the total available comment count and the parsed comment count.
- Create or update a comment artifact in `research/comments/` for every thread where comments are available or partially parsed.
- Each comment artifact must include a concise summary of the most useful comments for the current request.
- If comments were only partially parsed in a previous run, retry on the next run.
- If comments were unavailable or parsing failed, retry on the next run unless comments are explicitly disabled or unsupported for that source.
- Record comment counts, artifact paths, and retry status in `research/state/comment-source-registry.yaml`.
- Extract relevant external URLs from accepted signals and useful comments. Record each possible source in `research/state/candidate-source-registry.yaml` using the candidate-source rules in `research/config/write-rules.md`.
- Treat candidates as provisional: promote one to `research/config/signal-sources.json` only after the independent-evidence threshold or validated high-confidence community-thread exception; reject SEO, affiliate, generic vendor, and unreadable destinations.
- For each accepted signal, normalize the URL, deduplicate against existing files in `research/signals/`, and keep one canonical `.md` file per signal.
- Use `research/config/signal-template.md` for each signal file.
- Use `research/config/digest-template.md` for the daily digest in `research/digests/daily/YYYY-MM-DD.md`.
- If the run date is Monday or Friday, create or update one incremental refined MVP synthesis in `research/mvp-iterations/` using `research/mvp-iterations/TEMPLATE.md`.
- For MVP artifact work, follow `scripts/run-mvp-processing.codex.md`; it is the canonical instruction for the `mvp-iteration -> council -> product-spec -> release` chain.
- Keep the Monday/Friday MVP synthesis in that separate folder only.
- Base the synthesis on the cumulative sample already captured in `research/signals/` plus any newly added useful comments.
- Before writing, review the latest relevant MVP documents and the latest relevant product specifications.
- Use the source-of-truth precedence from `research/config/write-rules.md` instead of blending conflicting layers arbitrarily.
- Write the synthesis as a senior business analyst and implementation planner with strong backend and ops judgment.
- Identify all finalized decisions, changes, fixes, and requirements from the reviewed context.
- Keep the synthesis concise, specific, and optimized for token efficiency.
- Also act as an experienced venture investor and business consultant.
- Include the proposed MVP ops tool, which majority needs from the sample it closes, pros, cons, open questions, value and problem severity, business model and scalability, market and competitors, marketing and sales channels, and 3 main business risks with mitigations.
- Use `research/state/mvp-iteration-registry.yaml` to avoid duplicate Monday/Friday syntheses across repeated hourly runs on the same day.
- After writing or materially updating a Monday/Friday MVP synthesis, run the installed `agent-plugins:council` skill from `valentin-agent-plugins` (requested alias: `valentin-agent-plugins::counsil`) to brainstorm and pressure-test the whole MVP.
- Use the current MVP synthesis, the latest relevant product specification, and the strongest signal/comment evidence as council context.
- Save only the final Council Verdict as a separate markdown file in `research/mvp-council-verdicts/YYYY-MM-DD-mvp-iteration-NNN-council-verdict.md` using `research/mvp-council-verdicts/TEMPLATE.md`.
- If the same day's MVP synthesis is revised, update the matching council verdict file instead of creating another verdict file.
- Mention the council verdict file path in the run log and final run summary whenever it is created or updated.
- Whenever an MVP synthesis, its matching Council verdict, and its matching product specification are all prepared in the same run, create or update the GitHub release for that MVP iteration after committing and pushing the files. This release rule is artifact-driven and must not depend on the task scheduler or weekday trigger.
- Use tag `mvp-iteration-NNN`, title `MVP Iteration NNN - YYYY-MM-DD`, and release notes that summarize the MVP synthesis, the Council recommendation, the one thing to do first, and link the three prepared artifact paths.
- If the tag or release already exists for the same iteration, update the existing release notes instead of creating a duplicate release.
- Whenever an MVP synthesis is created or materially updated, create or update the matching versioned product specification in `research/product-specs/` using `research/product-specs/TEMPLATE.md` after the MVP synthesis and Council verdict are prepared.
- Base the product specification on the MVP document prepared in the same run from `research/mvp-iterations/`.
- Keep the product specification in that separate folder only.
- Write the product specification as an expert software architect, systems engineer, and business analyst.
- Make it a comprehensive pre-implementation blueprint.
- The product specification must cover both the product specification and the MVP architecture.
- The specification must recommend a product shape and stack that can be built quickly, cheaply, and with relatively easy maintenance and scaling.
- Structure the product specification with these exact top-level headers:
  - `Executive Summary`
  - `Pros & Benefits`
  - `Cons & Risks`
  - `Proposed Tech Stack & Tools`
- `Executive Summary` must be only a 2-word to 3-word overview of the proposed solution.
- `Proposed Tech Stack & Tools` must be a bulleted list of specific technologies with reasons, and should include the recommended MVP architecture and major system components.
- Use `research/state/product-spec-registry.yaml` to keep product specifications one-to-one with MVP iterations and avoid duplicate specifications across repeated runs.
- Write a human-readable run log under `research/logs/YYYY-MM-DD/run-HHmmss.md`.
- Continue if one source fails or rate-limits.
- Treat Windows-related ecosystem threads and Microsoft properties as valid first-class sources.
- Stage all changed files with `git add -A`.
- If the only staged changes are under `research/logs/`, do not commit and do not push.
- Otherwise, commit and push if there is a real diff after staging.
- Use commit message format `research: hourly signal update YYYY-MM-DD HHmm`.
- Push to branch `main`.
- Create or update the GitHub release only after the commit containing the prepared MVP synthesis, Council verdict, and product specification has been pushed to `main`.
- Do not edit config or templates unless they are clearly broken, except when promoting a validated candidate source under the candidate-source rules.

After the run:
- Summarize how many sources succeeded, how many failed, and how many signals were created or updated.
- Summarize how many comment-capable threads were checked, how many comments were available, how many were parsed, and which threads remain incomplete for retry.
- If a Monday or Friday MVP synthesis was created or updated, mention its file path and iteration id.
- If an MVP council verdict was created or updated, mention its file path and source MVP iteration id.
- If a GitHub release was created or updated, mention its tag and URL.
- If a product specification was created or updated, mention its file path, version id, and source MVP iteration id.
- If push failed, report the exact blocker.
- If release creation or update failed, report the exact blocker.
- Summarize candidate sources discovered, promoted, deferred, or rejected.
