---
source: "Server Fault"
url: "https://serverfault.com/questions/1190987/emails-sent-to-ms365-tenant-recipients-from-specific-user-always-flagged-as-spam"
canonical_id: "2025-08-27-serverfault-ms365-user-specific-spam"
comments_supported: "yes"
comments_available_count: 3
comments_parsed_count: 3
parse_status: "complete"
last_checked_at: "2026-07-16T23:43:27+02:00"
---

## Most Useful Comments Summary
The comments confirm that mailbox-specific sender reputation can evade generic mail testers: the sender had tested the exact problematic mailbox, but diagnosis still required evidence from the receiving tenant and mailbox.

## Useful Comment Artifacts
- Generic analyser success does not reproduce recipient-tenant filtering; retain recipient mailbox/provider context.
- The next diagnostic owner is the problem recipient tenant, not the sender's client or basic content test.

## Parsing Gaps
- None; all three visible comments were parsed.

## Source
- [Original thread](https://serverfault.com/questions/1190987/emails-sent-to-ms365-tenant-recipients-from-specific-user-always-flagged-as-spam)
