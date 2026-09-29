---
id: run-off-triangle
title: Run-off triangle
domains: [gi]
status: drafted
requires: []
spends:
  - {object: obj.cohort-index, domain: gi}
  - {object: obj.development-index, domain: gi}
anchor: [up.ias121.3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A run-off triangle arranges a cohort's claims by the period in which they arose
and the period in which they developed, giving the standard data layout for
general insurance reserving. Only the upper-left part of the array has been
observed by the valuation date, and the lower-right part is the future development
a reserving method must project.

## The expression

$$
C_{i,j}, \qquad i = 1, \ldots, n, \quad j = 1, \ldots, n - i + 1
$$

Here $i$ is the origin period the cohort arose in, $j$ is the development period
measuring elapsed time since origin, and $C_{i,j}$ is the cumulative claims
recorded for origin period $i$ at development period $j$. The constraint on $j$
marks the boundary of the observed triangle: a cell exists in the data only where
the cohort has had time to reach that development period by the valuation date.

## Why this node exists

A reserving method needs the claims data indexed by both how old the claim is and
when the underlying policy was written, since a claim's likely further development
depends on its age rather than on the calendar date, and neither index alone can
express that. Nothing in the graph yet requires this exact layout, so the
consequence stands on its own: without it, an origin period's still-developing
claims cannot be separated from the age effect that governs how they will grow.
