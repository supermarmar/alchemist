---
id: data-leakage
title: Data leakage
domains: [ml, stats]
status: stub
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l06]
vault_articles: []
vault_sources: []
taught_in: null
---

Data leakage occurs where a transformation such as an encoding map or a scaling constant is estimated using rows that later serve as the test sample, manufacturing an improvement that will not survive on genuinely unseen data. Its signature is nearly invisible in-sample, since a leaked model typically fits the training rows marginally worse rather than better, so only a procedural check on which rows an estimation step was allowed to see can catch it.
