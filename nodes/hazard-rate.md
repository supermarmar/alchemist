---
id: hazard-rate
title: Hazard rate
domains: [stats, life, gi, credit]
status: drafted
requires: [survival-function]
spends:
  - {object: obj.hazard, domain: life}
  - {object: obj.hazard, domain: gi}
  - {object: obj.hazard, domain: credit}
  - {object: obj.hazard, domain: stats}
  - {object: obj.survival, domain: credit}
anchor: [ifoa.cs2.2.1]
vault_articles: []
vault_sources: []
taught_in: S1_credit-survival-bridge
---

## Definition

The hazard rate at a time is the instantaneous rate at which the event occurs, given
that it has not already occurred by that time. It is undefined wherever survival to
that time has probability zero, for the same reason a conditional probability is
undefined when the event it conditions on cannot happen.

## The expression

$$
h(t) = \lim_{\Delta t \to 0} \frac{P\bigl(t \le T \lt t + \Delta t \mid T \ge t\bigr)}{\Delta t}
$$

Here $h(t)$ is the hazard rate at $t$, $T$ is the random time at which the event
occurs, $\Delta t$ is a short interval of time immediately after $t$, and the
conditioning event $T \ge t$ is the survival probability the previous node named.
Life, general insurance, credit and statistics each write the hazard under a
different symbol, $\mu_x$, $\lambda$, $h(t)$ and $\lambda(t)$ respectively, and the
table below sets those four side by side. Survival, spent here in credit alone as
$S(t)$, keeps the reading the previous node gave it.

## Why this node exists

A model built only on whether an event has occurred by one horizon cannot say when
within that horizon it is likely to occur, and a hazard is what supplies that
timing. It is also the object every domain in this corpus already estimates without
naming it as such: a force of mortality, a claim intensity and a default hazard are
the same quantity measured on three different books. What a lender can already fit
with its scorecard machinery is a discrete-time version of exactly this hazard, one
month at a time, and that discrete-time hazard needs it next.
