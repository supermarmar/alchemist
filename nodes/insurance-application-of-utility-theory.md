---
id: insurance-application-of-utility-theory
title: Insurance application of utility theory
domains: [eco, gi]
status: drafted
requires: [risk-aversion, utility-function]
spends: []
anchor: [ifoa.cm2.1.2-7]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The maximum premium a risk-averse individual will pay for insurance against a random loss is
the premium that leaves their expected utility exactly unchanged between facing the loss
uninsured and paying that premium with certainty.

## The expression

$$
U(W - P) = E\bigl[U(W - X)\bigr]
$$

Here $W$ is the individual's wealth before any loss or premium, $X$ is the random loss the
insurance would cover, $U$ is the individual's utility function, and $P$ is the maximum
premium: the certain payment whose utility equals the expected utility of bearing $X$
uninsured. Because $U$ is concave, Jensen's inequality gives $U(W - E[X]) \gt E[U(W - X)]$,
so the $P$ solving the equation above exceeds $E[X]$, and the excess is the amount a
risk-averse individual is willing to pay above the pure expected cost of the loss.

## Why this node exists

Expected monetary value alone cannot explain why anyone buys insurance priced above the
expected claim cost, since it ranks a certain payment and an uncertain loss of the same mean
as equivalent. Combining the utility function's concavity with the specific random loss an
insurer is being asked to cover turns that abstract preference for certainty into a number: the
premium at which a particular policyholder, facing a particular risk, is indifferent between
insuring and not. Every subsequent question about how an insurer should price that risk starts
from knowing what the buyer would actually be willing to pay for it.
