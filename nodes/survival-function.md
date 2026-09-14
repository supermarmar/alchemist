---
id: survival-function
title: Survival function
domains: [credit, life, stats]
status: drafted
requires: [conditional-probability, future-lifetime-random-variable]
spends:
  - {object: obj.survival, domain: stats}
  - {object: obj.survival, domain: life}
  - {object: obj.survival, domain: credit}
anchor: [ifoa.cs2.1.1, ifoa.cs2.4.1-3]
vault_articles: [methods/default-correlation-copula-models]
vault_sources: []
taught_in: null
---

## Definition

The survival function of a nonnegative random duration is the probability that the
event ending that duration has not yet occurred by a given time. It equals one at
every negative time, since a nonnegative duration cannot have ended before it began,
and it is degenerate, collapsing to a step from one to zero at a single point,
wherever the duration itself is not random at all.

## The expression

$$
S(t) = P(T > t)
$$

Here $S$ is the survival function, $T$ is the random time at which the event occurs,
and $t$ is the fixed time at which survival is being asked about. The same
probability is written ${}_tp_x$ in the life table and $S(t)$ everywhere else, which
the table below sets out symbol by symbol.

## Why this node exists

Every hazard model divides an instantaneous failure rate by the probability of
having survived this far, so a hazard cannot be written down until survival has a
name. Statistics, life insurance and credit risk each watch the same event-free
interval and call it something different, and this node is the single object those
names all mean. The hazard rate needs it next, since a hazard is defined only at a
time survival has not already ruled out.
