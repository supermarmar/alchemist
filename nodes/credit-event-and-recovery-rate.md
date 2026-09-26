---
id: credit-event-and-recovery-rate
title: Credit event and recovery rate
domains: [credit]
status: drafted
requires: []
spends:
  - {object: obj.exposure, domain: credit}
anchor: [ifoa.cm2.3.6-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A credit event is the contractually defined trigger, such as failure to pay or a
formal insolvency filing, that establishes that a borrower has defaulted on an
obligation; the recovery rate is the proportion of the exposure at default that is
ultimately recovered once that trigger has occurred.

## The expression

$$
\text{LGD} = 1 - RR = 1 - \frac{\text{Recoveries}}{\mathrm{EAD}}
$$

Here $\text{LGD}$ is the loss given default, $RR$ is the recovery rate, Recoveries is
the amount ultimately collected after the credit event, and $\mathrm{EAD}$ is the
exposure at default, the amount outstanding at the moment the credit event occurred.

## Why this node exists

A default flag alone says nothing about how much money is lost, since two loans that
both default can leave a lender with very different shortfalls depending on collateral
and seniority. Recovery rate converts a binary default outcome into a loss amount, and
pricing a credit default swap needs this conversion next, since the protection payment
it prices is exactly the loss the recovery rate leaves uncovered.
