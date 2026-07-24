---
source: "cPanel Community"
url: "https://support.cpanel.net/hc/en-us/community/posts/37610886986775"
canonical_id: "2026-01-12-cpanel-forwarder-backscatter-remediation-gap"
comments_supported: "yes"
comments_available_count: 11
comments_parsed_count: 11
parse_status: "complete"
last_checked_at: "2026-07-22T23:02:26+02:00"
---

## Most Useful Comments Summary
Все 11 комментариев показывают, что временный `blackhole`-transport устраняет backscatter и frozen retries, но cPanel обновление перезаписывает изменённый файл. Вендор сначала признал нужду в UI/поддерживаемой настройке, затем подтвердил, что исправление не будет backport'иться в 134/136 и появится только в 138+. Для оператора это не просто конфигурационная задача: workaround требует постоянного контроля изменений и версии.

## Useful Comment Artifacts
- Рабочий локальный эксперимент заменяет `:fail:`/`allow_fail` на `transport = blackhole`, чтобы не отвечать спамеру.
- Изменённый replacecf-файл был перезаписан update; автоматический hook становится хрупкой, но необходимой временной мерой.
- Участник запрашивает два явных UI-controls для no-bounce forwarding; moderator создаёт feature request.
- Июнь–июльское продолжение фиксирует product gap: известный production risk для LTS нельзя поддержанно устранить до будущего major release.

## Parsing Gaps
- Нет: все 11 доступных комментариев страницы разобраны.

## Source
- [Original thread](https://support.cpanel.net/hc/en-us/community/posts/37610886986775)
