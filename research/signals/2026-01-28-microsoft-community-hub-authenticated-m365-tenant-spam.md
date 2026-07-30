---
title: "Authenticated M365 tenant mail still classified as phishing spam"
source: "Microsoft Community Hub"
url: "https://techcommunity.microsoft.com/discussions/exchange_general/m365-tenant-emails-marked-as-spam-scl5-catphish-despite-perfect-authentication/4489993"
published_at: "2026-01-28"
discovered_at: "2026-07-30T19:05:38+02:00"
pain_type: "auth_ok_delivery_bad"
segment: "mid-volume"
confidence: "high"
tags:
  - "microsoft-365"
  - "authentication"
  - "reputation"
  - "provider-filtering"
  - "junk-placement"
  - "remediation"
canonical_id: "2026-01-28-microsoft-community-hub-authenticated-m365-tenant-spam"
---

## Summary

Пользователь Microsoft 365 сообщает, что деловые письма между tenant'ами M365 стабильно получают SCL 5 и CAT:PHISH, хотя SPF, DKIM, DMARC и composite authentication проходят. После недавнего включения DKIM команда не понимает, как отличить наследованную tenant reputation проблему от контента, маршрута или политики получателя и куда направить запрос на remediation.

## Why It Matters

Консоль должна объяснять, что успешная аутентификация не равна inbox placement. Для Microsoft-потока нужны раздельные гипотезы по domain/IP/tenant reputation, content signals, relay provenance и recipient Defender policy, evidence из заголовков и проверяемый порядок действий вместо совета «проверьте blocklist».

## Evidence

Автор фиксирует SPF, DKIM, DMARC и composite authentication как pass, но видит `X-MS-Exchange-Organization-SCL: 5` и `CAT:PHISH` при доставке в другие M365 tenant'ы.

## Comment Insights

Все 1 доступный комментарий разобран: [артефакт комментариев](../comments/2026-01-28-microsoft-community-hub-authenticated-m365-tenant-spam-comments.md). Ответ отделяет authentication от domain/IP reputation, content, sending pattern, receiver-side Defender policy и third-party relay reputation, предлагая сравнить получателей и trace route.

## Source

- [Original source](https://techcommunity.microsoft.com/discussions/exchange_general/m365-tenant-emails-marked-as-spam-scl5-catphish-despite-perfect-authentication/4489993)
