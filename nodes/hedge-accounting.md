---
id: hedge-accounting
title: Hedge accounting
domains: [fin-man, regulation]
status: drafted
requires: []
spends: []
anchor: [assa.f207.2.3-1, assa.f207.2.3-2, iasb.ifrs9.5.2-3, iasb.ifrs9.6.1-1, iasb.ifrs9.6.1-2]
vault_articles: [regulation/ifrs9-financial-instruments]
vault_sources: []
taught_in: null
---

## Definition

Hedge accounting is the accounting treatment that recognises gains and losses on
a hedging instrument in the same period as the offsetting gains and losses on the
item it hedges, so that an economically effective hedge does not itself create
earnings volatility. A hedge relationship qualifies for the treatment only where
an economic relationship between the two is demonstrated at inception and
monitored thereafter.

## The expression

$$
\text{Effectiveness ratio} = \frac{\Delta FV_{\text{hedging instrument}}}{\Delta FV_{\text{hedged item}}}
$$

Here $\Delta FV_{\text{hedging instrument}}$ is the change in fair value of the
hedging instrument over the assessment period, and $\Delta FV_{\text{hedged
item}}$ is the change in fair value, or in a cash flow hedge the change in
expected cash flows, of the item being hedged. International Accounting Standard
39 (IAS 39), the predecessor standard, treated a ratio between 80% and 125% at
inception as evidencing that a hedge was highly effective, the qualifying test
under that standard. International Financial Reporting Standard 9 (IFRS 9)
removed that bright-line test and asks instead for an economic relationship
between the hedged item and the hedging instrument, credit risk not dominating
the value changes that relationship produces, and a hedge ratio consistent with
the one actually used for risk management.

## Why this node exists

Under IFRS 9, a hedge qualifies for the accounting treatment only when it meets
all three conditions the expression above names, and the effectiveness ratio
feeds only the third: whether the hedge ratio matches the one actually used for
risk management. Without meeting all three, a hedge reverts to fair value
through profit or loss by default, since neither an auditor nor a supervisor can
treat an unqualified position as hedged. The fair value hedge needs this
qualifying test next, since it is the specific designation available once the
exposure being hedged is a recognised asset or liability.
