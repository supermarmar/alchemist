---
id: assurance-contract
title: Assurance contract
domains: [actuarial, life]
status: drafted
requires: []
spends:
  - {object: obj.discount-factor, domain: actuarial}
  - {object: obj.survival, domain: life}
anchor: [ifoa.cm1.3.1-1, ifoa.sp2.1.1-1, ifoa.sp2.1.1-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An assurance contract pays a benefit on the death of the life assured, on the life's
survival to a stated date, or on whichever comes first, with the whole-life, term, pure
endowment and endowment forms distinguished by which of those triggers apply.

## The expression

$$
A_x = \sum_{t=0}^{\infty} v^{t+1} \, {}_{t}p_x \, q_{x+t}
$$

Here $A_x$ is the expected present value of a whole-life assurance of one unit payable at
the end of the year of death, $v$ is the discount factor for one year, ${}_{t}p_x$ is the
probability that life $x$ survives $t$ years, and $q_{x+t}$ is the probability that a life
aged $x + t$ dies within the following year. A term assurance truncates the sum at the
term, and an endowment adds a survival benefit on top of it.

## Why this node exists

A death benefit is paid at an uncertain future time, so its value depends on both how far
into the future death is likely and how much a payment at that distance is worth today.
This node fixes the cash-flow pattern those two factors are applied to, and the with-profits
contract needs it settled before it can layer discretionary bonuses on top.
