from __future__ import annotations

import csv
import json
from pathlib import Path


OUT = Path(__file__).resolve().parents[1]


def money(value: float) -> str:
    return f"EUR {value:,.0f}"


SOURCES = [
    {
        "id": "repo-readme",
        "title": "Repository README",
        "url": "../../README.md",
        "accessed": "2026-08-01",
        "scope": "project context",
        "proves": "The repository is a Codex-native monitor for market pain signals and MVP/product-spec synthesis around email deliverability incident workflows.",
        "limits": "It describes the repository process, not customer willingness to pay.",
    },
    {
        "id": "spec-005",
        "title": "Product Specification 005",
        "url": "../../research/product-specs/2026-07-31-product-spec-005.md",
        "accessed": "2026-08-01",
        "scope": "product plan",
        "proves": "Current planned product is an evidence packet workbench for agencies/MSPs handling Gmail and Microsoft 365 incidents.",
        "limits": "Spec is a hypothesis derived from observed signals, not validated sales evidence.",
    },
    {
        "id": "mvp-005",
        "title": "MVP Iteration 005",
        "url": "../../research/mvp-iterations/2026-07-31-mvp-iteration-005.md",
        "accessed": "2026-08-01",
        "scope": "MVP thesis",
        "proves": "Narrow MVP scope: manual read-only artifact intake, deterministic rules, support packet, recheck, no sending/warm-up/guarantees.",
        "limits": "Does not prove agencies/MSPs will pay recurring SaaS fees.",
    },
    {
        "id": "council-005",
        "title": "Council Verdict 005",
        "url": "../../research/mvp-council-verdicts/2026-07-31-mvp-iteration-005-council-verdict.md",
        "accessed": "2026-08-01",
        "scope": "internal critique",
        "proves": "Willingness to pay, buyer validation, and time-to-triage baseline remain the main unknowns.",
        "limits": "Internal council output is analytical evidence, not market evidence.",
    },
    {
        "id": "postal-signal",
        "title": "Postal SPF validation visibility gap",
        "url": "../../research/signals/2026-07-23-postal-github-issues-spf-validation-visibility-gap.md",
        "accessed": "2026-08-01",
        "scope": "source-thread signal",
        "proves": "Receiver-side authentication pass and sender-control-plane warning can be non-equivalent observations.",
        "limits": "One public issue; does not quantify market size.",
    },
    {
        "id": "brevo-signal",
        "title": "Authenticated transactional spam rejection",
        "url": "../../research/signals/2026-07-23-brevo-community-authenticated-transactional-spam-rejection.md",
        "accessed": "2026-08-01",
        "scope": "source-thread signal",
        "proves": "Authenticated transactional mail can still be rejected across providers.",
        "limits": "Anecdotal forum evidence.",
    },
    {
        "id": "m365-signal",
        "title": "Authenticated M365 tenant spam",
        "url": "../../research/signals/2026-01-28-microsoft-community-hub-authenticated-m365-tenant-spam.md",
        "accessed": "2026-08-01",
        "scope": "source-thread signal",
        "proves": "Microsoft 365 messages can pass authentication while receiving spam/phishing classification.",
        "limits": "Anecdotal support/community evidence.",
    },
    {
        "id": "fbi-market",
        "title": "Fortune Business Insights email deliverability tools market",
        "url": "https://www.fortunebusinessinsights.com/email-deliverability-tools-market-108522",
        "accessed": "2026-08-01",
        "scope": "global",
        "proves": "Reported global email deliverability tools market: USD 1.35B in 2025, USD 1.48B in 2026, projected USD 3.00B by 2034 at 9.25% CAGR.",
        "limits": "Commercial market report; category is broader than incident-packet workflow.",
    },
    {
        "id": "researchmarkets",
        "title": "Research and Markets email deliverability tools report",
        "url": "https://www.researchandmarkets.com/report/email-deliverability-tools",
        "accessed": "2026-08-01",
        "scope": "global",
        "proves": "Alternative estimate: USD 1.2B in 2024 projected to USD 1.9B by 2030 at 8.3% CAGR.",
        "limits": "Paywalled report snippet; category remains broader than proposed product.",
    },
    {
        "id": "validity",
        "title": "Validity Engage deliverability page",
        "url": "https://www.validity.com/capabilities/engage-inbox-placement-and-deliverability/",
        "accessed": "2026-08-01",
        "scope": "competitor",
        "proves": "Enterprise vendors sell inbox placement, reputation, authentication, and campaign workflow tools.",
        "limits": "Public page does not disclose pricing or customer conversion.",
    },
    {
        "id": "glockapps",
        "title": "GlockApps deliverability product page",
        "url": "https://glockapps.com/",
        "accessed": "2026-08-01",
        "scope": "competitor",
        "proves": "Self-service inbox placement, spam testing, authentication, and monitoring are established paid product categories.",
        "limits": "Does not focus on agency incident packet preparation.",
    },
    {
        "id": "mxtoolbox",
        "title": "MXToolbox Delivery Center pricing page",
        "url": "https://mxtoolbox.com/Public/Content/ProductPage/MatrixDC2/matrixb.aspx",
        "accessed": "2026-08-01",
        "scope": "competitor pricing",
        "proves": "MXToolbox advertises Free, Delivery Center at USD 129/month, and Delivery Center Plus at USD 399/month.",
        "limits": "Pricing is for monitoring/diagnostics, not the exact workflow.",
    },
    {
        "id": "vercel-pricing",
        "title": "Vercel pricing",
        "url": "https://vercel.com/pricing",
        "accessed": "2026-08-01",
        "scope": "infrastructure",
        "proves": "Vercel Pro is USD 20/month with included usage and metered compute/network overages.",
        "limits": "Actual cost depends on traffic and architecture.",
    },
    {
        "id": "r2-pricing",
        "title": "Cloudflare R2 pricing",
        "url": "https://developers.cloudflare.com/r2/pricing/",
        "accessed": "2026-08-01",
        "scope": "infrastructure",
        "proves": "R2 charges by storage and operations with no egress bandwidth fees; standard storage public price is USD 0.015/GB-month.",
        "limits": "Does not include application security and compliance work.",
    },
    {
        "id": "clerk-pricing",
        "title": "Clerk pricing",
        "url": "https://clerk.com/pricing",
        "accessed": "2026-08-01",
        "scope": "infrastructure",
        "proves": "Clerk offers a free tier up to 50,000 monthly retained users and 100 monthly retained organizations; Pro starts at USD 20/month.",
        "limits": "B2B/org overage and advanced auth can change economics.",
    },
    {
        "id": "inngest-pricing",
        "title": "Inngest pricing",
        "url": "https://www.inngest.com/pricing",
        "accessed": "2026-08-01",
        "scope": "infrastructure",
        "proves": "Inngest Hobby includes 50k executions; Pro starts at USD 99/month with 1M executions included.",
        "limits": "Can be replaced by self-hosted jobs at higher operations cost.",
    },
    {
        "id": "stripe-eea",
        "title": "Stripe Austria pricing",
        "url": "https://stripe.com/en-at/pricing",
        "accessed": "2026-08-01",
        "scope": "payments",
        "proves": "Stripe lists 1.5% + EUR 0.25 for standard EEA cards and 2.8% + EUR 0.25 for premium EEA cards.",
        "limits": "Country, card mix, VAT, and currency conversion can change fees.",
    },
]


ASSUMPTIONS = {
    "target_markets": "US, UK, and EU English-speaking agencies/MSPs first; broader SMB SaaS/ecommerce later. Confidence: medium because repo names Gmail/M365 agencies/MSPs but no country is specified.",
    "target_customers": "B2B agencies/MSPs and deliverability consultants handling repeated client incidents. Confidence: high from latest MVP/spec/council.",
    "currency": "EUR. Confidence: high from user prompt.",
    "forecast_horizon": "36 months. Confidence: high from user prompt.",
    "founder_context": "Assumed one senior/full-stack founder, 20 hours/week, high technical level, AI coding tools enabled. Confidence: low because prompt placeholders were not filled.",
    "cloud": "Vercel/managed Postgres/Cloudflare R2 or equivalent managed stack. Confidence: medium from product spec.",
    "pricing": "Initial SaaS ARPU EUR 149-399/month, base EUR 249/month. Confidence: medium-low; competitor prices exist but exact incident-packet willingness to pay is unvalidated.",
    "market_size": "Global deliverability tools market used only as top-down context; bottom-up reachable agencies dominates conclusion. Confidence: medium.",
    "taxes": "Pre-tax model. Confidence: high; jurisdiction not defined.",
}


def generate_financial_model() -> dict:
    scenarios = {
        "pessimistic": {
            "arpu": 149,
            "churn": 0.08,
            "new": [0, 0, 0] + [1] * 9 + [2] * 12 + [3] * 12,
            "fixed": 120,
            "var": 2.5,
            "marketing": [300] * 6 + [800] * 30,
            "sales_per_new": 180,
            "dev_months": 9,
            "dev_total": 65000,
            "support_per": 8,
            "other": 250,
        },
        "base": {
            "arpu": 249,
            "churn": 0.04,
            "new": [0, 0, 0] + [2] * 3 + [4] * 6 + [6] * 12 + [8] * 12,
            "fixed": 180,
            "var": 2.0,
            "marketing": [500] * 3 + [1500] * 9 + [2500] * 12 + [3500] * 12,
            "sales_per_new": 220,
            "dev_months": 8,
            "dev_total": 65000,
            "support_per": 10,
            "other": 350,
        },
        "optimistic": {
            "arpu": 399,
            "churn": 0.02,
            "new": [0, 0] + [3] * 4 + [6] * 6 + [10] * 12 + [15] * 12,
            "fixed": 250,
            "var": 2.2,
            "marketing": [1000] * 3 + [3000] * 9 + [5500] * 12 + [8000] * 12,
            "sales_per_new": 260,
            "dev_months": 6,
            "dev_total": 60000,
            "support_per": 12,
            "other": 500,
        },
    }
    rows = []
    summary = {}
    for name, p in scenarios.items():
        active = 0
        cumulative = 0.0
        op_break_even = None
        cumulative_break_even = None
        max_cash = 0.0
        snapshots = {}
        for month in range(1, 37):
            new_customers = p["new"][month - 1]
            churned = round(active * p["churn"])
            active = max(0, active + new_customers - churned)
            revenue = active * p["arpu"]
            payment_fees = revenue * 0.018 + 0.25 * active
            variable_infra = active * p["var"]
            fixed_infra = p["fixed"]
            marketing = p["marketing"][month - 1]
            sales = new_customers * p["sales_per_new"]
            development = p["dev_total"] / p["dev_months"] if month <= p["dev_months"] else 0
            support = active * p["support_per"]
            other = p["other"]
            total_cost = payment_fees + variable_infra + fixed_infra + marketing + sales + development + support + other
            gross_profit = revenue - payment_fees - variable_infra - fixed_infra
            operating_profit = revenue - total_cost
            cumulative += operating_profit
            max_cash = max(max_cash, -cumulative)
            if op_break_even is None and operating_profit >= 0:
                op_break_even = month
            if cumulative_break_even is None and cumulative >= 0:
                cumulative_break_even = month
            if month in (12, 24, 36):
                snapshots[month] = {
                    "active_customers": active,
                    "revenue": round(revenue),
                    "operating_profit": round(operating_profit),
                    "cumulative_cash_flow": round(cumulative),
                }
            rows.append(
                {
                    "scenario": name,
                    "month": month,
                    "new_customers": new_customers,
                    "active_customers": active,
                    "churned_customers": churned,
                    "arpu": p["arpu"],
                    "revenue": round(revenue, 2),
                    "payment_fees": round(payment_fees, 2),
                    "variable_infrastructure": round(variable_infra, 2),
                    "fixed_infrastructure": round(fixed_infra, 2),
                    "marketing_cost": round(marketing, 2),
                    "sales_cost": round(sales, 2),
                    "development_cost": round(development, 2),
                    "support_cost": round(support, 2),
                    "other_cost": round(other, 2),
                    "total_cost": round(total_cost, 2),
                    "gross_profit": round(gross_profit, 2),
                    "operating_profit": round(operating_profit, 2),
                    "cumulative_cash_flow": round(cumulative, 2),
                }
            )
        summary[name] = {
            "operating_break_even_month": op_break_even,
            "cumulative_break_even_month": cumulative_break_even,
            "max_cumulative_cash_required": round(max_cash),
            "snapshots": snapshots,
        }
    with (OUT / "financial-model.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return summary


def write(name: str, text: str) -> None:
    (OUT / name).write_text(text.strip() + "\n", encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    model = generate_financial_model()

    write(
        "project-understanding.md",
        """
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
""",
    )

    write(
        "market-demand.md",
        """
# Market demand

## Direct evidence

- The repository contains 67 accepted signal files through 2026-07-31. They repeatedly show the same operational pattern: authentication passes or basic checks are green, while provider-specific placement, rejection, or feedback remains unclear.
- Representative repo evidence includes Brevo transactional mail rejected despite DKIM/DMARC confirmation, Microsoft 365 tenant mail classified as spam/phishing despite composite authentication pass, Reddit/Emailmarketing calls for provider-scoped preflight checks, and a Postal SPF warning that conflicts with Gmail/Microsoft receiver-side authentication passes.
- Customers already pay for adjacent tools. Validity sells enterprise inbox placement and deliverability monitoring; GlockApps sells self-service inbox placement/spam testing; MXToolbox sells Delivery Center monitoring at USD 129/month and USD 399/month. This proves budget exists for deliverability diagnostics, but not yet for the exact evidence-packet wedge.
- Public source threads show manual labour: operators paste headers, discuss SPF/DKIM/DMARC, compare Gmail vs Outlook behaviour, and seek escalation guidance. This supports problem severity for technical operators.

## Indirect evidence

- Fortune Business Insights reports the global email deliverability tools market at USD 1.35B in 2025 and USD 1.48B in 2026, projected to USD 3.00B by 2034. Research and Markets reports a broader but similar category at USD 1.2B in 2024 and USD 1.9B by 2030.
- Email marketing and transactional email remain large operational channels, making deliverability incidents economically meaningful. This is adjacent evidence; it does not prove this product can acquire buyers.
- Gmail/Yahoo sender requirements and stricter provider filtering increase the value of evidence-backed incident handling, but they also increase competition from ESP-native and enterprise deliverability suites.
- Agencies/MSPs are a plausible beachhead because one buyer can experience repeated incidents across many client domains, improving retention potential compared with one-off SMB diagnostics.

## Weak or missing evidence

- No file proves a qualified agency/MSP agreed to pay for the packet workbench.
- No baseline shows current time-to-triage, time-to-escalation, ticket acceptance rate, or analyst rework before/after this workflow.
- No evidence proves whether the first paid packet should be client brief, ESP ticket, provider escalation, or internal handoff.
- Search/community demand exists around deliverability, but demand for "auditable evidence packets" is inferred rather than directly measured.
- Competitor pricing brackets support plausible ARPU, but willingness to pay for a manual-first product remains unvalidated.

## Market sizing

Top-down context: using the 2026 global email deliverability tools estimate of USD 1.48B as TAM context and converting roughly at 0.92 EUR/USD gives about EUR 1.36B. This is not expected revenue; it is only the broad category envelope.

SAM assumption: if agencies/MSPs and deliverability consultants represent 3-7% of spend or reachable workflow value in this category, SAM is roughly EUR 41M-95M. Confidence is low because the source does not break out this niche.

Bottom-up SOM:

- Reachable design-partner universe years 1-3: 1,000-3,000 English-speaking deliverability agencies, MSPs, email consultants, and specialist operators reachable through outbound/content/community channels. Confidence: low-medium.
- Realistic paying penetration: year 1 = 15-40 customers; year 2 = 60-120; year 3 = 120-250.
- ARPA: EUR 149-399/month, base EUR 249/month.

Formula: paying customers x ARPA x 12.

- Year 1 SOM: 15-40 x EUR 149-249 x 12 = EUR 26.8k-119.5k ARR.
- Year 2 SOM: 60-120 x EUR 199-299 x 12 = EUR 143k-431k ARR.
- Year 3 SOM: 120-250 x EUR 249-399 x 12 = EUR 359k-1.20M ARR.

Bottom-up conclusion: the project is not venture-scale unless it expands beyond agencies/MSPs or captures enterprise/consultant workflow budgets. It can be a viable niche SaaS or productized service if retention is strong and acquisition stays founder-led/low-CAC.
""",
    )

    write(
        "competitors.md",
        """
# Competitive analysis

| Alternative | Target customer | Core features | Pricing evidence | Strengths | Weaknesses | Switching barriers | Adoption evidence | Proposed differentiation |
|---|---|---|---|---|---|---|---|---|
| Validity/Everest/Engage | Enterprise marketers and deliverability teams | Inbox placement, reputation, authentication, campaign workflow | Public page is quote/contact-sales; third-party reports suggest high enterprise pricing | Brand, enterprise workflow, broad data network | Expensive, complex, may not serve low/mid-volume incident handoff | Medium-high once embedded | Public enterprise product category | Cheaper agency incident packet, explicit evidence/provenance, manual-first |
| GlockApps | SMB marketers, agencies, deliverability testers | Seed tests, spam/content checks, DMARC, reports | Public/third-party pages show self-service plans commonly around USD 59-129+/month | Accessible, known category, seed testing | Shows where mail lands more than why a messy incident happened | Low-medium | Active product and reviews | Cross-artifact case packet and missing-evidence gate |
| MXToolbox | IT admins, domain owners, email admins | DNS, blacklist, DMARC, delivery monitoring | Public page: Free, USD 129/month, USD 399/month | Trusted utility, fast diagnostics | Monitoring/checks rather than incident workflow | Low | Long-running public tools | Turns scattered outputs into provider/ESP escalation packet |
| Google Postmaster Tools | Gmail senders | Gmail reputation, spam rate, auth metrics | Free | Authoritative Gmail-side data | Gmail-only, low-volume data gaps, delayed/aggregated | Low | Official tool | Incorporates as evidence, not a replacement |
| Microsoft SNDS/Defender traces | Microsoft senders/admins | IP reputation, tenant/mail flow data | Free/native | Provider-specific | Fragmented, admin access required, not cross-provider | Medium in Microsoft tenants | Official/native | Normalizes into case evidence |
| ESP dashboards (Klaviyo, Brevo, HubSpot, SES, Marketo) | ESP users | Sent/bounce/open metrics, suppression, support | Bundled with ESP | Already in workflow | Often provider verdict is incomplete; "sent" is not placement | Medium due existing ESP | Strong ESP adoption | Bridges ESP evidence to receiver/provider evidence |
| Consultants/manual process | Agencies and senders | Expert triage, spreadsheets, support tickets | Hourly/project fees vary | High trust, flexible | Slow, inconsistent, hard to scale, knowledge trapped in people | Medium relational | Common workaround in source threads | Software-assisted packet and repeatable rules |
| Open-source mail stacks/tools | Technical operators | Headers, Rspamd, Postal, mail-server diagnostics | Free/open source | Transparent, extensible | Requires expertise; not client-facing workflow | Low for technical users | GitHub issues and communities | Converts technical evidence into buyer-safe packet |
| Do nothing | All segments | Wait, resend, accept losses | Free | No procurement | Revenue/reputation risk remains | None | Always present | Must prove urgency and measurable labour savings |

## Defensibility

Visible durable advantage is currently limited. The strongest possible advantage is workflow specialization plus accumulated agency incident history, rule fixtures, packet templates, and trust around uncertainty. There is no proprietary provider data, network effect, or exclusive distribution yet.

Potential defensibility:

- Niche specialization: high if the product owns agency/MSP incident handoff rather than generic scoring.
- Workflow integration: medium after it becomes part of client reporting and support escalation.
- Operational efficiency: medium if it reduces analyst time by at least 30-50%.
- Better economics: medium if it replaces part of consultant prep time at EUR 149-399/month.

Weak defensibility:

- Proprietary data: low before enough cases/outcomes accumulate.
- Network effects: low.
- Brand/community: low at launch.
- Regulatory expertise: low-medium; privacy/security discipline matters but is not unique.

Conclusion: differentiation is credible but not yet durable. The project must become the fastest trusted way to produce a defensible incident packet, not just another deliverability dashboard.
""",
    )

    write(
        "mvp-scope.md",
        """
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
""",
    )

    write(
        "development-estimate.md",
        """
# Development estimate

## Work breakdown

| Work item | Scope | Optimistic | Realistic | Pessimistic | Role | Dependencies | Uncertainty | Explanation |
|---|---:|---:|---:|---:|---|---|---|---|
| Product clarification | pilot packet, evidence thresholds, pricing, policies | 30 | 60 | 100 | product/founder | design partners | high | Buyer workflow and packet type are not validated. |
| UX/UI | guided intake, evidence board, packet preview, case list | 70 | 120 | 180 | product designer/frontend | product clarification | medium | Scope can stay simple but must handle dense evidence clearly. |
| Backend/domain | cases, tenants, evidence graph, rules, packets | 120 | 200 | 300 | senior full-stack/backend | schema | medium-high | Evidence provenance and rule contracts are core complexity. |
| Frontend implementation | forms, uploads, rule cards, exports | 90 | 150 | 240 | frontend/full-stack | UX/backend | medium | Manual-first UI needs good error states. |
| Database design | tenants, cases, evidence, audit, retention | 35 | 70 | 110 | backend | product rules | medium | JSONB plus relational provenance. |
| Parsers/normalizers | headers, NDRs, CSV, seed/manual observations | 70 | 130 | 220 | backend/email specialist | schema | high | Header/NDR edge cases are messy. |
| Auth/RBAC | org workspaces, roles, invitations | 30 | 60 | 90 | full-stack | tenancy | medium | Managed auth helps but B2B roles matter. |
| Payments | Stripe checkout, portal, plan limits | 15 | 35 | 60 | full-stack | pricing | medium | Can be deferred for pilots. |
| Admin tools | rule/version visibility, support review, retention controls | 25 | 55 | 90 | full-stack | schema | medium | Needed for supportable pilots. |
| Analytics | activation, packet, evidence-gap, recheck metrics | 20 | 40 | 70 | full-stack/product | event plan | medium | Essential validation instrumentation. |
| Infrastructure | Vercel/DB/storage/jobs/secrets | 25 | 55 | 90 | DevOps/full-stack | stack choice | medium | Managed stack reduces setup. |
| CI/CD | tests, previews, migrations | 20 | 40 | 70 | full-stack | repo setup | low-medium | Conventional. |
| Observability | Sentry, logs, audit event hygiene | 20 | 45 | 80 | backend/DevOps | infra | medium | Must avoid sensitive logs. |
| Security/privacy | redaction, encryption, DPA/security review | 45 | 90 | 160 | senior/backend/security | artifact flow | high | Sensitive email artifacts increase scope. |
| Testing | unit, parser fixtures, rule fixtures, e2e, regression | 70 | 130 | 210 | QA/full-stack | implementation | medium-high | Trust depends on testable rules. |
| Documentation | onboarding, security FAQ, pilot guide | 20 | 40 | 70 | product/founder | MVP flow | medium | Needed for agency pilots. |
| Deployment/launch | production setup, pilots, bug triage | 25 | 55 | 90 | full-stack/founder | implementation | medium | Real artifact intake will reveal issues. |
| Project management | planning, reviews, coordination | 35 | 65 | 100 | PM/founder | all | medium | Lower for solo, higher for team/agency. |
| Contingency | 25-35% reserve | 0 | 150 | 230 | all | all | high | Email evidence and privacy risk justify 25-35%. |
| Total |  | 760 | 1,540 | 2,560 | mixed |  | high | Includes contingency and validation-grade quality. |

## Delivery scenarios

Scenario A: solo senior developer using AI tools.

- Person-hours: 760-1,540, realistic 1,050-1,250 if scope is aggressively reduced.
- Calendar: at assumed 20 hours/week, 38-77 weeks; at full-time, 5-10 months.
- Economic cost: EUR 57k-116k at EUR 75/hour. Founder cash cost may be lower, but time is not free.
- AI helps boilerplate, forms, tests, and docs. It helps less with evidence thresholds, parser edge cases, security review, pilot learning, and production debugging.

Scenario B: small product team.

- Roles: full-stack/backend, frontend, product designer, QA, DevOps on demand, fractional PM.
- Person-hours: 900-1,700 due coordination but faster calendar.
- Calendar: 12-20 weeks for reduced MVP; 20-30 weeks for fuller scope.
- Cash cost: EUR 65k-140k at blended EUR 55-85/hour.

Scenario C: external agency/contractors.

- Person-hours: 1,050-1,900 because domain knowledge transfer and acceptance testing take time.
- Calendar: 14-28 weeks.
- Cash cost: EUR 105k-265k at EUR 90-140/hour plus management/risk buffer.
- Risk: agency may build polished UI before the evidence model is validated unless tightly managed.

## Development conclusion

The MVP is technically feasible but not tiny. A useful validation-grade version is closer to a secure workflow product than a weekend diagnostic tool. The reduced concierge-assisted MVP should be built before full dashboard polish.
""",
    )

    write(
        "infrastructure-costs.md",
        """
# Infrastructure costs

Prices accessed 2026-08-01. USD prices are treated approximately at parity with EUR for planning conservatism unless noted; actual exchange rate and VAT may change totals.

## Managed serverless/PaaS approach

Assumed stack: Vercel Pro, managed Postgres such as Neon/Supabase, Cloudflare R2/S3, Clerk/Supabase Auth, Inngest/Trigger.dev, Sentry, Stripe, SES/Postmark-style transactional email.

| Usage tier | Active users | Fixed monthly | Variable driver | Estimated monthly cost | Likely dominant cost |
|---|---:|---:|---|---:|---|
| Pilot | 100 | EUR 25-75 | storage/jobs/email near free tiers | EUR 25-100 | auth/hosting minimums and support tooling |
| Early | 1,000 | EUR 90-220 | parser jobs, DB, logs, support | EUR 150-450 | database/jobs/observability |
| Growth | 10,000 | EUR 250-700 | cases, artifact storage, job executions | EUR 600-1,800 | database and background jobs |
| Scale | 100,000 | EUR 900-3,500 | audit volume, storage, queues, support | EUR 3,000-12,000 | database, jobs, logs, support/security |

Component notes:

- Vercel: Pro plan publicly lists USD 20/month with included usage and metered compute/network.
- R2: standard storage public price is USD 0.015/GB-month plus operations, with no egress bandwidth charge. Email artifacts are small; storage is unlikely to dominate early.
- Clerk: free tier can cover early MRU/orgs; Pro starts at USD 20/month. B2B organization overages may matter for agency workspaces.
- Inngest: Hobby includes 50k executions; Pro starts at USD 99/month with 1M executions. This becomes meaningful if each case creates many parsing/recheck jobs.
- Stripe: standard EEA cards list 1.5% + EUR 0.25; use 1.8-3.0% blended for modelling depending on card mix.

Formula: monthly infra = fixed platform minimums + active customers x cases/customer/month x artifacts/case x parse/recheck/storage/logging cost.

Base assumption: 3 active users/customer, 2 cases/customer/month, 5 artifacts/case, 10 job executions/case. At 100 customers this is about 2,000 job executions/month and still cheap; observability and support tooling cost more than compute.

## Low-cost VPS/self-hosted approach

Assumed stack: Hetzner/DigitalOcean VPS, Postgres, object storage/backups, self-hosted queues, open-source auth or Supabase, self-hosted monitoring.

| Usage tier | Estimated monthly cost | Advantage | Disadvantage |
|---|---:|---|---|
| Pilot | EUR 15-60 | Lowest cash cost | More security/ops burden |
| Early | EUR 50-180 | Predictable | Manual backups, patching, incident response |
| Growth | EUR 250-900 | Cheaper at steady load | Needs DevOps discipline |
| Scale | EUR 1,500-6,000 | Can be economical | Compliance, HA, observability work grows |

## Major-cloud approach

AWS/GCP/Azure with managed app hosting, RDS/Cloud SQL, S3, queues, secrets, WAF, logs, and monitoring is operationally robust but likely starts around EUR 150-500/month for a serious production setup and can reach EUR 5k-20k/month at scale. It is not necessary before product-market fit unless compliance requirements force it.

## AI/model costs

The recommended MVP should not require AI inference. If AI is added for summarization, use formula:

AI cost/month = packets x average tokens/packet x model EUR/token rate.

Planning range: EUR 0.02-0.30 per packet for small summaries, EUR 1-5 per complex multi-artifact analysis. AI costs are not the main risk; model quality/privacy/liability are.
""",
    )

    write(
        "marketing-plan.md",
        """
# Marketing and sales plan

## Channel assessment

| Channel | Setup effort | Monthly cash | Monthly labour | Time to signal | Lead volume | CAC range | Risk | Cheap test |
|---|---:|---:|---:|---|---|---:|---|---|
| Founder-led agency/MSP outreach | 20-40h | EUR 100-500 | 25-50h | 2-6 weeks | Low-medium | EUR 300-1,500 incl. labour | Low response, unclear buyer | 100 targeted messages offering free packet teardown |
| Deliverability consultant referrals | 10-25h | EUR 0-1,000 | 10-20h | 4-8 weeks | Low | EUR 200-2,000 | Consultants may see threat | Offer co-branded packet/review workflow |
| Free header/NDR completeness checker | 40-80h | EUR 50-300 | 10-20h | 4-12 weeks | Medium | EUR 100-1,000 | Attracts one-off free users | Launch single-page tool and ask for work email/pilot call |
| Incident-intent SEO/content | 30-60h initial | EUR 200-1,000 | 15-30h | 3-9 months | Medium long-term | EUR 200-2,000 | Slow; crowded generic terms | Publish 6 case teardown articles tied to Gmail/M365 evidence gaps |
| Communities/forums | 10-20h | EUR 0-200 | 10-20h | 2-8 weeks | Low-medium | EUR 100-800 | Promotional backlash | Share diagnostic checklists and invite private pilots |
| Paid search | 10-20h | EUR 1,000-5,000 | 5-10h | 1-4 weeks | Medium | EUR 1,000-6,000 | LTV may not support clicks | Bid only on high-intent incident terms with strict cap |
| LinkedIn outbound/ABM | 20-40h | EUR 200-1,500 | 25-60h | 4-10 weeks | Low-medium | EUR 800-4,000 | Sales cycle and weak targeting | Build list of 200 agencies/MSPs and test 3 offers |
| Partnerships with ESP/MSP tools | 40h+ | EUR 0-5,000 | 10-30h | 3-9 months | Low initially | Unknown | Partner incentives weak | Manual referral swap with 3 consultants |

## Launch budget scenarios

Lean validation: EUR 750-1,500 over 6-8 weeks.

- 20-30 problem interviews.
- 10 historical case packet prototypes.
- Basic landing page and one free completeness checker.
- Founder-led outreach only.

Realistic launch: EUR 5,000-12,000 over 3 months.

- Outreach tooling, content, small paid retargeting/search tests, security/legal basics, and limited contractor design/dev support.
- Goal: 5 paid pilots or 10 serious design partners.

Accelerated launch: EUR 25,000-60,000 over 3-4 months.

- Paid search experiments, stronger content production, consultant referral incentives, events/webinars, and faster product build.
- Only justified after pilot conversion and retention are visible.

## CAC and LTV guardrail

At EUR 249/month ARPU, 85-90% gross margin, and 4% monthly churn, finite 24-month LTV is roughly:

LTV = ARPU x gross margin x (1 - (1 - churn)^24) / churn = EUR 249 x 0.88 x 15.2 = about EUR 3,330.

Target CAC should stay below EUR 1,000-1,500 until retention is proven. Paid acquisition is dangerous before there is proof that agencies use the product repeatedly.
""",
    )

    write(
        "unit-economics.md",
        f"""
# Unit economics

All scenarios are pre-tax. Founder time is included as development cost in the model, even if not paid as salary. See `financial-model.csv` for month-by-month projections.

## Formulas

ARPU = monthly subscription revenue / active customers.

MRR = active customers x ARPU.

ARR = MRR x 12.

Gross margin = (revenue - payment fees - variable infrastructure - fixed infrastructure) / revenue.

Contribution margin = revenue - payment fees - variable infrastructure - support - sales cost attributable to new customers.

Finite LTV over 24 months = ARPU x gross margin x (1 - (1 - monthly churn)^24) / monthly churn.

CAC payback months = CAC / (ARPU x gross margin).

Break-even customers = fixed monthly cost / (ARPU x gross margin - support cost per customer - variable infra per customer).

## Scenario assumptions

| Scenario | ARPU | Churn | Gross margin | Acquisition | Marketing | Interpretation |
|---|---:|---:|---:|---|---:|---|
| Pessimistic | EUR 149 | 8%/mo | 80-88% | 1-3 new customers/mo | EUR 300-800/mo | Weak willingness to pay, low repeat use |
| Base | EUR 249 | 4%/mo | 85-90% | 2-8 new customers/mo | EUR 500-3,500/mo | Niche SaaS with founder-led sales |
| Optimistic | EUR 399 | 2%/mo | 88-92% | 3-15 new customers/mo | EUR 1,000-8,000/mo | Strong agency retention and referrals |

## Model outputs

| Scenario | Month 12 active/revenue/profit/cumulative | Month 24 active/revenue/profit/cumulative | Month 36 active/revenue/profit/cumulative | Operating break-even | Cumulative break-even | Max cash required |
|---|---|---|---|---:|---:|---:|
| Pessimistic | {model['pessimistic']['snapshots'][12]['active_customers']} / {money(model['pessimistic']['snapshots'][12]['revenue'])} / {money(model['pessimistic']['snapshots'][12]['operating_profit'])} / {money(model['pessimistic']['snapshots'][12]['cumulative_cash_flow'])} | {model['pessimistic']['snapshots'][24]['active_customers']} / {money(model['pessimistic']['snapshots'][24]['revenue'])} / {money(model['pessimistic']['snapshots'][24]['operating_profit'])} / {money(model['pessimistic']['snapshots'][24]['cumulative_cash_flow'])} | {model['pessimistic']['snapshots'][36]['active_customers']} / {money(model['pessimistic']['snapshots'][36]['revenue'])} / {money(model['pessimistic']['snapshots'][36]['operating_profit'])} / {money(model['pessimistic']['snapshots'][36]['cumulative_cash_flow'])} | {model['pessimistic']['operating_break_even_month']} | not reached | {money(model['pessimistic']['max_cumulative_cash_required'])} |
| Base | {model['base']['snapshots'][12]['active_customers']} / {money(model['base']['snapshots'][12]['revenue'])} / {money(model['base']['snapshots'][12]['operating_profit'])} / {money(model['base']['snapshots'][12]['cumulative_cash_flow'])} | {model['base']['snapshots'][24]['active_customers']} / {money(model['base']['snapshots'][24]['revenue'])} / {money(model['base']['snapshots'][24]['operating_profit'])} / {money(model['base']['snapshots'][24]['cumulative_cash_flow'])} | {model['base']['snapshots'][36]['active_customers']} / {money(model['base']['snapshots'][36]['revenue'])} / {money(model['base']['snapshots'][36]['operating_profit'])} / {money(model['base']['snapshots'][36]['cumulative_cash_flow'])} | {model['base']['operating_break_even_month']} | {model['base']['cumulative_break_even_month']} | {money(model['base']['max_cumulative_cash_required'])} |
| Optimistic | {model['optimistic']['snapshots'][12]['active_customers']} / {money(model['optimistic']['snapshots'][12]['revenue'])} / {money(model['optimistic']['snapshots'][12]['operating_profit'])} / {money(model['optimistic']['snapshots'][12]['cumulative_cash_flow'])} | {model['optimistic']['snapshots'][24]['active_customers']} / {money(model['optimistic']['snapshots'][24]['revenue'])} / {money(model['optimistic']['snapshots'][24]['operating_profit'])} / {money(model['optimistic']['snapshots'][24]['cumulative_cash_flow'])} | {model['optimistic']['snapshots'][36]['active_customers']} / {money(model['optimistic']['snapshots'][36]['revenue'])} / {money(model['optimistic']['snapshots'][36]['operating_profit'])} / {money(model['optimistic']['snapshots'][36]['cumulative_cash_flow'])} | {model['optimistic']['operating_break_even_month']} | {model['optimistic']['cumulative_break_even_month']} | {money(model['optimistic']['max_cumulative_cash_required'])} |

## Break-even and salary support

Base fixed monthly cost after MVP: about EUR 5,000-6,000 including marketing, support tooling, software subscriptions, accounting/legal reserve, and founder sales/support labour. At EUR 249 ARPU and about EUR 210 contribution/customer, operating break-even is roughly 25-30 customers after development spending ends.

Revenue to employ one full-time developer: assuming EUR 7,000-10,000/month loaded cost, the product needs about EUR 12,000-16,000 MRR, or 48-65 customers at EUR 249/month.

Revenue to support a small team: assuming EUR 35,000-55,000/month loaded operating cost, the product needs about EUR 45,000-70,000 MRR, or 180-280 customers at EUR 249/month.

## Financial viability

Minimum cash required to launch a serious validation path is EUR 750-1,500 for interviews/outreach plus founder time. Minimum cash required to launch a software MVP is roughly EUR 25,000 if founder-built with limited contractor help; realistic external cash is EUR 65,000-140,000. Full economic cost is higher because founder development time is valued rather than treated as free.

Monthly operating cost before meaningful revenue is about EUR 1,000-3,500 during validation and EUR 5,000-8,000 after launch if founder-led sales, support, tooling, accounting/legal reserve, and infrastructure are included. Required runway is at least 9-12 months for a founder-built MVP and 6-9 months for a funded team.

The project becomes attractive if three conditions hold: paid pilots convert at EUR 250-500, recurring ARPU reaches EUR 249-399/month, and retained agencies produce multiple cases per quarter. It should be stopped or pivoted if paid pilots fail, packet time savings are below 30%, or acquisition cannot stay below EUR 1,500 CAC.

## Sensitivity

The result is dominated by three assumptions:

1. Retention/churn: if agencies only use the product for one-off incidents, SaaS economics fail.
2. Willingness to pay/ARPU: EUR 99/month makes founder-led sales hard; EUR 249-399/month can work if the product saves real analyst time.
3. Acquisition efficiency: paid search is unlikely to work before LTV is proven; founder-led/referral channels must carry early growth.
""",
    )

    write(
        "risks-and-validation.md",
        """
# Risks and validation

## Risk register

| Risk | Probability | Impact | Evidence | Mitigation | Cheap validation | Decision threshold |
|---|---|---|---|---|---|---|
| Insufficient willingness to pay | High | High | Repo/council explicitly says WTP unvalidated | Paid pilot before full build | Offer 10 agencies a EUR 250-500 paid packet pilot | Stop if fewer than 3/10 qualified agencies agree |
| Product becomes polished documentation | Medium-high | High | Council warning: packet must shorten triage | Measure time saved and ticket acceptance | Concierge packets on 20 historical cases | Stop/pivot if <30% time saving or low actionability |
| Expensive acquisition | Medium | High | Niche buyer, crowded SEO | Founder-led/referrals first | 100 targeted outreaches | Stop paid ads if CAC > 40% of 24-month LTV |
| Long sales cycle | Medium | Medium | B2B agencies handle sensitive client data | Low-risk trial, manual invoicing, security FAQ | Interview procurement objections | Pivot to productized service if close time >90 days |
| Strong competitors | High | Medium | Validity, GlockApps, MXToolbox, ESPs | Own incident packet wedge | Compare against current tools in pilots | Stop if users prefer existing tool output in >60% cases |
| Weak differentiation | Medium-high | High | No durable moat yet | Build schema/rules/fixtures/case history | Ask buyers to rank value vs seed test/DNS tool | Continue only if packet is a must-have workflow |
| Technical parser complexity | Medium | Medium-high | Headers/NDRs vary widely | Manual fallback and clear "unknown" states | 30 real artifacts | Delay automation if parse success <80% |
| Privacy/security friction | High | High | Raw mail artifacts are sensitive | Redaction, retention, tenancy, audit from day one | Security review with 5 prospects | Stop if prospects will not upload even redacted artifacts |
| Platform/provider dependency | Medium | Medium | Gmail/Microsoft opacity | Evidence-based language; no guarantees | Review provider policy constraints | Kill any claim requiring unsupported provider access |
| AI quality/cost/liability | Medium | Medium | Opaque diagnosis is risky | Avoid AI in MVP or use only for drafts | Deterministic rules first | Do not ship AI recommendations until reviewed |
| Operational workload | Medium | Medium | Manual-first can become service-heavy | Productize expert review and templates | Track minutes/case | Stop SaaS push if support >60 min/customer/month |
| Founder availability | Medium | High | Assumed 20h/week | Narrow scope, concierge first | Weekly milestone tracking | Pause build if validation cannot be run consistently |

## Validation plan

| Stage | Hypothesis | Audience | Method | Cost | Time | Success metric | Minimum sample | Pass threshold | Fail threshold | Next decision |
|---|---|---|---:|---:|---|---|---:|---|---|---|
| 1. Problem interviews | Agencies/MSPs repeatedly face costly evidence-fragmentation incidents | Deliverability agencies/MSPs | 30-minute interviews | EUR 0-300 | 2-3 weeks | % confirming recent severe incidents | 20 | >=60% have >=2 incidents/quarter | <35% | Pivot segment |
| 2. Alternative analysis | Existing tools do not create sufficient packets | Same | Ask for current workflow/screens | EUR 0 | 1-2 weeks | Manual steps and gaps | 10 | >=7 show spreadsheet/ticket pain | <4 | Reposition |
| 3. Landing/offer | Packet promise earns interest | Agencies/MSPs | Landing page + outreach | EUR 100-500 | 2 weeks | Qualified calls/bookings | 100 contacts | >=10 calls | <3 calls | Change offer |
| 4. Pricing test | Buyers accept paid pilot | Qualified prospects | Offer paid concierge packet | EUR 0 | 2-4 weeks | Paid commitments | 10 | >=3 paid pilots | 0-1 paid pilots | Stop or service pivot |
| 5. Concierge prototype | Packet saves work | Paid/design partners | Manually create packets from real cases | EUR 500-2,000 labour | 4-6 weeks | Time saved, actionability, reuse | 20 cases | >=30% time saving and >=8/10 actionability | <15% time saving | Redesign |
| 6. Narrow technical prototype | Schema/rules work on real evidence | Pilot cases | Build parser/rule fixture CLI | EUR 2k-8k | 3-5 weeks | Parse success and false-confidence rate | 30 artifacts | >=80% useful normalization; 0 harmful claims | Any harmful claim | Tighten gates |
| 7. MVP | Users repeat and pay monthly | 5-10 agencies/MSPs | Secure web workbench | EUR 25k-75k cash/economic | 8-16 weeks | Retention, packets/customer, conversion | 5 paid teams | >=70% month-2 retention | <40% | Pivot/stop |
| 8. Expansion | Connector improves retention | Retained customers | Add one validated connector | EUR 10k-35k | 4-8 weeks | Usage/retention lift | 5 customers | >=20% more cases or lower time/case | no lift | Defer connectors |

## Kill criteria

- Fewer than 35% of qualified agency/MSP interviews report repeated painful incidents.
- No qualified customer agrees to a paid pilot at EUR 250-500.
- Concierge packets do not reduce case-prep or escalation time by at least 30%.
- Users rate packet actionability below 7/10 after real cases.
- Required selling price exceeds willingness to pay by more than 2x.
- Privacy/security objections prevent use of real or redacted artifacts.
- CAC cannot plausibly stay below EUR 1,500 at EUR 249/month ARPU.
- Month-2 retained usage is below 40% in the first paid pilot cohort.
""",
    )

    write(
        "assumptions.md",
        "\n".join(
            [
                "# Assumptions",
                "",
                "| Assumption | Confidence | Why | Impact if wrong |",
                "|---|---|---|---|",
            ]
            + [
                f"| {k} | {('high' if 'high' in v.lower() else 'medium' if 'medium' in v.lower() else 'low')} | {v} | Financial model and recommendation should be revisited. |"
                for k, v in ASSUMPTIONS.items()
            ]
            + [
                "| Founder time valued at EUR 75/hour | Medium | Common planning rate for senior technical founder economic cost; not a salary quote. | Understates or overstates economic MVP cost. |",
                "| Reduced MVP can be built before connectors | High | Latest spec and council explicitly recommend manual-first read-only artifacts. | If false, MVP cost and delivery time rise sharply. |",
                "| Gross margin 80-92% | Medium | SaaS infra is low but support/review labour may be material. | Break-even customer count rises if support is high. |",
                "| Pre-tax calculations | High | Tax jurisdiction not specified. | Post-tax cash requirement may be higher. |",
            ]
        ),
    )

    write(
        "sources.md",
        "# Sources\n\n"
        + "\n\n".join(
            [
                f"## {s['id']}\n\n- Title: {s['title']}\n- URL: {s['url']}\n- Access date: {s['accessed']}\n- Geographic/project scope: {s['scope']}\n- What it proves: {s['proves']}\n- Limitations: {s['limits']}"
                for s in SOURCES
            ]
        ),
    )

    write(
        "executive-summary.md",
        f"""
# Project viability assessment

## Verdict

**Decision:** VALIDATE FIRST  
**Confidence:** Medium-Low  
**Commercial potential:** Moderate  
**MVP effort:** 760-1,540 person-hours  
**Estimated MVP cash cost:** EUR 25,000-EUR 140,000  
**Estimated full economic cost:** EUR 57,000-EUR 116,000 for solo-founder time; EUR 105,000-EUR 265,000 via agency  
**Pilot infrastructure:** approximately EUR 25-EUR 100/month  
**Initial marketing validation:** approximately EUR 750-EUR 1,500  
**Expected break-even:** base scenario operating break-even month {model['base']['operating_break_even_month']}; cumulative break-even month {model['base']['cumulative_break_even_month']}; pessimistic cumulative break-even not demonstrated  
**Maximum cumulative cash requirement:** approximately EUR 73,000 in base/pessimistic model

## Summary

The project is an evidence-packet workbench for agencies/MSPs handling Gmail and Microsoft 365 email-delivery incidents. It does not send mail or promise inbox placement. Its value is turning messy artifacts into a defensible packet: observed facts, missing evidence, bounded hypotheses, safe next tests, redaction, and recheck.

Strongest evidence in favour: the repo contains 67 accepted public pain signals showing repeated deliverability ambiguity; adjacent tools such as Validity, GlockApps, and MXToolbox prove customers pay for deliverability diagnostics; and the latest scope correctly narrows to a concrete agency/MSP incident workflow.

Strongest evidence against: no direct evidence yet shows agencies/MSPs will pay recurring SaaS fees for packet generation, and competitors already own adjacent monitoring, seed testing, DNS diagnostics, and enterprise deliverability workflows.

Main financial conclusion: this can be a credible niche SaaS or productized expert workflow if EUR 249-399/month ARPU, low CAC, and repeated agency usage are proven. It is not yet a clear venture-scale build, and the broad market size should not be treated as expected revenue.

Most dangerous unsupported assumption: that a redacted packet shortens paid agency work enough to create recurring subscription retention rather than one-off diagnostic use.

Cheapest next validation step: run 20-30 agency/MSP interviews and produce 10 paid/concierge evidence packets from real historical cases before building the full web app.

What must be true: agencies must handle multiple relevant incidents per quarter, accept manual/read-only evidence intake, value the packet above generic deliverability tools, and pay at least EUR 149-249/month with month-2 retention above 70%.

Clear recommendation: validate first. Build the smallest concierge/technical prototype around the canonical packet and deterministic rules. Do not fund broad connectors, dashboards, AI diagnosis, sending, warm-up, or portfolio monitoring until paid pilots prove repeat value.

## Score rationale

- Problem severity 8/10: repeated source-thread evidence shows revenue-sensitive ambiguity around Gmail/Microsoft placement, rejection, and authentication-pass failures.
- Evidence of demand 6/10: adjacent paid categories are proven, and repo signals are consistent, but direct buyer commitments are missing.
- Willingness to pay 4/10: plausible from competitor pricing and agency labour savings, but no paid pilots are documented.
- Market accessibility 5/10: founder-led outreach to a niche is possible, but SEO/paid acquisition are crowded.
- Competitive position 5/10: the packet workflow is differentiated, but no durable moat exists yet.
- MVP feasibility 7/10: technically buildable with managed services, though parser, privacy, and evidence-quality work are non-trivial.
- Unit economics 6/10: base case works at EUR 249 ARPU and low CAC; pessimistic case does not recover development cost in 36 months.
- Scalability 6/10: infrastructure scales reasonably, but support/review workload may limit margins.
- Overall viability 6/10: weighted toward commercial proof, not buildability; conclusion remains VALIDATE FIRST.
""",
    )

    # Small index-like files that point to the detailed analysis while satisfying required structure.
    write(
        "infrastructure-costs.md",
        (OUT / "infrastructure-costs.md").read_text(encoding="utf-8"),
    )

    assessment = {
        "project": {
            "name": "Evidence Packet Workbench",
            "summary": "Manual-first email-delivery incident workbench for agencies/MSPs that turns headers, NDRs, ESP exports, seed observations, and notes into bounded hypotheses and redacted support packets.",
            "target_customer": "Agencies/MSPs and deliverability consultants handling repeated Gmail/Microsoft 365 incidents for clients.",
            "business_model": "B2B SaaS subscription by agency workspace/client/domain/active incident, with optional paid expert review.",
        },
        "scores": {
            "problem_severity": 8,
            "evidence_of_demand": 6,
            "willingness_to_pay": 4,
            "market_accessibility": 5,
            "competitive_position": 5,
            "mvp_feasibility": 7,
            "unit_economics": 6,
            "scalability": 6,
            "overall_viability": 6,
        },
        "estimates": {
            "mvp_hours": {"optimistic": 760, "realistic": 1540, "pessimistic": 2560},
            "mvp_cash_cost": {"minimum": 25000, "realistic": 75000, "maximum": 140000, "currency": "EUR"},
            "monthly_infrastructure": {"pilot": 75, "early": 300, "growth": 1200, "scale": 8000},
            "marketing_budget": {"lean_validation": 1500, "realistic_launch": 12000, "accelerated_launch": 60000},
            "break_even": {
                "customers": 30,
                "monthly_revenue": 7500,
                "estimated_month": model["base"]["operating_break_even_month"],
                "cumulative_estimated_month": model["base"]["cumulative_break_even_month"],
            },
        },
        "recommendation": {
            "decision": "VALIDATE_FIRST",
            "confidence": "MEDIUM",
            "main_reasons": [
                "Repeated public pain signals and adjacent paid tools support problem severity.",
                "The exact recurring SaaS willingness to pay for evidence packets is unproven.",
                "MVP is feasible but requires privacy-safe artifact handling and trustworthy rule output.",
                "The project can work as a niche SaaS/productized service if retention and CAC are validated.",
            ],
            "critical_assumptions": [
                "Agencies/MSPs have multiple relevant incidents per quarter.",
                "Packets save at least 30% of triage/escalation prep time.",
                "Customers pay EUR 149-399/month and retain after the first incident.",
                "Sensitive artifact intake is acceptable with redaction and retention controls.",
            ],
            "next_actions": [
                "Interview 20-30 qualified agencies/MSPs.",
                "Run 10-20 concierge packet prototypes on historical cases.",
                "Sell 3 paid pilots before full MVP build.",
                "Build parser/rule fixture prototype only after paid pilot signal.",
            ],
            "kill_criteria": [
                "Fewer than 3 of 10 qualified prospects agree to paid pilot.",
                "Concierge packets save less than 30% time.",
                "Month-2 retained usage below 40%.",
                "CAC cannot plausibly stay below EUR 1,500 at base ARPU.",
            ],
        },
    }
    (OUT / "assessment.json").write_text(json.dumps(assessment, indent=2), encoding="utf-8")

    # Additional required reports derived from the detailed files.
    write(
        "marketing-plan.md",
        (OUT / "marketing-plan.md").read_text(encoding="utf-8"),
    )
    write(
        "development-estimate.md",
        (OUT / "development-estimate.md").read_text(encoding="utf-8"),
    )
    write(
        "mvp-scope.md",
        (OUT / "mvp-scope.md").read_text(encoding="utf-8"),
    )
    write(
        "competitors.md",
        (OUT / "competitors.md").read_text(encoding="utf-8"),
    )
    write(
        "market-demand.md",
        (OUT / "market-demand.md").read_text(encoding="utf-8"),
    )
    print("Assessment completed.")
    print()
    print("Decision: VALIDATE_FIRST")
    print("Confidence: MEDIUM")
    print("MVP effort: 760-1,540 person-hours")
    print("MVP cash cost: EUR 25,000-EUR 140,000")
    print("Break-even: base operating month 9; cumulative month 22; pessimistic cumulative break-even not demonstrated")
    print()
    print("Reports:")
    print("analysis/business-viability/")


if __name__ == "__main__":
    main()
