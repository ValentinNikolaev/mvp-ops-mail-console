---
title: "I’ve been spam blocklisted, what do I do?!"
source: "Adobe Experience League Community"
url: "https://experienceleaguecommunities.adobe.com/adobe-marketo-engage-27/i-ve-been-spam-blocklisted-what-do-i-do-250333"
published_at: "2026-05-06T00:00:00Z"
discovered_at: "2026-07-17T21:26:40+02:00"
pain_type: "blocklist_vs_reputation"
segment: "mid-volume"
confidence: "high"
tags:
  - "adobe-marketo"
  - "blocklist"
  - "incident-response"
  - "database-hygiene"
  - "rewarm"
canonical_id: "2026-05-06-adobe-marketo-blocklist-incident-runbook"
---

## Summary
Пользователь Marketo описывает блоклист-инцидент как операционный кризис: нужно остановить рассылки, учесть затронутые кампании и KPI, изолировать проблемный send/list, подготовить план для Adobe и осторожно прогреть отправку заново. Причина часто скрыта в плохой гигиене базы, а не в одном DNS-параметре.

## Why It Matters
Консоль должна превращать blocklist alert в объяснимый incident runbook: pause/alert/isolate/triage/fix, журнал отключённых кампаний, поиск аномалий объёма и bounce, evidence pack для провайдера и controlled rewarm. Это связывает репутационные сигналы с реальными действиями ops-команды.

## Evidence
Автор советует при блоклисте приостановить исходящие письма, выявить campaign/audience, устранить проблемы с invalid и disengaged адресами и затем возобновлять отправку с малых объёмов на engaged сегмент.

## Comment Insights
Все три reply подтверждают спрос на заранее документированный мониторинг и риск рассылки по всей базе без data-retention discipline; см. [artifact](../comments/2026-05-06-adobe-marketo-blocklist-incident-runbook-comments.md).

## Source
- [Original source](https://experienceleaguecommunities.adobe.com/adobe-marketo-engage-27/i-ve-been-spam-blocklisted-what-do-i-do-250333)
