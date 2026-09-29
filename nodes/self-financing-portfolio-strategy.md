---
id: self-financing-portfolio-strategy
title: Self-financing portfolio strategy
domains: [fin-eng]
status: drafted
requires: [previsible-process]
spends: []
anchor: [ifoa.sp6.3.2-6, ifoa.sp6.3.2-7, ifoa.sp6.3.3-8, ifoa.sp6.3.3-9]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A portfolio strategy is self-financing where its value changes only through gains and losses on the assets already held, with no cash added to or withdrawn from the strategy after it begins.

## The expression

$$
V_t = V_0 + \int_0^t \phi_u \, dS_u
$$

Here $V_t$ is the portfolio's value at time $t$, $V_0$ is its initial value, $\phi_u$ is the previsible process giving the units of the risky asset held over $[u, u + du)$, and $S_u$ is the asset's price at $u$. The integral is the cumulative trading gain the strategy has earned by $t$, and the absence of any other term is exactly what makes the strategy self-financing: every change in $V_t$ traces to a price movement in an asset already held.

## Why this node exists

A strategy free to inject cash whenever it likes could replicate any payoff trivially, by simply topping up the shortfall at each step, so the self-financing restriction is what makes replication a genuine test of what a market's existing assets can span. Building a replicating strategy this way is how a derivative's price is pinned down by no-arbitrage alone, with no need to appeal to any model of how likely each outcome is.
