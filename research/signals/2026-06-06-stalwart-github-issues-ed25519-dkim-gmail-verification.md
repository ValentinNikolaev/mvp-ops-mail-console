---
title: "Ed25519 DKIM signatures fail Gmail verification while RSA passes"
source: "Stalwart GitHub Issues"
url: "https://github.com/stalwartlabs/stalwart/issues/3193"
published_at: "2026-06-06T01:11:31Z"
discovered_at: "2026-08-01T00:03:34+02:00"
pain_type: "auth_ok_delivery_bad"
segment: "mid-volume"
confidence: "high"
tags:
  - "dkim"
  - "gmail"
  - "dmarc-reports"
  - "authentication"
  - "visibility-gap"
  - "remediation"
canonical_id: "2026-06-06-stalwart-github-issues-ed25519-dkim-gmail-verification"
---

## Summary

Оператор Stalwart на семи доменах видит в Gmail и DMARC-отчётах стабильный `dkim=fail` для Ed25519, хотя DNS-ключ совпадает с ключом сервера, а RSA-подпись того же письма проходит. DMARC остаётся pass за счёт RSA, но поток отчётов создаёт неясную, повторяемую аутентификационную проблему без понятного owner и подтверждённой причины.

## Why It Matters

Консоль должна показывать результат по каждому selector и получателю, а не сворачивать всё в «DMARC pass». Для такого случая нужны доказательства из `Authentication-Results` и DMARC aggregate reports, разделение DNS/ключа/каноникализации/маршрута, уровень уверенности и безопасный workaround: отключить проблемный selector только после проверки резервной валидной подписи.

## Evidence

Автор сообщает, что Ed25519 DKIM не проходит у Gmail на всех семи tenant-доменах при совпадающем DNS public key, тогда как RSA на том же сообщении проходит. SPF и итоговый DMARC проходят, поэтому проблема остаётся видимой только в деталях отчётов и может быть пропущена общей панелью статуса.

## Comment Insights

[Comment artifact](../comments/2026-06-06-stalwart-github-issues-ed25519-dkim-gmail-verification-comments.md) фиксирует 1/1 ответ. Это только автоматический triage redirect без технической диагностики; новых claim или remediation из комментария нет.

## Source

- [Original source](https://github.com/stalwartlabs/stalwart/issues/3193)
