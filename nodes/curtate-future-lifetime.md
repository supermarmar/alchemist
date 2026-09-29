---
id: curtate-future-lifetime
title: Curtate future lifetime
domains: [life]
status: drafted
requires: [future-lifetime-random-variable]
spends:
  - {object: obj.survival, domain: life}
anchor: [ifoa.cs2.4.1-6]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The curtate future lifetime of a life currently aged $x$ is the integer number of complete future
years that life lives, obtained by rounding the future lifetime random variable down to the last
completed year.

## The expression

$$
K_x = \lfloor T_x \rfloor, \qquad P(K_x = k) = {}_kp_x - {}_{k+1}p_x, \quad k = 0, 1, 2, \dots
$$

Here $T_x$ is the future lifetime random variable, $\lfloor \cdot \rfloor$ rounds down to the
nearest integer, $K_x$ is the curtate future lifetime that rounding produces, and ${}_kp_x$ is the
probability of surviving $k$ further years, so that ${}_kp_x - {}_{k+1}p_x$ is the probability of
dying in the year that follows age $x+k$.

## Why this node exists

A life table records years lived in whole numbers, and no life table function can be read against
that record until the continuous future lifetime has been reduced to the same integer scale.
Expectation of life needs it next, since a life's expected remaining years is a sum taken over the
whole-year outcomes this node defines.
