---
id: out-of-sample-validation
title: Out-of-sample validation
domains: [ml, stats]
status: drafted
requires: []
spends:
  - {object: obj.response-mean, domain: ml}
anchor: [ucsc.dl-actuarial-2026.l02]
vault_articles: [methods/exponential-dispersion-family-and-glm]
vault_sources: []
taught_in: null
---

## Definition

Out-of-sample validation evaluates a fitted model on a held-out sample that took no part in
fitting it, since the in-sample loss on the fitting sample can be driven arbitrarily low by
memorising noise rather than by capturing genuine structure.

## The expression

$$
\hat{L}_{\text{test}} = \frac{1}{n_{\text{test}}} \sum_{i=1}^{n_{\text{test}}} \ell\bigl(y_i, \hat{y}_i\bigr)
$$

Here $\hat{L}_{\text{test}}$ is the out-of-sample loss, $n_{\text{test}}$ is the number of
observations in the held-out sample, $y_i$ is the observed response for observation $i$,
$\hat{y}_i$ is the model's prediction for that observation, and $\ell(\cdot,\cdot)$ is the loss
function comparing the two. This out-of-sample loss, also called the generalisation loss, is
the quantity model selection and model comparison should be judged against.

## Why this node exists

A model that is judged on the sample used to fit it will always favour the most complex model
available, since added complexity can only reduce the in-sample loss further, never raise it.
Early stopping needs this node next, since it halts training once the out-of-sample loss
measured here starts to rise, well before the in-sample loss would signal any problem at all.
