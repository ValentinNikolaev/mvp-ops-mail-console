---
title: "All requests from this subscription are blocked due to the sender reputation that affects your delivery"
source: "Microsoft Q&A"
url: "https://learn.microsoft.com/en-us/answers/questions/5880500/all-requests-from-this-subscription-are-blocked-du"
published_at: "2026-05-04T22:33:18Z"
discovered_at: "2026-07-19T15:01:57+02:00"
pain_type: "blocklist_vs_reputation"
segment: "low-volume"
confidence: "high"
tags:
  - "microsoft-qa"
  - "azure-communication-services"
  - "subscription-block"
  - "sender-reputation"
  - "support-escalation"
canonical_id: "2026-05-04-microsoft-qa-acs-subscription-reputation-block"
---

## Summary
Пользователь Azure Communication Services столкнулся с полной блокировкой отправки на уровне subscription из-за sender reputation. Смена домена отправителя не помогла: блокировка применялась до обычной доставки и требовала проверки и снятия через Azure Support.

## Why It Matters
Консоль должна отличать domain/IP проблему от provider-managed account или subscription enforcement. Для такого verdict она должна собрать subscription/resource, timestamps, SMTP/error evidence, bounce/complaint/suppression trends и выдать эскалационный пакет, а не советовать только сменить домен или проверить blocklist. Это закрывает критический операционный разрыв: одна репутационная защита может остановить весь поток low-volume отправителя.

## Evidence
Автор сообщил, что все запросы были заблокированы из-за sender reputation и что смена sender domain не сняла блок. Принятый ответ подтвердил subscription-level root cause, ручное снятие блокировки командой Azure и профилактику через failure rate ниже 1% и непрерывный мониторинг bounce/failure patterns.

## Comment Insights
В треде заявлен один комментарий, но его текст не был доступен в читаемом представлении при первом проходе; артефакт сохранён для следующей дневной попытки. Ответы уже добавляют важный workflow: verified custom domain, suppression/log evidence и support-led unblock. См. [artifact](../comments/2026-05-04-microsoft-qa-acs-subscription-reputation-block-comments.md).

## Source
- [Original source](https://learn.microsoft.com/en-us/answers/questions/5880500/all-requests-from-this-subscription-are-blocked-du)
