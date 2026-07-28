---
title: "Spam training via dovecot-antispam is silently broken on Dovecot 2.3.x"
source: "Mail-in-a-Box GitHub Issues"
url: "https://github.com/mail-in-a-box/mailinabox/issues/2570"
published_at: "2026-04-14T18:52:00Z"
discovered_at: "2026-07-28T16:04:34+02:00"
pain_type: "root_cause_visibility"
segment: "low-volume"
confidence: "high"
tags:
  - "spam-filtering"
  - "silent-failure"
  - "remediation"
  - "self-hosted"
canonical_id: "2026-04-14-mail-in-a-box-silent-spam-training-failure"
---

## Summary

Пользователь Mail-in-a-Box обнаружил, что обучение SpamAssassin по перемещению писем в Spam фактически молча не работает: современные IMAP-клиенты используют MOVE, а старый `dovecot-antispam` перехватывает только COPY. Аутентификация и видимая конфигурация плагина не показывают сбой, поэтому фильтр не учится на действиях пользователя и качество классификации не улучшается.

## Why It Matters

Это прямой сигнал для explainable ops console: одной проверки SPF/DKIM/DMARC и статуса сервиса недостаточно. Нужны контроль фактической работы feedback-loop, наблюдаемость «событие пользователя → обучение фильтра», обнаружение тихих несовместимостей версий и конкретный remediation plan с проверкой после исправления.

## Evidence

Автор воспроизвёл, что после IMAP MOVE счётчик `sa-learn` не растёт, а после COPY растёт; комментарии подтверждают IMAPSieve как совместимую замену и необходимость sieve-скриптов для Ubuntu 26.04.

## Comment Insights

Все 4 доступных комментария разобраны: [артефакт комментариев](../comments/2026-04-14-mail-in-a-box-silent-spam-training-failure-comments.md). Главный вывод — remediation должен проверять покрытие MOVE и legacy COPY, а не только факт установки нового плагина.

## Source

- [Original source](https://github.com/mail-in-a-box/mailinabox/issues/2570)
