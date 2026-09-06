---
id: autoencoder
title: Autoencoder
domains: [ml]
status: stub
requires: [representation-learning]
spends: []
anchor: [eth.dl-actuarial-2026.l03]
vault_articles: []
vault_sources: []
taught_in: null
---

An autoencoder is a network trained to reproduce its own input through a narrow bottleneck, learning a non-linear compression that minimises reconstruction error without ever seeing a response variable. Because the bottleneck optimises for the directions carrying the most variance in the covariates, it can reconstruct a dataset well while discarding the structure that predicts a rare or thinly represented response.
