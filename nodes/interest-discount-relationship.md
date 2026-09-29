---
id: interest-discount-relationship
title: Interest and discount rate relationship
domains: [actuarial]
status: drafted
requires: []
spends:
  - {object: obj.discount-factor, domain: actuarial}
anchor: [ifoa.cm1.1.1-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The annual effective rate of discount is the amount deducted from a unit payable
in one year to give its value now, and it relates to the annual effective rate of
interest through the same discount factor that converts a future payment into
its present value.

## The expression

$$
v = \frac{1}{1+i}, \qquad d = 1 - v = \frac{i}{1+i}
$$

Here $i$ is the annual effective rate of interest, $v$ is the discount factor for
one period, and $d$ is the annual effective rate of discount.

## Why this node exists

Every actuarial cash flow calculation moves a payment either forward to a future
date or back to the present, and both directions use the same factor, so a
relationship between $i$ and $d$ has to exist before either movement can be
written down consistently. Accumulated value needs it next, since it is the
operation that applies this factor's reciprocal to carry a payment forward in
time rather than back.
