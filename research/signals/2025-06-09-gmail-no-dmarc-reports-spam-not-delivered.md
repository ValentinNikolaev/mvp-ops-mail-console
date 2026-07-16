---
title: "Don't receive DMARC reports from Google"
source: "Gmail Community"
url: "https://support.google.com/mail/thread/349591744/don-t-receive-dmarc-reports-from-google?hl=en"
published_at: "2025-06-09T06:59:59Z"
discovered_at: "2026-07-16T20:25:54Z"
pain_type: "root_cause_visibility"
segment: "mid-volume"
confidence: "high"
tags:
  - "gmail-community"
  - "dmarc"
  - "spam"
  - "not-delivered"
  - "visibility-gap"
canonical_id: "2025-06-09-gmail-no-dmarc-reports-spam-not-delivered"
---

## Summary
Бизнес-отправитель не получает DMARC reports от Google, хотя записи настроены правильно и отчеты от других провайдеров приходят. При этом у него есть жалобы, что письма части Gmail-получателей уходят в spam или не доставляются, а причина неясна.

## Why It Matters
Это показывает разрыв между корректной technical setup и реальным операционным ответом на вопрос "почему Gmail режет доставку". Такой кейс хорошо ложится в explainable monitoring и root-cause analysis.

## Evidence
Автор пишет, что sender reputation excellent, но часть email "going to SPAM or not delivered", и он хочет понять почему, несмотря на корректный DMARC setup.

## Source
- [Original source](https://support.google.com/mail/thread/349591744/don-t-receive-dmarc-reports-from-google?hl=en)
