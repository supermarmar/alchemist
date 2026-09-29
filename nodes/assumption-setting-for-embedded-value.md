---
id: assumption-setting-for-embedded-value
title: Assumption setting for embedded value
domains: [actuarial, life]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp1.5.1-4, ifoa.sp2.5.1-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Embedded value assumption setting chooses the mortality, persistency, expense and economic
bases used to project the future shareholder cash flows a book of business is expected to
generate, before those cash flows are discounted back to embedded value.

## The expression

$$
\mathrm{EV} = \mathrm{ANAV} + \mathrm{VIF}
$$

Here $\mathrm{ANAV}$ is the adjusted net asset value, the shareholder-owned capital already
held, and $\mathrm{VIF}$ is the value of in-force business, the present value of the
projected future shareholder cash flows the in-force book is expected to release. Every
assumption chosen at this node feeds $\mathrm{VIF}$, since $\mathrm{ANAV}$ is a balance
sheet figure rather than a projection.

## Why this node exists

Embedded value is only as reliable as the projection assumptions behind $\mathrm{VIF}$,
so an unrealistic lapse or expense assumption overstates the shareholder value a book will
actually deliver. Embedded value calculation needs this node's assumptions fixed before it
can turn the projected cash flows into a single reported figure.
