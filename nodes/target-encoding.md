---
id: target-encoding
title: Target encoding
domains: [ml, stats]
status: stub
requires: [categorical-encoding]
spends: []
anchor: [eth.dl-actuarial-2026.l06]
vault_articles: []
vault_sources: []
taught_in: null
---

Target encoding replaces each level of a categorical covariate by the mean response observed on that level, compressing an arbitrarily large number of levels into a single numerical column. Estimated on data the encoding will later be evaluated on, it leaks information invisibly, since an in-sample check cannot detect the resulting overstatement of fit.
