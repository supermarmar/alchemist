---
id: lasso-regularisation
title: Lasso regularisation
domains: [ml, stats]
status: stub
requires: [regularisation]
spends: []
anchor: [eth.dl-actuarial-2026.l08]
vault_articles: []
vault_sources: []
taught_in: null
---

Lasso regularisation penalises the sum of absolute coefficient values, which can drive individual coefficients to exactly zero as the penalty weight rises and so performs variable selection alongside shrinkage. Increasing the penalty weight sends coefficients to zero one at a time, giving an ordering of the covariates by how much predictive weight the model is willing to give up before dropping each one.
