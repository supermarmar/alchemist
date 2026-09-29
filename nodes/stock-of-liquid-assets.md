---
id: stock-of-liquid-assets
title: Stock of liquid assets
domains: [fin-man]
status: drafted
requires: [sources-of-liquidity]
spends: []
anchor: [assa.f107.10.1-4]
vault_articles: [regulation/bcbs-liquidity-coverage-ratio-original]
vault_sources: []
taught_in: null
---

## Definition

The stock of liquid assets is the pool of unencumbered assets a bank counts toward the
numerator of the Liquidity Coverage Ratio, restricted to those that can be converted to cash
quickly and without material loss of value even under stress.

## The expression

$$
\mathrm{HQLA} = L_1 + \min\!\left(L_2,\ \tfrac{2}{3}L_1\right)
$$

Here $\mathrm{HQLA}$ is the eligible stock of liquid assets, $L_1$ is the market value of
Level 1 assets, eligible in full and without haircut, and $L_2$ is the market value of Level 2
assets after their prescribed haircuts. The multiplier on $L_1$ enforces the cap that Level 2
assets can contribute no more than 40% of the total stock, so a bank cannot inflate its buffer
by holding lower-quality assets alone.

## Why this node exists

The Liquidity Coverage Ratio divides this stock by projected net cash outflows, so the ratio
is only as reliable as the assets counted in its numerator actually are under stress. An asset
that trades freely in ordinary conditions can stop trading altogether once a bank's own
solvency is in question, which is why eligibility is restricted to instruments such as central
bank reserves and high-grade government securities, with the cap limiting how far
lower-quality assets can substitute for them. A bank that meets the ratio on paper is thereby
meeting it with assets a genuinely stressed market would still buy.
