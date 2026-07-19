---
title: "Campaign reputation spillover threatens everyday mail"
source: "Reddit Emailmarketing"
url: "https://www.reddit.com/r/Emailmarketing/comments/1t20vna/gmail_is_flagging_our_main_domain_as_spam_even/"
published_at: "2026-05-02T00:00:00+00:00"
discovered_at: "2026-07-19T17:04:13+02:00"
pain_type: "blocklist_vs_reputation"
segment: "mid-volume"
confidence: "high"
tags:
  - "gmail"
  - "domain-reputation"
  - "campaign-isolation"
  - "postmaster"
  - "remediation"
canonical_id: "2026-07-19-reddit-emailmarketing-campaign-spillover-reputation"
---

## Summary
Команда после двух 100k кампаний через Mailchimp увидела Gmail spam placement не только для campaign sender, но и для обычных Google Workspace reply с основного домена. SPF, DKIM, DMARC, list hygiene и публичные reputation checks были зелёными, поэтому перед следующей отправкой ей не хватает объяснимого решения: что именно ухудшилось, какие домены/потоки связаны и когда безопасно возобновить отправку.

## Why It Matters
MVP-консоль должна отделять authentication и public blocklists от provider-specific placement/reputation, связывать campaign и corporate streams по organizational domain/DMARC alignment и выдавать stop/go remediation runbook. Это закрывает риск, когда bulk reputation incident становится операционной проблемой для ежедневной почты, а ESP abuse metrics не объясняют Gmail verdict.

## Evidence
Автор сообщает, что после segmented 200k send «even routine reply emails» с основного домена стали попадать в spam, хотя authentication и внешние проверки выглядели нормальными.

## Comment Insights
См. [артефакт комментариев](../comments/2026-07-19-reddit-emailmarketing-campaign-spillover-reputation-comments.md). Комментарии требуют приостановить следующий send, различать subdomain и отдельный sibling domain, проверить Postmaster по обоим доменам, DMARC alignment, recipient consent и provider-side complaint signals, а не только ESP dashboard.

## Source
- [Original source](https://www.reddit.com/r/Emailmarketing/comments/1t20vna/gmail_is_flagging_our_main_domain_as_spam_even/)
