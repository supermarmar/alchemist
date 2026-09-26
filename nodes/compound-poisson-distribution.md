---
id: compound-poisson-distribution
title: Compound Poisson distribution
domains: [gi, stats]
status: drafted
requires: [collective-risk-model]
spends:
  - {object: obj.hazard, domain: gi}
anchor: [ifoa.cs2.1.2-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The compound Poisson distribution is the distribution of aggregate claims when the number of
claims follows a Poisson distribution and the individual claim amounts are independent and
identically distributed, and it carries the closure property that a sum of independent
compound Poisson random variables is itself compound Poisson.

## The expression

$$
S = \sum_{i=1}^{N} X_i, \qquad N \sim \mathrm{Poisson}(\lambda)
$$

Here $S$ is the aggregate claims for the period, $N$ is the number of claims, Poisson
distributed with mean $\lambda$, the claim intensity for the period, and $X_i$ is the amount
of the $i$-th claim, drawn independently of $N$ and of every other claim amount. The closure
property means a portfolio assembled from several independent compound Poisson sources, each
with its own $\lambda$ and claim amount distribution, can itself be analysed as a single
compound Poisson risk with the component parameters combined.

## Why this node exists

A collective risk model built only from a claim number distribution and a claim amount
distribution separately says nothing about their sum until that sum's own distribution is
named, and the compound Poisson is that name whenever the claim count itself is Poisson. The
moments of compound claim distributions need this construction settled before they can derive
the mean and variance of aggregate claims from the moments of $N$ and $X$ individually.
