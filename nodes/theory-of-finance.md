---
id: theory-of-finance
title: Theory of finance
domains: [fin-eng]
status: drafted
requires: []
spends: []
anchor: [up.fni700.1, up.fni700.2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The theory of finance covers the foundational results that later valuation and portfolio
techniques build on: that money has a time value, and that an asset's expected return is
determined by the systematic risk it adds to a diversified portfolio.

## The expression

$$
E(R_i) = R_f + \beta_i \bigl(E(R_m) - R_f\bigr)
$$

Here $E(R_i)$ is the expected return an investor requires on asset $i$, $R_f$ is the risk-free
rate, $E(R_m)$ is the expected return on the market portfolio, and $\beta_i$ measures how
sensitive asset $i$'s return is to the market's, so that $E(R_m) - R_f$ is the market risk
premium and $\beta_i$ scales how much of it asset $i$ must be compensated for.

## Why this node exists

Without a stated relationship between risk and expected return, a valuation has no defensible
discount rate to apply to a risky cash flow, and an investor has no basis for comparing two
assets that differ in risk rather than only in expected payoff. Capital structure and cost of
capital needs this relationship next, since the cost of equity it derives is exactly the
expected return this formula prices.
