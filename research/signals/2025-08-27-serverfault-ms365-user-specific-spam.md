---
title: "Emails sent to MS365 tenant recipients from specific user always flagged as spam. DKIM, DMARC, and SPF set correctly"
source: "Server Fault"
url: "https://serverfault.com/questions/1190987/emails-sent-to-ms365-tenant-recipients-from-specific-user-always-flagged-as-spam"
published_at: "2025-08-27T19:29:00Z"
discovered_at: "2026-07-16T20:25:54Z"
pain_type: "root_cause_visibility"
segment: "unknown"
confidence: "high"
tags:
  - "server-fault"
  - "ms365"
  - "account-level-reputation"
  - "spam-foldering"
  - "spf-dkim-dmarc-pass"
canonical_id: "2025-08-27-serverfault-ms365-user-specific-spam"
---

## Summary
В Server Fault описан кейс, где письма от одного конкретного пользователя стабильно улетают в spam у новых MS365 recipients, хотя SPF/DKIM/DMARC настроены корректно, blacklist issue не подтверждается, а те же письма от другого аккаунта проходят нормально.

## Why It Matters
Это полезный сигнал для продукта, потому что проблема не выглядит как простой domain-level issue. Здесь нужна консоль, которая помогает различать account-level reputation, tenant-specific filtering и content-related triggers.

## Evidence
Автор отдельно отмечает, что тот же subject/body, отправленный от другого account, проходит без проблем, что делает root cause непрозрачным для стандартных проверок.

## Source
- [Original source](https://serverfault.com/questions/1190987/emails-sent-to-ms365-tenant-recipients-from-specific-user-always-flagged-as-spam)
