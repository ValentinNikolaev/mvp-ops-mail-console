---
title: "Outlook.com content blocks persist below normal sending limits"
source: "Microsoft Q&A"
url: "https://learn.microsoft.com/en-us/answers/questions/5890488/remote-server-returned-554-5-7-0-%28-5-7-520-smtp-55"
published_at: "2026-05-14T08:55:46Z"
discovered_at: "2026-07-23T18:03:08+02:00"
pain_type: "silent_drop_or_throttle"
segment: "low-volume"
confidence: "high"
tags:
  - "outlook-com"
  - "content-block"
  - "low-volume"
  - "delist"
  - "remediation-friction"
canonical_id: "2026-05-14-microsoft-qa-outlook-low-volume-content-block"
---

## Summary
Владелец давно используемого Outlook.com-адреса сообщает о повторяющихся 554 5.7.520 content-as-spam блокировках. Проблема исчезает после нескольких дней простоя и возвращается даже для того же письма; попытка delist и проверка аккаунта не дали устойчивого результата. Это создаёт прямые потери времени и бизнеса для малого отправителя без управления SPF/DMARC или URL отправителя.

## Why It Matters
Консоль должна различать provider-side submission block, recipient-side placement и blocklist. Для low-volume consumer sender она должна сохранять точный SMTP verdict, объём/частоту, шаги delist и их результат, затем дать понятный путь escalation вместо повторения общих советов по контенту.

## Evidence
Автор отправляет обычно 20–30 писем в день и менее 500 получателям, но после временного успеха delist блокируются даже одиночные ответы и письма самому себе. В reply подтверждено, что 72-часовое ожидание после delist не решило проблему.

## Comment Insights
См. [артефакт комментариев](../comments/2026-05-14-microsoft-qa-outlook-low-volume-content-block-comments.md). Два доступных reply фиксируют несоответствие между обычными лимитами, статуса delist и фактическим блоком; это ключевой сигнал для evidence-backed escalation.

## Source
- [Original source](https://learn.microsoft.com/en-us/answers/questions/5890488/remote-server-returned-554-5-7-0-%28-5-7-520-smtp-55)
