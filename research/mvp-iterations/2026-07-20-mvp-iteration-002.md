# MVP Iteration 002 - 2026-07-20

## Snapshot

- Weekday: Monday
- Version: 002
- Based on sample through: 2026-07-20 (refined at 23:03:20)
- Reviewed MVP files: `2026-07-17-mvp-iteration-001.md`
- Reviewed product spec files: none available

## Potential MVP

An evidence-led deliverability incident console for low- and mid-volume senders. It ingests headers/NDRs, sender and campaign context, provider telemetry, and placement probes; classifies the failure layer; exposes uncertainty; and assigns a prioritized recovery runbook plus escalation packet. It joins reputation, blocklists, provider feedback, inbox placement, and remediation in one explainable case view.

## Finalized Decisions

- Remain a diagnosis-and-workflow layer, not an ESP, scoring oracle, or inbox guarantee.
- Treat provider verdicts, headers, actual DMARC alignment, and seed placement as stronger evidence than published DNS, generic blacklist tools, open rate, or aggregate delivery.
- Model low-volume/no-data and hidden provider reasons explicitly as `unknown` with a safe next evidence action.
- Keep marketing, transactional, and 1:1 flows separate in the evidence model; reputation spillover is a hypothesis to test, not an assumption.
- Treat forwarding-path failure as a separate, scoped hypothesis: it can invalidate SPF/DKIM on a received copy but must not overwrite evidence of a broader sender-reputation incident.

## Changes

- Add a business-outcome intake: reply-rate drop, revenue/support impact, segment and provider breakdown, with an automatic “placement hypothesis” when open/reply divergence appears.
- Add provider/flow placement matrix: Gmail, Outlook.com, Yahoo, corporate Microsoft 365, plus manual seed evidence, BCL/SCL and quarantine status where available.
- Add campaign-to-domain lineage: From, Return-Path, DKIM d=, SPF domain, sending IP/pool, ESP, subdomain/root relationship, and `on-behalf-of` status.
- Add forwarding-aware trace evidence: original versus forwarded recipient path, authentication result per hop, and a guardrail against changing DMARC policy to solve general Junk placement.

## Fixes

- Do not diagnose a campaign from published SPF/DKIM alone; parse actual alignment and aggregate reports.
- Do not suggest blind warm-up, domain swaps, or provider migration as root-cause proof; preserve baseline, change, and re-test evidence.
- Do not collapse a one-recipient forwarding exception into the campaign diagnosis; require a provider/recipient pattern before labeling the incident as reputation-driven.
- Prevent aggregate delivery, bounce rate, and open rate from being displayed as inbox-placement success.

## Requirements

- Header/NDR parser for SPF/DKIM/DMARC alignment, SMTP code, SCL/BCL, provider routing, EHLO/PTR, and IP evidence.
- Per-hop evidence capture for forwarded messages, including original and post-forward authentication outcomes.
- Incident evidence board with source, time, confidence, competing hypotheses, owner, next action, and scheduled recheck.
- Placement-test/manual probe capture with per-provider and per-flow results; support `not observable` states.
- Campaign/list-health inputs: opt-in evidence, complaints, engagement window, volume/cadence change, recent DNS change, and suppressed segment count.
- Guided runbooks: stop/isolate, auth repair, evidence collection, recipient/provider escalation, controlled re-entry, and outcome verification.
- Exportable support packet that redacts sensitive identifiers but retains decisive headers and timestamps.

## Majority Needs Covered

- Authentication passes but Gmail/Outlook still classifies messages as Spam/Junk.
- Low-volume senders have no usable Postmaster/SNDS evidence or provider explanation.
- SMTP/ESP success masks silent drop, quarantine, or non-inbox placement.
- Operators cannot tell whether reply/engagement loss is marketing performance or provider filtering.
- Teams need a repeatable recovery path instead of tool-hopping, generic blacklists, and consultant guesswork.

## Proposed MVP Shape

- Intake: paste headers/NDR, describe sender, campaign, provider, volume, and customer impact.
- Evidence board: auth and identity, reputation/blocklists, provider feedback, placement probes, list/campaign context, and explicit unknowns.
- Decision engine: transparent rules produce ranked hypotheses, missing evidence, confidence, and guardrails.
- Remediation workspace: owned checklist, pause/segment/re-entry plan, recheck schedule, escalation copy, and before/after record.
- Portfolio view: domains, flows, unresolved incidents, evidence freshness, and change alerts for agencies/MSPs.

## Pros

- Directly addresses the repeated gap between “sent/authenticated” and “in inbox/replied.”
- Rule-first, manual-evidence MVP is affordable, fast to build, auditable, and useful before costly integrations.
- Strong agency/MSP value: standardized incident triage across many small senders and reusable support packets.

## Cons

- Provider reputation remains opaque; guidance cannot guarantee placement or recovery time.
- High-fidelity placement and provider data may require paid seedlists, permissions, or fragile integrations.
- Bad/incomplete user evidence can still yield only a constrained hypothesis.

## Open Questions

- Which first buyer converts best: MSP/agency, SaaS ops team, or self-serve ecommerce operator?
- What placement-probe coverage is useful before paid seedlist cost outweighs early value?
- Which low-risk integrations can ship first: Google Postmaster, Microsoft SNDS, SES, ESP exports, or manual upload?

## Investor View

### Value And Problem

- Severity is high: lost replies, sales, transactional completion, and support time occur while conventional “all green” checks provide no root cause.
- The wedge is an explainable path from observable symptoms to the next safe action for telemetry-poor senders, not a claim to predict provider reputation.

### Business Model

- SaaS tiers by monitored domain/flow and retained incident history; paid placement credits, integrations, agency seats, and white-label support packets expand ARPA.
- Scales with low-cost parsing/rules and tenant isolation; human support must be constrained by playbooks and evidence-quality gates.

### Market And Competitors

- TAM: organizations that send business email; SAM: SMBs, ecommerce teams, SaaS, agencies, and MSPs with recurring placement incidents; SOM: low/mid-volume operators underserved by enterprise deliverability consulting.
- Alternatives: GlockApps/Validity seed monitoring, MXToolbox, ESP dashboards, Google Postmaster/SNDS, and consultants.
- Differentiation: cross-provider evidence synthesis and remediation workflow for low-volume/no-data cases, not another isolated score.

### Marketing And Sales

- Acquire via free header/DMARC-alignment diagnostic, incident-led SEO/community content, ESP implementers, MSP/agency partners, and deliverability consultants.
- Retain with incident history, evidence-freshness alerts, scheduled rechecks, provider packets, and multi-domain workflow memory.

### Top Risks

- Opaque provider data can create false certainty; mitigate with evidence provenance, confidence, alternatives, and explicit unknown outcomes.
- Expensive/brittle integrations and seed tests; mitigate with manual ingestion first and connector rollout only after paid demand.
- Crowded trust-sensitive category; mitigate with narrow incident workflow, strict no-guarantee language, and verified provider evidence.

## Evidence Base

- [Reply-rate placement diagnosis](../signals/2026-07-20-reddit-emailmarketing-reply-rate-placement-diagnosis.md)
- [Campaign spillover reputation](../signals/2026-07-19-reddit-emailmarketing-campaign-spillover-reputation.md)
- [Low-maintenance recovery demand](../signals/2026-07-18-reddit-emaildeliverability-low-maintenance-recovery.md)
- [Gmail low-volume feedback gap](../signals/2026-06-01-gmail-community-domain-reputation-escalation.md)
- [Microsoft S3150 verdict gap](../signals/2025-12-10-serverfault-microsoft-blocklist-verdict-gap.md)
- [New-domain reputation versus DMARC](../signals/2026-05-22-serverfault-new-domain-reputation-vs-dmarc.md)
- [Iteration 001](2026-07-17-mvp-iteration-001.md)
