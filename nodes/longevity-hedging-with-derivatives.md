---
id: longevity-hedging-with-derivatives
title: Hedging longevity risk with derivatives
domains: [fin-eng, life]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp6.2.8]
vault_articles: [methods/longevity-risk-transfer]
vault_sources: []
taught_in: null
---

## Definition

A longevity derivative pays out on the difference between a mortality rate fixed
at inception and the mortality rate a reference population actually experiences,
letting a pension scheme or insurer transfer longevity risk without transferring
the underlying assets or liabilities themselves.

## The expression

$$
\text{Payoff} = N \left(q^{\text{fixed}} - q^{\text{realised}}_t\right)
$$

Here $N$ is the notional amount of the contract, $q^{\text{fixed}}$ is the
mortality rate agreed at inception, and $q^{\text{realised}}_t$ is the mortality
rate the reference population actually experiences at time $t$. Where the
realised rate falls short of the fixed rate, meaning the population survives
longer than assumed, the payoff transfers value to the party holding the
longevity exposure.

## Why this node exists

An index-based instrument such as this one is only a hedge to the extent the
reference population's mortality tracks the hedger's own book, and the gap
between the two is the basis risk that has kept index-based volumes low next to
indemnity-based buy-ins and buy-outs. Without a settlement formula tied to an
observable index, a longevity swap could not be marked to market or reconciled
against that indemnity-based alternative at all.
