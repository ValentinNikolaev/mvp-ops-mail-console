---
title: "Rspamd feedback training lacks an operator workflow"
source: "Modoboa GitHub Issues"
url: "https://github.com/modoboa/modoboa/issues/4114"
published_at: "2026-07-21T18:26:33Z"
discovered_at: "2026-07-29T10:05:10+02:00"
pain_type: "root_cause_visibility"
segment: "low-volume"
confidence: "high"
tags:
  - "rspamd"
  - "spam-filtering"
  - "feedback-loop"
  - "remediation"
  - "operator-workflow"
canonical_id: "2026-07-21-modoboa-github-issues-rspamd-training-feedback-gap"
---

## Summary

Оператор Modoboa после миграции на Rspamd не может безопасно и управляемо передавать исправления пользователей (spam/ham) в обучение фильтра. Отдельный интерфейс Rspamd слишком сложен, а существующий продукт не даёт наблюдаемого workflow от выбранного письма к подтверждённому результату обучения.

## Why It Matters

Это прямой запрос на explainable remediation: консоль должна связать пользовательскую классификацию, активный фильтр и фактический результат обучения, а не просто показывать репутацию или blocklist. Нужны scope (message/folder/account), backend/configuration, audit trail, результат команды и безопасная политика ошибки, чтобы исправление не стало скрытой причиной ухудшения inbox placement.

## Evidence

Автор пишет, что для эффективных фильтров обучение необходимо, но управление всем через отдельный Rspamd UI непрактично; обсуждение сводится к общему командному интерфейсу и проверяемому backend-адаптеру вместо неявного webmail hook.

## Comment Insights

Все 6 доступных комментариев разобраны: [артефакт комментариев](../comments/2026-07-21-modoboa-github-issues-rspamd-training-feedback-gap-comments.md). Они формируют конкретный remediation contract: явный backend, контролируемый scope обучения, сохранение текущего mailbox behavior и видимая обработка ошибок.

## Source

- [Original source](https://github.com/modoboa/modoboa/issues/4114)
