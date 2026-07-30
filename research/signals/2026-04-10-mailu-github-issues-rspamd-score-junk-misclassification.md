---
title: "Low Rspamd score still sends mail to Junk"
source: "Mailu GitHub Issues"
url: "https://github.com/Mailu/Mailu/issues/4011"
published_at: "2026-04-10T09:28:46Z"
discovered_at: "2026-07-30T18:35:35+02:00"
pain_type: "root_cause_visibility"
segment: "low-volume"
confidence: "high"
tags:
  - "mailu"
  - "rspamd"
  - "dovecot"
  - "junk-placement"
  - "header-provenance"
  - "remediation"
canonical_id: "2026-04-10-mailu-github-issues-rspamd-score-junk-misclassification"
---

## Summary

Пользователь Mailu видит, что легитимные входящие письма с низким score Rspamd всё равно попадают в Junk. Проблема оказалась не в оценке Rspamd, а в скрытом взаимодействии Dovecot с унаследованным заголовком от mail forwarder: оператору не хватало видимости, какой компонент принял решение и по какому сигналу.

## Why It Matters

Explainable ops console должен связывать итоговое inbox/Junk placement с конкретным rule engine, заголовком и upstream-провайдером, а не ограничиваться общим spam score. Нужны timeline принятия решения, provenance заголовков и проверяемый remediation playbook с до/после результатом, особенно для малых self-hosted отправителей без отдельной команды почтовой эксплуатации.

## Evidence

Автор сообщает, что Rspamd возвращает `no action, score 0.90/15`, но Dovecot сохраняет письмо в Junk при отсутствии пользовательских фильтров. Комментарии показывают, что триггером был всегда присутствующий `X-Spam-Level` от forwarder, а не verdict Rspamd.

## Comment Insights

Все 2 доступных комментария разобраны: [артефакт комментариев](../comments/2026-04-10-mailu-github-issues-rspamd-score-junk-misclassification-comments.md). Они дают воспроизводимое объяснение mismatch и две remediation options: скорректировать Dovecot Sieve spam test или удалить чужой `X-Spam-Level` в Postfix до доставки.

## Source

- [Original source](https://github.com/Mailu/Mailu/issues/4011)
