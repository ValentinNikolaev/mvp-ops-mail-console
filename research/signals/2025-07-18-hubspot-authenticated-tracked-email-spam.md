---
title: "Sales emails deliver to spam"
source: "HubSpot Community"
url: "https://community.hubspot.com/t/sales-emails-deliver-to-spam/136470"
published_at: "2025-07-18T08:01:00Z"
discovered_at: "2026-07-16T23:02:46+02:00"
pain_type: "root_cause_visibility"
segment: "mid-volume"
confidence: "high"
tags:
  - "hubspot-community"
  - "authenticated"
  - "tracking"
  - "esp-differential"
  - "spam-placement"
  - "support-gap"
canonical_id: "2025-07-18-hubspot-authenticated-tracked-email-spam"
---

## Summary
Пользователь HubSpot описывает почту, которая проходит auth и не находится в blocklists, но один и тот же текст попадает в inbox из Outlook и в spam из HubSpot. Mark-as-not-spam и отключение tracking не дали устойчивого результата; support дает generic guidance, а не доказуемую причину.

## Why It Matters
Это сильный кейс для сравнительного diagnosis: консоль должна выделять change in sending path/ESP, tracking artifacts и recipient-specific outcome, а затем фиксировать проверенные remediation attempts вместо повторения общих рекомендаций.

## Evidence
"When we send the exact same email ... from our outlook client, it delivers to inbox ... via hubspot it delivers always in spam."

## Source
- [Original source](https://community.hubspot.com/t/sales-emails-deliver-to-spam/136470)
