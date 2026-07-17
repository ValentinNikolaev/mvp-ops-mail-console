---
source: "Microsoft Q&A"
url: "https://learn.microsoft.com/en-ca/answers/questions/5915665/emails-not-sending-as-identified-as-spam"
canonical_id: "2026-06-09-microsoft-qa-outbound-spam-block"
comments_supported: "yes"
comments_available_count: 1
comments_parsed_count: 1
parse_status: "complete"
last_checked_at: "2026-07-17T23:02:42+02:00"
---

## Most Useful Comments Summary
The sole visible comment makes recipient feedback operationally concrete: a sender that repeatedly sends the same message to a group can acquire low reputation when even a small number of recipients use “Report as Junk.” This supplements the exact SMTP rejection with a list-health and complaint-risk hypothesis.

## Useful Comment Artifacts
- Preserve the group-send pattern and recipient-junk-report hypothesis beside the `5.7.520` verdict.
- Do not treat a changed attachment format as a completed remediation when reputation evidence is still missing.

## Parsing Gaps
- None; the one visible question comment was parsed.

## Source
- [Original thread](https://learn.microsoft.com/en-ca/answers/questions/5915665/emails-not-sending-as-identified-as-spam)
