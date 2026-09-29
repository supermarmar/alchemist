---
id: risk-diversification
title: Diversification
domains: [fin-man]
status: drafted
requires: []
spends: []
anchor: [assa.f107.3.3-1]
vault_articles: [regulation/eba-retail-diversification]
vault_sources: []
taught_in: null
---

## Definition

Diversification is the spreading of exposure across borrowers, sectors or risk
types so that losses in one part of a book are unlikely to coincide with losses in
another. It reduces the variance of the aggregate loss below the sum of the
variances of the individual exposures, and the reduction is greatest where the
exposures are uncorrelated.

## The expression

$$
\operatorname{Var}\Bigl(\sum_{i=1}^n L_i\Bigr) = \sum_{i=1}^n \operatorname{Var}(L_i) + \sum_{i \ne j} \operatorname{Cov}(L_i, L_j)
$$

Here $L_i$ is the loss on exposure $i$, $\operatorname{Var}(L_i)$ is its own
variance, and $\operatorname{Cov}(L_i, L_j)$ is the covariance between the losses
on exposures $i$ and $j$. Aggregate variance falls towards the sum of the
individual variances alone as the covariance terms shrink towards zero, which is
the arithmetic diversification delivers, and it can rise well above that sum where
the covariances are large and positive instead.

## Why this node exists

A bank that measures each exposure's risk in isolation overstates how safe a
concentrated book is and understates how much a correlated one can lose at once,
since neither figure accounts for how losses move together. Correlation between
risks needs it next, because the covariance terms this node leaves as a residual
are exactly what that node goes on to model.
