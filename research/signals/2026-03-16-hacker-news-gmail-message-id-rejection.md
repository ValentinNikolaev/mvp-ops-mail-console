---
title: "Major European payment processor can't send email to Google Workspace users"
source: "Hacker News"
url: "https://news.ycombinator.com/item?id=46989217"
published_at: ""
discovered_at: "2026-07-16T23:28:48+02:00"
pain_type: "silent_drop_or_throttle"
segment: "mid-volume"
confidence: "high"
tags:
  - "hacker-news"
  - "google-workspace"
  - "hard-rejection"
  - "message-id"
  - "provider-policy"
  - "support-gap"
canonical_id: "2026-03-16-hacker-news-gmail-message-id-rejection"
---

## Summary
Европейский платежный провайдер не мог доставить verification emails пользователям Google Workspace: Gmail отклонял сообщения без заголовка Message-ID до inbox/spam. Полезные комментарии показывают более широкую проблему: auth и RFC-совместимость не гарантируют доставку, а у Google и Microsoft есть разные, непрозрачные provider-specific правила и слабый путь эскалации для малого отправителя.

## Why It Matters
Консоль должна отличать SMTP hard rejection от spam placement, проверять критические headers и показывать provider-specific compatibility risk. Нужны доказательства по mailbox/provider, понятный owner remediation и escalation packet, а не общий совет проверить SPF/DKIM.

## Evidence
"Google's mail servers reject the message outright. It doesn't even get a chance to land in spam." Комментарий: "deliverability in praxis is something you cannot just test and can break at any time."

## Source
- [Original source](https://news.ycombinator.com/item?id=46989217)
