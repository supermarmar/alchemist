---
id: ridge-regularisation
title: Ridge regularisation
domains: [ml, stats]
status: stub
requires: [regularisation]
spends: []
anchor: [eth.dl-actuarial-2026.l08]
vault_articles: []
vault_sources: []
taught_in: null
---

Ridge regularisation penalises the squared Euclidean norm of the parameter vector, shrinking every coefficient towards zero without ever setting one exactly to zero, and it needs no closed-form choice of penalty weight since one is usually selected by cross-validation. It earns its place on a wide design matrix with many collinear covariates, and does comparatively little on a narrow one with abundant data behind it.
