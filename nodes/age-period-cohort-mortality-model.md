---
id: age-period-cohort-mortality-model
title: Age-period-cohort mortality model
domains: [life]
status: drafted
requires: [age-period-cohort, mortality-projection-approaches]
spends: []
anchor: [ifoa.cs2.4.6-2, ifoa.cs2.4.6-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The age-period-cohort mortality model writes the log of the mortality rate at each
age and calendar period as the sum of an age effect, a period effect and a cohort
effect for the year of birth, fitted subject to an identifiability constraint on the
three linked axes.

## The expression

$$
\log m_{x,t} = \alpha_x + \kappa_t + \gamma_{t-x}
$$

Here $m_{x,t}$ is the mortality rate at age $x$ in calendar period $t$, $\alpha_x$
is the age effect, $\kappa_t$ is the period effect, and $\gamma_{t-x}$ is the
cohort effect for the cohort born in year $t-x$.

## Why this node exists

Without separating mortality into these three effects, a projection conflates a
genuine cohort effect, such as the improvement a decade's births went on to enjoy,
with age and period trends that have nothing to do with it. The age-period-cohort
identification problem shows the three axes are collinear, so the model can only be
fitted once an identifiability constraint is chosen, and only after that choice can
its period and cohort effects be extrapolated to project mortality forward.
