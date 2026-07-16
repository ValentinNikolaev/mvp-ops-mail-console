# State

This directory is tracked in Git.

Use it for lightweight runtime metadata that helps future runs stay deterministic, such as:

- last successful run summary
- deduplication cache material
- source health notes
- pipeline-side metadata that should remain visible in version history
- comment availability and recheck decisions for already parsed items in strict YAML
- Monday/Friday MVP iteration registry and versioning notes in strict YAML
- Tuesday product specification registry and versioning notes in strict YAML

Preferred machine-readable formats here:

- `.yaml` for small registries and structured state
- `.jsonl` only when append-only event history is truly needed
