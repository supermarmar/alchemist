---
id: regularisation
title: Regularisation
domains: [ml, stats]
status: stub
requires: [bias-variance-tradeoff]
spends: []
anchor: [eth.dl-actuarial-2026.l08, ifoa.cs2.5.1-3, up.wst212.8, up.wst311.10]
vault_articles: []
vault_sources: []
taught_in: null
---

Regularisation adds a penalty on the parameter vector to a fitting objective, trading a small increase in training loss for a model that is smoother, sparser or otherwise simpler, which controls overfitting on a finite sample and buys a model that is easier to explain and defend. Excluding the intercept from the penalty is standard practice, since penalising it forces the fitted level away from the observed rate.
