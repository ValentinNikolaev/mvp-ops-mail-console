---
source: "Listmonk GitHub Issues"
url: "https://github.com/knadh/listmonk/issues/645"
canonical_id: "2022-01-03-listmonk-smtp-message-throttling"
comments_supported: "yes"
comments_available_count: 3
comments_parsed_count: 3
parse_status: "complete"
---

## Most Useful Comments Summary

- A maintainer supplied concrete Listmonk controls—concurrency, message rate, batch size, and a sliding-window cap—but noted that a 30-per-minute provider constraint is operationally painful.
- A later low-volume sender reported a tighter provider cap of 100 messages per hour despite needing fewer than 400 sends, confirming that rate limits remain a practical remediation constraint.
- The original reporter ultimately routed newsletters through Brevo SMTP to protect transactional delivery, showing a workaround that shifts senders to an ESP when self-hosted delivery cannot meet provider constraints.

## Useful Comment Artifacts

- 2022-01-04 maintainer: recommends explicit concurrency, message-rate, batch, and sliding-window settings; calls 30/minute slow.
- 2025-11-13 sender: reports a 100/hour provider cap for a sub-400-send need.
- 2025-11-13 original reporter: adopted Brevo SMTP for newsletter sending to preserve transactional delivery.
