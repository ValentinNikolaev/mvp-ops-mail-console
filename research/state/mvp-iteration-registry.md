# MVP Iteration Registry

Use this file to track Monday and Friday MVP synthesis generation.

## Fields to track

- date
- weekday
- iteration_id
- file
- based_on_digest_or_signal_cutoff
- status: created|updated
- note

## Rules

- Store all Monday and Friday MVP syntheses in `research/mvp-iterations/`.
- Keep one primary synthesis file per Monday or Friday date.
- Repeated hourly runs on the same Monday or Friday should update the existing file instead of creating duplicates unless a materially different version is required.
- Increment `iteration_id` across the lifetime of the repository.
