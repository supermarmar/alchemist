---
id: geometric-distribution
title: Geometric distribution
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

The geometric distribution gives the probability that the first success in a sequence of
independent Bernoulli trials, each with success probability $p$, occurs on trial number $k$. It
is degenerate at $p = 1$, where the first trial always succeeds and no later trial is ever
reached.

## The expression

$$
P(X = k) = (1-p)^{k-1} p, \qquad k = 1, 2, 3, \ldots
$$

Here $X$ is the trial number of the first success, $p$ is the success probability shared by
every trial, and $1-p$ is the probability that each of the preceding $k-1$ trials failed. The
distribution is memoryless: the number of further trials needed, given that no success has
occurred yet, has this same distribution whatever $k$ has already been reached.

## Why this node exists

A model that counts trials to a first event, such as the number of premium periods before a
policyholder first lapses, needs this distribution before it can say anything about the trials
after that first event. Negative binomial distribution needs it next, since a negative binomial
count generalises the geometric to the trial of the $r$-th success, with the first success as
its special case where $r = 1$.
