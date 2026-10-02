---
id: common-utility-function
title: Common utility function
domains: [eco, fin-eng]
status: drafted
requires: [risk-aversion, utility-function]
spends: []
anchor: [ifoa.cm2.1.2-4, ifoa.cm2.1.2-6]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A utility function used in practice is chosen from a small family of standard forms, each
implying a different pattern of risk aversion as wealth changes, such as constant relative risk
aversion or constant absolute risk aversion.

## The expression

$$
U(w) = \frac{w^{1-\gamma}}{1-\gamma}, \qquad \gamma \neq 1
$$

$$
U(w) = -e^{-\alpha w}
$$

The first form is power, or constant relative risk aversion, utility, where $w$ is wealth and
$\gamma$ is the coefficient of relative risk aversion, constant across every level of wealth.
The second is exponential, or constant absolute risk aversion, utility, where $\alpha$ is the
coefficient of absolute risk aversion. Quadratic and logarithmic utility are the other two forms
most often used, the logarithmic form recovered as the limit of the power form as
$\gamma \to 1$.

## Why this node exists

An investor's actual risk preferences are unobservable, so a model has to assume some
functional form for utility before it can say anything quantitative about optimal portfolio
choice or insurance demand, and the choice between these forms changes the model's predictions.
A quadratic utility function implies risk aversion rising with wealth, which conflicts with
most evidence on investor behaviour, and this contrast between the standard forms is what a
model builder has to weigh before picking one.
