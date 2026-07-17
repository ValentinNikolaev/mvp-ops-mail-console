---
title: "Microsoft 365 rejecting email"
source: "Server Fault"
url: "https://serverfault.com/questions/1196264/microsoft-365-rejecting-email"
published_at: "2025-12-10T16:53:00Z"
discovered_at: "2026-07-16T23:43:27+02:00"
pain_type: "blocklist_vs_reputation"
segment: "mid-volume"
confidence: "high"
tags:
  - "server-fault"
  - "microsoft-365"
  - "s3150"
  - "blocklist"
  - "visibility-gap"
  - "delisting"
canonical_id: "2025-12-10-serverfault-microsoft-blocklist-verdict-gap"
---

## Summary
Отправитель получает Microsoft 365 hard rejection S3150: часть сети якобы в blocklist, хотя Sender Office сообщает, что блокировки нет, а MXToolbox не показывает проблем. Комментарии выявляют практическую ловушку: диагностика осложняется замаскированным IP, а provider verdict может расходиться с внешними blacklist checks. Ответ рекомендует проверить outbound-IP reputation, объём и compromise, затем подать delist через Microsoft OLC Support.

## Why It Matters
Консоль должна хранить provider SMTP verdict как первичное доказательство, не приравнивать внешнюю blacklist-проверку к Microsoft reputation, проверять корректность идентификаторов/IP и выдавать готовый delisting/escalation workflow.

## Evidence
Microsoft вернул `550 5.7.1` с `S3150`, тогда как `sender.office.com` утверждал, что IP не в Microsoft blocklist, и внешняя оценка была чистой.

## Comment Insights
Все 12 комментариев разобраны: помимо точного IP и безопасной маскировки они требуют проверить EHLO/PTR и SNDS до delist/escalation; см. [artifact](../comments/2025-12-10-serverfault-microsoft-blocklist-verdict-gap-comments.md).

## Source
- [Original source](https://serverfault.com/questions/1196264/microsoft-365-rejecting-email)
