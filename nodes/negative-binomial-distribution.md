---
id: negative-binomial-distribution
title: Negative binomial distribution
domains: [maths, stats]
status: drafted
requires: [geometric-distribution]
spends: []
anchor: [ifoa.cs1.2.1-1, up.wst211.10]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The negative binomial distribution gives the probability that a fixed number of
successes in a sequence of independent trials, each with the same success
probability, is reached on a given trial, generalising the geometric distribution
from one success to $r$.

## The expression

$$
P(X = k) = \binom{k - 1}{r - 1} p^r (1 - p)^{k - r}, \qquad k = r, r+1, \ldots
$$

Here $X$ is the trial on which the $r$th success occurs, $r$ is the fixed number of
successes required, $p$ is the success probability on each trial, and $k$ is the
number of trials taken.

## Why this node exists

The geometric distribution answers how long a wait for one success takes, and many
questions in the corpus, such as how many periods a portfolio takes to accumulate a
fixed count of defaults, ask the same question for a target count above one; the
negative binomial distribution is what extends the geometric case to answer it.
