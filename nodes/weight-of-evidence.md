---
id: weight-of-evidence
title: Weight of evidence
domains: [credit, stats]
status: stub
requires: [logistic-regression, target-encoding]
spends: []
anchor: [eth.dl-actuarial-2026.l06]
vault_articles: []
vault_sources: []
taught_in: null
---

Weight of evidence replaces each level of a categorical covariate by the log of its odds relative to the portfolio's overall odds, which is target encoding moved onto the log-odds scale a logit link expects. The transform is unbounded, so a level with no events of one outcome sends its weight of evidence towards infinity unless the estimate is shrunk first.
