# ReadySite independent email and domain implementation plan
Status: PLANNED ONLY — no domain purchased, account opened, DNS modified, inbox provisioned or form activated.
Prepared: October 21, 2026. Boundary: ReadySite only.

## Recommendation
Preferred national brand domain: goreadysite.com, contingent on live registrar availability, pricing, ownership/trademark and suitability checks. Secondary names may be proposed only after checking availability. Avoid location-specific readysiteok.com.

Initial address: hello@<approved-domain>. After initial testing, add support@ and sales@ as aliases or separately managed mailboxes if the provider supports and the operations justify them. Never present example addresses as functioning before testing.

## Provider options and limitations
1. Cloudflare Registrar for domain and DNS, with actual registration/renewal price confirmed before owner purchase. Public registrar policy is at-cost, not a fixed $10.46 guarantee.
2. Zoho Mail Forever Free if available in the applicable data center, up to five users on one domain with 5GB/user and web access. Lack of IMAP/POP/forwarding on free plan limits connector/agent integrations. Verify actual enrollment and alias features before selecting.
3. Google Workspace Starter as paid fallback, advertised from $7/user/month on annual commitment (check current offer and terms). Do not begin trial absent owner approval.
4. Cloudflare Email Routing can forward inbound aliases to verified destinations, but is not a full two-way mailbox; don't equate forwarding with secure independent ReadySite sending.

Sources researched:
- https://www.cloudflare.com/products/registrar/
- https://www.zoho.com/mail/help/adminconsole/subscription.html
- https://workspace.google.com/pricing
- https://developers.cloudflare.com/email-service/platform/pricing/

## Provisioning sequence requiring owner authorization
1. Verify candidate domain availability, final checkout total, renewals, and brand/trademark risk; request approval for exact domain and expense.
2. Owner registers domain in a dedicated ReadySite-controlled account, enables MFA, account recovery and domain lock; do not share or commit credentials.
3. Select Zoho free if offered; otherwise bring back a paid alternative with exact price for approval. Owner handles business identity verification and account setup.
4. Verify DNS ownership and configure mailbox MX, SPF, DKIM and DMARC. Start DMARC at observation policy and increase enforcement after authenticating legitimate senders. Use only one authoritative SPF record.
5. Create hello@ first and test delivery both ways using external test mailboxes. Inspect spam placement, reply-to/from identity, message headers, bounces and delivery delays.
6. Add support@ and sales@ only as justified; verify each address can be received and accurately replied from. Do not create fake identities.
7. Publish contact address and support details only after message receipt is tested, privacy/cancellation terms are reconciled, and owner approves deployment.
8. Connect inquiry form backend with spam filtering, consent/notice, rate limiting, duplicate control, secure storage, retention/deletion, alerts and transaction logging. No keys in public static site.
9. Separately prepare compliant outbound infrastructure with appropriate postal address, unsubscribe and domain reputation. A working inbox alone does NOT establish CAN-SPAM readiness or permission to send outreach.

## Cost envelope
- Domain: real checkout required. Planning allowance around $10–15/year for ordinary available .com, not a quote or commitment.
- Zoho free: $0/month if user and region eligible, but automation limitations may force upgrade.
- Business postal mailbox + verification/notarization: separate future expense if cold commercial email is approved; the Oct 20 audit's $21.35 estimate excluded $25 notary.
- No new expense authorized here.

## Acceptance criteria
- Selected domain owned by the business, credentials safeguarded and MFA on.
- Domain MX/SPF/DKIM/DMARC assessed and test-authenticated.
- Successful incoming and outgoing mail on a verified ReadySite address.
- Dedicated ReadySite owner and recovery path; no shared Saira/Grokbot customer access.
- Reply and opt-out workflow documented before any outreach.
- Support inbox monitored with a defined response owner.
- Contact CTA and inquiry form go live only after accurate legal copy, tested backend and explicit deployment approval.

## Next owner decision
Approve a domain for pricing/availability investigation, then separately approve any registration and account opening with a concrete quote. No purchase implied by accepting this plan.
