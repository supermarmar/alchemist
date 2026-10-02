---
id: bayesian-point-estimation
title: Bayesian point estimation
domains: [stats]
status: drafted
requires: [bayesian-prior-and-posterior]
spends: []
anchor: [ifoa.cs1.5.1-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A Bayesian point estimate of a parameter is the single summary of its posterior
distribution that minimises the expected value of a chosen loss function; under
squared-error loss it is degenerate in the sense that it always reduces to the
posterior mean, regardless of the posterior's shape.

## The expression

$$
\hat{\theta} = \arg\min_{a} \, E\bigl[L(\theta, a) \mid \text{data}\bigr]
$$

Here $\hat{\theta}$ is the Bayesian point estimate, $\theta$ is the unknown parameter,
$a$ ranges over candidate estimates, and $L(\theta, a)$ is the loss incurred by reporting
$a$ when the true value is $\theta$. Squared-error loss gives $\hat{\theta} = E[\theta
\mid \text{data}]$, the posterior mean, and absolute-error loss instead gives the
posterior median.

## Why this node exists

A posterior distribution is a full description of what the data and the prior together
imply about a parameter, but a pricing or reserving calculation downstream needs a single
number to plug in, and the loss function makes the choice of that number an
explicit decision.
