---
id: lifetime-distribution-function
title: Lifetime distribution function
domains: [credit, life, stats]
status: drafted
requires: [future-lifetime-random-variable]
spends:
  - {object: obj.lifetime-cdf, domain: credit}
  - {object: obj.lifetime-cdf, domain: life}
  - {object: obj.lifetime-cdf, domain: stats}
anchor: [ifoa.cs2.4.1-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The lifetime distribution function is the probability that the future lifetime has
ended by a given time, the cumulative distribution function of the future lifetime
random variable.

## The expression

$$
F(t) = P(T \le t)
$$

Here $F(t)$ is the lifetime distribution function, $T$ is the future lifetime random
variable already named, and $t$ is the fixed time at which the cumulative probability
is being asked about. Life table notation writes the same probability as ${}_tq_x$, and
credit risk writes it as the cumulative probability of default $F(t)$, both spelling the
one object the corpus's alias table sets out.

## Why this node exists

A model that can only state whether the event happened by one chosen horizon needs
this function to say by which horizon, and every other horizon besides, giving the full
curve rather than a single point on it. Relationships between survival function,
density and hazard rate need it next, since each of the three is recoverable once this
one is known.
