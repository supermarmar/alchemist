---
id: securitisation
title: Securitisation
domains: [credit, fin-eng]
status: drafted
requires: []
spends: []
anchor: [assa.f107.3.6-3, assa.f207.1.9-1, assa.f207.2.6-1, ifoa.sp5.2.1-6]
vault_articles: [regulation/bcbs-securitisation-framework, regulation/uk-securitisation-regulation]
vault_sources: []
taught_in: null
---

## Definition

Securitisation pools a portfolio of loans and sells tranched claims on their cash flows to
investors, so that the credit risk of the pool passes from the originating lender to whoever
holds each tranche.

## The expression

$$
L_{[a,d]}(l) = \frac{\min\bigl(\max(l - a, 0),\, d - a\bigr)}{d - a}
$$

Here $l$ is the pool's realised loss rate as a fraction of its notional, $a$ and $d$ are the
tranche's attachment and detachment points, also expressed as a fraction of pool notional, and
$L_{[a,d]}(l)$ is the fraction of the tranche's own notional absorbed once pool losses reach
$l$. A tranche absorbs nothing while losses sit below its attachment point and is wiped out
once they reach its detachment point.

## Why this node exists

Without tranching, a portfolio's credit risk could only be sold whole, so no investor could
take an exposure calibrated to their own appetite. Splitting the pool's realised losses by
seniority lets one buyer hold the deeply subordinated first-loss piece and another hold a
senior tranche protected by everything below it, and it is this same loss function that
regulators size capital against: the Basel SEC-IRBA approach takes a tranche's attachment and
detachment points as direct inputs, and the originator is separately required to retain a
material share of the first-loss risk rather than passing all of it on. Securitisation
valuation needs this loss function next, since pricing a tranche means pricing its expected
value under a chosen distribution for the pool's losses.
