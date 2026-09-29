---
id: probability-of-ruin
title: Probability of ruin
domains: [actuarial, fin-man, gi, stats]
status: drafted
requires: [surplus-process]
spends: []
anchor: [ifoa.cm2.4.1-4, ifoa.cm2.4.1-6, ifoa.cm2.4.1-8, ifoa.sp9.5.1-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The probability of ruin is the chance that an insurer's surplus process falls below zero at some
point over a stated time horizon, considered over an infinite horizon or truncated to a finite
one according to how the surplus process itself is modelled. Where no closed form is available
the probability is instead estimated by simulating the surplus process repeatedly and counting
the proportion of paths that breach zero.

## The expression

$$
\psi(u) = P\bigl(U(t) \lt 0 \text{ for some } t \ge 0\bigr)
$$

Here $u$ is the initial surplus, $U(t)$ is the surplus process the previous node defines, and
$\psi(u)$ is the infinite-horizon probability of ruin starting from initial surplus $u$;
restricting the condition to $t \le T$ for a fixed horizon $T$ gives the finite-horizon
probability $\psi(u, T)$ instead.

## Why this node exists

The probability of ruin computed directly from the surplus process has a closed form in only a
handful of special cases, so most practical work bounds or approximates it. Adjustment
coefficient needs this node next, since it supplies the exponential bound on $\psi(u)$ that
stands in for the exact probability wherever the exact one cannot be found.
