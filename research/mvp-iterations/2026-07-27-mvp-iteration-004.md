# MVP Iteration 004 - 2026-07-27

## Snapshot

- Weekday: Monday
- Version: 004
- Based on sample through: 2026-07-23 (no accepted signal since the prior iteration)
- Reviewed MVP files: `2026-07-24-mvp-iteration-003.md`
- Reviewed product spec files: `2026-07-21-product-spec-001.md`

## Potential MVP

An explainable email-delivery incident console for low- and mid-volume senders. It collects headers, NDRs, ESP exports, provider/seed observations, and operator context; separates authentication, sender/pool reputation, blocklists, provider verdicts, placement, content, list health, cadence, and measurement; and returns ranked, evidence-scoped hypotheses with the next safe action and a redacted escalation packet.

## Finalized Decisions

- Ship a workflow and evidence product, not a sending platform, warm-up service, inbox guarantee, or universal reputation score.
- SPF/DKIM/DMARC pass is necessary input, never case closure; provider and recipient scope remain first-class.
- Preserve distinct states for Inbox, Promotions, Spam/Junk, Quarantine, Bounce/Rejection, Silent Drop, and Not Observable.
- Launch manual imports and deterministic rules before fragile provider integrations; display provenance, freshness, uncertainty, and disconfirming evidence.

## Changes

- Make provider/flow placement matrix, preflight probe labelling, bounce-surge triage, and shared-ESP/IP escalation packet core paths.
- Add transactional stream intake alongside marketing flows and compare outcomes by provider, route, flow, and time window.

## Fixes

- Prevent aggregate opens, bounces, reply rates, or “sent” status from being mistaken for inbox placement.
- Guard against blind domain replacement, broad warm-up, artificial engagement, or repeat sends without an evidence threshold.

## Requirements

- Case intake for identity, sender/ESP/pool, flow, volume/cadence change, target provider, impact, headers/NDRs, and redacted message IDs.
- Evidence graph with source provenance, confidence, contradictions, owner, freshness, and recheck date.
- Transparent rule engine: hypothesis, supporting/disconfirming observations, missing evidence, safety guardrail, remediation runbook, verification step.
- Portfolio/case view, provider-placement matrix, support-ready packet, and scheduled rechecks; multi-tenant RBAC and redaction by default.

## Majority Needs Covered

- Authentication is green but Gmail/Outlook still junk, reject, or silently filter mail.
- Existing ESP/provider dashboards leave low-volume senders without actionable visibility.
- Operators need to distinguish content/list/cadence, shared-pool reputation, and provider policy before escalating or resending.

## Proposed MVP Shape

- Intake and parser -> normalized evidence board -> deterministic hypothesis/rule evaluation -> remediation and escalation workflow -> controlled verification/recheck.
- Initial screens: portfolio, incident intake, evidence board, provider matrix, hypothesis/runbook, and support-packet export.
- Treat Postmaster, SNDS, ESP, and seed adapters as optional `EvidenceSource` connectors after paid design-partner validation.

## Pros

- Directly addresses repeated high-urgency ambiguity rather than adding another isolated score.
- Small TypeScript monolith with managed services can reach useful manual-first value quickly.
- Case history, scheduled rechecks, and reusable packets create agency/MSP retention.

## Cons

- Provider opacity limits certainty; the product must never over-promise placement.
- Sensitive artifacts and incomplete manual evidence require careful UX, redaction, tenancy, and confidence controls.

## Open Questions

- Which first paid wedge has the strongest repeat incident frequency: agencies/MSPs, SaaS ops, or ecommerce/Klaviyo teams?
- Which connector creates paid retention first: Postmaster, SNDS, SES, or a major ESP export?
- What evidence threshold blocks risky remediation rather than merely lowering confidence?

## Investor View

### Value And Problem

- Severe, revenue-sensitive incidents combine opaque provider decisions with scattered tools; wrong remediation prolongs harm or worsens reputation.
- The product closes the majority need for provider-scoped explanation, evidence collection, and safe next actions when standard authentication checks are insufficient.

### Business Model

- SaaS meter: monitored domain/flow, active incidents, seats, retained evidence, and agency client workspaces; add paid probes, connectors, white-label reports, and escalation workflows.
- Rule-first architecture scales software margins; keep expert services optional and productized.

### Market And Competitors

- TAM: business-email senders; SAM: SMB SaaS, ecommerce, agencies, MSPs, and B2B teams with recurring placement incidents; beachhead is low/mid-volume senders underserved by enterprise tooling.
- Alternatives: ESP dashboards, Postmaster/SNDS, MXToolbox, GlockApps, Validity/Everest, consultants, and spreadsheets. Differentiation is cross-provider incident workflow with explicit uncertainty.

### Marketing And Sales

- Acquire through a free header/NDR diagnostic, incident-intent content, ESP/community partnerships, and agency/MSP or consultant referrals.
- Retain through case history, rechecks, evidence freshness, reusable support packets, and multi-domain alerting.

### Top Risks

- False certainty: mitigate with provenance, confidence, disconfirming evidence, and visible unknowns.
- Premature integration cost: mitigate with manual-first workflow and paid-design-partner gates per adapter.
- Category crowding: mitigate by owning incident coordination and measured time-to-next-action, not generic scoring.

## Evidence Base

- [MVP iteration 003](2026-07-24-mvp-iteration-003.md)
- [Product specification 001](../product-specs/2026-07-21-product-spec-001.md)
- [Authenticated transactional spam rejection](../signals/2026-07-23-brevo-community-authenticated-transactional-spam-rejection.md)
- [Seed-test preflight gap](../signals/2026-07-22-reddit-emailmarketing-seed-test-preflight-gap.md)
- [Promotions visibility gap](../signals/2026-07-22-reddit-emailmarketing-promotions-visibility-gap.md)
- [Provider-scoped reputation feedback gap](../signals/2026-06-23-reddit-digitalmarketing-provider-scoped-feedback-gap.md)
- [Gmail-concentrated bounce surge](../signals/2026-06-15-reddit-klaviyo-gmail-bounce-spike.md)
