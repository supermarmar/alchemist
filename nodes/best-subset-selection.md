---
id: best-subset-selection
title: Best-subset selection
domains: [stats]
status: stub
requires: [regularisation]
spends: []
anchor: [ucsc.dl-actuarial-2026.l08]
vault_articles: []
vault_sources: []
taught_in: null
---

Best-subset selection penalises the count of non-zero coefficients directly, choosing the smallest subset of covariates that keeps the fit adequate. It is rarely used in practice because the resulting optimisation is combinatorially hard, which is why lasso regularisation, its tractable convex relaxation, is generally reached for instead.
