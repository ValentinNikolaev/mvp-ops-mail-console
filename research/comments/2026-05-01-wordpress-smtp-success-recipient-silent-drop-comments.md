---
source: "WordPress Support"
url: "https://wordpress.org/support/topic/sending-test-successful-but-not-received-in-my-inbox/"
canonical_id: "2026-05-01-wordpress-smtp-success-recipient-silent-drop"
comments_supported: "yes"
comments_available_count: 6
comments_parsed_count: 6
parse_status: "complete"
last_checked_at: "2026-07-18T22:02:41+02:00"
---

## Most Useful Comments Summary
Поддержка сначала отделяет успешное подключение WordPress к SMTP от фактической доставки, затем локализует проблему на уровне получателя: Orange может фильтровать или тихо удалять письмо. После подтверждения корректных SPF/DKIM и From address полезный runbook добавляет aligned DMARC с `rua`, Force From Email, IP reputation и сравнительные seed tests в Gmail, Outlook/Hotmail и Yahoo. Автор подтверждает, что после недели попыток переход на Brevo и настройка DMARC решили проблему.

## Useful Comment Artifacts
- Успешный SMTP test подтверждает hand-off приложения, но не inbox placement; искать нужно после SMTP acceptance.
- При SPF/DKIM pass проверить DMARC alignment/reporting, From consistency и репутацию shared/"Other SMTP" IP.
- Сравнительные тесты в Gmail, Outlook/Hotmail и Yahoo отделяют provider-specific drop от общей sender-side неисправности.
- Provider-level filtering может не дать ни spam-folder placement, ни sender notification; evidence workflow должен включать recipient quarantine/filter state.
- Итоговый workaround — переход на dedicated transactional provider — снимает симптом, но консоль должна сохранить первичную диагностику и не выдавать смену провайдера за доказанную root cause.

## Parsing Gaps
- None; all six visible replies were parsed.

## Source
- [Original thread](https://wordpress.org/support/topic/sending-test-successful-but-not-received-in-my-inbox/)
