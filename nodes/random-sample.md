---
id: random-sample
title: Random sample
domains: [maths, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cs1.2.6-1, up.wst111.6]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A random sample is a collection of observations drawn independently from the
same population, so that each observation carries no information about any
other and every observation follows the same underlying distribution.

## The expression

$$
f(x_1, \dots, x_n) = \prod_{i=1}^{n} f(x_i)
$$

Here $x_1, \dots, x_n$ are the sample observations, $f$ is the common density
or probability function each observation follows, and the joint density of the
whole sample factorises into the product of the individual densities because
the observations are independent.

## Why this node exists

A single sample gives one realisation of whatever statistic is computed from
it. The sampling distribution needs this node next, to describe how that
statistic would vary across every sample the same independent, identically
distributed draw could have produced.
