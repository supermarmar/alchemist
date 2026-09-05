---
id: icenet
title: ICEnet
domains: [credit, ml]
status: stub
requires: [feed-forward-neural-network, individual-conditional-expectation, regularisation]
spends: []
anchor: [eth.dl-actuarial-2026.l08]
vault_articles: []
vault_sources: []
taught_in: null
---

ICEnet fits a network under a compound loss that penalises roughness and wrong-signed movement in its own individual conditional expectation curves for chosen covariates, constraining the fitted function's behaviour directly rather than constraining its weights the way a penalty on the parameter vector does. It lets a network be given the smoothness and monotonicity a scorecard curve is expected to show, at a predictive cost that is typically small.
