# MVP Council Verdict - 2026-07-27 - Iteration 004

## Snapshot

- MVP iteration: `research/mvp-iterations/2026-07-27-mvp-iteration-004.md`
- Based on sample through: 2026-07-23
- Reviewed product spec files: `research/product-specs/2026-07-21-product-spec-001.md`
- Reviewed signal/comment evidence:
  - `research/signals/2026-07-23-brevo-community-authenticated-transactional-spam-rejection.md`
  - `research/signals/2026-07-22-reddit-emailmarketing-seed-test-preflight-gap.md`
  - `research/signals/2026-07-22-reddit-emailmarketing-promotions-visibility-gap.md`
  - `research/signals/2026-06-23-reddit-digitalmarketing-provider-scoped-feedback-gap.md`
  - `research/signals/2026-06-15-reddit-klaviyo-gmail-bounce-spike.md`
- Council skill: `agent-plugins:council` from `valentin-agent-plugins`
- Requested alias: `valentin-agent-plugins::counsil`

## Council Question

Pressure-test the whole MVP: what is strongest, what will fail, what should be simplified or expanded, and what next implementation decision should be made?

## Where the Council Agrees

- The strongest product thesis is an evidence workflow, not a deliverability oracle. "Authentication passes" must remain an input, not a diagnosis closure.
- The MVP is still too broad across agencies/MSPs, SaaS ops, and ecommerce/Klaviyo teams. The first build needs one buyer and one repeatable incident pattern.
- The core user-facing language should be plain incident questions: who rejected it, where did it land, what changed, what can be proved, and what next action is safe?
- Confidence discipline is the product's trust layer. Every hypothesis needs observed evidence, missing evidence, contradictory evidence, not-observable states, and action risk.
- Manual imports are acceptable only if the output is immediately useful: a ranked explanation, a safe next step, a recheck path, and a redacted support packet.

## Where the Council Clashes

- Four advisors prefer agencies/MSPs as the first buyer because they see repeated incidents across clients, need reusable escalation packets, and can tolerate manual evidence handling.
- The Executor argues for ecommerce/Klaviyo Gmail anomaly triage first because the current sample clusters around Klaviyo/Gmail incidents and the import path is more concrete.
- The synthesis resolves this by choosing agencies/MSPs as the buyer wedge, but constraining the first incident template to Gmail/Outlook placement, rejection, or bounce anomalies that often appear in Klaviyo and ESP exports.

## Blind Spots the Council Caught

- Data acquisition is the fragile part. Headers, NDRs, ESP exports, screenshots, seed results, and support replies will be incomplete, inconsistent, pasted incorrectly, or unavailable.
- The MVP needs an evidence quality gate: the minimum evidence required to rank hypotheses, when to refuse ranking, and how to guide users to collect missing proof.
- The workflow needs a failure-mode contract: what the system says when it cannot explain an incident, what it refuses to claim, and how it still helps the user act safely.
- Governance matters: separate observed fact, inference, and recommended action; preserve audit trails, redaction previews, source credibility, and decision ownership.
- "Explainable" needs an evaluation loop: compare output against known incidents, measure time-to-cause, support-ticket quality, reduced false escalations, and safe next-action completion.

## The Recommendation

Build the MVP as an agency/MSP incident brief generator with a console workbench behind it. The first product surface should not be a broad dashboard; it should be a guided incident file that turns messy artifacts into a provider-scoped explanation, confidence-gated recommendation, recheck checklist, and redacted escalation packet.

Keep the first incident template narrow: "client mail suddenly stops reaching Gmail/Outlook, lands in Spam/Promotions, or starts bouncing/rejecting after a sending, DNS, content, list, cadence, or ESP change." This preserves the reusable evidence model while giving implementation a concrete path.

Defer deep provider matrices, broad portfolio analytics, many connectors, and rich RBAC until the evidence schema, confidence model, packet format, and manual import loop prove repeat value with design partners.

## The One Thing to Do First

Define and test the normalized evidence schema plus confidence/ranking rules for the first agency/MSP incident template before building UI polish or integrations.
