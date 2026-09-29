---
id: gamma-distribution
title: Gamma distribution
domains: [maths, stats]
status: drafted
requires: [exponential-distribution]
spends: []
anchor: [ifoa.cs1.2.1-2, up.wst211.10]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The gamma distribution is the distribution of the waiting time to the $\alpha$-th event
under a Poisson process running at a constant rate $\beta$, generalising the exponential
distribution, its own $\alpha = 1$ case, beyond a single event.

## The expression

$$
f(x) = \frac{\beta^\alpha}{\Gamma(\alpha)}\, x^{\alpha-1} e^{-\beta x}, \qquad x \gt 0
$$

Here $f(x)$ is the gamma density, $\alpha$ is the shape parameter, read as the number of
events waited for, $\beta$ is the rate parameter, and $\Gamma(\alpha)$ is the gamma
function that normalises the density to integrate to one.

## Why this node exists

The exponential distribution alone cannot describe a wait for more than one event, since
it stops the clock at the first arrival; the gamma extends the same constant-rate
assumption to any whole count of arrivals, and to fractional shape values beyond that.
Exponential dispersion family needs it next, since recognising the gamma as a member of
that wider family is what lets a generalised linear model use it as a response
distribution directly.
