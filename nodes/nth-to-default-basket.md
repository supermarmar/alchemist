---
id: nth-to-default-basket
title: Nth-to-default basket
domains: [credit, fin-eng]
status: drafted
requires: [credit-default-swap]
spends: []
anchor: [ifoa.sp6.2.9]
vault_articles: [methods/default-correlation-copula-models]
vault_sources: []
taught_in: null
---

## Definition

An nth-to-default basket swap pays out on the nth default among a specified group of reference
entities, and only the nth, so its payoff is triggered by an order statistic of the group's
default times.

## The expression

$$
\text{Payoff} = \mathbb{1}\{\tau_{(n)} \le T\} \cdot (1 - \delta_{(n)}) \cdot N
$$

Here $\tau_{(n)}$ is the $n$th order statistic of the reference entities' default times, the
time at which the $n$th obligor in the basket to default actually does so, $T$ is the swap's
maturity, $\delta_{(n)}$ is the recovery rate on the obligor that defaults nth, and $N$ is the
notional. The indicator is one where the nth default has occurred by maturity and zero
otherwise, so a first-to-default swap is the $n=1$ case and protection on later defaults in the
same basket becomes progressively cheaper as $n$ rises, since more defaults must occur first
before the nth one triggers payment.

## Why this node exists

Pricing this payoff needs the joint distribution of every obligor's default time, not each
obligor's marginal hazard taken on its own, because the nth order statistic depends on how the
defaults in the basket are correlated with one another. Copula-based credit portfolio model
needs this node next, supplying the dependence structure across obligors that turns the
marginal survival curves already available into the joint distribution this payoff is priced
against.
