---
id: classification-performance-metrics
title: Classification performance metrics
domains: [ml, stats]
status: drafted
requires: []
spends: []
anchor: [up.wst212.8]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Classification performance metrics summarise a classifier's predictions against known outcomes through the confusion matrix's four counts, combining them into single numbers that each weigh the two ways a classifier can be wrong.

## The expression

$$
F_1 = \frac{2\,P\,R}{P + R}
$$

Here $F_1$ is the F1 score, $P$ is precision, the share of predicted positives that are actually positive, and $R$ is recall, the share of actual positives the classifier finds. Precision is $TP/(TP+FP)$ and recall is $TP/(TP+FN)$, where $TP$, $FP$ and $FN$ are the confusion matrix's true positive, false positive and false negative counts.

## Why this node exists

A classifier can always trade precision for recall by moving its decision threshold, so a single number is needed to compare two classifiers that have made different trades. Without one, ranking classifiers would depend on which side of the trade-off happened to be reported.
