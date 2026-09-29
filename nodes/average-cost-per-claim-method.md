---
id: average-cost-per-claim-method
title: Average cost per claim method
domains: [gi]
status: drafted
requires: [development-factor]
spends:
  - {object: obj.cohort-index, domain: gi}
  - {object: obj.ultimate, domain: gi}
anchor: [ifoa.cm2.4.2-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The average cost per claim method estimates a cohort's ultimate claims by
projecting the ultimate number of claims and the ultimate average cost per claim
separately, then multiplying the two projections together.

## The expression

$$
U_i = N_i \times \bar c_i
$$

Here $U_i$ is the ultimate claims for cohort $i$, $N_i$ is the projected ultimate
number of claims for that cohort, and $\bar c_i$ is the projected ultimate average
cost per claim.

## Why this node exists

Projecting claim amounts directly from a run-off triangle mixes together two
processes, how many claims will ultimately be reported and how much each will
ultimately cost, that move independently and are best projected on their own
development pattern. Assumptions underlying reserving methods needs it next, since
it is exactly the separate assumptions this method makes about claim numbers and
average cost that get scrutinised there.
