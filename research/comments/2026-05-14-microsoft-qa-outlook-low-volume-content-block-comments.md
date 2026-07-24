---
source: "Microsoft Q&A"
url: "https://learn.microsoft.com/en-us/answers/questions/5890488/remote-server-returned-554-5-7-0-%28-5.7.520-smtp-55"
canonical_id: "2026-05-14-microsoft-qa-outlook-low-volume-content-block"
comments_supported: "yes"
comments_available_count: 2
comments_parsed_count: 2
parse_status: "complete"
last_checked_at: "2026-07-23T18:03:08+02:00"
---

## Most Useful Comments Summary
Два author reply добавляют операционно важную развязку: отправитель существенно ниже заявленных лимитов, delist-портал показывает отсутствие restriction, но не принимает webmail URL, а блокировка сохраняется после 72 часов. После BCC-рассылки примерно на 200 адресов account verification разрешила один send, однако затем блокировка распространилась даже на одиночные и self-sent письма.

## Useful Comment Artifacts
- Сохранять статус delist и точный provider verdict отдельно: «not restricted» не равно успешной отправке.
- Сегментировать by sender account и submission channel; BCC batch и последующая account verification — события для timeline.
- При повторении после ожидаемого delist window предлагать evidence package для provider escalation, а не только очередной content tweak.

## Parsing Gaps
- Нет: две видимые answer-level discussion replies полностью распарсены; question-level comments отсутствуют.

## Source
- [Original thread](https://learn.microsoft.com/en-us/answers/questions/5890488/remote-server-returned-554-5-7-0-%28-5.7.520-smtp-55)
