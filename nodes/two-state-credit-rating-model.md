---
id: two-state-credit-rating-model
title: Two-state credit rating model
domains: [credit]
status: drafted
requires: [credit-risk-modelling-approach]
spends:
  - {object: obj.hazard, domain: credit}
  - {object: obj.survival, domain: credit}
anchor: [ifoa.cm2.3.6-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A two-state credit rating model treats an obligor as occupying one of two states,
performing or defaulted, and moving from the first to the second at a constant
transition intensity; it is degenerate at an intensity of zero, under which the obligor
never defaults.

## The expression

$$
S(t) = P(T \gt t) = e^{-h t}
$$

Here $S(t)$ is the probability that the obligor is still performing at time $t$, $T$ is
the random time of the transition to default, and $h$ is the constant transition
intensity out of the performing state. Because $h$ does not vary with $t$, the model
carries only one free parameter, and it is exactly the constant-hazard case of the
hazard rate this corpus already names.

## Why this node exists

A rating agency's own transition matrices report many states, but a portfolio-level
default study often needs only whether an obligor has left the performing pool, and
collapsing the many-state chain to two states is what makes that study tractable without
estimating every off-diagonal transition. Where the assumption of a constant intensity
breaks down is the consequence: a real book's default rate moves with the credit cycle,
which a single fixed $h$ cannot represent.
