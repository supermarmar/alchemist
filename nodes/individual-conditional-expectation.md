---
id: individual-conditional-expectation
title: Individual conditional expectation
domains: [ml, stats]
status: drafted
requires: [feed-forward-neural-network]
spends:
  - {object: obj.response-mean, domain: ml}
anchor: [ucsc.dl-actuarial-2026.l08]
vault_articles: [methods/icenet-smoothness-and-monotonicity-constraints]
vault_sources: []
taught_in: null
---

## Definition

An individual conditional expectation curve fixes one observation's covariates other than a
single chosen covariate, varies that covariate across a grid of values, and records the fitted
model's prediction at each point, showing how that one observation's prediction responds to
the chosen covariate on its own.

## The expression

$$
\hat{y}_i(s) = \hat{f}(s, x_{i,C})
$$

Here $\hat{f}$ is the fitted model, $x_{i,C}$ is observation $i$'s vector of covariates other
than the one being varied, $s$ is a value on the grid taken by the varied covariate, and
$\hat{y}_i(s)$ is the model's prediction for observation $i$ once that covariate is set to $s$.
Tracing $\hat{y}_i(s)$ across the whole grid, with $x_{i,C}$ held fixed, produces the curve.

## Why this node exists

A fitted model's coefficients or feature importances say which covariates matter on average,
but they cannot show whether every observation responds to a covariate the same way a
generalised linear model's single coefficient would imply. A network's response to a covariate
can differ from one observation to the next in a way no single summary captures, and an
individual conditional expectation curve is what exposes that observation-level shape.
Averaging many such curves gives the partial dependence plot, which needs an individual curve
for every observation it averages.
