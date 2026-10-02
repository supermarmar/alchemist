---
id: state-dependent-utility-function
title: State-dependent utility function
domains: [eco]
status: drafted
requires: [utility-function]
spends: []
anchor: [ifoa.cm2.1.2-5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A state-dependent utility function values wealth differently depending on which state of the
world it is received in, so that the same level of wealth can carry a different marginal
utility in a state such as illness or unemployment than it does in an ordinary state.

## The expression

$$
U = U(W, s)
$$

Here $W$ is wealth and $s$ indexes the state of the world, and $U(W, s)$ is the utility that
wealth $W$ delivers when the individual is in state $s$. The partial derivative of $U$ with
respect to $W$ can therefore differ across states even at the same wealth level, which an
ordinary utility function defined on wealth alone cannot represent.

## Why this node exists

An investor who becomes ill values an extra pound differently from one who stays healthy, since
illness itself changes what that pound can buy in terms of welfare, and a utility function
defined on wealth alone has no way to capture that shift. Hence, this node supplies the extension
that lets an insurance or health economics application reason about a state that changes the
value of money itself.
