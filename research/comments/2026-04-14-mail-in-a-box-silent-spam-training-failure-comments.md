---
source: "Mail-in-a-Box GitHub Issues"
url: "https://github.com/mail-in-a-box/mailinabox/issues/2570"
canonical_id: "2026-04-14-mail-in-a-box-silent-spam-training-failure"
comments_supported: "yes"
comments_available_count: 4
comments_parsed_count: 4
parse_status: "complete"
---

## Most Useful Comments Summary

- A contributor confirms that IMAPSieve covers modern IMAP MOVE and the legacy COPY-plus-expunge path, removing the compatibility concern that blocks a safe remediation decision.
- A project contributor confirms that sieve scripts are required for the Ubuntu 26.04 upgrade path, turning the workaround into a near-term operational requirement rather than a theoretical improvement.
- The remaining comments support the proposed direction but add no separate root cause.

## Useful Comment Artifacts

- 2026-04-15 contributor: asks whether COPY plus expunge remains supported, surfacing an implementation-compatibility question.
- 2026-04-15 reporter: explains that IMAPSieve's COPY trigger covers MOVE, legacy COPY plus expunge, and ordinary COPY, whereas the legacy plugin misses MOVE.
- 2026-04-16 project contributor: says Ubuntu 26.04 requires sieve scripts and confirms the tested direction.
