---
id: localglmnet
title: LocalGLMnet
domains: [credit, ml]
status: stub
requires: [feed-forward-neural-network, glm]
spends: []
anchor: [eth.dl-actuarial-2026.l09]
vault_articles: []
vault_sources: []
taught_in: null
---

LocalGLMnet replaces a generalised linear model's single fixed coefficient vector with attention weights that a network computes as functions of the covariates, so the model is locally a generalised linear model everywhere and every prediction decomposes exactly into per-covariate contributions with nothing left over. Initialising the network at the fitted generalised linear model fixes each term's role before training starts, which avoids the model quietly reassigning one covariate's contribution to another term.
