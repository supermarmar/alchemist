---
id: gradient-descent
title: Gradient descent
domains: [ml]
status: drafted
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l04]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Gradient descent minimises a differentiable loss function by repeatedly moving the
parameter vector a small step in the direction opposite its gradient. It is a
first-order iterative method, so it uses only local slope information and carries
no guarantee of finding a global minimum once the loss is non-convex.

## The expression

$$
\theta_{t+1} = \theta_t - \eta \nabla L(\theta_t)
$$

Here $\theta_t$ is the parameter vector at iteration $t$, $\eta$ is the learning
rate governing the size of each step, and $\nabla L(\theta_t)$ is the gradient of
the loss $L$ evaluated at $\theta_t$.

## Why this node exists

Every network in this corpus, however deep, is fitted by adjusting weights until
the loss stops falling, and gradient descent is the rule that adjustment follows.
Recomputing the gradient over a dataset too large to hold in memory at every step
is impractical, and stochastic gradient descent needs it next, since it replaces
the full gradient this expression calls for with one estimated from a small batch.
