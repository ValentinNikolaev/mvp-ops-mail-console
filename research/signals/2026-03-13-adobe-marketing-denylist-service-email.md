---
title: "Marketing complaints suppress requested service email in a shared Adobe instance"
source: "Adobe Experience League Community"
url: "https://experienceleaguecommunities.adobe.com/campaign-classic-v7-campaign-v8-6/ac-marketing-instance-marketing-spam-denylist-preventing-servicing-email-communications-249190"
published_at: "2026-03-13T00:00:00Z"
discovered_at: "2026-07-18T19:03:21+02:00"
pain_type: "blocklist_vs_reputation"
segment: "mid-volume"
confidence: "high"
tags:
  - "adobe-campaign"
  - "transactional-email"
  - "suppression-list"
  - "reputation-isolation"
  - "service-continuity"
canonical_id: "2026-03-13-adobe-marketing-denylist-service-email"
---

## Summary
Пользователь Adobe Campaign сообщает, что клиенты отмечают marketing-письма как Spam, после чего единая Address/Quarantine denylist блокирует и запрошенные servicing-письма (statements и confirmations). В одной инсталляции и домене маркетинговая жалоба превращается в отказ от критичной клиентской коммуникации.

## Why It Matters
Консоль должна показывать, когда suppression или reputation boundary опасно объединяет marketing и service/transactional потоки. Нужны отдельные stream identities, явная классификация сообщения, предупреждение о collateral suppression и remediation-план: не обходить complaint сигнал вслепую, а изолировать sending subdomain/IP и governance-правила.

## Evidence
Автор пишет, что статус SPAM/Denylist после marketing-письма «preventing email execution» для paperless servicing deliveries, которые клиент специально запросил.

## Comment Insights
См. [артефакт комментариев](../comments/2026-03-13-adobe-marketing-denylist-service-email-comments.md). Оба ответа рекомендуют разделить marketing и service на subdomain, branding configuration и при возможности dedicated IP pool, чтобы жалобы одного потока не портили другой.

## Source
- [Original source](https://experienceleaguecommunities.adobe.com/campaign-classic-v7-campaign-v8-6/ac-marketing-instance-marketing-spam-denylist-preventing-servicing-email-communications-249190)
