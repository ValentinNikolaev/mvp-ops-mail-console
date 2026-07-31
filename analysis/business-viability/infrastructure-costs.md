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
