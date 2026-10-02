---
id: economic-loss-definition-for-lgd
title: Economic loss definition for LGD
domains: [credit, regulation]
status: drafted
requires: [loss-given-default]
spends:
  - {object: obj.exposure, domain: credit}
  - {object: obj.exposure, domain: regulation}
anchor: [bcbs.d424.irb.para-228]
vault_articles: [regulation/irb-lgd-estimation]
vault_sources: []
taught_in: null
---

## Definition

Economic loss given default measures the fraction of exposure at default an institution
expects to lose, with every recovery cash flow discounted at a rate reflecting its risk
and timing and every direct and indirect cost of the workout deducted before the ratio is
taken. An accounting write-off books recoveries at their nominal value and often nets
costs against a separate ledger line; this measure absorbs both effects into the one
figure the capital calculation uses.

## The expression

$$
\mathrm{LGD}_{\text{economic}} = 1 - \frac{PV(\text{recoveries}) - PV(\text{costs})}{\mathrm{EAD}}
$$

Here $PV(\text{recoveries})$ is the present value of the resolution's recovery cash flows,
discounted at a rate reflecting their risk and timing, $PV(\text{costs})$ is the present
value of the direct and indirect costs the workout incurs, and $\mathrm{EAD}$ is the
exposure at default the loss is measured against.

## Why this node exists

Discounting recoveries and deducting workout costs is what the regulatory guidelines add
to a plain cash count, and both steps move the same direction: a recovery received in
three years is worth less than one received immediately, and a workout that costs money
to run leaves less behind for the lender. Since the loss given default this node measures
feeds directly into risk-weighted assets, understating either adjustment understates the
capital a bank holds against the exposure. Downturn LGD estimation needs it next, since the
downturn calibration types apply their uplift to this economic measure.
