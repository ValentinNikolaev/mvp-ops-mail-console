# Project understanding

## Pre-assessment summary

1. Problem being solved: email operators, agencies, MSPs, and deliverability consultants face high-friction incidents where mail passes SPF/DKIM/DMARC or appears "sent" in an ESP, yet Gmail, Outlook/Microsoft 365, or another provider rejects, junk-filters, silently drops, or hides the true provider-scoped cause.
2. Proposed product: a manual-first, read-only email-delivery incident workbench that converts headers, NDRs, ESP exports, seed observations, and operator notes into observed facts, bounded hypotheses, missing-evidence prompts, safe next tests, and redacted support/client packets.
3. Target users and buyers: first user is an agency/MSP operator or deliverability consultant; first buyer/economic decision-maker is the agency/MSP owner or delivery/practice lead. Later segments could be SMB SaaS/ecommerce ops teams.
4. Expected value proposition: reduce time-to-triage and time-to-escalation, prevent unsafe remediation, create reusable provider/ESP support packets, and give agencies a defensible client-facing decision record.
5. Planned MVP scope: one incident workspace; four evidence inputs; canonical evidence schema; completeness gate; 8-12 deterministic Gmail/Microsoft rules; redaction; immutable audit; packet export; scheduled recheck. Manual artifacts first, connectors later.
6. Revenue model: not yet validated. The most plausible model is B2B SaaS by agency workspace/client/domain/active incident, with optional paid expert review or implementation.
7. Technical architecture: Next.js/TypeScript modular monolith, Route Handlers/Zod, PostgreSQL/Prisma, R2 or S3 object storage, Inngest/Trigger.dev jobs, Clerk/Supabase org auth, Sentry/logs/audit events.
8. Important unresolved assumptions: willingness to pay; incident frequency per agency; whether packet generation is better than a service/process improvement; minimum evidence threshold; first packet type; retention loop; acceptable raw-artifact retention policy.
9. Contradictions found: earlier specs included broader portfolio views, provider matrices, Yahoo/corporate provider scope, and possibly SaaS/ecommerce buyers; latest iteration narrows to agency/MSP Gmail/Microsoft support packets. Product spec version 005 exists twice with different dates (2026-07-28 and 2026-07-31), indicating versioning ambiguity. The README says product specs should use exact top-level headers, but current specs include extra sections such as Snapshot and MVP Architecture.
10. Features unnecessary before validation: broad connectors, continuous monitoring, portfolio analytics, automatic remediation, warm-up, sending, universal reputation scores, AI diagnosis, deep collaboration suite, white-label reporting beyond a basic packet, and multi-provider breadth beyond Gmail/Microsoft.

## Core business hypothesis

For agencies/MSPs and deliverability consultants who experience repeated client email-delivery incidents, the product provides an evidence-to-handoff workbench and redacted escalation packet, which is better than spreadsheets, ESP dashboards, generic DNS tools, seed tests, or ad hoc consulting notes because it preserves source-scoped facts, missing evidence, contradictions, confidence gates, and safe provider-specific next actions. Customers are expected to pay EUR 149-399/month through a B2B SaaS subscription, with optional paid expert review.

## Segment roles

User: deliverability analyst, agency operator, MSP email admin, or consultant.

Buyer: agency/MSP owner, delivery lead, or head of technical operations.

Economic decision-maker: the person accountable for consultant labour margin, escalation throughput, and client retention.

Beneficiary: agency client whose campaign, transactional, or business mail is affected.

Acquisition channel: founder-led outreach to deliverability agencies/MSPs, incident-intent content, free header/NDR completeness checker, consultant referrals, and relevant communities.

Search trigger: sudden Gmail/Outlook spam placement, rejection, bounce surge, "authentication passes but mail fails", client escalation, or ESP/provider support dispute.

Existing workaround: manual header review, Postmaster/SNDS/ESP dashboards, seed tests, MXToolbox/GlockApps/Validity, support tickets, spreadsheets, and consultants.

Switching cost: low for occasional diagnostic use, medium for agencies if case history and packets become client workflow records.

Refusal-to-pay reasons: consultants may prefer billable manual work; generic tools may be "good enough"; packet does not guarantee remediation; raw mail artifacts create privacy friction; incident frequency may be too low for recurring SaaS.

## Input coverage

The analysis recursively considered `research/`, including signals, comments, daily digests, candidates, logs, MVP iterations, council verdicts, product specs, state registries, and config. The latest product spec, latest MVP iteration, latest council verdict, prior product specs/iterations, and representative high-confidence signals were read in detail. Hourly logs and candidate ledgers were considered as provenance/process evidence rather than treated as primary product requirements.
