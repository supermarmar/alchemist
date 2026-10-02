---
id: inflation-adjusted-chain-ladder
title: Inflation-adjusted chain ladder
domains: [gi]
status: drafted
requires: [chain-ladder]
spends:
  - {object: obj.cohort-index, domain: gi}
  - {object: obj.development-factor, domain: gi}
  - {object: obj.development-index, domain: gi}
  - {object: obj.ultimate, domain: gi}
anchor: [ifoa.cm2.4.2-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The inflation-adjusted chain ladder method deflates each diagonal of a run-off triangle to a
common price base before development factors are estimated, and re-inflates the resulting
ultimate to reflect the claims inflation expected between the valuation date and settlement.

## The expression

$$
C_{i,j}^{*} = C_{i,j} \cdot \frac{I_0}{I_{i+j}}, \qquad U_i = \left( C_{i,I-i}^{*} \prod_{j=I-i}^{I-1} f_j^{*} \right) \cdot I_{i+I}
$$

Here $C_{i,j}$ is the cumulative claims for accident period $i$ at development period $j$,
$I_t$ is the price index at calendar time $t$, and $C_{i,j}^{*}$ is that same cumulative claims
figure restated in base-date prices. $f_j^{*}$ is the development factor estimated from the
deflated triangle, carrying a deflated cohort from development period $j$ to $j+1$, and $U_i$
is the projected ultimate for accident period $i$, inflated back up by $I_{i+I}$ to the price
level expected when that cohort finally settles.

## Why this node exists

Where claims inflation runs at a different rate from the pattern in a raw triangle, the plain
chain ladder's development factors mix the true development pattern with whatever inflation
happened to prevail over the historical period, and projecting those factors forward silently
carries the wrong inflation assumption into the reserve. Deflating first isolates the
development pattern from price movements, and re-inflating afterwards lets the reserving
actuary substitute their own view of future claims inflation for the historical average the
raw triangle would otherwise impose.
