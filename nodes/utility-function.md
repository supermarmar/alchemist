---
id: utility-function
title: Utility function
domains: [eco]
status: drafted
requires: []
spends: []
anchor: [ifoa.cm2.1.2-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A utility function maps an investor's wealth or consumption to a numerical measure of
satisfaction, used to rank uncertain outcomes rather than to measure satisfaction in any
absolute sense.

## The expression

$$
U'(W) \gt 0, \qquad U''(W) \lt 0
$$

Here $W$ is wealth, $U(W)$ is the utility it delivers, $U'(W)$ is the marginal utility of an
extra unit of wealth, and $U''(W)$ is how that marginal utility itself changes as wealth rises.
A positive $U'$ says more wealth is always preferred to less, and a negative $U''$ says each
extra unit is worth less than the one before it, which is what makes an investor with this
shape of utility function risk averse.

## Why this node exists

Ranking outcomes by their expected monetary value alone cannot explain why an investor buys
insurance against a loss whose expected cost the premium exceeds, since expected value treats a
certain loss and an uncertain one of the same expected size as equivalent. A utility function
that is concave in wealth resolves that, because it values a certain outcome above an uncertain
one with the same mean, and the expected utility theorem needs exactly this concavity to state
how an investor ranks a whole distribution of uncertain outcomes.
