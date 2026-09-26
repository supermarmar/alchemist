---
id: discriminatory-power
title: Discriminatory power
domains: [credit, regulation, stats]
status: drafted
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l02, ucsc.dl-actuarial-2026.l07]
vault_articles: [methods/classifier-calibration-discrimination, methods/discrimination-metrics-auc-and-somers-d]
vault_sources: []
taught_in: null
---

## Definition

Discriminatory power is the extent to which a model's scores separate observations that
experience the event from those that do not, measured entirely by the ordering of the scores
and never by their level.

## The expression

$$
D_{xy} = 2\bigl(\mathrm{AUC} - 0.5\bigr)
$$

Here $D_{xy}$ is Somers' D in the orientation that treats the model score as the independent
variable, equal to the Gini coefficient on the same scores, and $\mathrm{AUC}$ is the area
under the receiver operating characteristic curve, the probability that a randomly chosen
defaulting observation scores higher than a randomly chosen non-defaulting one.

## Why this node exists

Because $D_{xy}$ and $\mathrm{AUC}$ depend only on the relative order of the scores, they are
invariant to any strictly increasing transform of them, so a model can rank every case
correctly while its stated probabilities are badly wrong. Discriminatory power therefore
answers a narrower question than whether the model can be trusted, and a probability estimate
still needs checking on its own terms once ranking has been confirmed.
