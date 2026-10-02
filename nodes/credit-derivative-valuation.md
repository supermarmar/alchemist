---
id: credit-derivative-valuation
title: Credit derivative valuation
domains: [credit, fin-eng]
status: drafted
requires: [credit-derivatives]
spends:
  - {object: obj.hazard, domain: credit}
  - {object: obj.survival, domain: credit}
anchor: [ifoa.sp5.3.2-6]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Valuing a credit derivative, such as a credit default swap, requires setting the periodic
premium the protection buyer pays equal to the expected discounted payout the protection seller
makes if the reference obligor defaults, so the valuation rests on the obligor's default
probability and expected recovery, and not on the derivative's own price history.

## The expression

$$
s \approx (1-R)\,h
$$

Here $s$ is the credit default swap spread, the annualised premium the protection buyer pays,
$R$ is the expected recovery rate on the reference obligor's defaulted debt, and $h$ is the
obligor's hazard rate. The approximation holds where the hazard rate is roughly constant over
the swap's term and the premium and protection legs are valued off the same survival
probability $S(t)$, so that setting the two legs equal cancels $S(t)$ from both sides.

## Why this node exists

A credit derivative's payoff is triggered by an event, the reference obligor's default, that an
equity or interest rate derivative has no equivalent of, so its price cannot be built from a
model of the underlying's own volatility the way an option's can. The spread this valuation
produces is the market's implied estimate of the obligor's hazard rate net of recovery, which
is exactly the quantity a bank compares against its own internal estimate when it judges
whether the market is pricing an obligor's credit risk richly or cheaply.
