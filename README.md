# MVP Ops Mail Console Research Monitor

## Status

**Archived / suspended.**

This project is no longer being actively developed or monitored. The repository is kept as an archive of the research corpus, MVP iterations, council verdicts, product specifications, and the final business-viability assessment.

## Why This Project Was Suspended

The project was suspended after the business-viability assessment concluded **VALIDATE FIRST**, not **GO**.

The core idea remains plausible: an evidence-packet workbench for agencies, MSPs, and deliverability consultants handling Gmail and Microsoft 365 email-delivery incidents. The research corpus contains repeated public pain signals around authenticated email still landing in spam, being rejected, or producing contradictory provider feedback. Adjacent tools such as deliverability monitors, seed testing products, and DNS diagnostics also show that customers do spend money in this general category.

However, the assessment found that the project should not move into full build mode yet:

- There is no direct evidence that agencies or MSPs will pay recurring SaaS fees for an evidence-packet workflow.
- Willingness to pay scored only **4/10**.
- Evidence of demand scored **6/10**, because the pain is real but mostly inferred from public signals and adjacent competitors.
- Competitive position scored **5/10**, with no durable moat yet visible.
- The base financial model works only if the product reaches roughly **EUR 249/month ARPU**, low CAC, and repeated agency usage.
- The pessimistic case does not recover development cost within 36 months.
- A useful MVP is not tiny: the estimate was **760-1,540 person-hours**, with a realistic cash cost of **EUR 25,000-EUR 140,000** and full economic cost materially higher once founder time is counted.

The main unsupported assumption is that a redacted incident packet would save enough agency triage and escalation time to create recurring retention rather than one-off diagnostic use.

## Final Recommendation

Do not build the full product now.

The next rational step, if this project is ever revived, is validation before implementation:

1. Interview 20-30 qualified agencies, MSPs, or deliverability consultants.
2. Run 10-20 concierge packet prototypes on real historical incidents.
3. Sell at least 3 paid pilots before building a full web application.
4. Continue only if packets save at least 30% of triage or escalation preparation time.
5. Stop or pivot if month-2 retained usage is below 40%, or if CAC cannot plausibly stay below EUR 1,500 at the base ARPU.

## Archived Outputs

Primary viability assessment:

- `analysis/business-viability/executive-summary.md`
- `analysis/business-viability/assessment.json`
- `analysis/business-viability/financial-model.csv`
- `analysis/business-viability/sources.md`

Research and product artifacts:

- `research/signals/` - accepted market pain signals.
- `research/comments/` - useful source-thread comment artifacts.
- `research/digests/daily/` - daily monitoring digests.
- `research/mvp-iterations/` - synthesized MVP iterations.
- `research/mvp-council-verdicts/` - pressure-test verdicts.
- `research/product-specs/` - product specifications derived from the MVP iterations.
- `research/state/` - monitor state and registries.
- `research/config/` - historical monitoring and writing rules.

Automation and scripts are preserved for reference only:

- `automation/codex-hourly-market-monitor.prompt.md`
- `scripts/run-market-signal-pipeline.codex.md`
- `scripts/run-mvp-processing.codex.md`
- `scripts/market_signal_action.py`

## Archive Policy

The historical data should remain readable and reproducible, but the monitor should not be treated as active. Do not restart recurring collection, MVP synthesis, release automation, or product-spec generation unless the project is explicitly revived.

If revived, begin from the validation plan in `analysis/business-viability/risks-and-validation.md`, not from the old automation loop.
