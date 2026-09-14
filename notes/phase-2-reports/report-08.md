# Batch 8 report

8 of 40 nodes attached, 32 uncovered. One vault article covers three nodes (`fca-consumer-duty`
covers `conduct-risk` and `conduct-risk-mitigation`); one node draws on three articles
(`corporate-governance-principles`). Total attachments: 10 (article, node) pairs.

## Attached

**conduct-risk** → `regulation/fca-consumer-duty`. The Duty's three cross-cutting rules and four
outcome areas (products and services, price and value, consumer understanding, consumer support)
are directly the "customer harm" half of the node; supervisory Dear CEO findings supply the
regulatory-consequence half. The "market abuse" half of the node's definition is not covered;
this article is retail-conduct only.

**conduct-risk-mitigation** → same article. The products-and-services outcome ("offerings are
designed to meet the needs... of an identified target market, with no significant foreseeable
harm") and the fair-value assessment obligation are literally the mitigation actions the node
describes.

**copula-based-credit-model** → `methods/default-correlation-copula-models`. Li (2000): marginal
survival distributions from market prices joined by a copula into a portfolio-dependence
structure; the normal-copula/CreditMetrics equivalence. A precise match.

**corporate-governance-principles** → `regulation/bcbs-d328-corporate-governance`,
`regulation/eba-gl-2021-05-internal-governance`, `regulation/pra-ss5-16-corporate-governance`.
All three treat board accountability, oversight, and management/board separation as their primary
subject (RAF ownership, board committees, NED independence, three lines of defence).

**contractual-maturity-gap** → `regulation/bcbs-liquidity-nsfr-monitoring-tools`. Its "contractual
maturity mismatch tool" paragraph defines the exact mechanism: contractual inflows/outflows
reported across maturity buckets to expose funding cliffs.

**consumer-debt-workout** → `regulation/consumer-credit-arrears-and-recovery`. CONC 7's forbearance
duty and its enumerated measures (waiving interest, reduced payments) versus repossession/
bankruptcy as a last resort is the negotiated-arrangement-over-legal-recovery mechanism, though
framed as UK conduct regulation rather than the ASSA F207 syllabus's South African statutory
debt-counselling process; a page drafted from it will be UK-framed.

**confounding** → `methods/adjustment-set-selection`. Its "backdoor path... conditioning set
controls confounding when it blocks every such path" is the node's own mechanism stated with
causal-diagram precision, despite the node's own anchor lecture (an EDA/GLM/GBM pricing example)
not covering it at all.

**contagion-risk** → `regulation/bcbs-banks-nbfi-interconnections-systemic-risk`. Direct treatment
of distress propagation with worked scenarios (Archegos, UK LDI 2022); scoped to bank-NBFI
channels, so SP9's "different stakeholder groups" framing is only partly covered.

## Notable rejections

**copula** (general node): considered `default-correlation-copula-models` and rejected it, having
first leant towards attaching. The article states what a copula does inside Li's argument but
never gives the general definition (no Sklar, no uniform-marginals construction, no family
survey); a page drafted from it would be a credit-correlation page. Routed to the ledger instead,
reusing `ifoa-cs2-core-reading-2026` (same CS2 section, 1.3, as the already-ledgered sibling
`archimedean-copula`).

**corporate-exposure-risk-weights**: no wiki article treats the SA corporate risk-weight
hierarchy (checked `crr-credit-risk-provisions`, `eba-sme-supporting-factor`,
`basel-3-1-uk-implementation`, all passing mentions only). The node's own anchor,
`bcbs.d424.sa.para-37`, is wrong on inspection: paragraph 37 of d424 is "Exposures to securities
firms," not corporates; the corporate rules are paragraphs 38-43. Ledgered as a new document
(`bcbs-d424-sa-corporate-exposures`, already ingested).

**corporate-governance-failure-in-banking-crises** and **corporate-governance-structure-factors**:
both BCBS d328 and PRA SS5/16 name the 2008 crisis and "size and complexity" in one sentence each,
as motivation for their own current standard rather than as a treatment of either subject.
Rejected as passing mentions.

**convolutional-neural-network**: `deep-learning-foundations` and `deep-learning-implementation`
each name "convolutional networks" once in a book-chapter list, no definition. Rejected, but the
node's own anchor lecture (already ingested) does treat CNNs directly and substantively
(local connectivity, parameter sharing, the convolution operation) — ledgered as a wiki-scope gap.

**corporate-debt-restructuring**, **corporate-loan-pricing**, **contingency-funding-obligation-
modelling**, **correlation-measures**, **convolution-formula**: each had a plausible-looking
candidate that on reading applied the same vocabulary to a different problem (IFRS 9 EAD/CCF
provisioning vs. liquidity contingent funding; Somers' D/Kendall's tau as discrimination metrics
vs. general Pearson/Spearman/Kendall theory; Panjer's recursion avoiding convolution vs. teaching
it). All rejected with the specific clause named in the ledger notes.

**Zero-candidate stubs** (pure maths/stats/life/GI actuarial pedagogy, searched by title and
domain vocabulary, no vault hits): `conditional-distribution/-expectation/-probability`, all five
`confidence-interval-*` nodes, `conservation-laws-and-pde-modelling`, `consumer-utility-
maximisation`, `contingent-event-products-and-benefits`, `continuous-function-properties`,
`continuous-uniform-distribution`, `contract-alterations`, `contract-design`, `convergence-in-
distribution/-probability`, `convertible-bond`, `corporate-banking-activities`, `corporate-
transactions-and-insolvency`, `cost-and-contribution-determination`.

## Ledger

16 entries in `ledger-08.yaml`, 12 reusing an existing id (`ifoa-cs1/cs2/cb2/cp1/sp2/sp6`,
`assa-f107/f207`, `up-ias712/lew700/wst211/wst221`, `dl-actuarial-2026-l03`), 3 new University of
Pretoria/BCBS documents (`up-wtw386-course-notes`, `up-wtw310-course-notes`,
`bcbs-d424-sa-corporate-exposures`).

## Ambiguity in the brief

None found. `merge_ledger.py --dry-run` surfaced ~37 "note differs" complaints, all pre-existing
disagreements between other batches reusing the same seeded ids with different extending notes;
none named `ledger-08.yaml`, and the contract in `ledger.py` states these are non-blocking.

`check.py` last line: **1560 nodes, 13 paths, 0 failures.**
