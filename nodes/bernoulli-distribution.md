---
id: bernoulli-distribution
title: Bernoulli distribution
domains: [maths, stats]
status: drafted
requires: []
spends: []
anchor: [up.wst211.10]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The Bernoulli distribution describes a single trial that takes the value 1, a success, with fixed probability $p$, and 0 otherwise. It is degenerate at $p = 0$ or $p = 1$, where the outcome is certain and no trial is really being run.

## The expression

$$
P(X = x) = p^{x}(1-p)^{1-x}, \qquad x \in \{0, 1\}
$$

Here $X$ is the trial's outcome, $p$ is the probability that $X = 1$, and $1-p$ is the probability that $X = 0$.

## Why this node exists

Every count of successes across repeated trials is built by adding this one trial to itself, so a distribution for the count cannot be written down before the single trial has a name. The binomial distribution needs it next, since a binomial count is a sum of independent Bernoulli trials sharing the same $p$.
