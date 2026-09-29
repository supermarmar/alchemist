---
id: early-stopping
title: Early stopping
domains: [ml, stats]
status: drafted
requires: [out-of-sample-validation]
spends:
  - {object: obj.coefficients, domain: ml}
anchor: [ucsc.dl-actuarial-2026.l04]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Early stopping halts training once a model's out-of-sample loss, monitored on a validation set
after every epoch, stops improving, and it retains the parameters from whichever epoch achieved
the best validation loss seen so far rather than the parameters training ends on.

## The expression

$$
t^{*} = \arg\min_{t \le T} \hat L_{\text{test}}(\theta_t), \qquad \hat\theta = \theta_{t^{*}}
$$

Here $\theta_t$ is the network's parameters after $t$ epochs of training, $\hat L_{\text{test}}$
is the out-of-sample loss evaluated at those parameters, $T$ is the epoch training is halted at,
$t^{*}$ is the epoch achieving the lowest out-of-sample loss up to that point, and $\hat\theta$
is the parameter vector early stopping returns.

## Why this node exists

An overparametrised network's training loss keeps falling long after its out-of-sample loss has
started to rise, so a network trained to convergence on the training set alone is a network
trained past the point its predictions stopped generalising. Monitoring the out-of-sample loss
this node relies on and halting at its minimum limits how far training is allowed to travel from
initialisation, which regularises the network's effective capacity without changing its
architecture or adding a penalty term to the objective.
