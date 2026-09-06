---
id: dropout
title: Dropout
domains: [ml]
status: stub
requires: [feed-forward-neural-network]
spends: []
anchor: [eth.dl-actuarial-2026.l10]
vault_articles: []
vault_sources: []
taught_in: null
---

Dropout randomly zeroes a fraction of a layer's units at every training step, resampled independently each time, which forces the surviving units to cover for the ones removed and acts as a regulariser against overfitting. A gate that instead drops or keeps an entire token, such as a whole learned representation rather than one unit within it, is the same mechanism applied at a coarser granularity.
