---
id: premium-and-reserve-calculation
title: Premium and reserve calculation
domains: [life]
status: drafted
requires: [annuity-function, assurance-function]
spends:
  - {object: obj.discount-factor, domain: life}
anchor: [up.ias221.4, up.ias353.3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The equivalence principle sets a policy's premium so that the expected present value
of future premiums equals the expected present value of future benefits at the
outset, and the reserve held at any later duration is the expected present value of
future benefits still owed less the expected present value of future premiums still
due.

## The expression

$$
P \cdot \ddot{a}_x = A_x, \qquad {}_tV = A_{x+t} - P \cdot \ddot{a}_{x+t}
$$

Here $P$ is the level annual premium, $\ddot{a}_x$ is the annuity function valuing a
unit payable while the life aged $x$ survives, $A_x$ is the assurance function
valuing the benefit, and ${}_tV$ is the reserve held $t$ years after entry, once both
functions are re-evaluated at the attained age $x + t$.

## Why this node exists

A premium set only to cover the coming year's expected claims leaves nothing held
back for the years in which mortality or lapse experience runs worse than assumed,
and the reserve is precisely that shortfall, the gap between obligations still owed
and premiums still to come in. Pricing and reserving principles needs it next, since
every practical adjustment to a basis, expenses, lapses, or a risk margin, is applied
by amending this same equivalence rather than by replacing it.
