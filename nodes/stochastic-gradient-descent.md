---
id: stochastic-gradient-descent
title: Stochastic gradient descent
domains: [ml]
status: drafted
requires: [gradient-descent]
spends:
  - {object: obj.coefficients, domain: ml}
anchor: [ucsc.dl-actuarial-2026.l04]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Stochastic gradient descent replaces the exact gradient computed over a full training sample
with a gradient computed on a small random mini-batch at every step, dividing training into
epochs of such steps and trading a noisier direction of travel for a far cheaper one to compute.

## The expression

$$
\theta_{t+1} = \theta_t - \eta \nabla L_{B_t}(\theta_t)
$$

Here $\theta_t$ is the parameter vector at iteration $t$, $\eta$ is the learning rate, and
$\nabla L_{B_t}(\theta_t)$ is the gradient of the loss evaluated on the mini-batch $B_t$ drawn
at step $t$, a small subset of the full training sample. Each mini-batch gradient is an unbiased but
noisy estimate of the full gradient, and that noise is what a small learning rate or an adaptive
scheme such as Adam is chosen to manage.

## Why this node exists

Recomputing the exact gradient over a dataset too large to hold in memory is impractical at
every step of training, and stochastic gradient descent is what makes iterative optimisation
feasible at the scale a modern network is trained on. It is also the scheme every network
training routine in this corpus builds on, whatever adaptive refinement it adds on top.
