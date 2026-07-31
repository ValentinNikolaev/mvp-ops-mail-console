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
