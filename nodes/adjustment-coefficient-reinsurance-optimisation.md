---
id: adjustment-coefficient-reinsurance-optimisation
title: Optimising the adjustment coefficient under reinsurance
domains: [actuarial, gi]
status: drafted
requires: [adjustment-coefficient]
spends: []
anchor: [ifoa.cm2.4.1-7]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Optimising the adjustment coefficient under reinsurance chooses the retention level that
maximises the adjustment coefficient of the insurer's net-of-reinsurance surplus process,
since a larger adjustment coefficient gives a tighter Lundberg bound on the probability of
ruin.

## The expression

$$
\lambda + c(a)\, R = \lambda\, M_{X_a}(R)
$$

Here $a$ is the retention level, $c(a)$ is the insurer's net premium income once the
reinsurance premium has been ceded, $X_a$ is the insurer's retained loss per claim under
retention $a$, $M_{X_a}$ is its moment generating function, $\lambda$ is the claim frequency,
and $R$, here written $R(a)$, is the adjustment coefficient solving this equation for the given
retention. The optimal retention $a^{*}$ is the value of $a$ that maximises $R(a)$ over the
feasible range of retentions.

## Why this node exists

A retention chosen only to maximise expected profit can leave the surplus process more exposed
to ruin than a lower retention would, because ceding more claims also lowers the volatility
the reinsurance was bought to control. The adjustment coefficient captures that trade-off in
one number, so maximising it directly is how the optimal retention is actually chosen.
