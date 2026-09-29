---
id: contract-alterations
title: Contract alterations
domains: [life]
status: drafted
requires: [contract-design]
spends: []
anchor: [up.lew700.9]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A contract alteration is a mid-term change to a policy, such as an increase in cover or a
change of premium term, requested after the contract has started, and its actuarial treatment
recalculates the policy's future obligations from the alteration date onward under the revised
terms.

## The expression

$$
V_t + \mathrm{EPV}(P') = \mathrm{EPV}(B')
$$

Here $V_t$ is the reserve already held for the policy at the alteration date $t$, and
$\mathrm{EPV}(P')$ and $\mathrm{EPV}(B')$ are the expected present values, at that same date, of
the revised future premiums and the revised future benefits under the altered terms. Solving
this equation of value for whatever the alteration leaves free, typically the revised premium,
is what fixes the terms the policyholder is offered.

## Why this node exists

A policy priced once at outset cannot simply absorb a later change in its benefits or its
premium term without a fresh calculation, since the insurer's existing reserve reflects the
original terms and not the altered ones. Recasting the equation of value at the alteration date,
at the alteration date is what keeps the altered contract funded on the same basis as the
original one, so the insurer takes on no unpriced risk by agreeing to the change.
