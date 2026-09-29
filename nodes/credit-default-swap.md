---
id: credit-default-swap
title: Credit default swap
domains: [credit, fin-eng]
status: drafted
requires: []
spends:
  - {object: obj.hazard, domain: credit}
anchor: [assa.f207.1.9-2, ifoa.sp6.2.9, ifoa.sp6.2.9-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A credit default swap is a bilateral contract under which the protection seller
compensates the protection buyer for the loss on a reference obligation if a specified
credit event occurs, in exchange for a periodic premium paid until the earlier of
default or maturity.

## The expression

$$
s \approx (1-R)\, h
$$

Here $s$ is the fair, or par, spread paid on the swap, $R$ is the recovery rate
assumed on the reference obligation if it defaults, and $h$ is the reference entity's
hazard rate, so that a higher assumed loss on default or a higher default intensity
both raise the premium a protection seller demands.

## Why this node exists

A protection seller not compensated in line with the reference entity's default
intensity and its loss given default is pricing the contract below the risk it is
taking on, so this relationship is what any quoted spread is checked against. Pricing
a credit default swap needs it next, to replace the approximation with the present
value of the two legs it stands in for.
