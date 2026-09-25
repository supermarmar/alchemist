---
id: representation-learning
title: Representation learning
domains: [ml]
status: drafted
requires: []
spends:
  - {object: obj.coefficients, domain: ml}
anchor: [ucsc.dl-actuarial-2026.l03]
vault_articles: [methods/feed-forward-networks-claim-frequency]
vault_sources: []
taught_in: null
---

## Definition

Representation learning is the construction of a lower-dimensional mapping of raw
covariates on which a simple predictor performs well, built by the algorithm
itself instead of engineered by hand. A deep network builds that mapping by
composing several such layers, so later layers combine the structure earlier
layers detect.

## The expression

$$
z^{(l)} = f\bigl(W^{(l)} z^{(l-1)} + b^{(l)}\bigr), \qquad z^{(0)} = x
$$

Here $x$ is the raw covariate vector, $z^{(l)}$ is the representation produced at
layer $l$, $f$ is a non-linear activation function, and $W^{(l)}$ and $b^{(l)}$,
jointly written $\theta$, are the weights and bias the layer applies. The final
representation $z^{(L)}$ feeds a linear predictor exactly as a covariate vector
would in a generalised linear model, which is what makes a network a generalisation
of a GLM rather than a wholly different object.

## Why this node exists

A generalised linear model asks an analyst to specify every interaction and
functional form the response might need, which is feasible on a handful of
covariates and infeasible once the input runs to thousands. Representation
learning replaces that hand-engineering with a layer-by-layer search over
mappings, and the autoencoder needs it next, since an autoencoder is this same
composition trained with no response variable at all.
