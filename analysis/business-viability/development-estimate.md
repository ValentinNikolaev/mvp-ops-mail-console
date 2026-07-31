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
