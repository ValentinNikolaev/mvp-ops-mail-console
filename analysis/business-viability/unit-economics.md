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
| Pessimistic | 7 / EUR 1,043 / EUR -401 / EUR -71,966 | 19 / EUR 2,831 / EUR 1,046 / EUR -68,364 | 31 / EUR 4,619 / EUR 2,493 / EUR -47,400 | 17 | not reached | EUR 72,935 |
| Base | 26 / EUR 6,474 / EUR 3,129 / EUR -64,623 | 74 / EUR 18,426 / EUR 12,838 / EUR 34,383 | 122 / EUR 30,378 / EUR 22,547 / EUR 249,896 | 9 | 22 | EUR 72,958 |
| Optimistic | 45 / EUR 17,955 / EUR 11,672 / EUR -27,704 | 143 / EUR 57,057 / EUR 45,114 / EUR 320,069 | 274 / EUR 109,326 / EUR 90,749 / EUR 1,148,294 | 7 | 15 | EUR 68,299 |

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
