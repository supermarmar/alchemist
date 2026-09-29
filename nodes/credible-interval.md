---
id: credible-interval
title: Credible interval
domains: [stats]
status: drafted
requires: [bayesian-prior-and-posterior]
spends: []
anchor: [ifoa.cs1.5.1-5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A credible interval for a parameter is the Bayesian counterpart to a classical confidence
interval, built directly from the posterior distribution and not from the sampling
distribution of an estimator.

## The expression

$$
P\bigl(\theta_L \le \theta \le \theta_U \mid \text{data}\bigr) = 1 - \alpha
$$

Here $\theta$ is the parameter of interest, $\theta_L$ and $\theta_U$ are the lower and upper
bounds of the interval, and $1-\alpha$ is the credibility level, the posterior probability that
$\theta$ lies between those bounds given the observed data. The bounds are read directly off
the posterior distribution, most simply as its $\alpha/2$ and $1-\alpha/2$ quantiles.

## Why this node exists

A classical confidence interval's probability statement is about the procedure that generated
the interval, repeated over many hypothetical samples, and it says nothing about the probability
that this particular interval contains the true parameter. A credible interval answers that
different question directly, stating a probability about the parameter itself conditional on the
data actually observed, which is the interpretation prior and posterior distributions were
built to support.
