---
id: dcf-use-lifetime-roe-raroc
title: Lifetime ROE and RAROC
domains: [fin-man]
status: drafted
requires: [discounted-cashflow-model-pricing]
spends: []
anchor: [assa.f107.5.4-3-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Lifetime return on equity measures a product's whole-life present value against the equity
funding it, and the risk-adjusted return on capital measures the same present value against the
economic capital the product is assumed to consume. A riskier product is judged against a
larger capital base, and a safer one against a smaller one, so the two ratios need not move
together.

## The expression

$$
\text{Lifetime ROE} = \frac{PV}{E}, \qquad \text{RAROC} = \frac{PV}{K}
$$

Here $PV$ is the product's lifetime present value, $E$ is the equity allocated to fund it, and
$K$ is the economic capital assumed to support it, so that RAROC and lifetime ROE agree exactly
where a product's equity funding and its economic capital coincide.

## Why this node exists

A single-period margin rewards a product that looks profitable this year even where a longer
loan or a slower-amortising facility consumes capital for years after that margin is earned, and
neither ratio here can be read off a one-period income statement. Comparing two products on
either ratio is what lets a bank choose between a high-margin, capital-heavy product and a
lower-margin, capital-light one on the same footing, with capital consumption priced in.
