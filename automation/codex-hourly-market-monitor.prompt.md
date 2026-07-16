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
- If the run date is Monday or Friday, create or update one incremental refined MVP synthesis in `research/mvp-iterations/` using `research/mvp-iterations/TEMPLATE.md`.
- Keep the Monday/Friday MVP synthesis in that separate folder only.
- Base the synthesis on the cumulative sample already captured in `research/signals/` plus any newly added useful comments.
- Include the proposed MVP ops tool, which majority needs from the sample it closes, pros, cons, and open questions.
- Use `research/state/mvp-iteration-registry.md` to avoid duplicate Monday/Friday syntheses across repeated hourly runs on the same day.
- If the run date is Tuesday, create or update one versioned product specification in `research/product-specs/` using `research/product-specs/TEMPLATE.md`.
- Base the Tuesday specification on the latest available MVP document from `research/mvp-iterations/`.
- Keep the Tuesday specification in that separate folder only.
- Write the Tuesday specification as an expert software architect, systems engineer, and business analyst.
- Make it a comprehensive pre-implementation blueprint.
- The Tuesday specification must cover both the product specification and the MVP architecture.
- The specification must recommend a product shape and stack that can be built quickly, cheaply, and with relatively easy maintenance and scaling.
- Structure the Tuesday specification with these exact top-level headers:
  - `Executive Summary`
  - `Pros & Benefits`
  - `Cons & Risks`
  - `Proposed Tech Stack & Tools`
- `Executive Summary` must be only a 2-word to 3-word overview of the proposed solution.
- `Proposed Tech Stack & Tools` must be a bulleted list of specific technologies with reasons, and should include the recommended MVP architecture and major system components.
- Use `research/state/product-spec-registry.md` to avoid duplicate Tuesday specifications across repeated hourly runs on the same day.
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
- If a Monday or Friday MVP synthesis was created or updated, mention its file path and iteration id.
- If a Tuesday product specification was created or updated, mention its file path and version id.
- If push failed, report the exact blocker.
