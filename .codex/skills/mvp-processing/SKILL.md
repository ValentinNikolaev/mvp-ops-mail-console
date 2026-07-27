---
name: mvp-processing
description: "Run or maintain the repository MVP artifact workflow when Codex needs to create, update, or reason about MVP iterations, Council verdicts, product specifications, or MVP GitHub releases. Use for requests mentioning MVP processing, mvp-iteration -> council -> product-spec, Council verdict files, product specs tied to MVP iterations, or release creation from prepared MVP artifacts."
---

# MVP Processing

Use this skill for the repository's MVP artifact workflow.

The mandatory artifact order is:

1. `mvp-iteration`
2. `council`
3. `product-spec`
4. `release`

Read `scripts/run-mvp-processing.codex.md` before changing or executing MVP artifact behavior. Treat that file as the canonical operational prompt.

## Core rules

- Trigger product specs from prepared MVP artifacts, not from weekdays or scheduler configuration.
- Create or update the Council verdict immediately after the MVP iteration is prepared.
- Create or update the matching product spec only after the Council verdict is prepared.
- Keep MVP iterations, Council verdicts, and product specs one-to-one by MVP iteration id.
- Create or update the GitHub release only after the prepared artifacts are committed and pushed to `main`.
- Update existing same-iteration artifacts and releases instead of creating duplicates.

## Files

- MVP prompt: `scripts/run-mvp-processing.codex.md`
- MVP iterations: `research/mvp-iterations/`
- Council verdicts: `research/mvp-council-verdicts/`
- Product specs: `research/product-specs/`
- MVP registry: `research/state/mvp-iteration-registry.yaml`
- Product spec registry: `research/state/product-spec-registry.yaml`
- Write rules: `research/config/write-rules.md`
