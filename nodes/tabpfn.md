---
id: tabpfn
title: TabPFN
domains: [ml]
status: drafted
requires: [in-context-learning, tabular-foundation-model]
spends:
  - {object: obj.coefficients, domain: ml}
anchor: [ucsc.dl-actuarial-2026.l12]
vault_articles: [concepts/in-context-learning-tabular-actuarial-models]
vault_sources: []
taught_in: null
---

## Definition

TabPFN is a tabular foundation model that approximates the Bayesian posterior predictive
distribution for a query row given a context dataset, producing that approximation in a
single forward pass through a network whose weights were fixed once during pretraining and
are never re-estimated from the context at prediction time.

## The expression

$$
p_\theta(y \mid x, D) \approx \int p(y \mid x, \phi)\, p(\phi \mid D)\, d\phi
$$

Here $D$ is the context dataset supplied at prediction time, $x$ is the query row, $\phi$ is
the parameter of the data-generating process a classical model would fit to $D$, $p(\phi \mid
D)$ is its Bayesian posterior given that context, and $p_\theta$ is TabPFN's own network,
whose weights $\theta$ (spent here as coefficients) were learned once over many synthetic
tasks during pretraining and stay fixed at prediction time.

## Why this node exists

A model that stores a fitted parameter vector gives a lender a coefficient table to document,
monitor for drift, and re-estimate as new data arrives; TabPFN gives none of that, since the
context dataset determines the prediction completely without ever being distilled into a
stored parameter. Governance therefore shifts from reviewing parameter stability to reviewing
the context dataset supplied at each prediction, because that dataset is now doing the work a
fitted model's coefficients used to do.
