# Product Specification Registry

Use this file to track Tuesday product specification generation.

## Fields to track

- date
- weekday
- spec_id
- file
- based_on_mvp_file
- status: created|updated
- note

## Rules

- Store all Tuesday product specifications in `research/product-specs/`.
- Keep one primary specification file per Tuesday date.
- Repeated hourly runs on the same Tuesday should update the existing file instead of creating duplicates unless a materially different version is required.
- Increment `spec_id` across the lifetime of the repository.
