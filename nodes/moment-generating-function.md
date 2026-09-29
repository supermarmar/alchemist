---
id: moment-generating-function
title: Moment generating function
domains: [maths, stats]
status: drafted
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l02, ifoa.cs1.2.4-1, up.wst111.10, up.wst211.9, up.wst311.1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The moment generating function of a random variable collects every moment of that variable
into a single expression, so that differentiating it repeatedly at the origin recovers each
moment in turn. It is undefined at any $t$ for which the expectation below fails to converge,
which is why its existence on an interval around zero lets it pin down a distribution
completely.

## The expression

$$
M_X(t) = E\bigl[e^{tX}\bigr]
$$

Here $M_X(t)$ is the moment generating function of $X$ evaluated at $t$, $X$ is the random
variable whose moments are wanted, and $E[\cdot]$ is the expectation operator applied to
$e^{tX}$. The $k$th moment $E[X^k]$ is the $k$th derivative of $M_X$ at $t = 0$, and the
logarithm of $M_X$ is the cumulant generating function, which generates the cumulants by the
same differentiation.

## Why this node exists

Many distributions are easier to characterise through their moments than through their density
or distribution function directly, and a sum of independent random variables has a moment
generating function equal to the product of the individual ones, which turns a convolution
into multiplication. Moment extraction from a generating function needs this object next,
since differentiating $M_X$ is the mechanical step that recovers the mean, the variance, and
every higher moment from it.
