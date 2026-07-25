---
source: "Server Fault"
url: "https://serverfault.com/questions/1169936/spf-helo-ehlo-not-published-for-google-workspace-mailservers"
canonical_id: "2025-01-09-server-fault-spf-helo-ehlo-not-published-for-google-workspace-mailservers"
comments_supported: "yes"
comments_available_count: 3
comments_parsed_count: 3
parse_status: "complete"
---

## Most Useful Comments Summary
- Deterministic collector preserved the thread comments below for later review.

## Useful Comment Artifacts
- Correct, HELO is controlled by google.
- Hello, yes, I have read it. There is nothing unclear in the documentation and there is no problem with publishing SPF record, that includes _spf.google.com. The problem is SPF_HELO_NONE flag in some check tools. Google&#39;s documentation does not mention it at all. As far as I understand it, I cannot set it up, because I do not own Google&#39;s mailserver domains. But that means that Google does not provide HELO SPF records on their mailserver, ant there is nothing to do about it, is that right?
- Have you read Google&#39;s documentation? If so, what is unclear in that documentation?
