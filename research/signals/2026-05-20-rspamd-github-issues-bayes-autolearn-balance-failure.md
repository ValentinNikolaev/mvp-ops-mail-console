---
title: "Documented Bayes autolearn balance setting silently fails"
source: "Rspamd GitHub Issues"
url: "https://github.com/rspamd/rspamd/issues/6047"
published_at: "2026-05-20T10:06:19Z"
discovered_at: "2026-07-28T22:05:12+02:00"
pain_type: "root_cause_visibility"
segment: "low-volume"
confidence: "high"
tags:
  - "rspamd"
  - "bayes"
  - "spam-filtering"
  - "configuration"
  - "remediation"
canonical_id: "2026-05-20-rspamd-github-issues-bayes-autolearn-balance-failure"
---

## Summary

Оператор Rspamd обнаружил, что документированная настройка `check_balance = true` не включает балансировку автообучения Bayes: значение по умолчанию уже фиксирует `balance.enabled = false`, поэтому ожидаемая защита от перекоса обучения spam/ham молча не действует. В комментарии опубликован рабочий обходной путь с явным блоком `autolearn.balance`.

## Why It Matters

Это сигнал для explainable ops console: конфигурация, выглядящая корректной по документации, может оставлять фильтр в нежелательном состоянии без понятного verdict или remediation. Консоль должна проверять effective configuration, связывать её с признаками provider/filtering поведения, показывать риск перекоса классификации и выдавать проверяемый diff, post-change test и rollback.

## Evidence

Автор сообщает, что после `check_balance = true` балансировка не включается, потому что значение по умолчанию сохраняет `balance.enabled = false`; комментарий подтверждает, что явные `balance.enabled = true` и `min_balance = 0.9` восстанавливают ожидаемое поведение.

## Comment Insights

Все 2 доступных комментария разобраны: [артефакт комментариев](../comments/2026-05-20-rspamd-github-issues-bayes-autolearn-balance-failure-comments.md). Они уточняют, что затронут также `min_balance`, и дают конкретную конфигурационную remediation-последовательность.

## Source

- [Original source](https://github.com/rspamd/rspamd/issues/6047)
