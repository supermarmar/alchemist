---
id: single-index-model
title: Single-index model
domains: [fin-eng]
status: drafted
requires: [multifactor-model]
spends:
  - {object: obj.coefficients, domain: fin-eng}
anchor: [ifoa.cm2.3.3-2, ifoa.cm2.3.3-5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The single-index model is the multifactor model reduced to one systematic factor, the return on
a market index, so that every asset's return is explained by its sensitivity to that one factor
plus a residual specific to the asset.

## The expression

$$
R_i = \alpha_i + \beta_i R_m + \varepsilon_i
$$

Here $R_i$ is the return on asset $i$, $R_m$ is the return on the market index, $\beta_i$ is
asset $i$'s sensitivity to that market return, $\alpha_i$ is the return left unexplained by the
market, and $\varepsilon_i$ is the idiosyncratic residual, assumed uncorrelated across assets
and with $R_m$.

## Why this node exists

A multifactor model needs a separate covariance estimate between every pair of factors, which
becomes unwieldy as the number of factors grows, and collapsing every factor into one market
index removes that burden at the cost of assuming a single common source of risk explains
comovement between assets. That simplification is what makes portfolio variance tractable at
scale, since covariance between any two assets then reduces to their two betas and the
market's own variance alone.
