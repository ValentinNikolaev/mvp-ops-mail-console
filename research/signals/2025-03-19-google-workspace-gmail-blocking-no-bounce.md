---
title: "Gmail is rejecting/blocking emails from and to me"
source: "Google Workspace Admin Community"
url: "https://support.google.com/a/thread/332194303/gmail-is-rejecting-blocking-emails-from-and-to-me?hl=en"
published_at: "2025-03-19T16:30:28Z"
discovered_at: "2026-07-16T20:25:54Z"
pain_type: "silent_drop_or_throttle"
segment: "low-volume"
confidence: "high"
tags:
  - "google-workspace-admin-community"
  - "gmail"
  - "silent-drop"
  - "no-bounce"
  - "authentication-not-enough"
canonical_id: "2025-03-19-google-workspace-gmail-blocking-no-bounce"
---

## Summary
Пользователь Google Workspace жалуется, что письма внезапно блокируются в обе стороны, а часть исходящих сообщений вообще не доходит без bounce. Это не выглядит как простая DNS-ошибка: проблема затрагивает уже рабочую переписку и ведет себя непредсказуемо.

## Why It Matters
Это сильный сигнал в пользу explainability-консоли: здесь нужна склейка reputation, provider-side filtering и remediation steps, потому что стандартная проверка SPF/DKIM/DMARC сама по себе не объясняет silent failure.

## Evidence
Пользователь пишет, что некоторые письма "were never delivered" и при этом не было bounce-back, хотя переписка с клиентами уже шла раньше.

## Source
- [Original source](https://support.google.com/a/thread/332194303/gmail-is-rejecting-blocking-emails-from-and-to-me?hl=en)
