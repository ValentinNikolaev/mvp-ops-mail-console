---
title: "SES false permanent bounces suppress active Gmail recipients"
source: "AWS re:Post"
url: "https://repost.aws/de/questions/QUutjw2okCQcauMIJMAS821A/ses-sometimes-fails-to-reach-existing-email-accounts"
published_at: "2026-02-05T01:20:24Z"
discovered_at: "2026-07-16T23:28:48+02:00"
pain_type: "root_cause_visibility"
segment: "mid-volume"
confidence: "high"
tags:
  - "aws-repost"
  - "ses"
  - "false-bounce"
  - "suppression-list"
  - "gmail"
  - "remediation-workflow"
canonical_id: "2026-02-05-aws-repost-ses-false-bounce-suppression"
---

## Summary
Отправитель SES видит, как существующие Gmail-адреса периодически получают 5.1.1 permanent bounce и попадают в account-level suppression list, хотя затем снова работают после ручного unsuppress. Программный unsuppress снижает ущерб, но не гарантирует доставку и не объясняет, временная ли это ошибка recipient provider или неверная классификация.

## Why It Matters
Консоль должна связывать bounce diagnostic, suppression mutation и последующий успешный delivery, чтобы помечать вероятные false permanent bounces. Нужны защищённые remediation steps: holdout/retry policy, audit trail, threshold для auto-unsuppress и готовый пакет фактов для provider support.

## Evidence
"Our clients randomly stop receiving emails due to this" и адреса "work again once manually removed from the suppression list."

## Source
- [Original source](https://repost.aws/de/questions/QUutjw2okCQcauMIJMAS821A/ses-sometimes-fails-to-reach-existing-email-accounts)
