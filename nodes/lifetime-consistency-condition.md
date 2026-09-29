---
id: lifetime-consistency-condition
title: Consistency condition for future lifetime
domains: [life, stats]
status: drafted
requires: [future-lifetime-random-variable]
spends:
  - {object: obj.survival, domain: life}
anchor: [ifoa.cs2.4.1-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The consistency condition for future lifetime states that surviving from age $x$ for $t$ years
and then a further $s$ years is the same event as surviving from age $x$ for $t+s$ years
directly, so that the survival probabilities defined at every starting age agree with one
another instead of each standing as a free-standing assumption.

## The expression

$$
{}_tp_x \cdot {}_sp_{x+t} = {}_{t+s}p_x
$$

Here ${}_tp_x$ is the probability that a life aged $x$ survives a further $t$ years, ${}_sp_{x+t}$
is the probability that a life already aged $x+t$ survives a further $s$ years, and
${}_{t+s}p_x$ is the probability that a life aged $x$ survives the combined $t+s$ years in one
step. The identity holds because both sides describe the same underlying event, survival past
age $x+t+s$, conditioned on survival to age $x$.

## Why this node exists

A survival model would be unusable if the probability of surviving from age 40 for 20 years
depended on which starting age happened to be chosen for the calculation, since a single
policy is priced and reserved from several different starting ages over its life. This
condition is what guarantees a single survival model gives the same answer whichever starting
age the calculation is entered from, which is what lets the future lifetime random variable be
treated as one consistent object instead of a separate model at every age.
