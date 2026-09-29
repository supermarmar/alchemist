---
id: nagging
title: Nagging
domains: [ml]
status: drafted
requires: [ensemble-averaging, feed-forward-neural-network]
spends: []
anchor: [ucsc.dl-actuarial-2026.l06]
vault_articles: [methods/entity-embedding-and-network-ensembling]
vault_sources: []
taught_in: null
---

## Definition

Nagging, short for network aggregating, averages the predictions of several networks
of identical architecture fitted to the same training data, differing only in the
randomness of the fit itself, such as weight initialisation and mini-batch order.

## The expression

$$
\hat{y} = \frac{1}{M} \sum_{m=1}^{M} \hat{y}^{(m)}
$$

Here $\hat{y}^{(m)}$ is the prediction from the $m$th independently fitted network,
$M$ is the number of networks averaged, and $\hat{y}$ is the nagging predictor.

## Why this node exists

A single fitted network is one of infinitely many equally good solutions a finite
training sample admits, so two analysts running the same specification can produce
two different price lists, and averaging over refits is what removes that arbitrary
variation. Nagging reduces estimation variance alone: it carries no guarantee against
a bias shared by every member of the ensemble, which is the caveat any validation
report built on an averaged network prediction has to repeat.
