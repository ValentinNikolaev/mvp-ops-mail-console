# MVP Iteration 005 - 2026-07-31

## Snapshot

- Weekday: Friday
- Version: 005
- Based on sample through: 2026-07-30
- Reviewed MVP files: `2026-07-27-mvp-iteration-004.md`
- Reviewed product spec files: `2026-07-28-product-spec-005.md`

## Potential MVP

A manual-first, read-only email-delivery incident workbench for agencies and MSPs. It turns headers, NDRs, ESP exports, seed observations, and operator notes into a provider-scoped evidence timeline, bounded deterministic hypotheses, safe next tests, and a redacted escalation packet. It is not a sender, warm-up tool, inbox guarantee, or universal reputation score.

## Finalized Decisions

- Start with the agency/MSP buyer handling repeated Gmail and Microsoft 365 delivery escalations.
- Own the packet and decision record: observed facts, inference, confidence, missing/contradictory evidence, rule version, safe action, and verification date.
- Keep evidence ingestion read-only and remediation human-approved; apply redaction, tenant isolation, retention, and audit controls on the first path.

## Changes

- Narrow v1 from a broad incident console to one incident workspace and an exportable provider/ESP support packet.
- Use four initial evidence inputs: headers, NDRs, ESP delivery/bounce export rows, and seed observations.

## Fixes

- Do not label hypotheses as diagnosis or infer inbox placement from sent/open aggregates.
- Block risky advice when evidence is incomplete; return `confirmed`, `suspected`, or `insufficient evidence` plus the smallest next collection step.

## Requirements

- Canonical incident schema for identities, auth alignment, route, recipient provider, SMTP/NDR code, pool/IP, timestamps, source provenance, sensitivity, and freshness.
- Eight to twelve versioned deterministic rules for auth-pass spam placement, explicit 4xx/5xx/policy rejection, shared-pool suspicion, list/cadence/content changes, forwarding/path issues, and not-observable outcomes.
- Case-completeness rubric, redaction preview, immutable audit events, packet export, and scheduled outcome recheck.
- Measure baseline and pilot outcomes: time-to-triage, time-to-escalation, packet acceptance, recurrence, and operator throughput.

## Majority Needs Covered

- Explain Gmail/Outlook junk, rejection, or silent filtering after SPF/DKIM/DMARC pass.
- Close low-volume/provider-scoped visibility gaps without claiming unsupported causal certainty.
- Replace scattered dashboards, headers, and consultant/spreadsheet work with an evidence-backed safe next action.

## Proposed MVP Shape

- One guided case: paste/upload evidence -> normalize redacted facts -> assess completeness -> evaluate bounded rules -> create provider/ESP packet and recheck.
- First supported scope: Gmail and Microsoft 365 cases; defer connectors, continuous monitoring, collaboration suites, predictive scoring, and automatic changes.
- Validate against 20–30 historical agency/MSP incidents before adding integrations; select a connector only when it improves paid retention.

## Pros

- Directly addresses the sample's recurring diagnosis, visibility, and remediation-coordination failure.
- Manual-first reduces permissions, integration, and false-certainty risk while producing value on one incident.
- Reusable packets, rules, and case history compound across agency client workspaces.

## Cons

- Incomplete provider evidence can make the output feel like polished documentation unless it demonstrably shortens escalation work.
- Mail artifacts are sensitive and provider behavior opaque, requiring strong privacy controls and disciplined uncertainty UX.

## Open Questions

- Will agencies/MSPs pay for faster, defensible packets versus a service/process improvement?
- Which concrete packet earns adoption first: client brief, ESP ticket, or provider escalation?
- What measurable improvement threshold validates recurring SaaS rather than paid assisted triage?

## Investor View

### Value And Problem

- The recurring, revenue-sensitive pain is not lack of deliverability advice; it is converting contradictory evidence into a defensible provider-specific decision and escalation.
- Severity is high when sender reputation, campaign revenue, or transactional mail is at risk, but the product must prove time saved and safer action before claiming resolution impact.

### Business Model

- Price agency/client workspaces with active-incident or monitored-domain limits; add retained evidence, white-label packets, and validated connectors after core workflow fit.
- A rule-first, multi-tenant workflow has SaaS margins; optional expert review can seed rules without becoming the default delivery model.

### Market And Competitors

- Beachhead: agencies/MSPs and consultants with repeated client incidents; expansion: SMB SaaS and ecommerce operations underserved by enterprise deliverability suites.
- Alternatives include ESP dashboards, Postmaster/SNDS, GlockApps, Validity/Everest, MXToolbox, consultants, ticketing, and spreadsheets. Differentiation is an auditable cross-provider incident packet, not another score.

### Marketing And Sales

- Acquire through a free header/NDR case-completeness check, incident-intent content, deliverability consultant referrals, and agency/MSP design partners.
- Retain through repeatable packets, evidence history, rechecks, client reporting, and rules that reduce preparation time across accounts.

### Top Risks

- False certainty or harmful advice: show provenance, alternatives, missing evidence, confidence gates, and human-approved reversible steps.
- Weak willingness to pay: run a 20–30-case pilot with time-to-triage and packet-acceptance baselines before broad build-out.
- Privacy/integration drag: begin with read-only manual artifacts, strict retention/redaction, and no mailbox/provider write access.

## Evidence Base

- [MVP iteration 004](2026-07-27-mvp-iteration-004.md)
- [Product specification 005](../product-specs/2026-07-28-product-spec-005.md)
- [Authenticated transactional spam rejection](../signals/2026-07-23-brevo-community-authenticated-transactional-spam-rejection.md)
- [Authenticated M365 tenant spam](../signals/2026-01-28-microsoft-community-hub-authenticated-m365-tenant-spam.md)
- [Dovecot/Rspamd Junk misclassification](../signals/2026-04-10-mailu-github-issues-rspamd-score-junk-misclassification.md)
- [Seed-test preflight gap](../signals/2026-07-22-reddit-emailmarketing-seed-test-preflight-gap.md)
