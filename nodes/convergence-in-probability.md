---
id: convergence-in-probability
title: Convergence in probability
domains: [stats]
status: drafted
requires: [random-variable]
spends: []
anchor: [up.wst221.1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A sequence of random variables converges in probability to a limit when it becomes increasingly
likely, as the sample size grows, to lie arbitrarily close to that limit.

## The expression

$$
\lim_{n \to \infty} P\bigl(|X_n - X| > \varepsilon\bigr) = 0 \qquad \text{for every } \varepsilon > 0
$$

Here $X_n$ is the $n$th term of the sequence of random variables, $X$ is the limit it converges
to, and $\varepsilon$ is an arbitrarily small positive tolerance. The definition requires the
probability of a gap larger than $\varepsilon$ to vanish as $n$ grows, for every choice of
$\varepsilon$, however small.

## Why this node exists

An estimator that is unbiased at every sample size says nothing about what happens as more data
arrives, whereas convergence in probability is the property that justifies treating a large
enough sample's estimate as close to the true parameter with high confidence, which is what a
consistency argument for an estimator ultimately rests on. Without this notion of convergence,
a law of large numbers has no precise statement to prove.
