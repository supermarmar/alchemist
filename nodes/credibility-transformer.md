---
id: credibility-transformer
title: Credibility transformer
domains: [credit, ml]
status: stub
requires: [attention-mechanism, cls-token]
spends: []
anchor: [eth.dl-actuarial-2026.l10]
vault_articles: []
vault_sources: []
taught_in: null
---

The credibility transformer adds a second, covariate-free CLS token that learns the portfolio's overall mean, and blends it with the ordinary data-driven CLS token both by an explicit random gate during training and, as an incidental consequence of the softmax, through the attention weight the data-driven token places on itself. The attention-derived weight has the algebraic form of a Bühlmann credibility factor, but where a classical credibility factor grows with the experience behind a level, this weight has been found to vary mainly with which training run produced it rather than with any borrower's own thinness of experience.
