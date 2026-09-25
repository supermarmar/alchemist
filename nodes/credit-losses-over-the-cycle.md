---
id: credit-losses-over-the-cycle
title: Credit losses over the economic cycle
domains: [credit, eco]
status: drafted
requires: []
spends:
  - {object: obj.exposure, domain: credit}
anchor: [assa.f107.1.4-1]
vault_articles: [methods/credit-risk-procyclicality]
vault_sources: []
taught_in: null
---

## Definition

Credit losses over the cycle describes how a lender's realised and expected credit
losses rise during a downturn and fall during an expansion, since the probability of
default driving expected loss is itself a function of prevailing economic conditions
instead of a fixed constant.

## The expression

$$
EL_t = PD_t \times LGD \times \mathrm{EAD}
$$

Here $EL_t$ is the expected credit loss in period $t$, $PD_t$ is the point-in-time
probability of default prevailing in that period, and $LGD$ and $\mathrm{EAD}$ are the
loss given default and exposure at default, held fixed here so that the cyclicality in
$EL_t$ is attributed to the term that actually moves with the economy.

## Why this node exists

A lender that provisions against a single average probability of default understates
its losses in a recession and overstates them in a recovery, and that mismatch is the
procyclicality a forward-looking impairment standard exists to correct. Expected
credit losses over the economic cycle needs this point-in-time decomposition next, to
link $PD_t$ explicitly to a macroeconomic scenario.
