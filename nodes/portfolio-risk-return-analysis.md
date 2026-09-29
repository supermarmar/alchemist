---
id: portfolio-risk-return-analysis
title: Portfolio risk and return analysis
domains: [fin-eng, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp5.8.1-1, ifoa.sp5.8.1-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Portfolio risk and return analysis decomposes the realised volatility of a
portfolio's return into the contribution made by each individual holding, so
that a holding's price movements can be judged against the risk it actually
adds to the whole rather than against its risk held in isolation.

## The expression

$$
\mathrm{RC}_i = w_i \frac{\mathrm{Cov}(r_i, r_p)}{\sigma_p}
$$

Here $w_i$ is the portfolio weight of holding $i$, $r_i$ and $r_p$ are the
returns of the holding and the portfolio respectively, $\sigma_p$ is the
portfolio's return standard deviation, and $\mathrm{RC}_i$ is holding $i$'s
contribution to that standard deviation; the contributions across every holding
sum exactly to $\sigma_p$.

## Why this node exists

Knowing how much of a portfolio's risk each holding contributes says nothing
yet about whether the return earned for that risk was adequate. Risk-adjusted
performance measures need this node next, setting the return each holding
earned against the risk contribution computed here.
