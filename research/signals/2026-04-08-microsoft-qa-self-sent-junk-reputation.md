---
title: "I am having a problem when I am sending out emails to people, my emails are going directly to their junk mail"
source: "Microsoft Q&A"
url: "https://learn.microsoft.com/en-us/answers/questions/5855566/i-am-having-a-problem-when-i-am-sending-out-emails"
published_at: "2026-04-08T19:44:26Z"
discovered_at: "2026-07-19T14:01:15+02:00"
pain_type: "root_cause_visibility"
segment: "low-volume"
confidence: "high"
tags:
  - "microsoft-qa"
  - "outlook-com"
  - "sender-reputation"
  - "junk-placement"
  - "safe-senders"
  - "support-escalation"
canonical_id: "2026-04-08-microsoft-qa-self-sent-junk-reputation"
---

## Summary
Пользователь персонального аккаунта `@msn.com` видит, что обычные письма систематически попадают в Junk даже при отправке самому себе. «Not junk» и Safe Senders не устраняют симптом, а адрес нельзя добавить в свой собственный safe list. В итоге остаётся непрозрачная server-side reputation/filtering проблема, для которой нет self-service reset и нужен support case с примерами сообщений.

## Why It Matters
Консоль должна отделять mailbox-local настройки от provider-side filtering, показывать, когда «safe sender» — недействующий workaround, и формировать доказательный пакет эскалации: sender, recipient, timestamps, headers, placement и подтверждение отсутствия recipient rules. Для низкообъёмных отправителей это закрывает критический разрыв между доставкой и фактической видимостью.

## Evidence
Пользователь пишет, что его сообщения «go straight to the junk mail folder» даже при отправке себе, хотя получатели не создавали rule/filter; он не может добавить собственный адрес в Safe Senders.

## Comment Insights
Все 6 доступных ответных комментариев разобраны; см. [artifact](../comments/2026-04-08-microsoft-qa-self-sent-junk-reputation-comments.md). Они уточняют, что server-side Outlook.com filtering может игнорировать client-side safe-list действия, а поддержке нужны 2–3 точных примера.

## Source
- [Original source](https://learn.microsoft.com/en-us/answers/questions/5855566/i-am-having-a-problem-when-i-am-sending-out-emails)
