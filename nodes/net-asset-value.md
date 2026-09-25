---
id: net-asset-value
title: Net asset value
domains: [fin-eng]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp5.8.1-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The net asset value of a fund is the value of its holdings at market prices, net of its
liabilities, expressed per unit or per share in issue.

## The expression

$$
\text{NAV} = \frac{A - L}{n}
$$

Here $A$ is the market value of the fund's holdings, $L$ is the fund's liabilities, $n$ is the
number of units or shares in issue, and NAV is the resulting value attributable to a single
unit. A fund priced daily recomputes NAV from that day's closing market prices, so NAV tracks the
market value of the underlying holdings, whatever sentiment about the fund itself is doing.

## Why this node exists

A fund's traded price needs a benchmark independent of what investors are currently willing to
pay for it, otherwise there is nothing to compare that price against and no way to tell whether
the fund trades at a premium or a discount to its holdings. NAV supplies that independent
benchmark, computed from the market value of the assets themselves, and every later assessment
of a fund's performance starts from a NAV history.
