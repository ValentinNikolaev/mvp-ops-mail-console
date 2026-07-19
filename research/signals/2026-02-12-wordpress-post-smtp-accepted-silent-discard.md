---
title: "SMTP success masks malformed-header silent discard"
source: "WordPress Support"
url: "https://wordpress.org/support/topic/e-mails-showing-as-successfully-sent-not-getting-to-recipients/"
published_at: "2026-02-12T00:00:00+00:00"
discovered_at: "2026-07-19T16:02:02+02:00"
pain_type: "silent_drop_or_throttle"
segment: "low-volume"
confidence: "high"
tags:
  - "smtp-accepted"
  - "silent-discard"
  - "header-validation"
  - "evidence-gap"
canonical_id: "2026-02-12-wordpress-post-smtp-accepted-silent-discard"
---

## Summary
WordPress form notifications were logged as successful and accepted by SMTP, while every recipient saw no message and no bounce. The full SMTP transcript eventually exposed duplicate, header-like `From:` / `Subject:` lines in the generated payload; recipient providers can silently discard such malformed mail after hand-off.

## Why It Matters
The console must distinguish application success, SMTP acceptance, and recipient placement. It should request the session transcript and final queue ID, flag duplicate or header-like fields, and produce a narrow remediation checklist rather than treating a successful test email as proof that production messages arrived.

## Evidence
The user reports Post SMTP “Success” for all recipients but no deliveries or bounces. Support states that `250 Accepted / Queued` proves only that the message left WordPress, and identifies two `From:` headers as a likely silent-rejection cause.

## Comment Insights
See [comment artifact](../comments/2026-02-12-wordpress-post-smtp-accepted-silent-discard-comments.md). All eight visible replies were parsed; they preserve the diagnostic boundary and the field-level fix, while the final reporter response shows that the first formatting change still needed verification.

## Source
- [Original source](https://wordpress.org/support/topic/e-mails-showing-as-successfully-sent-not-getting-to-recipients/)
