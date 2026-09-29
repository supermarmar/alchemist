---
id: graduation-by-standard-table
title: Graduation by reference to a standard table
domains: [life]
status: drafted
requires: [graduation-rationale]
spends:
  - {object: obj.mortality-rate, domain: life}
anchor: [ifoa.cs2.4.5-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Graduation by reference to a standard table adjusts a published table of mortality rates, by a
single fitted multiplier, so that the adjusted rates match the crude data as closely as
possible. It is degenerate where the fitted multiplier equals one, at which point the graduated
rates are simply the standard table itself.

## The expression

$$
q_x^{(g)} = c\, q_x^{(s)}
$$

Here $q_x^{(g)}$ is the graduated rate at age $x$, $q_x^{(s)}$ is the published standard table's
rate at the same age, and $c$ is the multiplier fitted across the ages graduated, usually taken
as the ratio of actual deaths observed to the deaths the standard table would have predicted at
the same exposure.

## Why this node exists

Borrowing a standard table's shape gives a graduator a curve already known to be smooth and
plausible across the full age range, so fitting reduces to a single parameter instead of an
entire function. Consequently the method suits a population too small to support its own
parametric fit, provided a suitable standard table exists for the population it is drawn from.
