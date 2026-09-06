---
id: iteratively-reweighted-least-squares
title: Iteratively reweighted least squares
domains: [stats]
status: stub
requires: [exponential-dispersion-family, glm, linear-predictor]
spends: []
anchor: [eth.dl-actuarial-2026.l02, ifoa.cs1.4.2-6]
vault_articles: []
vault_sources: []
taught_in: null
---

Iteratively reweighted least squares fits a generalised linear model by repeatedly solving a weighted least squares problem on a working response formed from the current fit, and it is the algorithmic form Fisher's scoring method takes for this class of model. Under the canonical link it coincides with Newton-Raphson, and under the Gaussian member with a constant cumulant second derivative it collapses to ordinary least squares in one step.
