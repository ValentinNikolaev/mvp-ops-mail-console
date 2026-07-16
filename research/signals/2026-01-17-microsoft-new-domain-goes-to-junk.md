---
title: "New domain for my online marketplace, and they go to junk."
source: "Microsoft Q&A"
url: "https://learn.microsoft.com/en-us/answers/questions/5723349/new-domain-for-my-online-marketplace-and-they-go-t"
published_at: "2026-01-17T23:21:59Z"
discovered_at: "2026-07-16T20:25:54Z"
pain_type: "warmup_rewarm"
segment: "low-volume"
confidence: "high"
tags:
  - "microsoft-qa"
  - "new-domain"
  - "warmup"
  - "junk-placement"
  - "verification-email"
canonical_id: "2026-01-17-microsoft-new-domain-goes-to-junk"
---

## Summary
Новый маркетплейс настроил SPF, DKIM и DMARC, но verification emails все равно попадают в Junk. Это типичный warm-up pain: технический baseline есть, а доверие провайдера и inbox placement еще не сформированы.

## Why It Matters
Такой кейс особенно релевантен для low-volume sender'ов и новых доменов. Продукту нужен режим, который объясняет переход от "все зеленое в DNS" к реальному trust-building и remediation workflow.

## Evidence
Автор прямо пишет, что письма "meet all the technical requirements" и все же идут в junk/spam, то есть operational problem остается после прохождения базовой authentication checklist.

## Source
- [Original source](https://learn.microsoft.com/en-us/answers/questions/5723349/new-domain-for-my-online-marketplace-and-they-go-t)
