---
id: risk-optimisation
title: Risk optimisation
domains: [fin-man]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp9.6.1-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Risk optimisation chooses a portfolio, or an allocation across activities, that
maximises a stated objective for a given level of risk, subject to any constraints
placed on the risk the organisation may take. The classical case trades expected
return against variance, and every other formulation in the corpus is a variant of
the same trade-off with the objective or the constraint set changed.

## The expression

$$
\max_w \; w^{\mathsf T}\mu - \frac{\lambda}{2} w^{\mathsf T}\Sigma w
$$

Here $w$ is the vector of weights allocated across activities, $\mu$ is the vector
of their expected returns, $\Sigma$ is their return covariance matrix, and $\lambda$
is the risk-aversion parameter trading expected return against variance. A larger
$\lambda$ shifts the optimal $w$ towards the lower-variance activities even where
their expected return is smaller.

## Why this node exists

A stated risk appetite says only how much variance is acceptable, and by itself it
gives no allocation of capital across the activities available. This node supplies
the mechanism that converts a risk limit into a concrete weight for each activity,
so that the risk-return trade-off a board has agreed becomes an instruction a
business line can act on.
