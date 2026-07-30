---
source: "Microsoft Community Hub"
url: "https://techcommunity.microsoft.com/discussions/exchange_general/m365-tenant-emails-marked-as-spam-scl5-catphish-despite-perfect-authentication/4489993"
canonical_id: "2026-01-28-microsoft-community-hub-authenticated-m365-tenant-spam"
comments_supported: "yes"
comments_available_count: 1
comments_parsed_count: 1
parse_status: "complete"
last_checked_at: "2026-07-30T19:05:38+02:00"
---

## Most Useful Comments Summary

- Authentication is not the only decision input: the reply names domain and sending-IP reputation, content/signature signals, sender pattern, recipient Defender policy, and third-party relay reputation as separately testable causes of SCL 5/CAT:PHISH.
- The practical diagnostic is comparative: test other M365 tenants and private Gmail addresses, determine whether only direct tenant mail is affected, and inspect whether an external relay is the actual sending path.

## Useful Comment Artifacts

- A pass on SPF, DKIM, DMARC, and composite authentication narrows the remediation path; it does not establish inbox placement or exonerate sender/relay reputation.
- Check domain against blocklists, but do not use a clean blocklist result as a conclusion: collect header evidence and compare recipient/provider outcomes.
