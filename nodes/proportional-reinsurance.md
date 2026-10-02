---
id: proportional-reinsurance
title: Proportional reinsurance
domains: [gi]
status: drafted
requires: [excess-and-retention-limit]
spends: []
anchor: [ifoa.cs2.1.1-3]
vault_articles: [concepts/reinsurance]
vault_sources: []
taught_in: null
---

## Definition

Proportional reinsurance splits every premium and every claim between cedant and reinsurer in a
fixed proportion, agreed before any loss occurs, either as a single quota share percentage
applied to the whole portfolio or as a surplus treaty in which the retained proportion varies
risk by risk. The split applies identically to premium income and to claims paid, so neither
party's share of the underwriting result differs from its share of the risk.

## The expression

$$
X_{\text{ceded}} = \alpha X, \qquad X_{\text{retained}} = (1-\alpha) X
$$

Here $X$ is the loss on a policy within the treaty, $\alpha$ is the fixed proportion ceded to
the reinsurer, $X_{\text{ceded}}$ is the reinsurer's share of that loss, and
$X_{\text{retained}}$ is the cedant's own share; the same $\alpha$ applies to the premium the
cedant cedes in exchange.

## Why this node exists

A retention limit fixed in money terms leaves a cedant's own share of a large loss undiminished
in proportion; a fixed percentage split closes that gap by scaling with the loss itself.
Insurer and reinsurer loss distribution needs this node next, splitting the aggregate loss
distribution between the two parties in the proportion this node fixes.
