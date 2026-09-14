# Phase 2 attach report, batch 11

40 nodes, wave 1. 4 attached, 36 uncovered. Cluster: fin-man banking business (DCF loan
pricing, deposits, liquidity), fin-eng derivatives (SP6/F207), plus scattered maths, stats,
actuarial and eco stub nodes. Consistent with the brief: this is general-banking-business and
pure-technical ground, the vault's weakest, not its strongest.

## Attached

- **definition-of-default** -> `regulation/irb-definition-of-default`,
  `regulation/pra-ss3-24-definition-of-default-2026`. Both treat Article 178 CRR's past-due
  and UTP triggers, the materiality threshold and retail-level application directly and at
  length; this is the vault's strongest ground. Anchor also names bcbs.d424.irb.para-220,
  ucsc.dl-actuarial-2026.l01 and iasb.ifrs9.b5.5-37; represented under the first body
  (assa.f107) per the multi-body rule, all others noted here.
- **demand-deposit-behavioural-modelling** -> `regulation/irrbb-shock-calibration`. Its
  dedicated "Non-maturity deposit treatment and behavioural assumptions" section (deposit
  beta, insured-vs-uninsured stability, the SVB/Signature run-off case) is the node's subject
  almost verbatim. Caveat: the article's regulatory lens is IRRBB (EVE/NII), while the node
  sits in F107's liquidity chapter; the modelling substance is the same, so I attached it, but
  a Phase 3 writer should know the source frames it for rate risk rather than liquidity.
- **derivative-pricing-operational-considerations** -> `concepts/xva-overview`. The whole
  article is the family of costs (FVA funding, ColVA collateral, KVA capital, MVA margin
  funding) layered onto a derivative's theoretical price, which is exactly the node's subject.
- **derivatives-and-hedging-credit-risk** -> `regulation/counterparty-credit-risk-saccr`. Its
  "Proposed changes" section treats CDS-protection substitution and the guarantee/EAD
  mechanics directly, which is the node's "hedges... in credit risk exposure measurement and
  terminology" subject.

## Rejected, with the specific clause

- **defaulted-exposure-standardised-risk-weight**: `regulation/crr-credit-risk-provisions`
  gives one sentence ("100% or 150%... at least 20% of the unsecured exposure amount"),
  sharing its paragraph with Article 128 high-risk items, with no treatment of what a specific
  credit risk adjustment is or of collateral/guarantee netting. `grep -rn "Article 127"`
  across the wiki found nothing fuller. The vault's own raw extraction (markdown/bcbs/d424.md,
  line 1127, paras 90-94) does carry the full black-letter text, so this is a wiki-article
  gap, not an acquisition gap; ledgered accordingly.
- **default-events-cross-border-lending**: `regulation/bcbs-core-principles-banking-supervision`
  CP21 covers "country and transfer risk" supervisory expectations, not how the default
  definition applies to a cross-border obligor.
- **default-events-specialised-lending**: `regulation/eba-specialised-lending-risk-weights` is
  entirely about SSCA slotting-criteria risk weights, not default identification.
- **defining-liquidity, deposit-insurance-regulation, deposit-liquidity-value-factors,
  deposit-pricing-considerations, deposit-taking, deposits-analysis-template,
  deposit-behavioural-tenor**: checked `bcbs-liquidity-risk-framework`, `uk-liquidity-framework`,
  `pra-fscs-management-expenses-levy-limit`, `bcbs-liquidity-coverage-ratio-original`,
  `large-exposures-uk`, `uk-bank-resolution-recapitalisation`. All either assume liquidity as
  a known concept, cover a narrow adjacent administrative topic (the FSCS levy cap, not
  deposit protection itself), or mention deposits/protection in one clause of an unrelated
  article. `deposit-behavioural-tenor` specifically needs liquidity-risk tenor assignment;
  `irrbb-shock-calibration` covers the IRRBB analogue only (see above).
- **derivative-collateral-arrangements**: `uk-margin-requirements-nccd` is three narrow
  consultation proposals (equity-option exemption, AANA threshold timing), not general
  collateral arrangements; `xva-overview`/`funding-valuation-adjustment` price the funding
  cost of collateral but don't treat the legal/operational arrangement itself.
- **derivative-pricing-assumption-breakdown**: `xva-overview`'s one clause on unilateral CVA
  failing in 2007 is a single historical anecdote, not a treatment of when pricing
  assumptions generally break down.
- **derivative-risk-identification-and-management**: `counterparty-credit-risk-saccr` treats
  only the counterparty-credit dimension, not the market/liquidity/credit survey the node
  needs across listed vs exotic OTC instruments.
- **dcf-use-risk-based-pricing**: considered `concepts/economic-value-of-rating-systems`
  (risk-adjusted spread net of losses and capital) at length; rejected because its actual
  thesis is adverse selection from rating discriminatory power, not DCF-model-output pricing.
- **demographic-risk**: `methods/longevity-risk-transfer` is about the risk transfer market
  (bonds, swaps, buy-ins), not demographic risk as a mortality/longevity/lapse ERM category;
  `solvency-ii-scr-standard-formula` names life underwriting risk in one clause only.
- **demand-and-supply-analysis**: `bbb-small-business-finance-markets` and
  `eba-immovable-property-risk-weights` both use "supply and demand" in one clause of an
  unrelated argument, not the price-mechanism theory itself.
- **All other rejections** (dcf-assumption-* x6, dcf-use-lifetime-roe-raroc,
  dcf-use-marginal-pricing, deferred-and-increasing-annuity, deferred-annuity-certain,
  definite-and-indefinite-integrals, density-function, dependent-probabilities-from-forces,
  depreciation-and-reserves, derivative-hedging-applications, derivative-hedging-in-banks,
  derivative-investor-objectives, derivative-market-participants,
  derivative-portfolio-risk-profile-change, derivatives-market-characteristics): targeted
  greps (RAROC/FTP/DCF-model, annuity-certain/multiple-decrement/force of transition,
  definite integral/density function, depreciation/reserves, speculator/arbitrageur/hedger)
  returned nothing, or only passing uses of the term inside an unrelated derivation
  (`vasicek-asset-correlation-estimation`, `credit-valuation-adjustment` for density
  function). Pure maths, actuarial and general fin-eng/fin-man textbook material the vault
  does not reach.

## Ledger

11 fragment entries in `ledger-11.yaml`, covering all 36 uncovered nodes; 10 reuse ids already
minted (`ifoa-cm1-core-reading-2026` seeded, plus `ifoa-sp6-core-reading-2026`,
`assa-f107-study-material-2026`, `assa-f207-study-material-2026`, `up-ias211-course-notes`,
`up-fbs112-course-notes`, `up-wst211-course-notes`, `ifoa-sp9-core-reading-2026`,
`ifoa-cb2-core-reading-2026`, `bcbs-d424-irb-risk-weight-functions`), each with fields copied
verbatim and my own `note` added (each produces an expected non-blocking "note differs" line
in the dry run, since other batches already added their own notes to several of these ids).
One new id, `up-wtw114-course-notes`, for definite-and-indefinite-integrals; the dry run shows
a concurrent batch independently minted the same id for a different WTW114 topic
(differentiation), also expected and non-blocking.

`demand-and-supply-analysis` carries anchors to two bodies (ifoa.cb2 and up.ekn110); ledgered
under ifoa-cb2-core-reading-2026 per the first-body rule, up.ekn110 not separately proposed.

## Validation

`merge_ledger.py --dry-run`: exit 0, "would write 55 entries (4 seeded)", only non-blocking
note-differs disagreements (several pre-existing, one new from a concurrent batch's
up-wtw114-course-notes mint).

`check.py` last line: **1560 nodes, 13 paths, 0 failures**

## Brief notes

Nothing ambiguous or wrong in the brief. The advisor's second-pass catch (reuse
bcbs-d424-irb-risk-weight-functions for defaulted-exposure-standardised-risk-weight rather
than treating it as uncoverable, since the vault's raw d424 extraction does hold para 90) is
worth generalising into the brief: a one-sentence wiki mention is grounds to check the raw
vault extraction before concluding "wanted" is the right status, not just "uncovered".
