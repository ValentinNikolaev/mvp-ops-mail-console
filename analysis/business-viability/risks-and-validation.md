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
