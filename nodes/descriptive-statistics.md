---
id: descriptive-statistics
title: Descriptive statistics
domains: [stats]
status: drafted
requires: []
spends: []
anchor: [up.wst111.5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Descriptive statistics summarise a set of measurements through a small number of numerical
summaries of location and spread, without appealing to any model of how the data arose.

## The expression

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i, \qquad s^2 = \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar{x})^2
$$

Here $\bar{x}$ is the sample mean, $x_i$ is the $i$-th of $n$ observations, and $s^2$ is the
sample variance, the average squared deviation from $\bar{x}$ once one degree of freedom has
been spent estimating $\bar{x}$ itself.

## Why this node exists

Every inferential or predictive method compares an observed value against some baseline, and
the mean and variance are the baseline every such comparison starts from: a hypothesis test
asks whether $\bar{x}$ is far from an assumed value relative to $s^2$, and a fitted model is
judged by how much of that same variance it removes.
