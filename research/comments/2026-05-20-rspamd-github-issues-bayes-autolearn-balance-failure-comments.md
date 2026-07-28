---
source: "Rspamd GitHub Issues"
url: "https://github.com/rspamd/rspamd/issues/6047"
canonical_id: "2026-05-20-rspamd-github-issues-bayes-autolearn-balance-failure"
comments_supported: "yes"
comments_available_count: 2
comments_parsed_count: 2
parse_status: "complete"
---

## Most Useful Comments Summary

- The reporter confirms the documented `check_balance` path also fails to apply `min_balance`, reinforcing that the problem is not a single typo but a silent configuration-interpretation gap.
- A later community reply provides a tested remediation: define `autolearn.balance.enabled = true` and `min_balance = 0.9` explicitly in `classifier-bayes.conf`, rather than relying on `check_balance`.

## Useful Comment Artifacts

- 2026-05-20 reporter: observes that `min_balance` appears to be ignored by the same configuration path.
- 2026-07-10 community responder: shares an explicit `autolearn.balance` configuration that restores balancing.
