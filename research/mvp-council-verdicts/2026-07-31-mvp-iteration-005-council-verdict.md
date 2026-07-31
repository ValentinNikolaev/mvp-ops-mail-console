# MVP Council Verdict - 2026-07-31 - Iteration 005

## Snapshot

- MVP iteration: `research/mvp-iterations/2026-07-31-mvp-iteration-005.md`
- Based on sample through: 2026-07-31
- Reviewed product spec files: `research/product-specs/2026-07-28-product-spec-005.md`
- Reviewed signal/comment evidence: 68 accepted signals; the July Postal issue and 2/2 parsed replies demonstrate that receiver-side authentication passes and sender-UI warnings can be non-equivalent checks.
- Council skill: `agent-plugins:council` from `valentin-agent-plugins`
- Requested alias: `valentin-agent-plugins::counsil`

## Council Question

Pressure-test the whole MVP: what is strongest, what will fail, what should be simplified or expanded, and what next implementation decision should be made?

## Where the Council Agrees

- Build the product as a diagnosis-and-proof workflow, not deliverability optimization or a sending platform.
- A canonical incident/evidence schema is the durable core; it enables reproducible packets, uncertainty, auditability, and later integrations.
- Treat evaluator identity, SMTP path, raw-to-redacted provenance, and `cannot conclude` as first-class fields; do not show one unified authentication pass/fail badge.
- Keep v1 manual-first and narrow: four artifact inputs, deterministic checks, bounded hypotheses, redacted packet, and human-approved action.
- Start with agencies/MSPs and Gmail/Microsoft 365 escalation cases; measure time-to-triage and packet usefulness.

## Where the Council Clashes

- The strongest initial value may be a narrow provider/ESP escalation packet, while the longer-term opportunity is a broader incident workbench. The verdict favors the packet as the wedge and retains the workbench only as an internal implementation shape.
- Manual input reduces integration and privacy risk but adds onboarding friction. The answer is a strict case-completeness rubric, not early connector breadth.
- A strict gate prevents unsafe claims but can be a dead end. The resolution is a partial evidence-gap/handoff packet that asks precisely for the missing source fields.

## Blind Spots the Council Caught

- Buyer and willingness-to-pay remain unvalidated; faster triage must be compared with the current consultant, ticketing, and spreadsheet process.
- Define read-only data-access, redaction, retention, export, authorization, freshness, and provenance boundaries before UI expansion.
- Without a measurable baseline, the system risks becoming polished documentation rather than remediation infrastructure.
- Define agency/client roles, tenant isolation, retention/deletion, audit access, and evidence-export controls before piloting sensitive mail artifacts.

## The Recommendation

Build a narrow, evidence-to-handoff console for agencies/MSPs. Establish the canonical schema and 8–12 deterministic Gmail/Microsoft rules first. Every output must distinguish source-scoped fact, derived finding, hypothesis, confidence, missing SMTP-path evidence, and a reversible next test. Emit a decision-ready packet or an evidence-gap/handoff packet; gate connectors on a historical-case pilot showing materially faster, more accepted escalations.

## The One Thing to Do First

Prototype the canonical packet on 10–20 historical agency/MSP Gmail or Microsoft 365 cases, including the Postal SPF literal-include scenario; measure time-to-handoff, missing-evidence rate, analyst rework, and false-confidence incidents.
