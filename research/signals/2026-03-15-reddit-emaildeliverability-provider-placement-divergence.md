---
title: "Authenticated low-volume sender sees provider-specific spam placement"
source: "Reddit Email Deliverability"
url: "https://www.reddit.com/r/emaildeliverability/comments/1ruhpyb/high_spam_placement_1218_need_advice/"
published_at: "2026-03-15T00:00:00Z"
discovered_at: "2026-07-22T14:02:32+02:00"
pain_type: "root_cause_visibility"
segment: "low-volume"
confidence: "medium"
tags:
  - "provider-segmentation"
  - "inbox-placement"
  - "yahoo"
  - "reputation"
  - "seed-testing"
canonical_id: "2026-03-15-reddit-emaildeliverability-provider-placement-divergence"
---

## Summary
Низкообъёмный отправитель с настроенными SPF, DKIM и DMARC видит неодинаковый placement по провайдерам: 83–88% Inbox у Gmail/Google Workspace и 100% Spam у Yahoo. Простые изменения copy не снизили spam rate, поэтому агрегированная «deliverability» скрывает provider-specific инцидент.

## Why It Matters
MVP должен хранить placement отдельно по provider, sending identity, тесту и времени, а не выводить один общий score. Runbook должен сначала подтвердить Yahoo-specific scope, проверить качество аудитории и cadence, а затем запускать контролируемые изменения; чистая аутентификация и успешный warm-up не являются доказательством placement у каждого provider.

## Evidence
Автор сообщает о чистой DNS-аутентификации, 15 письмах в день с каждого из трёх новых Gmail accounts и 0% Inbox / 100% Spam у Yahoo, хотя другие provider tests заметно лучше.

## Comment Insights
[Артефакт комментариев](../comments/2026-03-15-reddit-emaildeliverability-provider-placement-divergence-comments.md) сохраняет четыре видимых комментария: они отделяют техническую готовность от provider-specific reputation, предостерегают от механического cadence и требуют проверять реальные audience signals, а не доверять одному warm-up score.

## Source
- [Original source](https://www.reddit.com/r/emaildeliverability/comments/1ruhpyb/high_spam_placement_1218_need_advice/)
