---
id: embedded-value-profit-analysis
title: Embedded value profit analysis
domains: [actuarial, life]
status: drafted
requires: [assumption-setting-for-embedded-value]
spends: []
anchor: [ifoa.sp1.5.3-1, ifoa.sp1.5.3-2, ifoa.sp2.5.3-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Embedded value profit analysis decomposes the change in a book's embedded value over a
period into the pieces that explain it: the value the period's new business adds at the
point of sale, the expected return that unwinds on the value already in force, the
variance between actual and assumed experience, and the impact of any change the actuary
makes to the assumptions themselves.

## The expression

$$
EV_1 = EV_0 + VNB + i\,EV_0 + \varepsilon_{\text{exp}} + \varepsilon_{\text{assum}}
$$

Here $EV_0$ and $EV_1$ are the embedded value at the start and end of the period, $VNB$ is
the value of new business written during the period, $i\,EV_0$ is the expected return that
unwinds on the opening value at the risk discount rate $i$, $\varepsilon_{\text{exp}}$ is
the variance between actual and assumed experience, and $\varepsilon_{\text{assum}}$ is the
change in embedded value attributable to a revised assumption.

## Why this node exists

Splitting the period's movement into these five pieces answers a question a single closing
figure cannot: whether the book grew because new business was written, because priced
profit emerged as expected, because experience ran better or worse than assumed, or
because the actuary revised an assumption. A management team reading only the closing
number could mistake a discount rate change for a deterioration in the underlying book,
and the analysis exists to keep those two causes apart.
