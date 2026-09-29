---
id: binomial-distribution
title: Binomial distribution
domains: [maths, stats]
status: drafted
requires: [bernoulli-distribution]
spends: []
anchor: [ifoa.cs1.2.1-1, up.wst211.10]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The binomial distribution gives the probability that a fixed number of independent trials,
each with the same success probability, produces a given total number of successes. It
degenerates to a single point mass at zero successes when that probability is zero, and to a
point mass at the full count when it is one.

## The expression

$$
P(X = k) = \binom{n}{k} p^{k} (1 - p)^{n - k}, \qquad k = 0, 1, \dots, n
$$

Here $X$ is the number of successes, $n$ is the fixed number of trials, $p$ is the success
probability common to every trial, and $k$ is the particular count whose probability is
wanted. The distribution has mean $np$ and variance $np(1-p)$, both of which follow directly
from writing $X$ as the sum of $n$ independent Bernoulli trials.

## Why this node exists

A Bernoulli trial only ever records one outcome, so nothing in the corpus can count how many
successes a batch of trials produced until the counts across many trials have a distribution
of their own. Once that count has a distribution, a confidence interval for a binomial
probability and a Poisson mean needs it settled first.
