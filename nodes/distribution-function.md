---
id: distribution-function
title: Distribution function
domains: [stats]
status: drafted
requires: [random-variable]
spends: []
anchor: [up.wst211.4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The distribution function of a random variable gives the probability that it takes a value
at or below each point on the real line, and it characterises the variable completely: two
random variables with the same distribution function have the same distribution, however
differently they might be constructed.

## The expression

$$
F(x) = P(X \le x)
$$

Here $X$ is the random variable and $F(x)$ is the probability that $X$ takes a value no
greater than $x$. $F$ is non-decreasing, right-continuous, and tends to zero as $x$ tends to
minus infinity and to one as $x$ tends to plus infinity, properties that follow from the
axioms of probability alone rather than from any assumption about $X$'s particular
distribution.

## Why this node exists

A random variable is defined on an abstract sample space, and the distribution function is
what turns that abstraction into a function of a real number that can be tabulated, plotted
and compared across variables. The density function needs it next, since a density is
defined as the distribution function's derivative wherever that derivative exists.
