---
id: asset-return-relationships
title: Asset return relationships
domains: [fin-eng, stats]
status: drafted
requires: [bond-markets, equity-markets]
spends:
  - {object: obj.asset-correlation, domain: stats}
anchor: [up.fni700.4, up.ias712.24]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Asset return relationships describe how the returns on different asset classes
move together, summarised by the correlation between each pair of return series.

## The expression

$$
\rho_{ij} = \frac{\mathrm{Cov}(R_i, R_j)}{\sigma_i \sigma_j}
$$

Here $R_i$ and $R_j$ are the returns on two assets, $\mathrm{Cov}(R_i, R_j)$ is
their covariance, $\sigma_i$ and $\sigma_j$ are their standard deviations, and
$\rho_{ij}$ is the correlation coefficient, bounded between $-1$ and $1$, that
results.

## Why this node exists

A portfolio's risk is not the average of its holdings' individual risks but
depends on how those holdings move together, so no portfolio can be built
sensibly until that joint behaviour has a number attached to it. Portfolio
management needs it next, since the diversification benefit a portfolio can
achieve depends entirely on how correlated the assets held together turn out to
be.
