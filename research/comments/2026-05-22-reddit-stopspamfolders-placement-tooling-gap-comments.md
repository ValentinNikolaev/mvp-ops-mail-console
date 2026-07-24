---
source: "Reddit StopSpamFolders"
url: "https://www.reddit.com/r/StopSpamFolders/comments/1tkm3lg/spent_3_weeks_figuring_out_why_our_emails_stopped/"
canonical_id: "2026-05-22-reddit-stopspamfolders-placement-tooling-gap"
comments_supported: "yes"
comments_available_count: null
comments_parsed_count: 11
parse_status: "partial-total-unavailable"
last_checked_at: "2026-07-22T00:04:57+02:00"
---

## Most Useful Comments Summary
Комментарии подтверждают ключевой разрыв: ESP `delivered` означает только приём сервером, а не Inbox. Для small/mid-volume отправителей особенно ценны непрерывное multi-provider placement-наблюдение, разбор MPP/image-proxy/security-scanner opens и понятная граница между delayed Google Postmaster и отсутствием Outlook/Exchange visibility. Практический workflow: при внезапном падении сегментировать ISP, сверить complaint/bounce и Postmaster, ограничить следующий send engagement-сегментом, затем проверить placement.

## Useful Comment Artifacts
- Один комментарий прямо формулирует, что `delivered` не показывает Inbox versus Spam — это объясняет денежный и операционный blind spot.
- Агентский комментарий описывает multi-client reporting как spreadsheet-heavy и отмечает ненадёжность Outlook monitoring; продукту нужны provider-level confidence и evidence freshness.
- Ветка о MPP, Google Image Proxy и security scanners требует отделять machine activity от human engagement до сегментации и решения о recovery send.
- Комментарий о Postmaster называет двухдневную задержку и отсутствие Outlook/Exchange visibility; console должен маркировать telemetry lag и источник покрытия.
- Диагностический ответ советует не масштабировать send при резком падении, а проверить ISP pattern, bounce/complaint и opt-in evidence.

## Parsing Gaps
- Поисковая выдача раскрыла 11 полезных видимых комментариев/ответов, но Reddit не показывает надёжный total и может скрывать expandable/deleted branches.
- Повторить проверку в следующий eligible calendar-day run, чтобы попытаться определить полный count.

## Source
- [Original thread](https://www.reddit.com/r/StopSpamFolders/comments/1tkm3lg/spent_3_weeks_figuring_out_why_our_emails_stopped/)
