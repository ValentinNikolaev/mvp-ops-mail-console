---
title: "SMTP configuration hides shared-host placement risk"
source: "WordPress Support"
url: "https://wordpress.org/support/topic/emails-going-to-spam-16/"
published_at: "2026-04-30T00:00:00+00:00"
discovered_at: "2026-07-19T17:04:13+02:00"
pain_type: "junk_or_quarantine"
segment: "low-volume"
confidence: "medium"
tags:
  - "wordpress"
  - "smtp"
  - "shared-ip"
  - "inbox-placement"
canonical_id: "2026-07-19-wordpress-shared-host-reputation-placement"
---

## Summary
Пользователь WordPress видит, что письма отправляются, но большинство попадает в spam и не понимает, является ли причина ошибкой SMTP plugin. Ответ поддержки отделяет plugin configuration от deliverability: собственный From-domain и authentication нужны, но shared hosting mail может иметь плохую IP reputation и требовать выделенного transactional provider.

## Why It Matters
Консоль должна показать low-volume sender, что успешная отправка и корректный plugin не доказывают inbox placement, затем объяснимо разделить DNS/alignment, shared-IP reputation, content и provider placement. Нужен action path от evidence collection к migration/verification, а не общий совет «проверьте SMTP».

## Evidence
Тема сформулирована как «emails are sending but most of them land in spam»; ответ прямо указывает, что проблема обычно не в WP Mail SMTP config, а в deliverability и reputation hosting IP.

## Comment Insights
См. [артефакт комментариев](../comments/2026-07-19-wordpress-shared-host-reputation-placement-comments.md). Единственный reply даёт конкретную последовательность: own-domain From, SPF/DKIM/DMARC, отказ от hosting mail и проверка placement после смены отправляющей инфраструктуры.

## Source
- [Original source](https://wordpress.org/support/topic/emails-going-to-spam-16/)
