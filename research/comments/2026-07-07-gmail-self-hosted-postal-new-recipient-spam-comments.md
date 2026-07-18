---
source: "Gmail Community"
url: "https://support.google.com/mail/thread/448677573/emails-from-self-hosted-postal-mail-server-are-delivered-to-gmail-spam-folder?hl=en"
canonical_id: "2026-07-07-gmail-self-hosted-postal-new-recipient-spam"
comments_supported: "yes"
comments_available_count: 1
comments_parsed_count: 1
parse_status: "complete"
last_checked_at: "2026-07-18T20:01:23+02:00"
---

## Most Useful Comments Summary
Единственный видимый ответ не предлагает считать ручное «Not spam» решением. Он направляет диагностику к DMARC в режиме `p=none` и к согласованности PTR с доменом отправителя — именно те инфраструктурные проверки, которые консоль должна ставить рядом с placement-тестом для новых получателей.

## Useful Comment Artifacts
- Проверить DMARC record в monitoring mode, даже если SPF и DKIM уже кажутся корректными.
- Проверить, что reverse DNS/PTR sending IP соответствует sending domain и проходит forward/reverse matching.

## Parsing Gaps
- None; the one visible community reply was parsed.

## Source
- [Original thread](https://support.google.com/mail/thread/448677573/emails-from-self-hosted-postal-mail-server-are-delivered-to-gmail-spam-folder?hl=en)
