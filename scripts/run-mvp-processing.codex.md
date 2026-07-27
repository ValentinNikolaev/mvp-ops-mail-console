# Run MVP Processing For Codex

This file is the canonical source instruction for the MVP artifact workflow.

Use this workflow whenever a run creates or materially updates an MVP synthesis, regardless of whether the run was started by an hourly scheduler, a manual Codex task, or another automation.

## Goal

Turn the current research sample into one complete MVP artifact set:

1. MVP iteration
2. Council verdict
3. Product specification
4. GitHub release

The order is mandatory: `mvp-iteration -> council -> product-spec -> release`.

## Inputs

- Existing files under `research/signals/`
- Existing files under `research/comments/`
- Existing files under `research/mvp-iterations/`
- Existing files under `research/mvp-council-verdicts/`
- Existing files under `research/product-specs/`
- Existing files under `research/config/`
- `research/state/mvp-iteration-registry.yaml`
- `research/state/product-spec-registry.yaml`
- Current run date and time

## Step 1: MVP iteration

- Create or materially update one MVP synthesis in `research/mvp-iterations/` using `research/mvp-iterations/TEMPLATE.md`.
- Use `research/state/mvp-iteration-registry.yaml` to reuse the same day's MVP file when appropriate and avoid duplicates.
- Base the synthesis on the cumulative sample in `research/signals/` plus useful captured comments.
- Review the latest relevant MVP documents and product specifications before writing.
- Use the source-of-truth precedence from `research/config/write-rules.md`.
- Keep the synthesis concise, specific, and optimized for token efficiency.
- Write from the perspective of a senior business analyst, implementation planner, experienced venture investor, and business consultant.

## Step 2: Council verdict

- After the MVP iteration is prepared, run `agent-plugins:council` from `valentin-agent-plugins` (requested alias: `valentin-agent-plugins::counsil`) on the whole MVP.
- Use the current MVP synthesis, the latest relevant product specification, and the strongest signal/comment evidence as council context.
- Frame the council question neutrally: pressure-test the whole MVP, identify what is strongest, what will fail, what should be simplified or expanded, and what next implementation decision should be made.
- Save only the final Council Verdict in `research/mvp-council-verdicts/YYYY-MM-DD-mvp-iteration-NNN-council-verdict.md` using `research/mvp-council-verdicts/TEMPLATE.md`.
- If the linked MVP synthesis is revised, update the matching Council verdict file instead of creating a duplicate.
- Do not store the full advisor transcript unless explicitly requested.

## Step 3: Product specification

- After the Council verdict is prepared, create or update the matching product specification in `research/product-specs/` using `research/product-specs/TEMPLATE.md`.
- Base the product specification on the current MVP iteration and Council verdict.
- Keep product specifications one-to-one with MVP iterations.
- Use the matching MVP iteration id as the product spec version id.
- If the linked MVP synthesis or Council verdict is revised, update the matching product spec file instead of creating a duplicate.
- Write from the perspective of an expert software architect, systems engineer, and business analyst.
- Make it a comprehensive pre-implementation blueprint for a product that can be built quickly, cheaply, and with relatively easy maintenance and scaling.
- Structure the product specification with these exact top-level headers:
  - `Executive Summary`
  - `Pros & Benefits`
  - `Cons & Risks`
  - `Proposed Tech Stack & Tools`

## Step 4: Release

- After the MVP iteration, Council verdict, and product specification are prepared, stage and commit the artifacts according to the repository Git policy.
- Push the commit to `main`.
- Create or update the GitHub release only after the pushed commit contains the prepared artifacts.
- Use tag `mvp-iteration-NNN`.
- Use title `MVP Iteration NNN - YYYY-MM-DD`.
- Release notes must summarize the MVP synthesis, the Council recommendation, the one thing to do first, and link the MVP iteration, Council verdict, and product specification files.
- If the tag or release already exists for the same iteration, update the existing release notes instead of creating a duplicate release.
- If release creation or update fails, leave the pushed files in place and report the exact blocker.

## Run log and summary

- Mention the MVP iteration path and iteration id.
- Mention the Council verdict path and source MVP iteration id.
- Mention the product specification path, version id, and source MVP iteration id.
- Mention the GitHub release tag and URL if created or updated.
- Report exact blockers for push or release failures.
