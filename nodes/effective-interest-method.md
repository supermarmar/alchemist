---
id: effective-interest-method
title: Effective interest method
domains: [fin-man, regulation]
status: drafted
requires: [initial-measurement-at-fair-value]
spends: []
anchor: [iasb.ifrs9.5.4-1, iasb.ifrs9.b5.4-1, iasb.ifrs9.b5.4-4]
vault_articles: [concepts/effective-interest-rate]
vault_sources: []
taught_in: null
---

## Definition

The effective interest method recognises interest revenue on a financial asset measured at
amortised cost by applying a single rate, fixed at initial recognition, to the asset's gross
carrying amount throughout its expected life.

## The expression

$$
\mathrm{GCA}_0 = \sum_{t=1}^{n} \frac{\mathrm{CF}_t}{(1 + \mathrm{EIR})^t}
$$

Here $\mathrm{GCA}_0$ is the gross carrying amount at initial recognition, $\mathrm{CF}_t$ is
the contractual cash flow expected in period $t$, $n$ is the number of periods to the
instrument's expected maturity, and $\mathrm{EIR}$ is the effective interest rate, the single
discount rate that makes the equation hold exactly. The equation is solved for
$\mathrm{EIR}$ numerically, since a general cash flow schedule admits no closed form, and the
same rate then accrues interest income period by period on the amortised cost carrying
amount that remains outstanding.

## Why this node exists

A loan's nominal contractual rate ignores the upfront fees and costs a lender incurs to
originate it, so recognising interest income at that nominal rate would misstate income in
every period the fee affects. Spreading those fees over the instrument's expected life,
through a single rate solved once at inception, is what the effective interest method exists
to do, and fees integral to the effective interest rate needs it next to say which fees
belong inside that calculation.
