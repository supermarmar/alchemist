---
id: autoencoder
title: Autoencoder
domains: [ml]
status: drafted
requires: [representation-learning]
spends: []
anchor: [ucsc.dl-actuarial-2026.l03]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An autoencoder is a network trained to reproduce its own input through a narrow
bottleneck, learning a non-linear compression that minimises reconstruction error
without ever seeing a response variable.

## The expression

$$
\hat x = g(f(x)), \qquad \mathcal{L}(x) = \lVert x - \hat x \rVert^2
$$

Here $f$ is the encoder, mapping the input $x$ to a lower-dimensional code, $g$ is
the decoder, mapping that code back into input space, $\hat x$ is the resulting
reconstruction, and $\mathcal{L}(x)$ is the reconstruction loss the network is
trained to minimise.

## Why this node exists

Because the bottleneck optimises for the directions carrying the most variance in
the covariates, an autoencoder can reconstruct a dataset well while discarding the
structure that predicts a rare or thinly represented response. The
reconstruction-discrimination gap needs it next, since that gap measures exactly
the distance between what an autoencoder reconstructs well and what a downstream
task actually needs discriminated.
