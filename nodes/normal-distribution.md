---
id: normal-distribution
title: Normal distribution
domains: [maths, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cs1.2.1-2, up.wst211.10]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The normal distribution is the symmetric, bell-shaped continuous distribution fixed by its
mean and its variance, and it degenerates to a point mass at the mean wherever the variance is
zero.

## The expression

$$
f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)
$$

Here $f(x)$ is the density evaluated at $x$, $\mu$ is the mean, the location the distribution is
centred on, and $\sigma$ is the standard deviation, the scale governing how tightly the density
concentrates around $\mu$. The density is symmetric about $\mu$ and falls away at a rate set
entirely by $\sigma$, which is why the normal family needs only these two parameters to be
fully specified.

## Why this node exists

Most of the rest of the syllabus measures a result against the normal distribution, whether by
assuming it directly, by invoking it as the limit a sample statistic converges to, or by testing
whether a residual departs from it. The sampling distribution of the normal sample mean and
variance needs this node next, since it starts from a normal population and asks what
distribution the sample mean and sample variance themselves follow.
