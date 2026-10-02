---
id: universal-approximation-theorem
title: Universal approximation theorem
domains: [maths, ml]
status: drafted
requires: [feed-forward-neural-network]
spends:
  - {object: obj.coefficients, domain: ml}
anchor: [ucsc.dl-actuarial-2026.l04]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The universal approximation theorem states that a feed-forward network with a single hidden
layer of sufficient width and a non-polynomial activation can approximate any continuous
function on a compact set to any prescribed accuracy. It guarantees existence alone; finding
such a network's weights from finite training data is a separate problem left to the fitting
procedure.

## The expression

$$
\sup_{x \in K} \bigl| f(x) - N(x; \theta) \bigr| \lt \varepsilon
$$

Here $K$ is a compact subset of the input space, $f$ is the continuous function being
approximated, $N(x;\theta)$ is the network with weights $\theta$ (spent here as coefficients)
and a single hidden layer of sufficient width, and $\varepsilon$ is the prescribed accuracy the
theorem guarantees can always be met by choosing that width large enough.

## Why this node exists

The theorem settles what a network can represent in principle before anything is said about
how training actually finds good weights, so it answers a question about capacity that is
logically prior to any question about learning. A feed-forward network's later move to several
narrower layers is a choice made for trainability and computational efficiency, against a
background where a single sufficiently wide layer was already known to suffice for
representation alone. The guarantee says nothing about generalisation to unseen data, which
regularisation and early stopping have to supply separately.
