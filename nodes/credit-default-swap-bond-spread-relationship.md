---
id: credit-default-swap-bond-spread-relationship
title: Relationship between credit default swap and bond spreads
domains: [credit, fin-eng]
status: drafted
requires: [credit-default-swap]
spends: []
anchor: [ifoa.sp6.2.9-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A no-arbitrage argument ties the spread on a credit default swap referencing a bond issuer to
the credit spread on that issuer's own corporate bond, and the gap that opens between the two
in practice, rather than in theory, is called the basis.

## The expression

$$
\text{basis} = \text{CDS spread} - \text{bond spread}
$$

Here the CDS spread is the periodic premium paid to buy default protection on the reference
entity, and the bond spread is the yield on the entity's corporate bond over the equivalent
risk-free rate. A positive basis means protection costs more in the derivative market than the
bond market implies it should; a negative basis means the reverse, and either case signals a
funding, liquidity or supply difference between the two markets, since the credit risk itself
is the same reference entity in both.

## Why this node exists

If the two spreads always matched exactly, a basis trade could never make money, and it is
precisely because funding costs, liquidity and counterparty risk in the CDS market differ from
those in the bond market that a persistent basis exists to trade against. Any credit desk
running both instruments on the same reference entity needs this relationship to judge whether
either market is temporarily mispriced against the other.
