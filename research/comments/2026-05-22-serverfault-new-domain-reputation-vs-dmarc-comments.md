---
source: "Server Fault"
url: "https://serverfault.com/questions/1199036/mail-deliverability-issues-reputation-or-p-reject"
canonical_id: "2026-05-22-serverfault-new-domain-reputation-vs-dmarc"
comments_supported: "yes"
comments_available_count: 5
comments_parsed_count: 5
parse_status: "complete"
last_checked_at: "2026-07-17T22:03:29+02:00"
---

## Most Useful Comments Summary
The comments separate DMARC rollout from inbox placement: `p=none` is a monitoring phase for finding legitimate unauthorised senders before enforcing policy, not an inbox-placement remedy. A strict `p=reject` should reject failing mail rather than explain a delivered message being sent to Junk; the remaining issue is recipient-side filtering and reputation.

## Useful Comment Artifacts
- `p=none` permits observation and alignment before stricter enforcement; it does not guarantee delivery.
- A message that reaches Spam is not evidence that `p=reject` caused the placement; recipient filters remain outside sender control.

## Parsing Gaps
- None. All five available question comments were parsed through the Stack Exchange API.

## Source
- [Original thread](https://serverfault.com/questions/1199036/mail-deliverability-issues-reputation-or-p-reject)
