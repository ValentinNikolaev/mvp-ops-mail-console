---
source: "Modoboa GitHub Issues"
url: "https://github.com/modoboa/modoboa/issues/4114"
canonical_id: "2026-07-21-modoboa-github-issues-rspamd-training-feedback-gap"
comments_supported: "yes"
comments_available_count: 6
comments_parsed_count: 6
parse_status: "complete"
---

## Most Useful Comments Summary

- The operational need is not merely a UI button: users need a reliable feedback path from marked junk/ham messages into the active filter so classification can improve without manually managing a separate Rspamd interface.
- The implementation discussion converges on a generic, pluggable training command and an isolated Rspamd adapter instead of coupling learning to webmail moves. That preserves existing mailbox behavior and makes training failures observable.
- The thread identifies the key safety choices an ops tool must surface: explicit backend/controller configuration, permission handling, whether learning failure is best-effort or blocking, and scope from one message to a folder, account, or domain.

## Useful Comment Artifacts

- 2026-07-25 implementation proposal: retrieve full RFC822 before a move, call `rspamc learn_spam` or `learn_ham`, retain existing UI behavior, and test inactive-backend and training-failure paths.
- 2026-07-26 reporter: migration to Rspamd exposed that filter training cannot be treated as fully separate; requests optional user-controlled folder/message feedback and a generic, pluggable backend.
- 2026-07-27 implementation follow-up: proposes `train <ham|spam> <domain> <account> [folder] [msgid]`, with the active spam-filter setting selecting a backend and nonzero failures visible to operators.
