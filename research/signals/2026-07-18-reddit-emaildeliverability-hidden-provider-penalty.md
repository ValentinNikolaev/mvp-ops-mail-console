---
title: "Clean public checks mask provider-specific inbox placement collapse"
source: "Reddit Email Deliverability"
url: "https://www.reddit.com/r/emaildeliverability/comments/1tv3dw9/a_reminder_to_test_your_assumptions_our_domains/"
published_at: ""
discovered_at: "2026-07-18T17:19:55+02:00"
pain_type: "root_cause_visibility"
segment: "mid-volume"
confidence: "high"
tags:
  - "inbox-placement"
  - "provider-specific"
  - "reputation"
  - "content-fingerprinting"
canonical_id: "2026-07-18-reddit-emaildeliverability-hidden-provider-penalty"
---

## Summary
Отправитель с валидными SPF/DKIM/DMARC, чистыми blocklist-проверками и хорошим public sender score получил почти полное попадание в Google Spam, тогда как Microsoft доставлял письма. Контролируемые тесты выявили причину: повторяющийся campaign copy и жалобы, а не инфраструктура.

## Why It Matters
Консоль не должна выдавать «всё зелёное» по DNS и внешним репутационным сервисам как итоговый вердикт. Нужны provider-specific placement-проверки, связывание complaint/engagement с контентными вариантами и экспериментальный runbook «менять по одному фактору».

## Evidence
Автор сообщает, что публичные сигналы были чистыми, но только Google отправлял кампанию в Spam; стерильное письмо доставлялось во inbox, а повторяемый текст кампании воспроизводимо вызывал фильтрацию.

## Comment Insights
См. [артефакт комментариев](../comments/2026-07-18-reddit-emaildeliverability-hidden-provider-penalty-comments.md). Комментарии уточняют ограничения Postmaster Tools при малом объёме и shared IP, а также необходимость не смешивать Gmail и Microsoft в один health score.

## Source
- [Original source](https://www.reddit.com/r/emaildeliverability/comments/1tv3dw9/a_reminder_to_test_your_assumptions_our_domains/)
