---
title: "Reply-rate decline hides provider-specific inbox-placement failure"
source: "Reddit Emailmarketing"
url: "https://www.reddit.com/r/Emailmarketing/comments/1urqr3s/2026_email_deliverability_issues/"
published_at: "2026-07-12T00:00:00+00:00"
discovered_at: "2026-07-18T18:03:10+02:00"
pain_type: "root_cause_visibility"
segment: "mid-volume"
confidence: "high"
tags:
  - "inbox-placement"
  - "reply-rate"
  - "provider-diagnostics"
  - "sales-email"
canonical_id: "2026-07-18-reddit-emailmarketing-reply-rate-placement-gap"
---

## Summary
Команда, отправляющая внешние письма через Pardot от имени продаж, сократила список на 30%, но получила ещё меньше ответов. Это не видно по обычному статусу доставки и показывает разрыв между «accepted/delivered» и фактическим размещением у Gmail, Outlook и корпоративных Microsoft 365 tenants.

## Why It Matters
Консоль должна сопоставлять reply-rate, placement seed tests, DMARC alignment и provider-level результаты, а не объявлять проблему list hygiene только по сокращению объёма. Нужны отдельные проверки «маркетинговая платформа отправляет как sales-rep», рекомендации по разделению потоков и evidence-led remediation до следующей кампании.

## Evidence
Автор сообщает, что ответов стало меньше даже после сокращения адресной базы на 30%; полезные комментарии связывают это с размещением в spam/Other, не с простым размером списка.

## Comment Insights
См. [артефакт комментариев](../comments/2026-07-18-reddit-emailmarketing-reply-rate-placement-gap-comments.md). Участники предлагают provider-seed test, проверку DKIM/SPF alignment для «on behalf of» и разделение массовых кампаний от настоящей 1:1 sales-переписки.

## Source
- [Original source](https://www.reddit.com/r/Emailmarketing/comments/1urqr3s/2026_email_deliverability_issues/)
