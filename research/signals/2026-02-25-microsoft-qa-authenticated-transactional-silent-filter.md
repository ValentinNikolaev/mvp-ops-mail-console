---
title: "Authenticated transactional SES mail silently filtered by Microsoft 365"
source: "Microsoft Q&A"
url: "https://learn.microsoft.com/en-us/answers/questions/5788143/deliverability-issue-valid-transactional-emails-be"
published_at: "2026-02-25T09:34:03Z"
discovered_at: "2026-07-21T11:03:31+02:00"
pain_type: "silent_drop_or_throttle"
segment: "low-volume"
confidence: "high"
tags:
  - "microsoft-qa"
  - "transactional-email"
  - "amazon-ses"
  - "authentication-pass"
  - "silent-filtering"
  - "new-domain-reputation"
canonical_id: "2026-02-25-microsoft-qa-authenticated-transactional-silent-filter"
---

## Summary
Новый low-volume SaaS sender отправляет ожидаемые signup/verification письма через Amazon SES, но Microsoft 365 не показывает их ни во Inbox, ни в Junk. SPF, DKIM и DMARC с alignment проходят, а внешние проверки дают 10/10; пользователь остаётся без provider verdict, trace и понятного пути исправления.

## Why It Matters
Это подтверждает, что «auth pass» и SMTP acceptance не доказывают placement. MVP-консоль должна отделять конфигурацию от provider-specific reputation/filtering risk, фиксировать отсутствие Inbox/Junk как отдельный исход и собирать escalation packet: timestamps, recipients, headers, SES event data и запрос message trace у получателя.

## Evidence
Автор сообщает, что user-requested verification links «not landing in the Inbox or the Junk folder», хотя SPF/DKIM/DMARC строго aligned и проходят; подозрение — false positive new-domain reputation filter.

## Comment Insights
В треде доступно 0 комментариев; два ответа не дают backend-verdict. Полезный человеческий ответ подтверждает remediation gap: sender должен запросить message trace у администратора получателя и параллельно эскалировать к ESP.

## Source
- [Original source](https://learn.microsoft.com/en-us/answers/questions/5788143/deliverability-issue-valid-transactional-emails-be)
