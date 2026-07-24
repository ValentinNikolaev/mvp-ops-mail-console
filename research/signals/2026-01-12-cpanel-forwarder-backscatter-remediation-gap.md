---
title: "Spam-forwarding protection creates backscatter and frozen retries"
source: "cPanel Community"
url: "https://support.cpanel.net/hc/en-us/community/posts/37610886986775"
published_at: "2026-01-12T14:22:00Z"
discovered_at: "2026-07-22T23:02:26+02:00"
pain_type: "blocklist_vs_reputation"
segment: "mid-volume"
confidence: "high"
tags:
  - "cpanel"
  - "exim"
  - "forwarding"
  - "backscatter"
  - "rbl"
  - "remediation"
canonical_id: "2026-01-12-cpanel-forwarder-backscatter-remediation-gap"
---

## Summary
Администратор включил защиту cPanel, запрещающую пересылку spam-писем на внешний адрес, но стандартный `:fail:` генерирует bounce исходному спамеру. Когда его сервер отклоняет bounce по RBL, Exim замораживает сообщение и повторяет доставку. Рабочий обход — silently blackhole пересылаемую копию — перезаписывается обновлениями cPanel; в июле вендор подтвердил, что поддерживаемого backport для текущих LTS-релизов нет.

## Why It Matters
Консоль должна отличать inbound anti-spam decision от исходящего backscatter-инцидента: связывать правило/версию конфигурации, bounce, frozen queue, RBL rejection и риск репутации. Нужен explainable remediation path: безопасно подавить bounce, зафиксировать временный workaround, предупредить о его overwrite при update и показать ожидаемую версию vendor fix.

## Evidence
Поток показывает последовательность «spam detection → external forward blocked → bounce to spammer → RBL rejection → frozen retries». Одиннадцать комментариев подтверждают, что локальный blackhole workaround работает, но update его перезаписывает, а поддерживаемый fix остаётся недоступным до cPanel 138+.

## Comment Insights
Полный разбор 11 комментариев сохранён в [artifact](../comments/2026-01-12-cpanel-forwarder-backscatter-remediation-gap-comments.md): главный пробел — не отсутствие антиспам-правила, а отсутствие устойчивого, поддерживаемого no-backscatter remediation workflow.

## Source
- [Original source](https://support.cpanel.net/hc/en-us/community/posts/37610886986775)
