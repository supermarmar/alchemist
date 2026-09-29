---
id: lgd-foundation-approach-unsecured-claims
title: LGD foundation approach for unsecured claims
domains: [credit, regulation]
status: drafted
requires: [loss-given-default]
spends: []
anchor: [bcbs.d424.irb.para-70]
vault_articles: [regulation/eba-credit-insurance-unfunded-protection]
vault_sources: []
taught_in: null
---

## Definition

The foundation approach supervisory loss given default for an unsecured claim is a fixed
value set by borrower type and seniority, applied in place of a bank's own estimate.

## The expression

$$
LGD_{FIRB} =
\begin{cases}
0.45 & \text{senior, unsecured, bank or financial institution} \\
0.40 & \text{senior, unsecured, other corporate} \\
0.75 & \text{subordinated, any borrower type}
\end{cases}
$$

Here $LGD_{FIRB}$ is the loss given default a bank applies under the foundation approach.
A senior claim on a bank or another financial institution carries 45 per cent, a senior claim
on any other corporate carries 40 per cent, and a subordinated claim carries 75 per cent
whatever the borrower type, since subordination alone dominates the borrower distinction the
senior values draw.

## Why this node exists

A bank using the foundation approach estimates its own probability of default but not its own
loss given default, and without a fixed value the foundation approach would have nothing to
put in that second slot of the expected loss calculation. The EBA's 2024 review of credit
insurance tested exactly the 45 per cent value against empirical bank data and found the
distribution centred close to it, which is the evidence a supervisory parameter this coarse
needs to stay credible. The LGD foundation approach for real estate and receivables collateral
needs this node next, since it is the same foundation-approach logic applied once a claim
carries collateral rather than standing unsecured.
