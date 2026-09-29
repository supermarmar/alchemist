---
id: estimator-properties
title: Properties of an estimator
domains: [stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cs1.3.1-3, ifoa.cs1.3.1-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An estimator's bias is the gap between its expected value and the parameter it targets, and an
estimator is unbiased when that gap is zero. Bias and variance are separate criteria: an
estimator can be unbiased and still highly variable, or biased and still tightly concentrated
around a value other than the truth.

## The expression

$$
\operatorname{MSE}(\hat{\theta}) = \operatorname{Var}(\hat{\theta}) + \bigl[\operatorname{Bias}(\hat{\theta})\bigr]^2, \qquad \operatorname{Bias}(\hat{\theta}) = E[\hat{\theta}] - \theta
$$

Here $\hat{\theta}$ is the estimator, $\theta$ is the parameter it targets, $\operatorname{Bias}(\hat{\theta})$
is the systematic gap between the estimator's expectation and $\theta$, $\operatorname{Var}(\hat{\theta})$
is its sampling variance, and $\operatorname{MSE}(\hat{\theta})$ is the mean square error the two
combine into. A consistent estimator has both terms shrinking to zero as the sample size grows,
and an efficient estimator is the unbiased one with the smallest variance among a stated class.

## Why this node exists

A model is compared against alternatives on these four criteria before anything is said about
what it estimates, since a lower-variance estimator that carries a persistent bias can still lose
to a noisier unbiased one once both are judged on mean square error. The bootstrap method needs
this node next, because resampling is how an estimator's bias and variance are approximated when
no closed form for either exists.
