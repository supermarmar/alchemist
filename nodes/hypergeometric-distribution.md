---
id: hypergeometric-distribution
title: Hypergeometric distribution
domains: [maths, stats]
status: drafted
requires: [binomial-distribution]
spends: []
anchor: [ifoa.cs1.2.1-1, up.wst211.10]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The hypergeometric distribution gives the probability that a fixed number of draws from a
finite population, made without replacement, contains a given number of successes. The number
of draws cannot exceed the population size, and the number of successes drawn cannot exceed
either the draws taken or the successes present in the population.

## The expression

$$
P(X = k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}, \qquad k = 0, 1, \dots, \min(n, K)
$$

Here $X$ is the number of successes among the draws, $N$ is the population size, $K$ is the
number of successes present in that population, $n$ is the number of draws taken, and $k$ is
the particular count whose probability is wanted.

## Why this node exists

A population of fixed, known composition changes its odds with every draw: removing one
success from the population lowers the chance the next draw is also a success, so a model
that holds the success probability constant across trials no longer describes it. The
hypergeometric distribution supplies the probability law for that shrinking population, which
an audit sample, a credit portfolio draw or a stock check taken without replacement from a
known population all need.
