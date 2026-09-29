---
id: entity-embedding
title: Entity embedding
domains: [ml]
status: drafted
requires: [categorical-encoding]
spends: []
anchor: [ucsc.dl-actuarial-2026.l06]
vault_articles: [methods/entity-embedding-and-network-ensembling]
vault_sources: []
taught_in: null
---

## Definition

Where target encoding fixes each categorical level's representation before the network
ever sees it, entity embedding learns that representation jointly with the network's own
weights, as a dense vector of fixed dimension produced by the same gradient descent that
fits the rest of the model.

## The expression

$$
z_i = E_{c_i,\,:}
$$

Here $z_i$ is the embedding vector assigned to observation $i$, $c_i$ is the level that
observation $i$'s categorical covariate takes, and $E$ is the learned embedding matrix,
carrying one row per level and $d$ columns, with $d$ chosen well below the number of
levels.

## Why this node exists

A high-cardinality covariate forces a choice: a one-hot block wide enough to carry every
level, which the network must then learn a weight for, or a fixed encoding step computed
before training, which can leak response information at a scarce level. Learning the
vector jointly avoids both, and it places every covariate, continuous or categorical,
inside one representation space that gradient descent can search directly. Feature
tokenisation needs it next, since it embeds every covariate, continuous included, the way
this node embeds a categorical level alone.
