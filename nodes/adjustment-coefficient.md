---
id: adjustment-coefficient
title: Adjustment coefficient
domains: [actuarial, gi]
status: drafted
requires: [probability-of-ruin]
spends:
  - {object: obj.hazard, domain: gi}
anchor: [ifoa.cm2.4.1-5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The adjustment coefficient of a surplus process is the positive root of an equation
balancing the insurer's premium loading against the moment generating function of claim
size, and Lundberg's inequality uses it to bound the probability of ruin from above; it
does not exist where claim sizes are heavy-tailed enough that the moment generating
function is infinite for every positive argument.

## The expression

$$
\lambda + cR = \lambda M_X(R)
$$

Here $R$ is the adjustment coefficient, $\lambda$ is the claim intensity, $c$ is the
insurer's premium income rate, and $M_X(R)$ is the moment generating function of the
individual claim size $X$ evaluated at $R$. Lundberg's inequality then bounds the
probability of ruin from initial surplus $u$ by $e^{-Ru}$.

## Why this node exists

The probability of ruin itself has no closed form for most claim-size distributions, so a
usable bound has to come from somewhere else, and the adjustment coefficient is the
single number that inequality is built on. Optimising the adjustment coefficient under
reinsurance needs it next, since choosing a reinsurance arrangement to raise $R$ is the
most direct way to tighten the bound on ruin.
