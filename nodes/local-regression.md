---
id: local-regression
title: Local regression
domains: [ml, stats]
status: drafted
requires: [linear-regression]
spends:
  - {object: obj.coefficients, domain: stats}
anchor: [up.wst212.11]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Local regression fits a separate weighted linear regression around each point of interest,
giving nearby observations more weight than distant ones, so that the fitted curve traces the
data's local shape.

## The expression

$$
\hat{\beta}(x_0) = \arg\min_{\beta} \sum_{i=1}^{n} K_h(x_i - x_0) \, \bigl(y_i - x_i^{\top} \beta\bigr)^2
$$

Here $x_0$ is the point at which the fit is wanted, $K_h$ is a kernel function with bandwidth
$h$ that weights each observation $i$ by how close its covariate value $x_i$ lies to $x_0$,
$y_i$ is that observation's response, and $\hat{\beta}(x_0)$ is the coefficient vector fitted
from this weighted least squares problem. The fitted value at $x_0$ is read off this local fit,
and repeating the whole procedure at a grid of points traces out the fitted curve.

## Why this node exists

A single linear regression imposes one slope across the whole range of a covariate, which
misses any curvature or change in relationship the data actually carries. Local regression
lets the fitted relationship vary smoothly by re-estimating it at every point from a
neighbourhood of nearby observations, giving a flexible curve without committing to a
parametric functional form for the whole range at once.
