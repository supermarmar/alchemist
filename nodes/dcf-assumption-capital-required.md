---
id: dcf-assumption-capital-required
title: Capital required assumption in a discounted cashflow model
domains: [fin-man]
status: drafted
requires: [discounted-cashflow-model-pricing, risk-weighted-assets]
spends: []
anchor: [assa.f107.5.4-2-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The capital required assumption in a discounted cashflow model is the amount of capital the
model assumes must be held against a product, set as a fixed proportion of the risk-weighted
assets that product generates.

## The expression

$$
K = k \times \mathrm{RWA}
$$

Here $\mathrm{RWA}$ is the product's risk-weighted assets, $k$ is the minimum capital ratio the
bank targets against them, covering both the regulatory minimum and any internal buffer held
above it, and $K$ is the resulting capital the model assumes the product must be funded with.

## Why this node exists

Capital is not free: it must earn a return for the shareholders who supply it, and a loan priced
without regard to how much capital it consumes can look profitable while destroying value once
that capital's cost is charged against it. This assumption is what lets a discounted cashflow
model deduct that capital cost from a product's projected return, rather than pricing every
product as though it were funded entirely by deposits.
