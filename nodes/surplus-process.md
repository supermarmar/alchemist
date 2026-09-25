---
id: surplus-process
title: Surplus process
domains: [actuarial, gi]
status: drafted
requires: []
spends:
  - {object: obj.hazard, domain: gi}
anchor: [ifoa.cm2.4.1-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The surplus process models an insurer's cash position over time as its initial capital, plus
premium income received, less the aggregate claims paid out, so that the insurer's surplus at
any date can be read directly off the process.

## The expression

$$
U(t) = u + ct - S(t), \qquad S(t) = \sum_{i=1}^{N(t)} X_i
$$

Here $U(t)$ is the surplus at time $t$, $u$ is the initial surplus, $c$ is the constant rate at
which premium income accrues, and $S(t)$ is the aggregate claims paid by time $t$. $S(t)$ is
itself a compound process: $N(t)$ counts the number of claims by time $t$ and is usually taken
as a Poisson process with claim intensity $\lambda$, and $X_i$ is the size of the $i$-th claim.

## Why this node exists

An insurer needs to know not just its expected profitability but the chance that its capital is
exhausted before claims can be met, and that question cannot be asked at all until the surplus
itself is written as a stochastic process rather than a single expected figure. Probability of
ruin needs this process next, since ruin is defined as the first time $U(t)$ falls below zero.
