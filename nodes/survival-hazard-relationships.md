---
id: survival-hazard-relationships
title: Relationships between survival function, density and hazard rate
domains: [life, stats]
status: drafted
requires: [hazard-rate, lifetime-distribution-function, survival-function]
spends:
  - {object: obj.hazard, domain: life}
  - {object: obj.hazard, domain: stats}
  - {object: obj.lifetime-cdf, domain: life}
  - {object: obj.lifetime-cdf, domain: stats}
  - {object: obj.survival, domain: life}
  - {object: obj.survival, domain: stats}
anchor: [ifoa.cs2.4.1-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The survival function, the lifetime density and the hazard rate of a future lifetime
are three views of one distribution, and each is recoverable from either of the other
two.

## The expression

$$
S(t) = \exp\!\left(-\int_0^t \lambda(u) \, du\right)
$$

Here $S(t)$ is the survival function, $\lambda(u)$ is the hazard rate at each instant
$u$ between $0$ and $t$, and the integral is the cumulative hazard accumulated over
that span. Life table notation writes the same hazard as $\mu_{x+u}$ and the same
survival probability as ${}_tp_x$, the two spellings the corpus's alias table carries
alongside statistics' own.

$$
\lambda(t) = \frac{f(t)}{S(t)}, \qquad F(t) = 1 - S(t)
$$

Here $f(t)$ is the lifetime density, the rate of change of $F(t)$, and $F(t)$ is the
lifetime distribution function already named; life table notation writes it as
${}_tq_x$.

## Why this node exists

A hazard estimated from data and a survival curve fitted from the same data have to
agree, and these identities are what force that agreement instead of leaving the two
objects free to drift apart. Integral formulae for tpx and tqx need this next, turning
the general identity above into the specific forms a life table calculation evaluates.
