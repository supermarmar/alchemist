---
id: expected-credit-loss
title: Expected credit loss
domains: [credit, regulation]
status: drafted
requires: [cash-shortfall]
spends:
  - {object: obj.exposure, domain: credit}
  - {object: obj.exposure, domain: regulation}
anchor: [assa.f207.1.12-3, assa.f207.5.1-2, assa.f207.5.2-1, iasb.ifrs9.5.5-17, iasb.ifrs9.5.5-18, iasb.ifrs9.b5.5-41, iasb.ifrs9.b5.5-42]
vault_articles: [concepts/ifrs9-expected-credit-loss]
vault_sources: []
taught_in: null
---

## Definition

IFRS 9 requires a bank to recognise expected credit loss on a financial instrument from
the date it is first recognised, replacing the incurred loss model that recognised a loss
only once objective evidence of impairment existed. The allowance is recalculated at every
reporting date as economic conditions move and as the instrument's stage changes.

## The expression

$$
\mathrm{ECL} = \sum_{t=1}^{T} PD_t \times LGD_t \times \mathrm{EAD}_t \times v^t
$$

Here $PD_t$ is the marginal probability of default in period $t$, $LGD_t$ is the loss
given default in period $t$, $\mathrm{EAD}_t$ is the exposure at default in period $t$,
$v^t$ discounts that period's expected loss back to the reporting date, and $T$ is the
horizon the instrument's stage assigns to the sum.

## Why this node exists

Combining probability of default, loss given default and exposure at default is what
turns a general concern that loan quality is deteriorating into a number a bank can
provision against and hold capital behind, and discounting each period's expected loss
keeps a loss twenty years away from being counted as heavily as one due next month.
Twelve-month versus lifetime expected credit losses needs it next, since it is this same
sum, truncated at $T = 12$ months or carried to the instrument's full lifetime, that
distinguishes a Stage 1 allowance from a Stage 2 or Stage 3 one.
