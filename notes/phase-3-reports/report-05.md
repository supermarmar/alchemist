# Phase 3 batch 05 report

Nodes written: 12
Nodes written from articles: 4
Nodes written without: 8
Nodes not landed: 28

## Nodes

### ensemble-averaging
- Sources: methods/entity-embedding-and-network-ensembling
- Spends: none
- Collision candidates: none
- Split candidates: none

### estimator-properties
- Sources: stub and anchor only
- Spends: none
- Collision candidates: none
- Split candidates: none

### excess-and-retention-limit
- Sources: concepts/reinsurance
- Spends: none
- Collision candidates: none
- Split candidates: none

### exponential-distribution
- Sources: stub and anchor only
- Spends: obj.survival:stats
- Collision candidates: bare lambda for the constant rate sits close to obj.hazard's stats alias lambda(t); recorded as a candidate since the two are algebraically equal here (constant hazard) but objects.yaml has no object for a plain scalar rate outside the hazard function.
- Split candidates: none

### exposure-at-default
- Sources: methods/ifrs9-ead-ccf-modelling
- Spends: obj.exposure:credit
- Collision candidates: none
- Split candidates: none

### filtration
- Sources: stub and anchor only
- Spends: none
- Collision candidates: none
- Split candidates: none

### forward-futures-payoff
- Sources: stub and anchor only
- Spends: none
- Collision candidates: none
- Split candidates: none

### frequency-severity-modelling-banking
- Sources: stub and anchor only
- Spends: none
- Collision candidates: none
- Split candidates: none (no unlocks found; ends on the consequence)

### functions-limits-and-continuity
- Sources: stub and anchor only
- Spends: none
- Collision candidates: none
- Split candidates: none

### funds-transfer-pricing
- Sources: stub and anchor only
- Spends: none
- Collision candidates: none
- Split candidates: none

### global-statistical-unbiasedness
- Sources: concepts/balance-property-and-auto-calibration
- Spends: none
- Collision candidates: none
- Split candidates: none (no unlocks found; ends on the consequence)

### equilibrium-versus-no-arbitrage-interest-rate-models
- Sources: stub and anchor only
- Spends: none
- Collision candidates: none
- Split candidates: none (no unlocks found; ends on the consequence)

## Not landed

- emerging-risks: qualitative: identifying and analysing emerging risk exposure is a professional-practice topic with no defining formula in the standard SP9 treatment.
- employee-benefits-overview: qualitative: a survey of benefit scheme types and providers, with no single object the standard treatment measures by formula.
- enterprise-risk-management-concept: qualitative: defines ERM and its governing terms; a definitional and process topic, not a measured object.
- equity-markets: qualitative: an overview of the equity market, how shares are traded and valued, with no single defining formula for the node's own object.
- esg-risk: qualitative: the vault article (regulation/climate-risk-management) describes a regime of governance expectations and disclosure frameworks, with no formula the standard treatment attaches to ESG risk itself.
- exchange-traded-derivative-counterparty-exposure: qualitative: describes where counterparty exposure comes from once a derivative is cleared, a structural and regulatory description rather than a formula.
- exotic-derivative-risk-management: qualitative: covers risk-management characteristics of exotic contracts in general; no single formula defines the object across the family.
- expense-allowance-and-allocation: qualitative: the types of expense a provider meets and the methods used to allocate them is a process topic, not one measured object.
- expense-risk: qualitative: a risk description (actual expenses exceeding those loaded), with no standard defining formula for the node.
- experience-monitoring-rationale: qualitative: the rationale for tracking experience is a process and professional-practice topic.
- external-environment-analysis: qualitative: a PESTLE-style survey of external factors shaping product design and pricing, with no formula.
- fair-pricing-of-retail-financial-products: qualitative: a regulatory and strategic pressure topic, not a measured object.
- fair-value-accounting: qualitative: the practice of carrying assets and liabilities at market value rests on a valuation hierarchy, not a single formula.
- financial-institution-regulatory-role: qualitative: describes the systemic role of financial institutions; a professional-practice and regulatory topic.
- financial-instruments: qualitative: a classification overview of contract types, not one measured object.
- financial-planning-process: qualitative: the steps of a financial planning process is a process topic.
- financial-sector-functions: qualitative: an overview of what the financial sector does, not a measured object.
- financial-technology-disruption-risk: qualitative: the vault article (regulation/digitalisation-in-finance) is a supervisory survey of competitive and technology risk themes, with no formula.
- foreign-exchange-hedging-instruments: qualitative: a survey of FX hedging instrument types (forwards, swaps); no single formula represents the node's plural scope without narrowing it to one instrument the stub does not privilege.
- foundation-model: uncertain: the stub and vault article (concepts/foundation-models-credit-risk) describe capability following a scaling law in compute, data and parameters, but neither states its functional form, and the published forms in the wider literature differ enough that stating one as this node's standard treatment risks misrepresenting it.
- fraud-analytics: qualitative: the vault article (methods/statistical-fraud-detection) is explicit that analysis yields a suspicion score for investigation rather than a formula-driven verdict; a practice topic by the source's own framing.
- fraud-risk: qualitative: a risk description (deliberate misrepresentation going undetected), with no defining formula.
- futures-and-options: qualitative: a survey of contract types, trading and uses distinct from the payoff formula already owned by forward-futures-payoff; no single formula covers the node's own broader scope.
- gains-from-trade-and-specialisation: qualitative: the stub is a fully narrative statement of comparative advantage at introductory level, with no formula in the standard CB2 treatment.
- general-insurance-accounting: qualitative: the stub frames the node as a principles overview (how reserves and reinsurance are reflected in accounts), not one measured object.
- general-insurance-market: qualitative: a market overview of products and the risks they create for insurers.
- general-insurance-product: qualitative: a survey of product types and the risks they pose, not one measured object.
- globalisation: qualitative: a narrative description of economic integration, with no formula in the standard CB2 treatment.
