---
title: "emails not sending as identified as spam"
source: "Microsoft Q&A"
url: "https://learn.microsoft.com/en-ca/answers/questions/5915665/emails-not-sending-as-identified-as-spam"
published_at: "2026-06-09T15:46:56Z"
discovered_at: "2026-07-17T23:02:42+02:00"
pain_type: "silent_drop_or_throttle"
segment: "low-volume"
confidence: "high"
tags:
  - "microsoft-qa"
  - "outlook-com"
  - "spam-block"
  - "550-5-7-520"
  - "sender-reputation"
  - "recipient-feedback"
canonical_id: "2026-06-09-microsoft-qa-outbound-spam-block"
---

## Summary
Небольшой отправитель Outlook.com получил блокировку исходящей почты с `554 5.7.0` / `550 5.7.520`: смена формата вложения не изменила результат. Единственный комментарий добавляет важный операционный механизм: при рассылке группе даже небольшое число жалоб «Report as Junk» может понизить reputation. Это не сводится к проверке SPF/DKIM и требует связать SMTP verdict с объёмом, аудиторией и complaint-risk.

## Why It Matters
Консоль должна распознавать provider-side outbound block как отдельный incident state, извлекать точный код, отделять content experiment от reputation remediation и выдавать безопасный recovery-runbook: остановить широкую рассылку, проверить список/жалобы, сохранить NDR и контролировать восстановление.

## Evidence
Пользователь сообщает: `554 5.7.0 < #5.7.520 smtp;550 5.7.520 Message blocked because it contains content identified as spam. AS(4810)>` и что изменение формата вложения не помогло.

## Comment Insights
Один из одного доступного комментария разобран: регулярная отправка одинакового письма группе и даже немного recipient junk reports могут объяснить low reputation; см. [artifact](../comments/2026-06-09-microsoft-qa-outbound-spam-block-comments.md).

## Source
- [Original source](https://learn.microsoft.com/en-ca/answers/questions/5915665/emails-not-sending-as-identified-as-spam)
