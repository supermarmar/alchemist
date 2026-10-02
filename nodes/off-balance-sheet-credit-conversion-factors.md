---
id: off-balance-sheet-credit-conversion-factors
title: Off-balance sheet credit conversion factors
domains: [credit, regulation]
status: drafted
requires: [standardised-approach-credit-risk]
spends:
  - {object: obj.exposure, domain: credit}
  - {object: obj.exposure, domain: regulation}
anchor: [bcbs.d424.irb.para-100, bcbs.d424.sa.para-78]
vault_articles: [regulation/eba-off-balance-sheet-ccf-standardised]
vault_sources: []
taught_in: null
---

## Definition

A credit conversion factor turns an off-balance sheet commitment or facility into an
on-balance-sheet-equivalent exposure by scaling its notional amount down according to
how likely it is to be drawn before default, from full conversion for a direct credit
substitute to a small fraction for an unconditionally cancellable commitment.

## The expression

$$
\mathrm{EAD}_i = \mathrm{CCF}_i \times N_i
$$

Here $\mathrm{EAD}_i$ is the exposure at default the off-balance sheet item
contributes, $N_i$ is its notional amount, and $\mathrm{CCF}_i$ is the credit
conversion factor set by the bucket the item is allocated to.

## Why this node exists

A commitment a bank has not yet drawn still carries default risk, because a
borrower's creditworthiness can deteriorate right up to the point of default and the
bank often cannot stop the drawdown in time, so capital held only against the drawn
balance would systematically understate exposure. Leverage ratio off-balance sheet
exposure measurement needs it next, since the leverage ratio's exposure measure
reuses the same conversion logic without any risk weighting on top.
