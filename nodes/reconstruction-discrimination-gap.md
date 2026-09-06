---
id: reconstruction-discrimination-gap
title: Reconstruction-discrimination gap
domains: [ml, stats]
status: stub
requires: [autoencoder, pca]
spends: []
anchor: [eth.dl-actuarial-2026.l03]
vault_articles: []
vault_sources: []
taught_in: null
---

A representation that reconstructs its covariates well need not discriminate a response well, because an unsupervised objective follows the directions of largest variance while the response's signal can sit in columns that carry little variance at all. Only an objective that names the response as its target is guaranteed to preserve the structure that response depends on.
