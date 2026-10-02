---
id: expected-utility-theorem
title: Expected utility theorem
domains: [eco]
status: drafted
requires: [utility-function]
spends: []
anchor: [ifoa.cm2.1.2-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The expected utility theorem states that a decision maker whose preferences satisfy the
von Neumann-Morgenstern axioms, completeness, transitivity, continuity and independence,
ranks uncertain outcomes by the expected value of a utility function applied to them.
Where the outcome is certain, the expected utility collapses to the utility of that single
outcome.

## The expression

$$
EU(L) = \sum_i p_i\, u(x_i)
$$

Here $EU(L)$ is the expected utility of a lottery $L$, $p_i$ is the probability of its
$i$-th outcome, $x_i$ is the payoff of that outcome, and $u(\cdot)$ is the decision maker's
utility function.

## Why this node exists

Two lotteries can share the same expected wealth and still leave a decision maker with a
different view of them, and a ranking rule built only on expected wealth cannot say why.
The theorem licenses the substitution: a rational ranking of gambles runs on expected
utility, with expected wealth recovered only as the special case where the utility
function happens to be linear. Every later result on risk aversion and the shape of the
utility function stands on this licence to rank by $EU$ at all.
