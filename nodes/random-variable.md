---
id: random-variable
title: Random variable
domains: [stats]
status: drafted
requires: [probability-theory-foundations]
spends: []
anchor: [up.wst111.8, up.wst211.3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A random variable is a function that assigns a real number to every outcome in the sample space,
measurable so that the probability of the variable falling in any given range is itself well
defined. It may be discrete, taking only countably many values, or continuous, taking any value
in an interval, according to which values the underlying experiment can produce.

## The expression

$$
X : \Omega \to \mathbb{R}, \qquad X^{-1}\bigl((-\infty, x]\bigr) \in \mathcal{F} \ \text{for every } x \in \mathbb{R}
$$

Here $\Omega$ is the sample space, $X$ is the random variable, and the measurability condition
on the right states that the set of outcomes for which $X$ does not exceed $x$ is itself an
event in $\mathcal{F}$, for every real $x$; this is exactly what is needed for the probability
$P(X \le x)$ to be defined.

## Why this node exists

A probability statement about an event defined directly, as a subset of the sample space,
becomes unwieldy once outcomes are numerical and the questions asked concern ranges of numbers.
Distribution function needs this node next, since $F(x) = P(X \le x)$ is exactly the
measurability condition here read as a cumulative probability.
