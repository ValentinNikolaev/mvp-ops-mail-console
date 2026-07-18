---
title: "Successful SMTP hand-off can hide recipient-provider silent drop"
source: "WordPress Support"
url: "https://wordpress.org/support/topic/sending-test-successful-but-not-received-in-my-inbox/"
published_at: "2026-05-01T00:00:00Z"
discovered_at: "2026-07-18T22:02:41+02:00"
pain_type: "silent_drop_or_throttle"
segment: "low-volume"
confidence: "high"
tags:
  - "wordpress"
  - "smtp"
  - "silent-drop"
  - "recipient-provider-filtering"
  - "dmarc"
  - "reputation"
canonical_id: "2026-05-01-wordpress-smtp-success-recipient-silent-drop"
---

## Summary
WordPress-пользователь получил успешный SMTP test, но письмо не появилось в целевом ящике Orange. SPF и DKIM были проверены, адрес отправителя совпадал с SMTP-настройкой, а вручную отправленная почта в этот же Orange-ящик работала. Обсуждение указывает на provider-specific filtering или тихое удаление после SMTP hand-off; после недели ручной диагностики пользователь сменил поток на Brevo и настроил DMARC reporting.

## Why It Matters
Консоль должна разделять «application/SMTP accepted» и «provider inbox outcome». Нужны provider-specific seed tests, проверка aligned DMARC и From consistency, репутация SMTP IP, evidence trail по фильтру/карантину получателя и ясный порядок remediation. Иначе маленький отправитель ошибочно считает успешный тест доставкой и тратит время на не тот слой стека.

## Evidence
Автор сообщает, что WP Mail SMTP отметил тест как успешный, но письмо в Orange не пришло при уже проверенных SPF/DKIM; поддержка объясняет, что Orange может фильтровать или silently discard сообщение после приёма SMTP, а смена на Brevo решила проблему.

## Comment Insights
См. [артефакт комментариев](../comments/2026-05-01-wordpress-smtp-success-recipient-silent-drop-comments.md). Все шесть ответов показывают практический runbook: разделить отправку и placement, тестировать Gmail/Outlook/Yahoo, проверить DMARC `rua`, force-From и репутацию SMTP IP; пользователь подтверждает решение после перехода на транзакционный провайдер.

## Source
- [Original source](https://wordpress.org/support/topic/sending-test-successful-but-not-received-in-my-inbox/)
