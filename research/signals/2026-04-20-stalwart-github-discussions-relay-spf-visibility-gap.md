---
title: "Automatic DNS leaves an outbound relay outside SPF authorization"
source: "Stalwart GitHub Discussions"
url: "https://github.com/stalwartlabs/stalwart/discussions/3004"
published_at: "2026-04-20T00:00:00Z"
discovered_at: "2026-07-28T19:03:25+02:00"
pain_type: "auth_ok_delivery_bad"
segment: "low-volume"
confidence: "high"
tags:
  - "spf"
  - "relay"
  - "gmail"
  - "dns-automation"
  - "self-hosted"
canonical_id: "2026-04-20-stalwart-github-discussions-relay-spf-visibility-gap"
---

## Summary

Оператор self-hosted Stalwart после обновления настроил исходящую доставку через отдельный relay, но автоматическое DNS-управление оставило SPF как `v=spf1 mx -all`. Письмо успешно передавалось relay, однако Gmail показывал `Received-SPF: fail`, потому что relay не был авторизован. Ручное добавление relay в TXT-запись изменило результат Gmail на pass, но вопрос об автоматизации остался без подтверждённого ответа.

## Why It Matters

Это прямой сигнал для explainable ops console: «SMTP accepted» и «DNS managed» не означают, что получатель видит корректную авторизацию. Консоль должна сопоставлять маршрут исходящей доставки, фактический SPF TXT, IP/hostname из headers и verdict конкретного провайдера, затем давать проверяемый remediation plan и post-change test.

## Evidence

В комментариях автор приложил Gmail headers: с автоматически созданным `v=spf1 mx -all` Gmail вернул SPF fail для IP relay; после ручного `a:relay.example.com` — SPF pass.

## Comment Insights

Все 304 доступных комментария разобраны: [артефакт комментариев](../comments/2026-04-20-stalwart-github-discussions-relay-spf-visibility-gap-comments.md). Важный операционный вывод: диагностика должна различать входящую SPF-проверку, исходящий route и публикацию SPF, а не сводить проблему к общей «репутации».

## Source

- [Original source](https://github.com/stalwartlabs/stalwart/discussions/3004)
