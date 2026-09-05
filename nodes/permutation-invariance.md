---
id: permutation-invariance
title: Permutation invariance
domains: [credit, ml]
status: stub
requires: [attention-mechanism]
spends: []
anchor: [eth.dl-actuarial-2026.l10]
vault_articles: []
vault_sources: []
taught_in: null
---

An unmasked attention layer is permutation equivariant, so reordering the elements of its input reorders its output identically and changes no computed value, which means the layer alone has no way to tell one position in a sequence from another without an explicit positional signal. A sequence fed to such a model in the wrong order can therefore still train and validate cleanly, since a held-out sample sharing the same ordering error will not expose the mistake.
