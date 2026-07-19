---
source: "WordPress Support"
url: "https://wordpress.org/support/topic/e-mails-showing-as-successfully-sent-not-getting-to-recipients/"
canonical_id: "2026-02-12-wordpress-post-smtp-accepted-silent-discard"
comments_supported: "yes"
comments_available_count: 8
comments_parsed_count: 8
parse_status: "complete"
last_checked_at: "2026-07-19T16:02:02+02:00"
---

## Most Useful Comments Summary
Восемь видимых ответов чётко отделяют SMTP hand-off от фактической доставки: `250 Accepted / Queued` означает, что WordPress передал сообщение, но не подтверждает placement. Разбор транскрипта находит два `From:` header и header-подобные строки в body как вероятную причину silent discard; исправление — фиксированный доменный From, visitor address только в Reply-To и переименование body-полей.

## Useful Comment Artifacts
- Для triage собирать SMTP session transcript, message headers, timestamp, recipient и наличие вложений; это даёт доказательство точки hand-off.
- `250 OK` подтверждает queue acceptance, после которого provider ещё может фильтровать, quarantine или silently drop сообщение.
- Не использовать visitor email как From; применять существующий адрес домена и `Reply-To: [your-email]`.
- Literal `From:`, `Subject:`, `To:` или `Cc:` в начале строк body могут интерпретироваться как дополнительные headers; заменить их на `Submitted by:`, `Topic:` или аналогичные labels.
- Финальный ответ автора сообщает, что первое изменение не восстановило доставку, поэтому remediation должна завершаться повторным seed/recipient test, а не предположением об успехе.

## Parsing Gaps
- Нет: страница явно сообщает 8 replies, и все восемь видимых ответов разобраны.

## Source
- [Original thread](https://wordpress.org/support/topic/e-mails-showing-as-successfully-sent-not-getting-to-recipients/)
