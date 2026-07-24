---
source: "cPanel Community"
url: "https://support.cpanel.net/hc/en-us/community/posts/37028318150167-Outgoing-spam-false-positives"
canonical_id: "2025-12-15-cpanel-outbound-spamassassin-false-positive"
comments_supported: "yes"
comments_available_count: 16
comments_parsed_count: 16
parse_status: "complete"
last_checked_at: "2026-07-21T10:08:18+02:00"
---

## Most Useful Comments Summary
Полный поток подтверждает два похожих, но разных пути: локальная rule/TLD/DNSBL оценка может требовать узкой настройки, а системная регрессия после обновления cPanel/Exim может блокировать легитимный outbound mail до SMTP handoff. В последнем случае нужны логи и version evidence для вендорской эскалации; смена sender reputation, blocklist или warm-up не устраняет дефект.

## Useful Comment Artifacts
- OP нашёл `spamd_error_log`: `.work` TLD, KAM/URIBL flags и blocked DNSBL-запросы подняли оценку до 8.4/5.0. Это требует сохранения raw rule hits, а не только итогового «spam» статуса.
- Несколько администраторов сообщили о массовых false positives после 11 декабря 2025; ранняя блокировка не создавала полезный bounce, а Outlook генерировал неинформативное сообщение. Консоли нужен признак «blocked before send» и проверка доступности trace.
- Поздняя vendor-эскалация подтвердила неверный разбор headers SpamAssassin после Exim 4.99.1/cPanel 132: client IP и EHLO ошибочно проверялись как SMTP-инфраструктура. Версия и change window — первичные диагностические поля.
- Временная рекомендация — Webmail или точечный SpamAssassin Welcome List; она рискованна как широкое решение, поэтому должна быть ограниченной, журналируемой и привязанной к vendor case.

## Parsing Gaps
- Нет: все 16 видимых комментариев потока разобраны.

## Source
- [Original thread](https://support.cpanel.net/hc/en-us/community/posts/37028318150167-Outgoing-spam-false-positives)
