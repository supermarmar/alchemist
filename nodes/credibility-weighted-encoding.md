---
id: credibility-weighted-encoding
title: Credibility-weighted encoding
domains: [credit, ml]
status: stub
requires: [weight-of-evidence]
spends: []
anchor: [ucsc.dl-actuarial-2026.l06]
vault_articles: []
vault_sources: []
taught_in: null
---

Credibility-weighted encoding shrinks a level's target-encoded or weight-of-evidence value towards the overall mean in proportion to how much data the level carries, so a scarcely populated level is pulled towards the portfolio and a well-populated one keeps its own value. The construction matches the minimum-bin-size merging that scorecard development already practises, expressed instead as a single tunable shrinkage parameter.
