---
id: isotonic-regression
title: Isotonic regression
domains: [stats]
status: drafted
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l07]
vault_articles: [concepts/balance-property-and-auto-calibration]
vault_sources: []
taught_in: null
---

## Definition

Isotonic regression fits the non-decreasing step function that lies closest, in
squared error, to a set of observed values ordered by a single predictor. It takes
no smoothing hyperparameter, so unlike a spline fit there is nothing left to tune
once the ordering is fixed.

## The expression

$$
\hat{g} = \operatorname*{arg\,min}_{g \text{ non-decreasing}} \sum_{i=1}^{n} \left(y_i - g(x_i)\right)^2
$$

Here $\hat{g}$ is the fitted step function, $y_i$ is the observed value for
observation $i$, $x_i$ is the predictor $i$ is ordered on, and the minimisation
ranges only over functions $g$ that are non-decreasing in $x_i$, which is the
constraint that forces the fit into steps rather than an unconstrained
interpolation.

## Why this node exists

A recalibrated predictor is only useful if the recalibration itself does not
introduce new bias, and isotonic regression is the standard way to guarantee that
without choosing a bandwidth or a spline degree first. Calibration repair needs it
next, since repairing a network's predictions after the fact is exactly the job
this node's monotone fit was built for.
