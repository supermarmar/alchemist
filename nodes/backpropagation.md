---
id: backpropagation
title: Backpropagation
domains: [ml]
status: stub
requires: [feed-forward-neural-network, gradient-descent]
spends: []
anchor: [eth.dl-actuarial-2026.l04]
vault_articles: []
vault_sources: []
taught_in: null
---

Backpropagation computes the gradient of a network's loss with respect to every weight by applying the chain rule layer by layer from the output back to the input, in one backward pass for every forward pass. Automatic differentiation frameworks implement it directly, which is why fitting a network of arbitrary depth needs no gradient to be derived by hand.
