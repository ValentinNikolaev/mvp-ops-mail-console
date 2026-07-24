---
title: "Outgoing spam false positives"
source: "cPanel Community"
url: "https://support.cpanel.net/hc/en-us/community/posts/37028318150167-Outgoing-spam-false-positives"
published_at: "2025-12-15T14:23:00Z"
discovered_at: "2026-07-21T10:08:18+02:00"
pain_type: "root_cause_visibility"
segment: "mid-volume"
confidence: "high"
tags:
  - "cpanel"
  - "spamassassin"
  - "exim"
  - "false-positive"
  - "outbound-block"
  - "diagnostic-gap"
canonical_id: "2025-12-15-cpanel-outbound-spamassassin-false-positive"
---

## Summary
После обновления cPanel/Exim легитимные исходящие письма у нескольких администраторов ошибочно получали spam verdict до отправки. Для части инцидентов не появлялись полезные bounce или message trace, поэтому команда не могла увидеть, какие правила сработали. Эскалация cPanel подтвердила дефект: SpamAssassin неверно разбирал заголовки и проверял client IP/EHLO как будто это SMTP-сервер, присваивая ложные SPF, rDNS и HELO сигналы.

## Why It Matters
Консоль должна отделять provider-side placement от локального outbound-policy block и показывать точку отказа, версию mail stack, rule hits, сканируемые headers и наличие/отсутствие SMTP handoff. Это позволяет не предлагать бесполезные действия с blocklist, DMARC или warm-up, когда причина — локальная регрессия фильтра. Нужны готовый evidence bundle для эскалации и безопасные временные меры с явным риском allowlist.

## Evidence
Ветка содержит 16 комментариев. Пользователь сообщает, что письмо «never actually get sent», а поздняя эскалация подтверждает, что после Exim 4.99.1 SpamAssassin ошибочно применял SPF/DKIM/rDNS/EHLO проверки к client headers; на момент ответа постоянного workaround не было, кроме Webmail или точечного Welcome List.

## Comment Insights
Полный разбор 16 комментариев — в [artifact](../comments/2025-12-15-cpanel-outbound-spamassassin-false-positive-comments.md). Он сохраняет различие между TLD/rule-score случаем и подтверждённой версионной регрессией, а также необходимость собирать `spamd_error_log`, версию Exim/cPanel и transport-stage evidence до изменения правил.

## Source
- [Original source](https://support.cpanel.net/hc/en-us/community/posts/37028318150167-Outgoing-spam-false-positives)
