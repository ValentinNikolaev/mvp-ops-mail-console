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
