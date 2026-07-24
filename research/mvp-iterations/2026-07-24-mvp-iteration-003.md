# MVP Iteration 003 - 2026-07-24

## Snapshot

- Weekday: Friday
- Version: 003
- Based on sample through: 2026-07-23
- Reviewed MVP files: `2026-07-20-mvp-iteration-002.md`
- Reviewed product spec files: `2026-07-21-product-spec-001.md`

## Potential MVP

An explainable delivery-ops console for low- and mid-volume senders that turns scattered evidence into one incident workspace. The product ingests headers, NDRs, ESP exports, provider telemetry, seed/probe results, message IDs, and operator context; separates authentication, identity, reputation, blocklists, provider verdicts, placement, content, list health, and cadence; then produces a ranked hypothesis, missing-evidence checklist, remediation plan, and support-ready escalation packet.

## Finalized Decisions

- Stay workflow-first: the MVP diagnoses and coordinates remediation; it does not send mail, sell warm-up, or promise inbox placement.
- Treat SPF/DKIM/DMARC pass as necessary evidence, not proof of deliverability.
- Make provider scope a first-class dimension: Gmail, Outlook.com, corporate Microsoft 365, Yahoo, and smaller hosts can diverge materially.
- Model shared ESP/IP risk separately from sender-domain configuration so one DNS fix cannot falsely close a case.
- Label Promotions, Spam/Junk, Bounce/Rejection, Quarantine, Silent Drop, and Unknown as separate states.
- Keep low-volume/no-data cases explicit; the next best evidence action is part of the product value.

## Changes

- Elevate pre-send placement preflight from optional probe to a core workflow for risky campaigns.
- Add transactional-stream intake alongside marketing campaigns because welcome/API mail can fail even with verified DKIM/DMARC.
- Add bounce-surge triage that requires provider segmentation, reason-code mix, and stop/send-lane guardrails before another broad send.
- Add shared-pool escalation mode: collect message IDs, sending IP/pool, timeline, domain alignment, and provider stats for ESP support.
- Add category-aware placement tracking so Promotions findings are not treated as Spam findings.

## Fixes

- Prevent aggregate bounce, delivery, open, or reply metrics from being interpreted without provider and flow scope.
- Do not recommend domain swaps, broad warm-up, or artificial engagement without evidence that the current lane is irrecoverable.
- Do not collapse provider advice into a closed diagnosis; record whether the provider actually supplied account-specific evidence.
- Do not let seed tests overclaim recipient truth; label coverage, freshness, provider, account type, and sample size.

## Requirements

- Intake for sender identity, flow type, ESP, campaign or transactional stream, volume/cadence change, business impact, and target providers.
- Header/NDR parser for SPF, DKIM, DMARC alignment, SMTP code, SCL/BCL, Return-Path, DKIM d=, sending IP, EHLO/PTR, forwarding hops, and provider routing.
- Evidence board with provenance, freshness, confidence, contradictory observations, unknowns, owner, and scheduled recheck.
- Provider placement matrix supporting Inbox, Promotions, Spam/Junk, Quarantine, Bounce/Rejection, Silent Drop, and Not Observable.
- Reason-code and provider anomaly view for sudden bounce or rejection spikes.
- Shared ESP/IP evidence pack with message IDs, dates, recipients redacted by default, pool/IP context, auth state, and provider verdicts.
- Remediation workspace for pause/quarantine, content isolation test, list/cadence adjustment, support escalation, controlled re-entry, and verification.

## Majority Needs Covered

- "Authentication is green but Gmail/Outlook still spam, reject, or block."
- "The ESP says sent or authenticated but cannot explain provider placement."
- "Low-volume senders have too little Postmaster/SNDS data to know what changed."
- "A campaign metric collapsed, but the team cannot tell whether it is content, reputation, provider filtering, or measurement."
- "Seed checks exist, but teams need provider-scoped, cautious preflight and recheck workflows."
- "Shared IP or ESP reputation may be involved, but the operator needs evidence before escalation."

## Proposed MVP Shape

- Case intake: manual upload/paste plus structured questions about sender, flow, provider, volume, and impact.
- Evidence board: auth/identity, reputation/blocklists, provider feedback, placement probes, bounce verdicts, content/list/cadence, ESP/shared-pool context, and unknowns.
- Rule engine: transparent ranked hypotheses with disconfirming evidence and the next required observation.
- Remediation plan: stop/isolate, test, escalate, re-enter, and verify with owners and due dates.
- Portfolio view: monitored domains/flows, active incidents, evidence freshness, provider risk, and unresolved escalations for agencies/MSPs.

## Pros

- Directly matches repeated operator pain where standard checks are green but delivery outcomes remain bad.
- Cheap and fast to ship with manual ingestion, deterministic rules, and managed infrastructure.
- Strong expansion path into agencies/MSPs because cross-client memory and support packets reduce repeated triage labor.
- Useful even when providers expose little data, because the product can organize uncertainty and the next evidence step.

## Cons

- Cannot eliminate provider opacity; it can only make hypotheses and escalation stronger.
- Manual inputs can be incomplete or wrong, so UX must enforce evidence quality without becoming slow.
- Seed/probe data is directional and may create false confidence if poorly labeled.
- Provider and ESP integrations are retention drivers but add permission, privacy, and maintenance complexity.

## Open Questions

- Is the sharpest initial wedge a free incident diagnostic, agency/MSP workspace, or ecommerce/Klaviyo-focused preflight tool?
- Which first connector is most worth automating: Google Postmaster, Microsoft SNDS, Klaviyo export, Brevo export, SES, or seed-list provider?
- What minimum evidence threshold should block high-risk remediation recommendations?
- Should transactional and marketing incidents share the same pricing meter or be separate product lanes?

## Investor View

### Value And Problem

- Problem solved: operators lose revenue, replies, onboarding completion, and support time while each tool shows only one fragment of the truth.
- Severity is high because the failure is urgent, ambiguous, and reputation-sensitive; repeated wrong remediation can make the incident worse.

### Business Model

- SaaS priced by monitored domain/flow, active incidents, seats, retained evidence history, and agency workspaces.
- Expansion revenue from paid probes, provider connectors, white-label reports, and premium escalation packet workflows.
- Scales if the product stays rule-first and evidence-first; human expert services should be packaged as add-ons, not required for every case.

### Market And Competitors

- TAM: all organizations sending business email; SAM: SMB ecommerce, SaaS, agencies, MSPs, and B2B outbound teams with recurring provider-placement incidents; SOM: low/mid-volume operators underserved by enterprise deliverability tools.
- Competitors and substitutes: ESP dashboards, Google Postmaster, Microsoft SNDS, MXToolbox, GlockApps, Validity/Everest, consultants, and ad hoc spreadsheets.
- Likely USP: a cross-provider incident workflow that explains uncertainty and turns evidence into remediation, instead of another isolated score or checklist.

### Marketing And Sales

- Best CAC channels: free header/NDR diagnostic, "why did Gmail/Outlook block me" incident SEO, ESP/community answers, agency/MSP partnerships, and deliverability consultant referrals.
- Retention optimization: case history, scheduled rechecks, provider-specific evidence freshness, reusable support packets, and multi-domain portfolio alerts.

### Top Risks

- False certainty damages trust; mitigate with confidence levels, provenance, disconfirming evidence, and explicit unknowns.
- Integrations become expensive before demand is proven; mitigate with manual upload first and paid-design-partner gating for each connector.
- Crowded category with skeptical buyers; mitigate by focusing on incident workflow, provider-scoped evidence, and measurable time saved.

## Evidence Base

- [MVP iteration 002](2026-07-20-mvp-iteration-002.md)
- [Product specification 001](../product-specs/2026-07-21-product-spec-001.md)
- [Authenticated transactional spam rejection](../signals/2026-07-23-brevo-community-authenticated-transactional-spam-rejection.md)
- [Gmail-concentrated bounce surge](../signals/2026-06-15-reddit-klaviyo-gmail-bounce-spike.md)
- [Seed-test preflight gap](../signals/2026-07-22-reddit-emailmarketing-seed-test-preflight-gap.md)
- [Promotions visibility gap](../signals/2026-07-22-reddit-emailmarketing-promotions-visibility-gap.md)
- [Provider-scoped reputation feedback gap](../signals/2026-06-23-reddit-digitalmarketing-provider-scoped-feedback-gap.md)
- [Shared ESP IP reputation block](../signals/2026-04-07-brevo-community-shared-ip-reputation-block.md)
