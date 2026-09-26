---
id: investment-returns-theoretical-relationships
title: Investment returns theoretical relationships
domains: [eco, fin-eng]
status: drafted
requires: []
spends: []
anchor: [ifoa.cp1.4.4-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The total return on an asset over a period is the income it pays plus the change
in its price, both measured as a proportion of the price paid at the start of the
period. Equities, bonds and cash decompose the same total differently: an equity's
return splits into dividend yield and capital growth, a bond's into coupon and
price movement toward redemption, and cash's collapses to interest alone, since it
has no capital value to move.

## The expression

$$
R_t = \frac{I_t + (P_t - P_{t-1})}{P_{t-1}}
$$

Here $R_t$ is the total return earned over period $t$, $I_t$ is the income
received during the period, and $P_t$ and $P_{t-1}$ are the asset's price at the
end and at the start of the period. Splitting the nominal return further, the
Fisher relationship states that one plus the nominal return is approximately one
plus the real return times one plus the inflation rate, which is how price and
earnings inflation feed into the income and capital components above.

## Why this node exists

A portfolio holding equities, bonds and cash cannot be compared on a like basis
until each asset's return is broken into the same income-and-capital shape, and a
real-terms comparison cannot be made until inflation is stripped out of the
nominal figure. Equity fundamental analysis needs this decomposition next, since
it prices an equity from its expected dividend and growth components rather than
from the single nominal return this node defines.
