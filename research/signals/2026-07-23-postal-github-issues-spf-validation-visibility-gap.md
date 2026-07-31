---
title: "SPF validation reports false negative with Proofpoint Email Protection hosted SPF"
source: "Postal GitHub Issues"
url: "https://github.com/postalserver/postal/issues/3611"
published_at: "2026-07-23T01:25:24Z"
discovered_at: "2026-07-31T21:10:00+02:00"
pain_type: "root_cause_visibility"
segment: "mid-volume"
confidence: "high"
tags:
  - "spf"
  - "provider-feedback"
  - "visibility-gap"
  - "remediation"
canonical_id: "2026-07-23-postal-github-issues-spf-validation-visibility-gap"
---

## Summary

Оператор Postal видит предупреждение о неверном SPF в панели DNS, хотя тестовые доставки в Gmail и Microsoft 365 проходят SPF, DKIM и DMARC. Проблема — не просто настройка SPF, а неочевидное расхождение между буквальной проверкой конфигурации и фактической проверкой конкретного SMTP-маршрута через Proofpoint.

## Why It Matters

Консоль должна разделять наблюдаемый результат у получателя, проверку конфигурации отправляющей системы и вывод о причине. Иначе она превращает частичный факт в ложный диагноз. Нужны источники доказательств, контекст маршрута, явный статус `insufficient evidence` и безопасный следующий запрос: redacted заголовки с MAIL FROM, HELO, подключающим IP и `Authentication-Results`.

## Evidence

Автор сообщает, что Gmail и Microsoft 365 показывают SPF/DKIM/DMARC PASS, тогда как Postal выводит ошибку SPF. Разобранные комментарии уточняют: receiver-side PASS относится к наблюдаемому пути и идентичности, а проверка Postal ищет буквально объявленный include; без IP, sender и HELO нельзя честно выполнить RFC-оценку.

## Comment Insights

[Comment artifact](../comments/2026-07-23-postal-github-issues-spf-validation-reports-false-negative-with-proofpoint-email-protecti-comments.md) фиксирует 2/2 ответа. Полезная рекомендация — переименовать предупреждение в узкое утверждение о конфигурации, не называть весь SPF policy invalid и показать оператору минимальные данные для проверки топологии.

## Source

- [Original source](https://github.com/postalserver/postal/issues/3611)
