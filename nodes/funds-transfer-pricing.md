---
id: funds-transfer-pricing
title: Funds transfer pricing
domains: [fin-eng, fin-man]
status: drafted
requires: []
spends: []
anchor: [assa.f207.4.3-1, assa.f207.4.4-4, assa.f207.4.5-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Funds transfer pricing charges each business unit an internal price for the funding it uses or the
deposits it raises, so that a lending decision and a deposit-gathering decision are each judged
against the bank's true cost of funds rather than against each other's cash flows.

## The expression

$$
m_{\text{lend}} = r_{\text{cust}} - r_{\text{ftp}}, \qquad m_{\text{fund}} = r_{\text{ftp}} - r_{\text{cost}}
$$

Here $r_{\text{cust}}$ is the rate charged to the borrower, $r_{\text{ftp}}$ is the internal
transfer rate assigned to that funding, and $r_{\text{cost}}$ is the bank's actual cost of raising
the equivalent funding. $m_{\text{lend}}$ is the commercial margin the lending unit earns and
$m_{\text{fund}}$ is the margin the funding unit earns, and the two together reconstitute the
bank's net interest margin on the transaction.

## Why this node exists

Without a transfer price, a lending unit funded by cheap retail deposits would appear more
profitable than an identical loan funded at wholesale rates, purely because of where the money
came from instead of anything the lending unit did. The funds transfer pricing curve
needs this node next, since it fixes how the transfer rate itself varies with the tenor of the
underlying loan or deposit.
