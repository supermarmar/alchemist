---
id: identity-initialisation
title: Identity initialisation
domains: [ml]
status: stub
requires: [feed-forward-neural-network]
spends: []
anchor: [eth.dl-actuarial-2026.l12]
vault_articles: []
vault_sources: []
taught_in: null
---

Identity initialisation zeroes the weights of an added layer or mechanism so that, before any training happens, it returns its input unchanged and the surrounding model reproduces exactly whatever it computed beforehand. It turns a comparison between a baseline model and an extended one into a clean measurement of what the added mechanism contributes, since training starts from a state in which it contributes nothing.
