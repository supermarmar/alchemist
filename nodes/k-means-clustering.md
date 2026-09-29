---
id: k-means-clustering
title: K-means clustering
domains: [ml, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cs2.5.1-6, up.wst212.12]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

K-means clustering partitions a set of observations into a fixed number of groups
by minimising the total squared distance from each observation to the mean of the
group it is assigned to, updating the assignments and the means alternately until
neither changes.

## The expression

$$
\operatorname*{arg\,min}_{C_1, \dots, C_k} \sum_{j=1}^{k} \sum_{x_i \in C_j} \lVert x_i - \mu_j \rVert^2
$$

Here $k$ is the fixed number of clusters chosen in advance, $C_j$ is the set of
observations assigned to cluster $j$, $x_i$ is an individual observation, and
$\mu_j$ is the mean of the observations currently assigned to $C_j$.

## Why this node exists

A dataset with no labelled outcome still often has structure worth finding, and
this node gives the simplest way to find it: group observations so that each
group is as internally similar as its own mean allows. An observation that never
settles close to any cluster mean is, by the same construction, a candidate
anomaly, which is what makes the technique useful for outlier flagging as well as
for segmentation.
