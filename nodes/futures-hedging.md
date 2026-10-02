---
id: futures-hedging
title: Futures
domains: [fin-eng]
status: drafted
requires: [hedging]
spends: []
anchor: [assa.f107.7.5-4-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Because a futures contract's price rarely moves in exact step with the exposure being
hedged, the number of contracts a hedger holds is chosen to minimise the variance of the
hedged position's value. A one-for-one match between contracts and exposure only achieves
that minimum where the two move in perfect step, which is the special case the general
hedge ratio below reduces to.

## The expression

$$
h^* = \rho\, \frac{\sigma_S}{\sigma_F}
$$

Here $h^*$ is the minimum-variance hedge ratio, $\rho$ is the correlation between changes
in the spot price and changes in the futures price, and $\sigma_S$ and $\sigma_F$ are the
standard deviations of those two changes.

## Why this node exists

A hedge sized one contract for one unit of exposure assumes the futures price and the
underlying move together perfectly, an assumption basis risk violates whenever the two
are not identical. The minimum-variance ratio corrects for that imperfect correlation, and
the number of contracts a hedger actually holds follows from scaling $h^*$ by the relative
size of the exposure and a single futures contract.
