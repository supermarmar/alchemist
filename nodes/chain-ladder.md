---
id: chain-ladder
title: Chain ladder method
domains: [gi, stats]
status: drafted
requires: [development-factor]
spends:
  - {object: obj.cohort-index, domain: gi}
  - {object: obj.development-factor, domain: gi}
  - {object: obj.development-index, domain: gi}
  - {object: obj.ultimate, domain: gi}
anchor: [ifoa.cm2.4.2-2]
vault_articles: [methods/chain-ladder-reserving]
vault_sources: []
taught_in: null
---

## Definition

The chain ladder method projects a cohort's claims to their ultimate value by applying a chain
of development factors, observed in a run-off triangle, to the cohort's latest cumulative
claims figure.

## The expression

$$
U_i = C_{i, I-i} \prod_{j = I-i}^{I-1} f_j
$$

Here $U_i$ is the projected ultimate claims for accident period $i$, $C_{i, I-i}$ is the
cumulative claims for that period at its latest observed development period $I-i$, and $f_j$
is the development factor carrying any cohort from development period $j$ to $j+1$. Chaining
the remaining factors together projects the latest diagonal of the triangle out to the tail.

## Why this node exists

A claims triangle only observes each accident period up to its current age, so nothing in the
data alone says what an immature period will ultimately cost until development factors carry
that immaturity forward. Where the method's own assumptions on the mean and variance of
development break down, the Bornhuetter-Ferguson method offers a projection that leans less
heavily on a young period's own emerging experience.
