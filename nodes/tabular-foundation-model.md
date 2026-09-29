---
id: tabular-foundation-model
title: Tabular foundation model
domains: [ml]
status: drafted
requires: [foundation-model]
spends:
  - {object: obj.response-mean, domain: ml}
anchor: [ucsc.dl-actuarial-2026.l12]
vault_articles: [concepts/in-context-learning-tabular-actuarial-models]
vault_sources: []
taught_in: null
---

## Definition

A tabular foundation model is pretrained across many synthetic tables drawn from a prior over
how tabular relationships tend to behave, with no real dataset in its training data, and it
reuses that prior at prediction time on a table it has never seen, adjusting its output from
the examples given in context without any retraining.

## The expression

$$
\hat{y} = f_\theta(x, \mathcal{D})
$$

Here $x$ is the feature vector of the row being predicted, $\mathcal{D}$ is the context set of
similar rows and their observed outcomes supplied at prediction time, $f_\theta$ is the
pretrained network, and $\hat{y}$ is the prediction it returns; $f_\theta$ approximates the
Bayesian posterior predictive distribution implied by the context, computed in a single forward
pass with no parameter update.

## Why this node exists

A conventional model must be trained anew on every dataset it is applied to, which is exactly
what fails on a small or newly assembled portfolio with too little history to fit a model of
its own. By contrast, a tabular foundation model answers that gap by carrying a prior learned across many
synthetic tables into a table it has never trained on, and TabPFN needs this node next as the
specific architecture that alternates attention across a table's columns and rows to do so.
