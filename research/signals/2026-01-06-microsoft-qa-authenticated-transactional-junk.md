---
title: "Outlook/Microsoft 365 marking fully authenticated transactional emails as Junk (SCL=5) for new sending domain"
source: "Microsoft Q&A"
url: "https://learn.microsoft.com/en-us/answers/questions/5694073/outlook-microsoft-365-marking-fully-authenticated"
published_at: "2026-01-06T03:37:52Z"
discovered_at: "2026-07-16T23:43:27+02:00"
pain_type: "auth_ok_delivery_bad"
segment: "low-volume"
confidence: "high"
tags:
  - "microsoft-qa"
  - "transactional-email"
  - "authentication-pass"
  - "scl-5"
  - "new-domain"
  - "reputation"
canonical_id: "2026-01-06-microsoft-qa-authenticated-transactional-junk"
---

## Summary
Небольшой e-commerce отправитель сообщает, что order confirmations и pick tickets попадают в Junk у Microsoft 365 с SCL=5, хотя SPF, DKIM, DMARC и composite authentication проходят, нет bulk-рассылок, жалоб или bounce. В ответе Microsoft признаёт, что после auth остаются непрозрачные filtering/reputation signals и нет одного sender-side переключателя; реальный путь — support case с traces и verdicts.

## Why It Matters
Это сильный MVP-сигнал для low-volume transactional sender: консоль должна показывать auth-pass отдельно от inbox placement, сохранять SCL/header evidence, объяснять cold-reputation риск и собирать provider-specific escalation packet.

## Evidence
"SPF/DKIM/DMARC and composite authentication are passing", но `X-MS-Exchange-Organization-SCL: 5` и `dest:J; RF:JunkEmail`; автор сообщает о пропущенных заказах и потере выручки.

## Comment Insights
Один комментарий автора фиксирует точные SCL/Junk headers; см. [artifact](../comments/2026-01-06-microsoft-qa-authenticated-transactional-junk-comments.md).

## Source
- [Original source](https://learn.microsoft.com/en-us/answers/questions/5694073/outlook-microsoft-365-marking-fully-authenticated)
