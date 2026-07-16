---
title: "Survey invite emails bouncing for specific providers (e.g., Gmail)"
source: "Qualtrics Community"
url: "https://community.qualtrics.com/survey-platform-54/survey-invite-emails-bouncing-for-specific-providers-e-g-gmail-33289"
published_at: "2026-04-30T00:00:00Z"
discovered_at: "2026-07-16T20:25:54Z"
pain_type: "junk_or_quarantine"
segment: "mid-volume"
confidence: "high"
tags:
  - "qualtrics-community"
  - "gmail"
  - "bounce"
  - "spam-flagged"
  - "provider-specific"
canonical_id: "2026-04-30-qualtrics-gmail-bounce-spam"
---

## Summary
Пользователь Qualtrics описывает provider-specific bounce behavior: survey invite emails к Gmail consistently bounce с причиной, что сообщения считаются spam. Это болезненный operational case, потому что проблема проявляется не у всех провайдеров, а точечно.

## Why It Matters
Для продукта это важный сценарий provider filtering и remediation: нужно быстро отделять generic domain health от Gmail-specific failures и подсказывать следующий шаг расследования.

## Evidence
В обсуждении прямо указано, что bounce reason связан с spam-flagging именно у конкретного provider, а ответ сводится к проверке SPF/DKIM/DMARC, spam complaint rate, domain age и list hygiene.

## Source
- [Original source](https://community.qualtrics.com/survey-platform-54/survey-invite-emails-bouncing-for-specific-providers-e-g-gmail-33289)
