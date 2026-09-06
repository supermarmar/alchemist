---
id: early-stopping
title: Early stopping
domains: [ml, stats]
status: stub
requires: [out-of-sample-validation]
spends: []
anchor: [eth.dl-actuarial-2026.l04]
vault_articles: []
vault_sources: []
taught_in: null
---

Early stopping partitions the learning sample into a training set used for gradient steps and a validation set monitored after every epoch, retaining the parameter with the best validation loss seen so far and halting once that loss stops improving. It is a form of implicit regularisation, limiting an overparametrised network's capacity to memorise the training sample by limiting how far training is allowed to travel from initialisation.
