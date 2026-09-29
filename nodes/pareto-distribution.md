---
id: pareto-distribution
title: Pareto distribution
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

The Pareto distribution describes a continuous random variable that cannot fall
below a fixed minimum value and whose probability of exceeding a large threshold
decays according to a power law. Its mean is undefined once the shape parameter
falls to one or below, since the power-law tail is then too heavy for the
integral defining the expectation to converge.

## The expression

$$
f(x) = \frac{\alpha x_m^{\alpha}}{x^{\alpha + 1}}, \qquad x \ge x_m
$$

Here $\alpha$ is the shape parameter governing how quickly the tail thins, $x_m$
is the minimum value the variable can take, and $x$ is the point at which the
density is evaluated.

## Why this node exists

Without a distribution whose tail decays by a power law instead of exponentially,
nothing in the corpus can represent a loss severity or an income figure whose
largest observations dominate the total, which is the behaviour the corpus's
general insurance and extreme-value material both rely on.
