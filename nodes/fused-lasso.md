---
id: fused-lasso
title: Fused lasso
domains: [credit, ml, stats]
status: stub
requires: [lasso-regularisation]
spends: []
anchor: [ucsc.dl-actuarial-2026.l08]
vault_articles: []
vault_sources: []
taught_in: null
---

Fused lasso penalises the absolute difference between coefficients that sit next to each other along a natural ordering, such as consecutive age bands, driving some of those differences to exactly zero and so forcing the adjacent coefficients to be equal. It performs the coarse classing of a continuous covariate that a scorecard analyst otherwise does by hand, choosing where to place a boundary and where the data supports none at all.
