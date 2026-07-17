---
title: "email deliverability issue"
source: "Microsoft Q&A"
url: "https://learn.microsoft.com/en-us/answers/questions/5909406/email-deliverability-issue"
published_at: "2026-06-02T18:46:30Z"
discovered_at: "2026-07-17T21:26:40+02:00"
pain_type: "blocklist_vs_reputation"
segment: "low-volume"
confidence: "high"
tags:
  - "microsoft-qa"
  - "s3150"
  - "shared-ip"
  - "blocklist"
  - "remediation"
canonical_id: "2026-06-02-microsoft-qa-shared-ip-s3150-block"
---

## Summary
Владелец небольшого домена внезапно потерял доставку в Outlook/Hotmail из-за S3150 для IP хостинга. Он не управляет shared IP, а смена IP у провайдера платная, поэтому обычная рекомендация «проверьте репутацию» не превращается в исполнимый план.

## Why It Matters
Консоль должна отличать domain-level настройку от инфраструктуры, которой управляет провайдер, связывать SMTP verdict с IP/сетью и выдавать маршрут: проверить внешнюю репутацию, запросить remediation у хостера, оценить delist и подтвердить доставку. Это закрывает частую дыру low-volume отправителей: им доступны симптомы, но не рычаги исправления.

## Evidence
Автор получил `550 5.7.1 ... part of their network is on our block list (S3150)` и сообщил, что провайдер запросил $150 в год за смену IP после внезапной блокировки.

## Comment Insights
Два комментария к ответу подтвердили точный S3150 verdict и shared-infrastructure constraint: репутацию сети должен исправлять или менять её владелец. См. [artifact](../comments/2026-06-02-microsoft-qa-shared-ip-s3150-block-comments.md).

## Source
- [Original source](https://learn.microsoft.com/en-us/answers/questions/5909406/email-deliverability-issue)
