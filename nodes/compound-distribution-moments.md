---
id: compound-distribution-moments
title: Moments of compound claim distributions
domains: [gi, stats]
status: drafted
requires: [collective-risk-model, compound-poisson-distribution]
spends: []
anchor: [ifoa.cs2.1.2-4, ifoa.cs2.1.2-5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The moments of a compound distribution, such as a compound Poisson or compound negative
binomial random variable, are built from the moments of the claim count and the individual
claim size, and they are the usual entry point for approximating the aggregate claims
distribution itself.

## The expression

$$
E[S] = E[N]\,E[X], \qquad
\mathrm{Var}(S) = E[N]\,\mathrm{Var}(X) + \mathrm{Var}(N)\,E[X]^2
$$

Here $S$ is the aggregate claims random variable, $N$ is the number of claims, and $X$ is the
size of an individual claim, assumed independent of $N$ and identically distributed across
claims. The variance carries two sources of uncertainty: variability in claim size, weighted by
how many claims occur on average, and variability in claim count itself, weighted by the square
of the average claim size.

## Why this node exists

An aggregate loss distribution rarely has a closed form even when the claim count and claim
size distributions are both simple, so a normal or translated gamma approximation, fitted to
match these first two moments, is usually the practical way to work with the aggregate
distribution at all. Once a proportional or excess of loss reinsurance arrangement is applied to
the underlying losses, both moments change in a way that has to be recalculated from the
arrangement's own terms before that approximation can be refitted.
