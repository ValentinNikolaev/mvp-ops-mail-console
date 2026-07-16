# Write Rules

This file is the canonical write-policy reference for unattended runs.

## Naming rules

- Signals: `YYYY-MM-DD-<source-slug>-<topic-slug>.md`
- Daily digests: `YYYY-MM-DD.md`
- Run logs: `YYYY-MM-DD/run-HHmmss.md`
- Monday/Friday MVP syntheses: `YYYY-MM-DD-mvp-iteration-NNN.md`
- Tuesday product specifications: `YYYY-MM-DD-product-spec-NNN.md`

## Versioning rules

- `NNN` is a zero-padded repository-wide sequence number from the relevant YAML registry.
- On the same calendar date, update the existing MVP synthesis or product spec file instead of inventing a second filename unless there is a materially different version requirement.
- Registry files are the source of truth for file reuse and next version ids.

## Commit gating

- Always stage all changes with `git add -A`.
- If the only staged changes are under `research/logs/`, do not commit and do not push.
- If any staged changes exist outside `research/logs/`, commit and push, and it is acceptable to include the corresponding log file in the same commit.

## Synthesis precedence

- Monday/Friday MVP and Tuesday product-spec outputs must use this source-of-truth order:
  1. `research/signals/` plus useful captured comments
  2. `research/config/` and YAML state registries
  3. latest Tuesday product specification
  4. older MVP syntheses
- When there is conflict, prefer the higher-ranked source and note the conflict briefly.
