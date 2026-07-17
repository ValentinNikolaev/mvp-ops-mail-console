---
source: "Server Fault"
url: "https://serverfault.com/questions/1196264/microsoft-365-rejecting-email"
canonical_id: "2025-12-10-serverfault-microsoft-blocklist-verdict-gap"
comments_supported: "yes"
comments_available_count: 12
comments_parsed_count: 12
parse_status: "complete"
last_checked_at: "2026-07-17T22:03:29+02:00"
---

## Most Useful Comments Summary
The full comment pass shows that a provider rejection needs exact IP and identity evidence: reviewers found the real header IP on UCEPROTECTL3, corrected misleading obfuscation, asked for forward/reverse-DNS alignment, and pointed to Microsoft SNDS. The thread validates evidence-quality checks before offering a delist workflow.

## Useful Comment Artifacts
- Provider verdicts and external blocklist results must be tied to the exact outbound IP.
- Sanitisation must preserve diagnostic meaning; otherwise it creates false disagreement.
- Verify EHLO forward DNS and reverse DNS before classifying the incident as a provider-only block.
- Use SNDS status as provider-side evidence; rotate among clean addresses only as a last-resort containment option.

## Parsing Gaps
- None. All 12 question comments were parsed through the Stack Exchange API.

## Source
- [Original thread](https://serverfault.com/questions/1196264/microsoft-365-rejecting-email)
