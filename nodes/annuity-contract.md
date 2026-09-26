---
id: annuity-contract
title: Annuity contract
domains: [actuarial, life]
status: drafted
requires: []
spends:
  - {object: obj.discount-factor, domain: actuarial}
  - {object: obj.survival, domain: life}
anchor: [ifoa.cm1.3.1-1, ifoa.sp2.1.1-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An annuity contract pays a series of benefits while the life assured survives, running for
the whole of life, for a fixed term, or from a deferred date, with the guaranteed and
return-of-premium variants each attaching a further condition to that basic pattern.

## The expression

$$
a_x = \sum_{t=1}^{\infty} v^{t} \, {}_{t}p_x
$$

Here $a_x$ is the expected present value of a whole-life annuity of one unit a year paid
in arrear to a life aged $x$, $v$ is the discount factor for one year, and ${}_{t}p_x$ is
the probability that life $x$ survives $t$ years. A temporary annuity truncates the sum at
the term, and a deferred annuity starts it at the deferred date rather than at $t = 1$.

## Why this node exists

A benefit contingent on survival cannot be valued by discounting alone, since a payment
due in ten years is worth less again once the chance of not being alive to receive it is
weighed in. This node fixes the cash-flow pattern that valuation multiplies by survival
probability, and contract design needs it settled before that valuation can begin.
