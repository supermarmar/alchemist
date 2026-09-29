---
id: lognormal-distribution
title: Lognormal distribution
domains: [maths, stats]
status: drafted
requires: [normal-distribution]
spends: []
anchor: [ifoa.cs1.2.1-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A random variable follows the lognormal distribution where its logarithm follows a normal
distribution, so the variable itself is always positive and its dispersion grows with its
level.

## The expression

$$
f(x) = \frac{1}{x\sigma\sqrt{2\pi}} \exp\left(-\frac{(\ln x - \mu)^2}{2\sigma^2}\right), \qquad x \gt 0
$$

Here $f(x)$ is the lognormal density evaluated at $x$, $\mu$ is the mean of the underlying
normal distribution of $\ln X$, not the mean of $X$ itself, and $\sigma$ is the standard
deviation of that same underlying normal distribution. The extra factor of $1/x$ against the
normal density comes from the change of variables between $X$ and $\ln X$, and it is what keeps
the density well defined only for $x \gt 0$.

## Why this node exists

A quantity that must stay positive and whose variability scales with its own size, a claim
size, a share price, or a loss severity, is poorly modelled by a normal distribution, which
assigns positive probability to negative values and holds its spread constant regardless of
level. Taking logarithms first and modelling those logarithms as normal solves both problems at
once, which is why the lognormal recurs across claim severity, asset pricing and loss
modelling wherever the underlying quantity is strictly positive and right-skewed.
