---
id: regression-function
title: Regression function
domains: [maths, stats]
status: drafted
requires: []
spends:
  - {object: obj.response-mean, domain: stats}
anchor: [ucsc.dl-actuarial-2026.l01]
vault_articles: [methods/exponential-dispersion-family-and-glm]
vault_sources: []
taught_in: null
---

## Definition

The regression function of a response given a set of covariates is the conditional
expectation of that response at each covariate value. It is the best predictor of
the response under squared-error loss, and more generally under any Bregman loss,
so no other function of the covariates achieves a lower expected loss of that kind.

## The expression

$$
m(x) = E[Y \mid X = x]
$$

Here $Y$ is the response, $X$ is the covariate vector, $x$ is a fixed value it can
take, and $m(x)$ is the regression function evaluated there. Averaging $m(X)$ back
over the covariate distribution returns $E[Y]$, the response's overall mean, a
property a fitted model is expected to reproduce.

## Why this node exists

Every regression method in the corpus, from a generalised linear model's
exposure-weighted mean to a network's learned representation, is an attempt to
estimate this one function from a finite sample. Without a name for what is being
estimated, a model's target and the noise around it cannot be told apart, and
probability of default needs it next, since a default probability is this
regression function evaluated on a binary response.
