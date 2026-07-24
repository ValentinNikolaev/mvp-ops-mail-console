---
title: "Shared ESP IP reputation can block unrelated business mail"
source: "Brevo Community"
url: "https://community.brevo.com/t/low-ip-reputation-score-causing-issues-with-email-deliverability-of-brevo-marketing-emails/7054"
published_at: "2026-04-07"
discovered_at: "2026-07-23T20:02:53+02:00"
pain_type: "blocklist_vs_reputation"
segment: "mid-volume"
confidence: "high"
tags:
  - "shared-ip"
  - "ip-reputation"
  - "gmail"
  - "provider-feedback"
  - "remediation"
canonical_id: "2026-04-07-brevo-community-shared-ip-reputation-block"
---

## Summary
Клиент Brevo сообщил, что Gmail блокирует его исходящую почту и meeting invitations, а Google mail stats связывают проблему с низкой IP-репутацией Brevo. Обновление DMARC снизило число инцидентов, но не устранило их полностью, поэтому оператор не может отличить собственную конфигурацию от риска общего ESP IP.

## Why It Matters
Консоль должна отделять domain/authentication health от shared-IP/provider reputation и показывать, когда после исправления DMARC остаётся provider-specific block. Нужны message IDs, timeline по provider, IP/pool context и управляемая эскалация в ESP support, а не ложный вывод, что один DNS-фикс закрывает инцидент.

## Evidence
Пользователь описывает блокировку Gmail деловой почты при "Low IP reputation scores from Brevo emails"; после DMARC-изменения инцидентов стало меньше, но один повторился.

## Comment Insights
См. [артефакт комментариев](../comments/2026-04-07-brevo-community-shared-ip-reputation-block-comments.md). Единственный доступный ответ направляет в account-specific support с примерами message ID, что подтверждает необходимость сохранять доказательства, пригодные для эскалации.

## Source
- [Original source](https://community.brevo.com/t/low-ip-reputation-score-causing-issues-with-email-deliverability-of-brevo-marketing-emails/7054)
