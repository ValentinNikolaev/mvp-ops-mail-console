---
source: "Microsoft Q&A"
url: "https://learn.microsoft.com/en-us/answers/questions/5855566/i-am-having-a-problem-when-i-am-sending-out-emails"
canonical_id: "2026-04-08-microsoft-qa-self-sent-junk-reputation"
comments_supported: "yes"
comments_available_count: 6
comments_parsed_count: 6
parse_status: "complete"
last_checked_at: "2026-07-19T14:01:15+02:00"
---

## Most Useful Comments Summary
The exchange establishes that an Outlook.com/`@msn.com` sender can reproduce Junk placement by emailing themself even after recipient-rule checks. Safe Sender is not a reputation reset: self-addresses cannot be added and client-side configuration may not affect server-side filtering. The practical remedy is an evidence-backed Outlook.com support escalation, not repeated whitelisting.

## Useful Comment Artifacts
- The sender reports that «Not junk» and Safe Senders had no durable effect, including in self-sent tests; this is a strong signal to classify the case as provider-side rather than recipient-local.
- The moderator clarifies that a sender cannot add their own address to Safe Senders; an ops workflow must reject that misleading remediation suggestion.
- The moderator recommends a support case with 2–3 message examples (date/time and recipient) after recipient filters have been ruled out; this defines a minimum escalation packet.

## Parsing Gaps
- None. All six visible answer-thread comments were parsed.

## Source
- [Original thread](https://learn.microsoft.com/en-us/answers/questions/5855566/i-am-having-a-problem-when-i-am-sending-out-emails)
