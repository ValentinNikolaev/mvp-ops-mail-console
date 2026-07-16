---
source: "Server Fault"
url: "https://serverfault.com/questions/1196264/microsoft-365-rejecting-email"
canonical_id: "2025-12-10-serverfault-microsoft-blocklist-verdict-gap"
comments_supported: "yes"
comments_available_count: 12
comments_parsed_count: 5
parse_status: "partial"
last_checked_at: "2026-07-16T23:43:27+02:00"
---

## Most Useful Comments Summary
The retrieved comments show that a provider rejection needs exact IP evidence: a reviewer found the real header IP on UCEPROTECTL3, while the author had obscured it, and another commenter warns to use documentation-reserved addresses rather than another live address. The thread therefore validates a tool check for evidence quality before diagnosis.

## Useful Comment Artifacts
- Provider verdicts and external blocklist results must be tied to the exact outbound IP.
- Sanitisation must preserve diagnostic meaning; otherwise it creates false disagreement.

## Parsing Gaps
- Seven additional comments were hidden behind the thread's "Show 7 more comments" control and were not retrievable; retry next run.

## Source
- [Original thread](https://serverfault.com/questions/1196264/microsoft-365-rejecting-email)
