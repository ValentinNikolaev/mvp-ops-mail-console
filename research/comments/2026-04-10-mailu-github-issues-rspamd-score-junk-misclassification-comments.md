---
source: "Mailu GitHub Issues"
url: "https://github.com/Mailu/Mailu/issues/4011"
canonical_id: "2026-04-10-mailu-github-issues-rspamd-score-junk-misclassification"
comments_supported: "yes"
comments_available_count: 2
comments_parsed_count: 2
parse_status: "complete"
---

## Most Useful Comments Summary

- The reporter traced the false Junk placement to Dovecot testing the length of an always-present `X-Spam-Level` header rather than the Rspamd verdict. Reconfiguring the Sieve spam test to use `X-Spam` immediately stopped the incorrect filing.
- The final remediation removes the unwanted forwarded `X-Spam-Level` header in Postfix before Dovecot sees it, while preserving `X-Spam-Status`; this restores intended spam detection without log noise.
- For an ops console, the thread makes header provenance, the active decision rule, and the before/after remediation evidence essential: a low filter score alone does not explain mailbox placement.

## Useful Comment Artifacts

- 2026-04-10: a Dovecot override changes `sieve_spamtest_status_header` from `X-Spam-Level` to `X-Spam` and changes the comparison mode from string length to text.
- 2026-04-11: a Postfix `header_checks` rule ignores injected `X-Spam-Level` before delivery; the reporter confirms it fixes the incident and retains Rspamd's intended detection.
