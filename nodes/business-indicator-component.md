---
id: business-indicator-component
title: Business Indicator Component
domains: [fin-man, regulation]
status: drafted
requires: [standardised-approach-operational-risk-2023]
spends: []
anchor: [bcbs.d424.oprisk.para-5]
vault_articles: [regulation/operational-risk-business-indicator]
vault_sources: []
taught_in: null
---

## Definition

The Business Indicator Component scales the Business Indicator, a financial-statement-based
proxy for a bank's operational risk exposure, into a capital charge through marginal
coefficients that rise in steps as the Business Indicator grows.

## The expression

$$
\mathrm{BIC} = \sum_{k=1}^{3} \alpha_k \, \bigl[\min(\mathrm{BI}, u_k) - u_{k-1}\bigr]_{+}
$$

Here $\mathrm{BI}$ is the Business Indicator, $u_0 = 0$, $u_1$ and $u_2$ are the band
boundaries the framework sets, at 1 billion euro and 30 billion euro, $u_3 = \infty$, $\alpha_k$
is the marginal coefficient applied to the slice of $\mathrm{BI}$ falling within band $k$, at
12%, 15%, and 18% respectively, and $[\,\cdot\,]_{+}$ denotes the positive part.
$\mathrm{BIC}$ is the sum of these marginal contributions across all three bands.

## Why this node exists

The Business Indicator Component scales purely with the size of the income proxy, so a bank
with a clean loss history and one with a poor loss history of the same size receive the same
charge from this formula alone. The Internal Loss Multiplier needs this node next, since it is
the factor some jurisdictions apply on top of the Business Indicator Component to bring a
bank's own loss experience back into the charge.
