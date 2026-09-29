---
id: corporate-loan-pricing
title: Corporate banking loan pricing
domains: [credit, fin-man]
status: drafted
requires: [risk-based-pricing]
spends:
  - {object: obj.exposure, domain: credit}
anchor: [assa.f107.5.3-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Corporate loan pricing sets the interest rate a bank charges on a loan negotiated individually
with a corporate borrower, building the rate up from the bank's cost of funding, the expected
loss the loan carries, the capital it consumes and the bank's required margin.

## The expression

$$
r = r_f + \mathrm{PD} \times \mathrm{LGD} \times \frac{\mathrm{EAD}_i}{L} + c_o + k\cdot c_e + m
$$

Here $r$ is the loan's interest rate, $r_f$ is the bank's cost of funds, $\mathrm{PD}$ and
$\mathrm{LGD}$ are the borrower's probability of default and loss given default, $\mathrm{EAD}_i$
is the exposure at default and $L$ the loan's principal, so the middle term is the expected loss
rate. The remaining terms are the operating cost rate $c_o$, the cost of the economic capital
$c_e$ the loan consumes at rate $k$, and the margin $m$ the bank requires above breakeven.

## Why this node exists

A corporate loan is negotiated individually, unlike a retail rate priced off a fixed card, so the
bank has to be able to justify its rate loan by loan against the specific borrower's credit
standing, and building the rate up from its separate cost components is what makes that
justification possible. Without this decomposition, a bank cannot tell whether a competitively
priced loan is still covering its expected loss and its cost of capital, or whether it is
being underpriced to win the relationship.
