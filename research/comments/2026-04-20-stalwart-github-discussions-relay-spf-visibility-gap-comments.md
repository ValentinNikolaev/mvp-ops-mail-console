---
source: "Stalwart GitHub Discussions"
url: "https://github.com/stalwartlabs/stalwart/discussions/3004"
canonical_id: "2026-04-20-stalwart-github-discussions-relay-spf-visibility-gap"
comments_supported: "yes"
comments_available_count: 304
comments_parsed_count: 304
parse_status: "complete"
---

## Most Useful Comments Summary

- A self-hosted operator showed that Stalwart's automatic DNS created `v=spf1 mx -all` even though outbound delivery was routed through a separate relay; Gmail therefore reported SPF fail despite successful SMTP handoff.
- The same operator tested a manual TXT change that included the relay and captured Gmail changing to SPF pass. This separates a recipient-visible authorization failure from a generic transport or reputation diagnosis.
- Replies point to an operational workaround (manage the SPF record at the registrar / include the relay IP or host) but do not establish automatic relay-SPF customization. Several migration replies separately show that auth, spam-filter, logging, and telemetry settings may need explicit post-upgrade review.

## Useful Comment Artifacts

- 2026-05-01 reporter: asks how to authorize an outbound relay in the automatically managed SPF record.
- 2026-05-03 responder: distinguishes inbound SPF verification from the sender's DNS authorization and points to relay routing.
- 2026-05-04 reporter: supplies Gmail headers proving failure with the generated record and pass after the manual relay reference; asks whether automatic customization exists.
- 2026-05-11 operator: reports numerous manually reviewed migration settings, including spam-filter entries and observability configuration, reinforcing the need for post-change evidence checks.
