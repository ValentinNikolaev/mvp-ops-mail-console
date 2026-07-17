---
title: "Mail deliverability issues: reputation or p=reject?"
source: "Server Fault"
url: "https://serverfault.com/questions/1199036/mail-deliverability-issues-reputation-or-p-reject"
published_at: "2026-05-22T00:00:00Z"
discovered_at: "2026-07-17T22:03:29+02:00"
pain_type: "auth_ok_delivery_bad"
segment: "low-volume"
confidence: "high"
tags:
  - "server-fault"
  - "new-domain"
  - "sender-reputation"
  - "dmarc"
  - "outlook-junk"
  - "visibility-gap"
canonical_id: "2026-05-22-serverfault-new-domain-reputation-vs-dmarc"
---

## Summary
Малый отправитель с новым доменом настроил SPF, DKIM и DMARC, получает PASS и чистый blacklist report, но письмо к крупному поставщику через Outlook попало в Junk. До настройки аутентификации он отправил 48 писем, из которых 11 hard-bounce; при объёме около 72 исходящих писем у него нет достаточного provider feedback для уверенной диагностики. Обсуждение отделяет DMARC policy от placement: `p=reject` не является общим объяснением Junk, а корректная аутентификация не создаёт reputation автоматически.

## Why It Matters
Консоль должна показывать отдельные слои: authentication, domain age/history, bounce spike, внешние blocklists, provider-specific placement и доказательства по каждому. Она должна объяснять, что переключение DMARC policy не является лечением reputation, предложить безопасный warm-up и список наблюдаемых метрик, а также явно отметить границы контроля отправителя над recipient filtering.

## Evidence
У автора SPF/DKIM/DMARC проходят, MXToolbox не находит listing, однако Outlook-получатель видит Junk после ранней кампании с 11 hard bounces из 48 адресов.

## Comment Insights
Полный разбор пяти комментариев сохранён в [artifact](../comments/2026-05-22-serverfault-new-domain-reputation-vs-dmarc-comments.md): `p=none` полезен для поэтапного наблюдения и выравнивания authorised senders, но не гарантирует Inbox; `p=reject` ожидаемо ведёт к reject, а не к Spam.

## Source
- [Original source](https://serverfault.com/questions/1199036/mail-deliverability-issues-reputation-or-p-reject)
