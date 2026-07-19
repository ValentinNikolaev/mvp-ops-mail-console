---
source: "Microsoft Q&A"
thread_url: "https://learn.microsoft.com/en-au/answers/questions/5881008/emails-im-sending-going-to-junk-spam"
canonical_id: "2026-05-05-microsoft-qa-shared-outlook-html-filtering"
comments_available_count: 4
comments_parsed_count: 4
parse_status: "complete"
checked_at: "2026-07-19T21:01:31+02:00"
---

## Useful comment summary

The expert first asks for the recipient's original internet headers, not a forwarded message, because those headers are needed to distinguish provider handling from sender assumptions. The sender reports that a plain-text test to Gmail succeeds while earlier HTML mail did not appear, even in Junk. That makes a content or hidden-HTML trigger a testable hypothesis, but not a confirmed root cause; the console should preserve the A/B result and request privacy-safe headers before recommending escalation.

## Preserved comment artifacts

- Comment 1: request a redacted recipient internet header, preserving the sending domain, because it is the evidence needed for diagnosis.
- Comment 2: the sender cannot retrieve a recipient header and says some Gmail tests were absent from both Inbox and Junk.
- Comment 3: ask for a plain-text test as a controlled content-format comparison.
- Comment 4: the sender confirms the plain-text Gmail test arrived, indicating a possible hidden HTML/content classification issue.

## Source

- [Original thread](https://learn.microsoft.com/en-au/answers/questions/5881008/emails-im-sending-going-to-junk-spam)
