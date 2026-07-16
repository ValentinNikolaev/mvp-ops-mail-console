---
title: "Spam detection issue in emails sent to Office 365 enterprise customers!!!"
source: "Microsoft Q&A"
url: "https://learn.microsoft.com/en-us/answers/questions/5813892/spam-detection-issue-in-emails-sent-to-office-365"
published_at: "2026-03-09T09:49:57Z"
discovered_at: "2026-07-16T23:02:46+02:00"
pain_type: "auth_ok_delivery_bad"
segment: "mid-volume"
confidence: "high"
tags:
  - "microsoft-qa"
  - "office-365"
  - "shared-ip"
  - "authentication-pass"
  - "false-positive"
  - "remediation"
canonical_id: "2026-03-09-microsoft-shared-ip-auth-pass-spam"
---

## Summary
Почтовый хостинг сообщает, что письма нескольких клиентов в Office 365 уходят в Spam, хотя SPF, DKIM, DMARC, PTR и RBL уже проверены. В полезном комментарии Microsoft объясняет, что EOP оценивает репутацию общего sending IP целиком, и предлагает recipient-admin false-positive submission и изолированный plain-text тест без ссылок и вложений.

## Why It Matters
Это прямой запрос на объяснимый remediation workflow: показать, что auth и blocklist-проверки не закрывают shared-IP reputation, собрать provider-specific evidence и выдать следующий шаг, который требует действия у получателя.

## Evidence
"Dmarc, DKIM, SPF, RBL, and PTR were all checked"; Microsoft отвечает, что при shared IP EOP оценивает репутацию IP "as a whole".

## Source
- [Original source](https://learn.microsoft.com/en-us/answers/questions/5813892/spam-detection-issue-in-emails-sent-to-office-365)
