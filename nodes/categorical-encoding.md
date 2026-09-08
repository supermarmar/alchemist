---
id: categorical-encoding
title: Categorical encoding
domains: [ml, stats]
status: stub
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l06]
vault_articles: []
vault_sources: []
taught_in: null
---

A categorical covariate must be converted to a numerical form before a regression model can use it, whether by ordinal coding for genuinely ordered levels, one-hot encoding into a basis vector per level, or dummy coding against a chosen reference level. All three become sparse and unstable as the number of levels grows, which is a numerical problem for gradient-based fitting and a statistical one for a level with few observations behind it.
