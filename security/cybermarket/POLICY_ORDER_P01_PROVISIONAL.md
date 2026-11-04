# CyberMarket CR — P-ORDER-01 (PROPOSED POLICY; NOT APPROVED)

**Owner:** hypothetical CyberMarket CR security-design research.
**State:** PROPOSED / NOT APPROVED by any product owner or Saleor maintainer.
**Versioned subject:** `Arkthos/saleor` source baseline `4cb1609a90eade14b6275a407bc7a00c35698090`.
**Companion case:** `CM-T22` (risk R11; observation H12).
**Scope:** selected GraphQL `order(id:)` response fields `userEmail`, `billingAddress.streetAddress1`, `shippingAddress.streetAddress1`.

## Proposed criterion

For the CyberMarket CR scenario, unless the application explicitly grants a separate read capability to an actor, **knowledge of an order UUID alone should not entitle an unrelated customer or anonymous request to retrieve personal billing/shipping fields or the raw customer email**.

This is a *candidate enterprise security requirement* for a fictional deployment. It must be reconciled with Saleor's intended business behavior, which may deliberately support externally shareable or nonauthenticated order access. It is **not** a statement that Saleor breached an authoritative Saleor requirement.

## Evidence and expected outcome

- C3/C7: `CM-T05` and `CM-T06` **characterize** observed raw field visibility to unrelated/anonymous actors given a known new-UUID order ID. They are not conformance tests.
- `CM-T07` demonstrates a distinct legacy order-number branch where selected fields are masked for nonowners.
- `CM-T22` applies this *proposed* rule to two synthetic actors (unrelated customer, anonymous). It uses `pytest.mark.xfail(strict=True)` to distinguish **expected policy failure** from a system/test crash or a passing control.
- A correctly reported `XFAIL` represents a reproducing *gap against the proposed policy*, not authorization to report a confirmed software vulnerability.
- A future `XPASS` produces a strict pytest failure and triggers manual review of whether code or requirements changed. It is not automatically a vulnerability fix.

## Decision gate

Before moving `P-ORDER-01` from proposed to accepted:
1. Document owner/customer/staff/app/anonymous access entitlement for each selected field.
2. Determine whether knowing an order UUID represents an intended bearer capability.
3. Specify if identifiers can be shared externally, their entropy, and any authorization requirements for recipient access; do **not** assume UUID enumeration is practical.
4. Define permitted masking/redaction values for each field and data category.
5. Verify the policy in a realistic deployment and/or ask the course team's hypothetical CyberMarket CR product owner to approve it.
6. Only after authorization decide whether `CM-T22` should become a strict passing security contract, remain a characterization/policy candidate, or be withdrawn.

## Accepted conclusions *today*

- **Confirmed implementation behavior (synthetic fixture):** selected personal fields are visible to additional actors given a UUID in the pinned revision.
- **Proposed design gap:** behavior differs from the more restrictive P-ORDER-01 hypothetical CyberMarket policy.
- **Unproven:** real-world exploitability, actual PII compromise, Saleor-design nonconformance, UUID guessability, a deployed-frontend flow that exposes UUIDs, and whether the desired policy is correct for Saleor.
- **No product code remediation is authorized by this document.**

Reference: [C7 experiment](experiment_C7_2026-10-18.md) and the source-level order resolver analysis in the approved Avance 1. Do not rewrite the approved academic manuscript in this testing phase.
