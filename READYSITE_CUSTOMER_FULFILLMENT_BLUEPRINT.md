# ReadySite First-Customer Fulfillment Blueprint
Status: Staged internal plan, not production proof. No other business assets or credentials authorized.

## Pilot offer under test
$499 one-time implementation, $99/month. See READY_SITE_OFFER_MANIFEST.json for current commercial hypothesis. No charging until pricing, agreement, refund logic, and invoice/payment provider are actually approved and tested.

## Lead to launch sequence
1. **Inquiry**: customer submits to verified endpoint; opt-in/disclosure, spam screening, acknowledgement, and internal record created. BLOCKED: business inbox/end-point not yet established.
2. **Qualification**: confirm service geography, industry, legitimate business, website objective, decision maker, and fit. Proposed lead fields: intake_id, received_at, lead_source, business_name, business_contact, trade, jurisdiction, requested_services, consent_record, status, owner_approval.
3. **Proposal**: scope one page, revisions, updates, hosting/domain responsibility, exclusions, launch timing, ownership/portability, support and cancellation. No universal guarantee.
4. **Agreement & payment**: human-approved contract, valid tax/business information, actual processor, completed test transaction and refund procedure. BLOCKED.
5. **Intake**: request only needed client business facts and permission to use customer-provided logos/images; secure storage and access per-client. Intake demo is `intake-preview.html`, browser-local and no persistence.
6. **Generate**: use existing generator only after verifying its source and test inputs; all public claims must reflect client-provided facts.
7. **QA**: mobile/desktop rendering, working phone/link, contact form delivery if included, performance, accessibility, metadata, no fake reviews, factual accuracy, domain/SSL, consent, ownership rights.
8. **Approval**: client sign-off on copy and content; separately recorded owner approval for publication.
9. **Deploy**: use scoped credentials, isolated client site/project, HTTPS and rollback. No shared editable secrets.
10. **Handoff**: record URL, deployment commit, contact test, client ownership, support channel, subscription start, renewal date, export/backup.
11. **Monthly care**: uptime and links checks, up to two bounded text edits, monthly metrics only where tracking is actually installed, customer support, billing and cancellation/portability workflows.
12. **Exceptions**: outage, revoked permission, refund request, billing failure, abusive use, domain expiration, cancellation. Ensure support escalation path.

## Suggested data and logging controls
- Do not store real customer PII in a public GitHub repository, static HTML, or branch.
- No universal inbox API keys embedded in JS or client pages.
- Every lead and client needs a unique stable ID and separated access boundary.
- Keep immutable status transitions and human approvals; document retention and deletion requirements.
- Limit agent access to ReadySite-only scopes; owner review before external action.

## Acceptance test matrix
| Gate | Demonstration | Current state |
|---|---|---|
| Business email | Test messages arrive in monitored mailbox, retries/alerts | BLOCKED |
| Inquiry submit | Real HTTPS submission, spam filters, no duplicate leads | BLOCKED |
| Consent/Privacy | Approved disclosure, retention and deletion mechanics | BLOCKED |
| Proposal | Generated from canonical offer; exclusions accurate | DESIGN ONLY |
| Agreement | Legally reviewed terms with signature receipt | BLOCKED |
| Payment | Successful test charge, webhooks, refund, cancellation | BLOCKED |
| Site generator | Actual realistic intake produces releasable site | DRY-RUN REPORTED ONLY |
| Site QA | Mobile/a11y/link/claims checks and rollback | NOT VERIFIED |
| Reporting | Instrumented visits, uptime and monthly report | NOT BUILT |
| Monthly updates | Request, bounded delivery, time tracking | NOT VERIFIED |

## Commercial instrumentation
Track sales funnel counts (valid inquiries -> qualified -> proposed -> signed -> paid -> live), time-to-go-live, setup hours, hours/month, failures, refunds, collected MRR, churn, and client-paid direct costs. Model owner labor at a real replacement wage. No profit claims from projected contribution alone.

## Release authority
This file and the demo do not enable customer submissions, contracts, payments, outbound messaging, uploads or publication.
