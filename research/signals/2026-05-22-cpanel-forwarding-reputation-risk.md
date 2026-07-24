---
title: "Why does forwarding mail off the server hurt my server's mail reputation?"
source: "cPanel Community"
url: "https://support.cpanel.net/hc/en-us/articles/1500007071781-why-does-forwarding-mail-off-the-server-hurt-my-server-s-mail-reputation"
published_at: "2026-05-22T00:00:00Z"
discovered_at: "2026-07-21T00:03:27+02:00"
pain_type: "auth_ok_delivery_bad"
segment: "low-volume"
confidence: "high"
tags:
  - "cpanel"
  - "forwarding"
  - "spf"
  - "sender-reputation"
  - "remediation"
canonical_id: "2026-05-22-cpanel-forwarding-reputation-risk"
---

## Summary
Пересылка всей входящей почты с хостингового сервера на внешний ящик создаёт двойной риск: пересланный спам выглядит для получателя как исходящий с сервера и ухудшает его репутацию, а даже легитимные пересланные письма могут потерять SPF и попасть в Spam. Для небольшого хостингового отправителя это выглядит как необъяснимая placement-проблема, хотя DNS и собственные исходящие письма могут быть в порядке.

## Why It Matters
Консоль должна отдельно распознавать forwarding/relay path, отличать первичное исходящее письмо от пересланной копии и запрещать общую remediation-рекомендацию по репутации без проверки этого пути. Нужны evidence capture для original sender, forwarding host, ARC/SPF/DKIM per-hop и безопасные альтернативы пересылке.

## Evidence
cPanel прямо указывает, что relayed spam выглядит так, будто его отправил пересылающий сервер, а forwarding легитимной почты способен сломать SPF и сделать её похожей на spam.

## Comment Insights
Комментарии недоступны: это справочная статья без обсуждения.

## Source
- [Original source](https://support.cpanel.net/hc/en-us/articles/1500007071781-why-does-forwarding-mail-off-the-server-hurt-my-server-s-mail-reputation)
