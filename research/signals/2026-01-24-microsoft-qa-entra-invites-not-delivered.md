---
title: "Entra external-user invitations complete but are not delivered"
source: "Microsoft Q&A"
url: "https://learn.microsoft.com/en-us/answers/questions/5737161/since-end-december-2025-add-user-%29-invite-external"
published_at: "2026-01-24T07:59:05Z"
discovered_at: "2026-07-16T23:28:48+02:00"
pain_type: "silent_drop_or_throttle"
segment: "mid-volume"
confidence: "high"
tags:
  - "microsoft-qa"
  - "entra"
  - "transactional-email"
  - "silent-non-delivery"
  - "manual-workaround"
  - "support-gap"
canonical_id: "2026-01-24-microsoft-qa-entra-invites-not-delivered"
---

## Summary
Несколько tenant'ов сообщают, что Entra создаёт guest user со статусом Pending acceptance, но invitation и CC не доставляются с конца 2025 года. В результате команды вручную копируют redemption link и отправляют его со своего домена; Microsoft подтвердил, что workflow завершается, а проблема именно в email delivery.

## Why It Matters
Это кейс, где application success скрывает business failure. MVP должен сопоставлять application event, provider outcome и recipient confirmation, поднимать alert для pending invitation без delivery evidence и выдавать безопасный fallback с direct redemption link.

## Evidence
"The guest user object is created successfully and remains in Pending acceptance, but the invitation email (including CC) is not delivered."

## Source
- [Original source](https://learn.microsoft.com/en-us/answers/questions/5737161/since-end-december-2025-add-user-%29-invite-external)
