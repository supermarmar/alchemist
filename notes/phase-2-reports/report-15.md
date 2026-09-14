# Phase 2 batch 15 attachment report

40 nodes worked. 9 attached, 31 uncovered. 9 total attachments.

This batch runs from external-environment-analysis to forms-of-interest-rate-risk
alphabetically, and mixes IFRS 9 accounting, UCSC deep-learning, IRRBB regulation, and a long
tail of general-finance and pure-maths topics (ASSA F107/F207, IFoA CB2/CM1/CM2/CP1/SP5/SP6/
SP9, University of Pretoria WTW/WST/FBS course notes) against a credit-risk research vault.
The credit-risk-adjacent clusters (IFRS 9 classification, deep learning architecture, IRRBB)
hit real ground; the general-finance and pure-maths cluster found almost nothing, as expected.

## Attached

### factors-and-interactions
Candidates: `methods/ols-predictor-importance` (open, partial match), `methods/nguyen-2025-enhancing-credit-risk-ml` (open, rejected).
Attached: `methods/ols-predictor-importance`. Its "Tree-based interaction extraction for PD
models" section defines interaction terms directly: "combinations of predictor values that
carry joint predictive power beyond their marginal contributions." Partial-scope note: this
covers interaction terms only, applied to PD modelling rather than the general GLM framing;
it does not treat factors (categorical explanatory variables) at all. Rejected
`nguyen-2025-enhancing-credit-risk-ml`: names "interaction terms" once as a feature-engineering
step with no definition.

### fair-value-through-other-comprehensive-income-classification
Candidates: `regulation/ifrs9-financial-instruments` (open, matches directly).
Attached. Its "Classification and measurement" section states the test almost verbatim:
"Assets held both to collect and to sell, passing SPPI, are measured at fair value through
other comprehensive income (FVOCI)."

### fair-value-through-profit-or-loss-classification
Candidates: `regulation/ifrs9-financial-instruments` (open, matches directly).
Attached. Same section: "All other assets, including those failing the SPPI test, are
measured at fair value through profit or loss (FVTPL)," matching the node's residual-category
framing. Partial-scope note: the article does not name derivatives or held-for-trading
instruments as the typical residents of this category, which the node's second sentence does.

### feature-tokenisation
Candidates: `methods/credibility-transformer` (open, matches directly), `concepts/foundation-models-credit-risk` (rejected, different sense of "tokenisation"), `ai-agents/nlp-and-language-models` (rejected, subword tokenisation is a different concept).
Attached: `methods/credibility-transformer`. Its "Getting tabular data into a transformer"
section states the mechanism almost verbatim: "Feature tokenisation converts every covariate,
categorical and continuous alike, into a vector of common dimension... Categorical covariates
use entity embedding. Continuous covariates get their own small feed-forward embedding." Same
UCSC lecture (l10) the node's own anchor names.

### feed-forward-neural-network
Candidates: `methods/feed-forward-networks-claim-frequency` (open, matches).
Attached. States "The hidden layers perform representation learning and the last layer is a
linear model whose inputs are the learned representation" and frames the network directly
against "a Poisson generalised linear model on the same covariates, because a network
generalises a GLM," matching the node's core claim. Partial-scope note: framed around an
insurance claim-frequency use case rather than as a standalone architecture definition, and
does not spell out the per-layer affine-map-plus-activation construction explicitly.

### fees-integral-to-effective-interest-rate
Candidates: `concepts/effective-interest-rate` (open, partial match).
Attached. States that "upfront origination fees, processing costs, or other charges that are
integral to the lending arrangement" raise the EIR above the nominal rate. Partial-scope note:
covers origination fees only; does not address commitment fees for an undisbursed loan or the
separate treatment of a post-origination service fee such as loan servicing.

### financial-condition-reporting
Candidates: `regulation/solvency-ii-reporting-disclosure` (open, matches), `regulation/eiopa-supervisory-monitoring` (rejected, passing mention), `regulation/solvency-uk-reform` (rejected, passing mention).
Attached: `regulation/solvency-ii-reporting-disclosure`. Its subject is literally named after
the node: the Solvency and Financial Condition Report (SFCR), "the reports and systems a
provider sets up to track the progress of its financial condition," at Solvency II depth
rather than CP1's generic control-cycle framing. Rejected the other two candidates: each
mentions the SFCR only in a single clause about a different topic (Article 138(4) extensions;
PS2/24 capital add-on disclosure).

### financial-technology-disruption-risk
Candidates: `regulation/digitalisation-in-finance` (open, matches directly).
Attached. States the mechanism directly: "the emergence of new competitors, including fintech
firms and large technology platforms... banks may face revenue pressure that increases risk
appetite in other areas," matching "the strategic risk a bank faces from disruptive
innovation by financial technology firms and new entrant banks."

### forms-of-interest-rate-risk
Candidates: `regulation/eba-gl-2022-14-irrbb-csrbb` (open, matches directly), `regulation/bcbs-d368-irrbb-standard` (rejected, broader overview), `concepts/eve-and-nii` (rejected, subsumed).
Attached: `regulation/eba-gl-2022-14-irrbb-csrbb`. States the four channels verbatim: "The
guidelines require that measurement encompasses the full range of repricing risk, yield curve
risk, basis risk, and optionality risk components within the banking book perimeter." Rejected
`bcbs-d368-irrbb-standard`: covers the same IRRBB ground (six shocks, EVE/NII, behavioural
optionality) but never names the four-channel taxonomy the node states; the dedicated match
subsumes it.

## Uncovered (31)

**No vault content at all** (confirmed by index search and full-text grep across `vault/wiki`,
including broad synonym sweeps: extreme value/Pareto/Gumbel/heavy-tail, Galois/irreducible
polynomial, epsilon-delta, hitting time/absorbing state, exchange rate regime/peg, decrement
table, translation risk): externalities, extreme-value-theory, f-distribution,
factor-models-and-arbitrage-pricing-theory (the vault's own "factor model" hits are Gordy's
credit-portfolio ASRF construction, a different tradition from asset-pricing factor models and
APT), fat-tailed-return-distribution, field-extension, filtered-time-series, filtration
(the one grep hit was "exfiltration"), financial-derivatives, financial-institution-regulatory-role,
financial-institutions, financial-instruments (the vault's IFRS 9 article presupposes
instruments already exist rather than surveying the classes of contract the node names),
financial-planning-process, financial-sector-functions, financial-statement-interpretation,
financial-statement-preparation, finite-difference-method-option-pricing, first-passage-time,
fiscal-policy, fixed-income-option-pricing, fixed-income-valuation (the one hit, Li 2000, was a
false positive on its publishing journal's name, *Journal of Fixed Income*), fixed-versus-floating-exchange-rates,
forces-from-dependent-probabilities, foreign-exchange-hedging-of-dividends-and-subsidiary-net-asset-value,
formal-definition-of-a-limit.

**Passing mentions only, rejected:**
- external-environment-analysis: `regulation/prudent-person-principle` names "the external
  environment" once in a list of things a firm must monitor, unrelated to product design;
  `regulation/pure-protection-market-study` treats commission-structure incentives in depth
  but as a narrow FCA conduct study on one product line, not the general SP2 category of
  external factors the node names.
- external-rating-recognition-restrictions: every hit (`bcbs-securitisation-framework`,
  `pra-cp16-22-basel31-consultation`, `eba-esg-green-brown-prudential-factors`) mentions
  "external rating" in the context of a different rule (SEC-ERBA lookup tables, due-diligence
  reduction, an environmental-risk principal-agent model); none states the group-entity
  restriction or the solicited/unsolicited preference the node's anchor paragraph sets out.
  Verified the actual text directly against `vault/markdown/bcbs/bcbs_d424.md` paragraphs
  115-116, which state the node's claim closely but are not drawn on by any wiki article.
- fair-pricing-of-retail-financial-products: `regulation/debt-collection-sector-conduct-supervision`
  covers "treating customers fairly" at length, but as FCA conduct supervision of debt
  collection and vulnerable-customer treatment, not the strategic pricing-versus-return
  pressure the node (ASSA F207) names.
- fair-value-accounting: `concepts/xva-overview` and `concepts/credit-valuation-adjustment`
  each use "fair-value accounting" or "fair value" once, in the context of XVA/CVA
  derivative pricing adjustments; neither defines the general practice of carrying assets and
  liabilities at market value rather than historical cost.
- fair-value-hedge: `regulation/ifrs9-financial-instruments`'s "Hedge accounting" section
  covers the 80-125% effectiveness range and the rebalancing requirement but never names or
  defines the three hedge relationship types (fair value, cash flow, net investment), so it
  does not state what the node itself asks for.
- fixed-income-option-pricing: `regulation/eba-gl-2022-14-irrbb-csrbb` mentions "embedded cap
  and floor structures" that "must also be captured within the EVE cash flow model," but as a
  modelling-scope requirement, not a pricing method; the other IRRBB shock-calibration hits use
  "caps and floors" to mean bounds on the shock size, an unrelated sense of the term.
- foreign-exchange-hedging-instruments: the FRTB and SA-CCR hits treat foreign exchange only
  as a capital-charge asset class (add-ons, sensitivities), never the hedging instruments
  themselves or their use.

**Considered and deliberately not attached despite surface similarity:**
- financial-condition-reporting was close to this category rather than a clean attach: the
  node's CP1 framing is generic ("the reports and systems a provider sets up") while
  `regulation/solvency-ii-reporting-disclosure` is Solvency-II-specific. Attached anyway
  because the SFCR's own name is "Financial Condition Report," judged a genuine dedicated
  instance rather than a passing mention.

## Ledger (`ledger-15.yaml`)

20 entries: 17 reuse a seeded id (extending `needed_by` with this batch's nodes and adding a
note on which different part of the document is needed, claim/document/tier/acquisition/status
copied verbatim), plus 3 new ids. `merge_ledger.py --dry-run` reports "would write 73 entries
(4 seeded)" with no complaints; it flags a non-blocking disagreement on the new
`up-wtw354-course-notes` id, where another batch has separately proposed the same document for
a different WTW354 topic (investment risk measures beyond variance) -- expected where two
batches independently reach for the same course-notes document, and left for the gate to
reconcile per the brief.

New ids: `bcbs-d424-sa-external-rating-recognition` (paragraphs 115-116, `status: ingested`
since `bcbs_d424.md` is already in the vault and only the wiki article is missing, verified by
direct read), `up-wtw354-course-notes` (factor models and arbitrage pricing theory), and
`up-wtw381-course-notes` (field extensions). One entry departs from a single anchor-body
default because the node itself carries four anchors across four different documents
(external-environment-analysis): represented under its first-listed anchor only, per the
precedent set in `ledger-04.yaml` for `arbitrage-and-market-completeness`. The
`ifoa-cb2-core-reading-2026` id is reused across five of this batch's nodes and
`assa-f207-study-material-2026` across three; both notes list every needed section explicitly
so they merge without ambiguity.
