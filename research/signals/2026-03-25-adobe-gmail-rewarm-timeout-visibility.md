---
title: "Gmail ‘Ignored’ bounces during IP re-warming"
source: "Adobe Experience League Community"
url: "https://experienceleaguecommunities.adobe.com/adobe-journey-optimizer-15/gmail-ignored-bounces-during-ip-re-warming-249440"
published_at: "2026-03-25T00:00:00Z"
discovered_at: "2026-07-16T23:02:46+02:00"
pain_type: "silent_drop_or_throttle"
segment: "mid-volume"
confidence: "high"
tags:
  - "adobe-community"
  - "gmail"
  - "re-warming"
  - "throttling"
  - "timeouts"
  - "visibility-gap"
canonical_id: "2026-03-25-adobe-gmail-rewarm-timeout-visibility"
---

## Summary
После периода low volume команда re-warm'ит поддомен и видит Gmail timeouts, которые AJO классифицирует как "Ignored" bounces; в delivery logs нет точной причины. Полезный ответ связывает их с Gmail 421/4xx deferral или throttling и объясняет, что корректный DMARC p=none сам по себе не является причиной.

## Why It Matters
Нужна нормализация provider events: превратить неоднозначный vendor label в понятную гипотезу, отделить конфигурационную ошибку от reputation/volume problem и предложить retry-window, volume и data-quality проверки.

## Evidence
"many Gmail bounces due to timeouts, classified as ‘Ignored’" и вопрос, можно ли увидеть "exact gmail bounce reason" в delivery logs.

## Source
- [Original source](https://experienceleaguecommunities.adobe.com/adobe-journey-optimizer-15/gmail-ignored-bounces-during-ip-re-warming-249440)
