---
title: "Authenticated transactional mail can still be rejected across providers"
source: "Brevo Community"
url: "https://community.brevo.com/t/high-probability-of-spam-when-sending-transactional-emails/7185"
published_at: "2026-06-12T08:23:00Z"
discovered_at: "2026-07-23T03:03:17+02:00"
pain_type: "auth_ok_delivery_bad"
segment: "low-volume"
confidence: "high"
tags:
  - "transactional-email"
  - "spam-rejection"
  - "dkim"
  - "dmarc"
  - "new-domain-reputation"
  - "shared-ip"
canonical_id: "2026-07-23-brevo-community-authenticated-transactional-spam-rejection"
---

## Summary
Разработчик приложения отправляет простые welcome-письма через Brevo API. Несмотря на подтверждённые DKIM и DMARC, сообщения отклоняются как spam у Outlook, Gmail и сторонних mail-серверов. Это прямой пример разрыва между «аутентификация настроена» и фактической доставкой на нескольких provider.

## Why It Matters
Консоль должна не завершать диагностику на DNS-проверке: она должна показать различие между authentication, репутацией домена/пула IP и provider-specific verdict, собрать доказательства по каждому provider и дать безопасный remediation-порядок. Для малых transactional senders это снижает время на бесполезные правки контента, когда первопричина — новый stream или репутационный контекст.

## Evidence
Автор сообщает, что Brevo подтвердил DKIM и DMARC, но обычные «Welcome to the app» письма получили spam-rejection у Outlook, Gmail и cPanel-подобных серверов. Видимый ответ указывает на репутацию нового shared-IP/домена, резкий старт объёма и HTML/link patterns как независимые от authentication факторы.

## Comment Insights
См. [артефакт комментариев](../comments/2026-07-23-brevo-community-authenticated-transactional-spam-rejection-comments.md). Единственный доступный ответ полностью распарсен и даёт полезную последовательность: зафиксировать provider verdict, проверить возраст/каденцию stream и репутационный контекст, затем изолированно тестировать HTML и ссылки.

## Source
- [Original source](https://community.brevo.com/t/high-probability-of-spam-when-sending-transactional-emails/7185)
