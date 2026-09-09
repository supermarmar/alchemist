---
id: nagging
title: Nagging
domains: [ml]
status: stub
requires: [ensemble-averaging, feed-forward-neural-network]
spends: []
anchor: [ucsc.dl-actuarial-2026.l06]
vault_articles: []
vault_sources: []
taught_in: null
---

Nagging, short for network aggregating, averages several networks that differ only in the randomness of their fitting, such as the weight initialisation and the mini-batch order, rather than resampling the training data the way bagging does. It needs no bootstrap, because refitting the same architecture on the same data already supplies as many distinct solutions as the ensemble wants.
