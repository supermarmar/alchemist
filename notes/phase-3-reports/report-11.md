# Batch 11 report

Nodes written: 21
Nodes written from articles: 3
Nodes written without: 18
Nodes not landed: 19

## Entries

### securitisation
- Sources: regulation/bcbs-securitisation-framework, regulation/uk-securitisation-regulation
- Spends: none
- Collision candidates: none
- Split candidates: none

### share-capital-issuance
- Sources: stub and anchor only
- Spends: none
- Collision candidates: none
- Split candidates: none

### shortfall-probability
- Sources: stub and anchor only
- Spends: none
- Collision candidates: none
- Split candidates: none

### standardisation
- Sources: stub and anchor only
- Spends: none (mean/sd notation kept apart from obj.response-mean's mu, which would mislead)
- Collision candidates: none
- Split candidates: none

### stationary-time-series
- Sources: stub and anchor only
- Spends: none. Used m for the process mean rather than mu, since objects.yaml's mu (obj.response-mean, stats domain) names the GLM response mean, a different object; a same-domain symbol collision, not the cross-domain kind the spend protocol anticipates
- Collision candidates: a distinct process-mean object may be worth registering if the time-series branch keeps needing mu
- Split candidates: none

### stock-market-indices
- Sources: stub and anchor only
- Spends: none
- Collision candidates: none
- Split candidates: none

### structural-credit-model
- Sources: methods/structural-credit-risk-models
- Spends: obj.normal-cdf:credit
- Collision candidates: none
- Split candidates: none

### supervised-learning
- Sources: stub and anchor only
- Spends: obj.response-mean:ml
- Collision candidates: none
- Split candidates: none

### surplus-process
- Sources: stub and anchor only
- Spends: obj.hazard:gi (lambda as the claim intensity of the Poisson counting process)
- Collision candidates: none
- Split candidates: none

### survival-model
- Sources: stub and anchor only
- Spends: obj.survival:stats (S_0(x) is the same object as S(t) with age in place of duration; life's tp_x alias is a different, conditional quantity so not spent)
- Collision candidates: none
- Split candidates: none

### tail-risk-management
- Sources: stub and anchor only
- Spends: none
- Collision candidates: none
- Split candidates: none

### taxation-of-companies
- Sources: stub and anchor only
- Spends: none
- Collision candidates: none
- Split candidates: none

### theory-of-finance
- Sources: stub and anchor only
- Spends: none
- Collision candidates: none
- Split candidates: none

### time-series-operator-notation
- Sources: stub and anchor only
- Spends: none
- Collision candidates: none
- Split candidates: none

### time-value-of-money
- Sources: stub and anchor only
- Spends: obj.discount-factor:actuarial, obj.discount-factor:fin-eng
- Collision candidates: none
- Split candidates: none

### total-return-swap
- Sources: stub and anchor only
- Spends: none
- Collision candidates: none
- Split candidates: none

### tracking-error
- Sources: stub and anchor only
- Spends: none
- Collision candidates: none
- Split candidates: none

### trading-income
- Sources: stub and anchor only
- Spends: none
- Collision candidates: none
- Split candidates: none

### transaction-costs
- Sources: concepts/effective-interest-rate
- Spends: none
- Collision candidates: none
- Split candidates: none

### unemployment-causes-and-costs
- Sources: stub and anchor only
- Spends: none
- Collision candidates: none
- Split candidates: none

### utility-function
- Sources: stub and anchor only
- Spends: none
- Collision candidates: none
- Split candidates: none

## Not landed

- solely-payments-of-principal-and-interest-test: qualitative: the SPPI test is a legal classification rule for IFRS 9, with no defining formula of its own
- speculative-and-pure-risk: qualitative: a conceptual distinction between risk types taken on for profit and risk merely mitigated, no formula
- stakeholder-analysis: qualitative: an advisory process for identifying and weighing stakeholders, no formula
- state-health-care-provision-objectives: qualitative: a list of policy aims a State sets for its own provision, no formula
- statistical-modelling-portfolio-management: qualitative: a methodology description (statistical rather than judgemental portfolio management), no single defining formula
- strategic-case-study-analysis: qualitative: an analytical and writing skill applied to a case study, no formula
- strategic-planning-considerations: qualitative: an enumerated list of factors a bank weighs, no formula
- strategic-risk: qualitative: a risk definition (strategy proving unsuited or poorly executed), no formula
- stress-testing: qualitative: a process of assessing performance under a severe scenario, no defining formula distinct from the models it stresses
- stress-testing-regulatory-landscape: qualitative: a comparative description of stress-testing regimes across jurisdictions, no formula
- supra-national-and-national-regulators: qualitative: an institutional and jurisdictional structure, no formula
- surplus-management: qualitative: a decision process over retaining, distributing or otherwise applying surplus, distinct from the surplus process's own formula and with no single measure of its own
- sustainability-risk: qualitative: a risk category description (environmental and social factors reducing portfolio value), no formula
- sustainable-banking-through-cycle: qualitative: a strategic practice of running a bank across the whole cycle; the procyclicality mechanics the vault article describes belong to the capital and provisioning formulae they stress, not to this node itself
- three-lines-of-defence: qualitative: a governance and assurance model allocating responsibilities across three lines, no formula
- trading-and-funding-policy: qualitative: a policy setting boundaries for treasury activity, no formula
- treasury-function-structure: qualitative: an organisational structure and remit description, no formula
- twin-peaks-regulation: qualitative: a regulatory model splitting prudential and conduct supervision, no formula
- underwriting-purposes: qualitative: a statement of why an insurer underwrites, no formula
