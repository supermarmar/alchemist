---
id: binning
title: Binning
domains: [credit, stats]
status: stub
requires: []
spends: []
anchor: [eth.dl-actuarial-2026.l06]
vault_articles: []
vault_sources: []
taught_in: null
---

Binning discretises a continuous covariate into a finite set of labelled intervals, giving a step function that is simple to document, handles a non-monotone effect without specifying its shape, and isolates missing values into their own attribute. The cost is a fitted effect that is constant within each interval and discontinuous at its boundaries, which a smooth function fitted by a network need not carry.
