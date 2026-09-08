---
id: combined-actuarial-neural-network
title: Combined actuarial neural network
domains: [credit, ml]
status: stub
requires: [glm]
spends: []
anchor: [ucsc.dl-actuarial-2026.l03]
vault_articles: []
vault_sources: []
taught_in: null
---

A combined actuarial neural network adds a trained network's output to a frozen, previously fitted generalised linear model's linear predictor, so the network learns only the correction the approved model left on the table. Restricting the correction to a constant recovers the ordinary practice of recalibrating an approved scorecard's intercept without touching its coefficients.
