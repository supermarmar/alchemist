---
id: cross-validation
title: Cross-validation
domains: [ml, stats]
status: stub
requires: [bias-variance-tradeoff]
spends: []
anchor: [ifoa.cs2.5.1-2, up.wst212.8, up.wst311.9]
vault_articles: []
vault_sources: []
taught_in: null
---

A method for evaluating a model on data it was not fitted on, by repeatedly splitting the available data into a training portion and a held out portion and averaging performance across the splits. It is also the standard way to choose a hyperparameter, such as the complexity of a model, without touching a final test set.
