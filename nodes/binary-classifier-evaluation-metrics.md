---
id: binary-classifier-evaluation-metrics
title: Binary classifier evaluation metrics
domains: [ml, stats]
status: drafted
requires: [supervised-learning]
spends: []
anchor: [ifoa.cs2.5.1-5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A binary classifier evaluation metric summarises how well a fitted classifier separates the
two classes, and the right metric depends on the relative cost of a false positive against a
false negative rather than on any single figure that suits every problem.

## The expression

$$
\text{precision} = \frac{TP}{TP + FP}, \qquad \text{recall} = \frac{TP}{TP + FN}
$$

Here $TP$ is the count of true positives, $FP$ the count of false positives and $FN$ the
count of false negatives, all read off the confusion matrix at a chosen classification
threshold. Precision asks what share of predicted positives are correct; recall asks what
share of actual positives were found. The two trade off as the threshold moves, and the
receiver operating characteristic curve traces recall against the false positive rate across
every threshold in turn.

## Why this node exists

A classifier that is never evaluated cannot be compared against an alternative or checked for
degradation once deployed, so a fitted model is not usable until some metric stands in
judgement over it. Choosing precision over recall, or the reverse, is a decision about which
error the business can least afford, and that decision cannot be made until both are on the
table together.
