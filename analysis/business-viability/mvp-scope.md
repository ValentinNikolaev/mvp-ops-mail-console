# MVP scope

## Smallest product that tests the core hypothesis

Primary user flow:

1. Create agency/client incident case.
2. Paste/upload headers, NDR text, ESP delivery/bounce CSV rows, seed observation, and short operator notes.
3. System extracts normalized facts and labels source, freshness, sensitivity, and confidence.
4. Completeness gate either permits bounded rules or returns a missing-evidence checklist.
5. Deterministic rules produce confirmed/suspected/insufficient-evidence findings with alternatives and prohibited unsafe actions.
6. User exports a redacted ESP/provider/client packet and schedules a recheck.

Admin/operational flow: manage workspace/client roles, retention policy, redaction manifest, audit log, rule version, fixture tests, and manual support review queue.

Payment flow: Stripe Checkout/Customer Portal for monthly agency subscription; manual invoicing acceptable for first 5-10 pilots.

Minimum analytics: activation, cases created, packets exported, evidence-gap rate, time-to-first-packet, recheck completion, user-rated actionability, paid conversion, churn reason.

Minimum security: org tenancy, RBAC, MFA-ready auth, encrypted object storage, presigned uploads, no raw email content in logs, redaction preview, retention/deletion policy, audit events, DPA/security FAQ before pilots.

Required integrations: payment, auth, object storage, email notifications. Provider/ESP connectors are not required for MVP.

Manual operations allowed: expert review, onboarding, redaction policy setup, case fixture import, pilot success interviews, and invoice collection.

## Feature classification

| Feature | Classification | Rationale |
|---|---|---|
| Guided incident intake | Required for MVP | Tests whether users will submit enough evidence. |
| Header/NDR/CSV/manual parsing | Required for MVP | Core artifact-to-evidence value. |
| Canonical evidence schema | Required for MVP | Durable product core. |
| Completeness gate | Required for MVP | Prevents false certainty and creates useful partial output. |
| 8-12 deterministic Gmail/Microsoft rules | Required for MVP | Tests whether explainable guidance is useful. |
| Redacted packet export | Required for MVP | Primary value wedge. |
| Audit/retention controls | Required for MVP | Sensitive mail artifacts make this non-optional. |
| Scheduled recheck | Useful but deferrable to late MVP | Important retention loop, can start as reminders. |
| Stripe subscription | Useful but deferrable for pilots | Manual invoicing can validate payment first. |
| Google Postmaster/SNDS connectors | Post-MVP | Add only after retention proof. |
| ESP deep integrations | Post-MVP | High support cost; manual CSV is enough to test value. |
| Portfolio dashboard | Dangerous scope expansion before validation | Earlier docs included it, latest scope correctly narrows. |
| Sending/warm-up/auto-remediation | Unnecessary and risky | Conflicts with trust and safety positioning. |
| AI diagnosis | Dangerous scope expansion | Raises quality, privacy, and cost risk before deterministic baseline. |
| Universal reputation score | Unnecessary before validation | Crowded and undermines evidence discipline. |

## Recommended reduced MVP

Build only the packet compiler and internal workbench for one incident type: agency/MSP client mail suddenly fails at Gmail or Microsoft 365 despite apparently correct authentication. Validate on 20-30 historical/concierge cases before building a polished dashboard.
