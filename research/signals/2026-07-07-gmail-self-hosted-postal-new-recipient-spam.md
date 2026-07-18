---
title: "Authenticated self-hosted sender reaches Gmail inbox only after recipient-level training"
source: "Gmail Community"
url: "https://support.google.com/mail/thread/448677573/emails-from-self-hosted-postal-mail-server-are-delivered-to-gmail-spam-folder?hl=en"
published_at: "2026-07-07T09:55:38Z"
discovered_at: "2026-07-18T20:01:23+02:00"
pain_type: "auth_ok_delivery_bad"
segment: "low-volume"
confidence: "high"
tags:
  - "gmail"
  - "self-hosted-sender"
  - "inbox-placement"
  - "recipient-training"
  - "reputation"
canonical_id: "2026-07-07-gmail-self-hosted-postal-new-recipient-spam"
---

## Summary
Пользователь с self-hosted Postal настроил SPF, DKIM, MX и Return-Path, но новые Gmail-получатели получают тестовые письма в Spam. После ручного «Not spam» для нескольких ящиков следующие письма в эти же ящики попадают во Inbox, тогда как для новых получателей проблема остаётся. Это показывает разрыв между корректной аутентификацией и переносимой репутацией/placement.

## Why It Matters
Консоль должна отличать локальное recipient-level обучение от доказанной общей deliverability. Нужны provider-specific seed tests для новых и уже взаимодействовавших ящиков, проверка aligned DMARC и PTR/forward-confirmed reverse DNS, а также объясняемый remediation-план вместо ложного вывода «настройки исправны, проблема решена».

## Evidence
Автор пишет, что после ручного «Not Spam» письма стали приходить во Inbox только в те же Gmail-ящики, но для новых аккаунтов всё ещё идут в Spam при валидных SPF/DKIM/MX/Return-Path.

## Comment Insights
См. [артефакт комментариев](../comments/2026-07-07-gmail-self-hosted-postal-new-recipient-spam-comments.md). Единственный видимый ответ добавляет проверку DMARC в monitoring mode и PTR matching как следующий диагностический шаг, но не опровергает placement gap для новых получателей.

## Source
- [Original source](https://support.google.com/mail/thread/448677573/emails-from-self-hosted-postal-mail-server-are-delivered-to-gmail-spam-folder?hl=en)
