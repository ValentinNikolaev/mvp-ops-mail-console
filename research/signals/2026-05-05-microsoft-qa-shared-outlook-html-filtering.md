---
title: "Shared Outlook sender cannot remediate infrastructure or isolate content filtering"
source: "Microsoft Q&A"
url: "https://learn.microsoft.com/en-au/answers/questions/5881008/emails-im-sending-going-to-junk-spam"
published_at: "2026-05-05T11:12:49+00:00"
discovered_at: "2026-07-19T21:01:31+02:00"
pain_type: "root_cause_visibility"
segment: "low-volume"
confidence: "high"
tags:
  - "outlook-com"
  - "shared-sender-infrastructure"
  - "html-filtering"
  - "header-evidence"
  - "silent-non-delivery"
canonical_id: "2026-05-05-microsoft-qa-shared-outlook-html-filtering"
---

## Summary
Пользователь Outlook.com видит, что почти все письма уходят в Junk, а часть тестов вообще не появляется в Gmail, включая Spam. Внешний тест сообщает о reverse-DNS, аутентификации и blocklist, но для shared Outlook-инфраструктуры эти параметры не контролируются самим отправителем. В обсуждении единственный доступный диагностический эксперимент — отправка plain-text версии: она дошла, поэтому вероятен контентный или скрытый HTML-фактор; для доказательства следующего шага нужны заголовки от получателя.

## Why It Matters
Консоль должна сначала установить границу ответственности: не советовать владельцу shared mailbox «починить SPF/rDNS/IP», которые ему не принадлежат. Затем она должна предложить минимальный воспроизводимый тест (plain text против HTML), запросить privacy-safe recipient headers и разделить placement, silent non-delivery и provider-side escalation. Это заменяет общий чек-лист объяснимым деревом действий.

## Evidence
Тесты показали, что часть сообщений в Gmail не видна даже в Junk, тогда как plain-text отправка дошла; автор не может получить заголовки без помощи получателя.

## Comment Insights
[Комментарийный артефакт](../comments/2026-05-05-microsoft-qa-shared-outlook-html-filtering-comments.md) фиксирует четыре доступных reply-комментария: plain text изолирует возможный скрытый HTML-триггер, а исходный internet header от получателя — обязательное следующее доказательство.

## Source
- [Original source](https://learn.microsoft.com/en-au/answers/questions/5881008/emails-im-sending-going-to-junk-spam)
