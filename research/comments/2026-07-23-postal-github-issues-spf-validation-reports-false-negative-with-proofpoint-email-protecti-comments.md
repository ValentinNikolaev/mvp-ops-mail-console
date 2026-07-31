---
source: "Postal GitHub Issues"
url: "https://github.com/postalserver/postal/issues/3611"
canonical_id: "2026-07-23-postal-github-issues-spf-validation-reports-false-negative-with-proofpoint-email-protecti"
comments_supported: "yes"
comments_available_count: 2
comments_parsed_count: 2
parse_status: "complete"
---

## Most Useful Comments Summary

- The key reply separates Postal's literal control-plane include check from an RFC 7208 evaluation of an SMTP transaction. A Gmail/Microsoft pass verifies one observed path; it cannot prove that Postal's configured include was present or traversed.
- A safe UI should describe the narrow configuration fact, support a distinct relay/gateway mode, and treat missing SMTP context, DNS limits, and lookup errors as indeterminate rather than passing.
- The maintainer reply confirms Postal does not follow nested or flattened SPF records and suggests verifying a sent message independently; this is remediation context, not proof of root cause.

## Useful Comment Artifacts

- Required redacted evidence for a conclusive path check: `smtp.mailfrom`, connecting client IP, HELO, and final-recipient `Authentication-Results`.
- Product rule: distinguish observed receiver authentication, configuration expectation, and unobservable effective-path evaluation.
- Safe next action: retain the warning as scoped configuration evidence while requesting a redacted received-message comparison before changing DNS or routing.
