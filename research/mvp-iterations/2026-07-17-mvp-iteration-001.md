# MVP Iteration 001 - 2026-07-17

## Snapshot

- Weekday: Friday
- Version: 001
- Based on sample through: 2026-07-17
- Reviewed MVP files: none (first iteration)
- Reviewed product spec files: none (no prior Tuesday specification)

## Potential MVP

An explainable deliverability incident console for low- and mid-volume senders: ingest a test-message header and sender profile, classify the failure layer (auth, reputation, blocklist, provider verdict, placement, or feedback gap), retain evidence, and produce a prioritized remediation and escalation runbook. It must explicitly distinguish “auth passes” from “will inbox,” and “external blacklist clean” from provider reputation.

## Finalized Decisions

- Start as an evidence-and-workflow product, not a deliverability scoring oracle or sending platform.
- Treat provider SMTP verdicts, headers, and provider dashboards as stronger evidence than generic blacklist tools.
- Model unknown/low-volume provider telemetry as an explicit state, never a green result.
- Keep one incident timeline with ownership, remediation steps, retry dates, and an exportable support packet.

## Changes

- Add a sender-history lens: domain age, early bounce bursts, volume changes, complaints, and engagement proxies.
- Add an identity-evidence preflight: outbound IP, EHLO, forward/reverse DNS, alignment, and provider-specific IDs.
- Add an outbound-block gate: preserve provider SMTP codes such as `5.7.520`, pause broad sends, and distinguish a content test from reputation recovery.

## Fixes

- Prevent false diagnosis from redacted or mismatched IP evidence.
- Separate DMARC rollout guidance from inbox-placement guidance; do not suggest weakening policy as a reputation fix.
- Make provider escalation status and low-volume telemetry gaps visible and actionable.

## Requirements

- Header parser with SPF/DKIM/DMARC, SMTP/NDR, SCL/BCL, provider code, and routing extraction.
- Checks for DNS/auth, exact-IP blocklist evidence, provider portals (Postmaster/SNDS where available), and list-health inputs.
- Explainable rule output: evidence, confidence, alternative hypotheses, owner, next action, and recheck date.
- Remediation templates: stop/isolate, list hygiene, credential/compromise check, gradual rewarm, delist/escalation packet, and validation send.
- Recipient-feedback risk check: campaign/group-send pattern, opt-in evidence, recent junk complaints, and a constrained re-entry audience.
- Inbox-placement test integration or manual evidence capture; do not claim placement from delivery alone.

## Majority Needs Covered

- “Authentication passes but Gmail/Outlook still sends mail to Spam or Junk.”
- “No Postmaster/SNDS data or no visible provider reason at low volume.”
- “Blocklist/reputation verdicts conflict across Microsoft, external tools, and shared-IP providers.”
- “I need a concrete incident runbook, evidence packet, and controlled recovery path.”

## Proposed MVP Shape

- Incident intake: paste headers/NDR, sender facts, volume and list-quality snapshot.
- Evidence board: auth/DNS, IP identity, blocklists, provider evidence, placement probes, and unknowns.
- Decision engine: transparent rules with confidence and a non-diagnostic “insufficient data” result.
- Remediation layer: owned checklist, scheduled rechecks, provider-specific escalation copy, and before/after evidence.

## Pros

- Solves the cross-tool explanation gap without requiring customers to replace their ESP.
- Useful at low volume because it gives a safe evidence path rather than pretending dashboards have data.
- Rule-first scope is fast to build, auditable, and can later learn from resolved incidents.

## Cons

- Provider reputation remains partially opaque; the product cannot guarantee inbox placement.
- Some high-value integrations and seedlist tests cost money or require customer permissions.
- Advice quality depends on accurate headers, account data, and operating discipline.

## Open Questions

- Which initial integrations are feasible without fragile scraping: Google Postmaster, Microsoft SNDS, SES, or manual upload?
- Is the first paid persona an MSP/agency managing several small senders, or a single-company operator?
- What minimum placement-probe coverage provides useful confidence without enterprise seedlist cost?

## Investor View

### Value And Problem

- The pain is operationally severe: missed sales, failed transactional mail, support queues, and reputational damage occur while conventional checks report “all green.”
- Initial wedge: explain why the sender cannot see a root cause and drive the next safe action in minutes instead of consultant-led trial and error.

### Business Model

- Tiered SaaS by monitored sender/domain and retained incident history; paid placement tests and MSP multi-tenant seats as expansion.
- Software margins scale well because parsing and rules are cheap; support burden requires strong guided remediation and scoped claims.

### Market And Competitors

- TAM: email-sending businesses; SAM: SMB, agencies, MSPs, and SaaS teams using ESPs or Microsoft/Google; SOM: operators with recurring unexplained placement incidents.
- Competitors include GlockApps/Validity seedlist monitoring, Mailgun/SendGrid/SES dashboards, Postmaster/SNDS, MXToolbox, and deliverability consultants.
- USP: evidence-led cross-provider diagnosis and remediation workflow for the telemetry-poor sender, rather than another isolated score.

### Marketing And Sales

- Acquire through deliverability incident content, DNS/header diagnostic tools, MSP/agency partners, and ESP implementation consultants.
- Retain through incident history, scheduled evidence refresh, reusable support packets, team playbooks, and multi-domain monitoring.

### Top Risks

- Opaque provider signals can make recommendations look authoritative when they are not; mitigate with evidence labels, confidence, and “unknown” outcomes.
- Integrations and placement data can be expensive or brittle; mitigate with manual evidence ingestion and a connector roadmap gated by demand.
- The category is crowded and trust-sensitive; mitigate with narrow low-volume workflow focus, accurate provider citations, and no inbox-guarantee claims.

## Evidence Base

- [New-domain reputation versus DMARC](../signals/2026-05-22-serverfault-new-domain-reputation-vs-dmarc.md)
- [Microsoft S3150 verdict gap](../signals/2025-12-10-serverfault-microsoft-blocklist-verdict-gap.md)
- [Gmail low-volume feedback gap](../signals/2026-06-01-gmail-community-domain-reputation-escalation.md)
- [Marketo blocklist incident runbook](../signals/2026-05-06-adobe-marketo-blocklist-incident-runbook.md)
- [AWS false bounce and suppression](../signals/2026-02-05-aws-repost-ses-false-bounce-suppression.md)
- [Microsoft outbound spam block](../signals/2026-06-09-microsoft-qa-outbound-spam-block.md)
