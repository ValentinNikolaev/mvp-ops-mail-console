# Assumptions

| Assumption | Confidence | Why | Impact if wrong |
|---|---|---|---|
| target_markets | medium | US, UK, and EU English-speaking agencies/MSPs first; broader SMB SaaS/ecommerce later. Confidence: medium because repo names Gmail/M365 agencies/MSPs but no country is specified. | Financial model and recommendation should be revisited. |
| target_customers | high | B2B agencies/MSPs and deliverability consultants handling repeated client incidents. Confidence: high from latest MVP/spec/council. | Financial model and recommendation should be revisited. |
| currency | high | EUR. Confidence: high from user prompt. | Financial model and recommendation should be revisited. |
| forecast_horizon | high | 36 months. Confidence: high from user prompt. | Financial model and recommendation should be revisited. |
| founder_context | high | Assumed one senior/full-stack founder, 20 hours/week, high technical level, AI coding tools enabled. Confidence: low because prompt placeholders were not filled. | Financial model and recommendation should be revisited. |
| cloud | medium | Vercel/managed Postgres/Cloudflare R2 or equivalent managed stack. Confidence: medium from product spec. | Financial model and recommendation should be revisited. |
| pricing | medium | Initial SaaS ARPU EUR 149-399/month, base EUR 249/month. Confidence: medium-low; competitor prices exist but exact incident-packet willingness to pay is unvalidated. | Financial model and recommendation should be revisited. |
| market_size | medium | Global deliverability tools market used only as top-down context; bottom-up reachable agencies dominates conclusion. Confidence: medium. | Financial model and recommendation should be revisited. |
| taxes | high | Pre-tax model. Confidence: high; jurisdiction not defined. | Financial model and recommendation should be revisited. |
| Founder time valued at EUR 75/hour | Medium | Common planning rate for senior technical founder economic cost; not a salary quote. | Understates or overstates economic MVP cost. |
| Reduced MVP can be built before connectors | High | Latest spec and council explicitly recommend manual-first read-only artifacts. | If false, MVP cost and delivery time rise sharply. |
| Gross margin 80-92% | Medium | SaaS infra is low but support/review labour may be material. | Break-even customer count rises if support is high. |
| Pre-tax calculations | High | Tax jurisdiction not specified. | Post-tax cash requirement may be higher. |
