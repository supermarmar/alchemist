---
id: expected-value
title: Expected value
domains: [stats]
status: drafted
requires: [random-variable]
spends: []
anchor: [up.wst211.7]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The expected value of a random variable is its probability-weighted average, the long-run
mean an experiment would produce if it were repeated indefinitely under identical conditions.

## The expression

$$
E[X] = \sum_{x} x \, P(X = x)
$$

Here $X$ is a discrete random variable, $x$ ranges over the values $X$ can take, and
$P(X = x)$ is the probability of each. For a continuous random variable with density $f$,
the same weighted average is written $E[X] = \int_{-\infty}^{\infty} x f(x) \, dx$, replacing
the sum with an integral and the point probability with a density.

## Why this node exists

A distribution function describes a random variable completely, but a single summary number
is usually wanted before that description can be compared, combined, or reported, and expected
value is the summary that a probability-weighted average supplies. Conditional expectation
needs it next, since conditioning on extra information narrows the probabilities the average
is weighted by, without changing what the average itself means.
