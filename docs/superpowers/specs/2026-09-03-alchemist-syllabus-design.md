# Alchemist: design

A comprehensive quantitative syllabus, held as a dependency graph and rendered as a
teaching corpus. Credit risk is the trunk, life and general insurance run alongside it
throughout, and the roots reach down into mathematics, statistics, financial engineering,
data engineering, feature engineering, machine learning, economics, financial management and actuarial science.

- **Status:** approved 3 September 2026, pending implementation plan.
- **Repo:** `~/Documents/Repos/alchemist`, public, published at
  `https://supermarmar.github.io/alchemist/`.
- **Trunk material:** the seventeen credit lectures in
  `~/Documents/Repos/actuarial_deep_learning/credit_lectures/`.

A note on the count. This document said "seventeen credit lectures" throughout, taken from the
sibling repo's `index.html` on 3 September 2026. The KaTeX sweep in Task 10 found eighteen
`.qmd` files that same day, because the sibling repo is under active development and five
lectures landed in it during this session. The count is therefore a moving target and is not
load-bearing anywhere: every script and sweep globs the directory rather than counting it. Read
"seventeen" below as "every credit lecture in the sibling repo at the time of writing".

## 1. Purpose

The corpus has one job: teach this material to somebody else, now and in twenty years,
without the teacher present. Three consequences follow, and they drive every decision below.

A student must be able to walk any concept down to its roots and find something rigorous at
every step, so coverage matters more than depth at the leaves. Notation must mean one thing,
so a reader who learns a symbol in one domain recognises the object when a second domain
spells it differently. And a rendered lecture must open from a bare disk with no network,
because a corpus that depends on a content delivery network staying up is a corpus with an
expiry date.

## 2. Relationship to the existing repos

Three repos already hold relevant material, and each takes exactly one role here.

| Repo                        | Role in Alchemist                                                                                                                                                                                                                                         |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `vault`                   | The sole source of truth for citations. A node cites vault wiki articles, and vault source-register ids where it quotes primary text.                                                                                                                     |
| `actuarial_deep_learning` | Origin of the trunk. Its seventeen credit lectures, its Quarto render chain, its PDF printer, and its stylesheet are**copied** across, never moved. It keeps the ETH authors' material, its own site, and its own scope, and nothing in it changes. |
| `guides`                  | A hint channel, read once during Phase 2 and then dropped. Its 719 lectures and 175 wiki files carry no citation weight in Alchemist, and its Notion-purple stylesheet is retired.                                                                        |

The `guides` repo is not migrated. Where it covers a node, the harvest records what primary
source that coverage was itself built from and writes a gap-ledger entry, so the citation
lands in the vault rather than pointing at a second knowledge base.

## 3. Decisions taken

Six decisions were settled during brainstorming. Each is recorded with its reason, because
re-litigating one later costs more than reading it.

1. **A new repo, with `guides` and `vault` as sources.** Neither existing repo can host the
   corpus: `actuarial_deep_learning` is scoped to one summer school and holds third-party
   material, and `guides` is scoped to the ASSA F107 exam with a divergent presentation
   layer and a style guide that bans LaTeX outside code fences.
2. **Two tiers.** Every node produces a reference page. Trunk nodes and branch junctions
   additionally produce a full lecture. A uniform full-lecture standard, at the observed cost
   per lecture in `actuarial_deep_learning/notes/`, would take years and leave the graph
   unwritten meanwhile.
3. **Notation names objects; symbols are aliases.** Each domain keeps its field-standard
   notation, and the cross-domain bridge table is generated from the alias rows.
4. **Paths are first-class; node ids carry no ordinal.** Ordering lives in path files. The
   ordinal filenames in `guides` (`01-cashflow_models.html` through `07-...`) demonstrate the
   failure this avoids: inserting a prerequisite forces a rename cascade that breaks every
   relative cross-link.
5. **Root depth is externally anchored where a syllabus exists, and chosen where none does.**
   "Comprehensive" needs a stopping rule you can point at. Expected size was 400 to 600 nodes
   at design time and is **1,100 to 1,400** after gate 1, which is recorded under section 9's
   Phase 1 row rather than here. The figure moved because gate 1 settled the anchor-body list
   at 20 documents and the grain at syllabus item level, and the two together are what set the
   count. Nothing else in this document depends on the number.
6. **Vendored KaTeX and self-contained output.** This removes a documented silent failure,
   recorded in `actuarial_deep_learning/CLAUDE.md`: a slow CDN response yields raw TeX in a
   PDF that still exits zero, still carries its `%%EOF` trailer, and is still A4.

## 4. Data model

### 4.1 The node record is the reference page

One file per node at `nodes/<id>.md`. YAML frontmatter carries the machine-readable graph and
the body carries the tier-1 prose, so there is no separate registry to drift out of step. The
graph is derived by scanning frontmatter.

```yaml
---
id: hazard-rate                      # stable slug, never renamed
title: Hazard rate
domains: [stats, life, gi, credit]   # closed vocabulary, see below
status: stub                         # stub | drafted | reviewed
requires: [survival-function, conditional-probability]
spends:                              # the symbols this node uses, declared not parsed
  - {object: obj.hazard, domain: credit}
  - {object: obj.survival, domain: credit}
anchor: [ifoa.cs2.2.1]               # external syllabus reference, or the literal `chosen`
vault_articles: [methods/exponential-dispersion-family-and-glm]
vault_sources: [dl-actuarial-2026-l02-glm]
taught_in: S1_credit-survival-bridge   # null until a lecture covers it
---
```

Field notes, covering the choices that are load-bearing rather than obvious:

- **`id`** is a stable slug and is never renamed. Every cross-reference, path entry, and
  generated link resolves through it.
- **`unlocks` is deliberately absent.** It is derived by inverting every node's `requires`,
  so it cannot drift.
- **A tier field is deliberately absent, for the same reason.** A node is at tier 2 exactly
  when `taught_in` is non-null, so storing the tier as well would let the two disagree.
- **`domains` draws on a closed vocabulary**, fixed as `maths`, `stats`, `ml`, `data-eng`,
  `fin-eng`, `actuarial`, `life`, `gi`, `credit`, `eco`, `fin-man` and `regulation`. The
  vocabulary has to be closed because check 2 below is scoped to a domain, and an open one
  would make it meaningless. `model.py` enforced ten of the twelve until gate 1, omitting `eco`
  and `fin-man`; Phase 1 widens it, because the body list settled at gate 1 carries CB2
  economics and CP1 actuarial practice and neither has anywhere else to sit.
- **`taught_in`** points forward from node to lecture. The lecture never claims nodes, which
  keeps one direction of truth. It takes the **flat** stem, `S1_credit-survival-bridge`, not
  `credit/S1_credit-survival-bridge`: `lectures/` is a flat directory (section 6), check 8
  resolves the value against `lectures/<value>.qmd`, and `site.py` links
  `../../lectures/<value>.html`.
- **`anchor`** records which published syllabus put the node in the corpus. The literal
  `chosen` marks a node whose depth you selected, which is honest about where the stopping
  rule is yours rather than external.
- **`vault_articles`** takes vault wiki slugs. **`vault_sources`** takes vault source-register
  ids and is used only where the node quotes primary text.
- **`spends`** declares each symbol as an object-and-domain pair, and the rendering is looked
  up rather than written out. Declaring it beats parsing it, for the reason given under check 1.
  A useful side effect: a bridge node is exactly one that spends the same object in two
  domains, so the bridge table generates itself from `spends` with no separate field.
- **`anchor` follows a fixed grammar**, `<body>.<subject>.<section>[.<item>]`, lowercase and
  dot-separated: `ifoa.cs2.3.2`, `assa.f107.4.1`, `bcbs.d424.irb.para-220`,
  `ucsc.dl-actuarial-2026.l02`. Phase 1 populates this field across 20 anchor bodies in
  parallel, so the grammar is stated here rather than left to each transcriber to invent.
- **A three-level syllabus spends its third level on the item segment**, hyphenated. The
  grammar allows four dot-separated segments at most, and the IFoA subjects number three deep:
  topic 1, section 1.1, item 1.1.5. Consequently CS2 item 1.1.5 is written `ifoa.cs2.1.1-5`,
  following the precedent `bcbs.d424.irb.para-220` already sets for a composite final segment. The
  alternative, widening `model.py`'s `ANCHOR` pattern to five segments, was considered at gate
  1 and rejected: it reopens a grammar three documents call fixed, for a gain in readability
  alone. Each body's numbering maps into the grammar differently, so **the mapping is fixed per
  body in the Phase 1 plan's anchor table** rather than derived by each transcriber.

### 4.1a How big is a node

A node is **one thing a reader can be examined on separately and that carries its own
prerequisites**, targeting one node per twenty to forty minutes of teaching.

The rule is stated because Phase 1 runs one agent per syllabus document, and a line such as
"CS2 3.2: Cox regression" is one node or six depending on the transcriber. Inconsistent grain
is invisible in a node list read once, and it surfaces only in Phase 3 when some pages come
out at two paragraphs and others are lectures in disguise. Consequently the reconcile step
flags grain outliers for you rather than trusting each agent to have judged alike.

**Gate 1 tied the rule to the syllabus item.** Where a body numbers three levels deep, one
node corresponds to one item, meaning CS2 1.1.5 rather than CS2 1.1, and the coarser
section-level reading was considered and rejected because a section runs to an hour and a half
of teaching. The tie is a default rather than an identity: an item reading "apply the result in
1.2.4 to the reinsurer's share" restates its neighbour and folds into it, and an item naming
three distributions a reader is examined on separately splits. Since the reconcile step
measures grain rather than judging it, the numbers it reports are nodes per body, nodes per
syllabus section, the `requires`-count distribution, and every title carrying "and" or a comma,
which is the reliable tell for two examinable things fused into one node.

### 4.2 Notation contract

One file, `notation/objects.yaml`. It names mathematical objects and hangs the field-standard
renderings off them as aliases.

```yaml
- id: obj.hazard
  name: Hazard rate
  canonical: h(t)
  definition: >
    The instantaneous rate at which the event occurs, conditional on survival to t.
  aliases:
    - domain: life
      symbol: \mu_x
      name: force of mortality
      note: age-indexed and continuous
    - domain: gi
      symbol: \lambda
      name: claim intensity
    - domain: credit
      symbol: h(t)
      name: default hazard
    - domain: stats
      symbol: \lambda(t)
      name: hazard function
```

The collisions this exists to resolve are real, and the seed set covers at least these. Note
what "at least" is doing. The twelve were derived from credit, life and general insurance **as
the ETH course frames them**, which is a modelling frame rather than a reserving one, so the
general-insurance reserving vocabulary (cohort index, development index, development factor,
ultimate) is absent by construction rather than by oversight, and Phase 1 seeds it. Phase 1
also sweeps for other vocabularies the trunk's frame omits, since one such gap implies others.

| Object                   | Canonical            | Life            | General insurance | Credit       | Statistics and ML    |
| ------------------------ | -------------------- | --------------- | ----------------- | ------------ | -------------------- |
| Hazard                   | `h(t)`             | `\mu_x`       | `\lambda`       | `h(t)`     | `\lambda(t)`       |
| Survival function        | `S(t)`             | `{}_tp_x`     |                   | `S(t)`     | `S(t)`             |
| Lifetime distribution    | `F(t)`             | `{}_tq_x`     |                   | `F(t)`     | `F(t)`             |
| Standard normal CDF      | `\Phi(\cdot)`      |                 |                   | `N(\cdot)` | `\Phi(\cdot)`      |
| Standard normal quantile | `\Phi^{-1}(\cdot)` |                 |                   | `G(\cdot)` | `\Phi^{-1}(\cdot)` |
| Asset correlation        | `\rho`             |                 |                   | `R`        | `\rho`             |
| Response mean            | `\mu`              |                 | `\mu`           |              | `\mu = E[Y]`       |
| Dispersion               | `\varphi`          |                 | `\varphi`       |              | `\varphi`          |
| Regularisation weight    | `\lambda`          |                 |                   |              | `\lambda`          |
| Exposure                 | `v`                |                 | `v_i`           | `EAD`      | offset               |
| Discount factor          | `v`                | `v = 1/(1+i)` |                   |              |                      |
| Regression coefficients  | `\beta`            |                 | `\beta`         | `\beta`    | `\theta`           |

Two entries in that table deserve their own note, since they are the cases a single global
symbol table cannot survive. `\lambda` carries three unrelated meanings, and `v` is the
actuarial discount factor in life and the exposure weight in the Wuthrich general-insurance
notation. Neither can be renamed without making the corpus look wrong to a practitioner in
the field it borrows from.

**Settled at gate 1: the regularisation weight keeps its subscript.** `obj.regularisation`
renders as `\lambda_{\mathrm{reg}}` in both `ml` and `stats`, and the paragraph above is
softened to cover `v` alone. The reasoning is that Phase 1 gives `obj.hazard` an `ml` alias,
since deep survival models are machine learning, so a node spending the hazard and the
regularisation weight together in `ml` would otherwise fail check 1 with no remedy available:
the check is node-scoped and both objects would render as bare `\lambda`. Resolving it the
other way would have meant accepting that no `ml` node may ever spend both objects, which is a
real constraint on a corpus whose trunk runs through deep survival modelling.

Two things worth keeping, because they explain why the choice ever read as unmotivated. Check
2 did not force the subscript: `obj.hazard` carried no `ml` alias before Phase 1, so bare
`\lambda` in `ml` would have collided with nothing and passed. And the note in `objects.yaml`
justifying the subscript was one of the three that YAML silently truncated at its first comma,
so what a reader saw was "subscripted deliberately" with the reason missing.

`notation/symbols.md` renders the table for a reader. It is generated by `build_site.py` and
never hand-edited, and it is committed so that it reads on github.com. Check 7 below verifies
it matches `objects.yaml`, which is what stops a committed build artefact drifting.

### 4.3 Paths

One file per path at `paths/<id>.yaml`.

```yaml
id: credit-trunk
title: Credit risk, with life and general insurance alongside
builds_on: [maths-stats-prerequisites]   # path ids whose nodes this path takes as given
preamble: >
  One paragraph on who the path is for and where it lands.
nodes: [conditional-probability, hazard-rate, ..., credibility-transformer]
```

`builds_on` exists because a domain path does not restate its own prerequisites. The life path
assumes the mathematics and statistics path, and without a way to say so, check 4 would fail on
every path in the corpus. A node sits in as many paths as it earns. Expected initial paths are the credit trunk, a life
path, a general-insurance path, a mathematics-and-statistics prerequisite path, and the
braided cross-domain paths, of which survival analysis is the first.

### 4.4 Gap ledger

Two files of one shape, `sources/wanted.yaml` and `sources/to-ingest.yaml`. Each entry
names a source a node needs. It sits in `wanted.yaml` where nobody holds the document yet and
in `to-ingest.yaml` where the vault holds it and no node has drawn on it, and `status` is
what decides: `wanted` and `located` to the first, `in-raw` and `ingested` to the second.

```yaml
- id: ifoa-cm1-core-reading-2026
  needed_by: [compound-interest, level-annuities, equations-of-value]
  claim: >
    The standard actuarial notation for annuity-certain values and the
    equation-of-value formulation.
  document: "IFoA CM1 Core Reading, 2026"
  url: null
  expected_tier: T4
  acquisition: public-download        # public-download | regulator | journal | purchased-personal
  status: wanted                      # wanted | located | in-raw | ingested
```

One file until 14 September 2026, when Phase 2's merge took the ledger to 135 entries and
made the mixture visible: 73 named documents to buy or download, and 62 named documents the
vault had all along. Acquisition and ingest are different jobs, and one file holding both
invited shopping for what the vault held. The split is a reorganisation rather than a
reclassification, since `status` already carried the distinction correctly.

`status` therefore stays on every record rather than being read off the file name, because
the two ingest statuses do not mean the same thing to rule 6: an `ingested` entry is skipped,
and an `in-raw` one blocks its nodes exactly as a `wanted` one does. The required and
optional fields are identical across the two files, so the fragment contract is unchanged and
`wanted.yaml`'s header carries the whole status vocabulary for both.

Every reader takes the pair. `scripts/merge_ledger.py` reads both files, unions them with any
fragments, and partitions by status on write, so the split maintains itself rather than
needing a tool run once: an entry whose document reaches the vault crosses over on the next
merge, and a later fragment proposing a document the ingest file holds extends that entry
rather than writing a second copy under acquisition.

The ledger drains rather than accumulates, because **no node reaches `status: reviewed` while
it carries an open gap.** Acquisition runs through the vault's existing route: into
`vault/raw/`, then `doc-to-markdown`, then `kb-ingest`, under the vault's `curation-workflow`
rule that every file entering `raw/` yields either a wiki article or a recorded exclusion.

`acquisition: purchased-personal` is a last resort, for the F107 study notes and university
summaries on the other laptop. Where the ledger records one, it also records the public
primary source those notes were distilled from, and that primary source is what the node
eventually cites.

## 5. Checks

`scripts/check.py` enforces eleven rules and blocks a commit that breaks any of them. Rules 1
to 4 are the reason the schema is worth carrying, rules 5 and 6 follow from the repo being
public, rule 7 keeps a committed build artefact honest, and rules 8 and 9 keep a forward
reference from going stale.

1. **Declared symbols resolve.** Every `spends` entry resolves to a domain alias in
   `objects.yaml`, and no two **distinct objects** render as the same symbol inside one node.
   One object spending two domains that happen to share a spelling passes, since
   `obj.survival` is `S(t)` in both statistics and credit and that is one meaning rather than
   a collision.
   **There is no fallback to the canonical rendering**, and the absence is deliberate. An
   earlier draft of this rule said a spend resolves to a canonical rendering *or* a domain
   alias; the checker has always raised where the object carries no alias for the domain, and
   the fix wave corrected the spec rather than the code. The stricter rule forces every
   (object, domain) pair a node actually spends into `objects.yaml`, where a reader can see
   the spelling and the note beside it. A silent fallback would instead let a node spend the
   hazard in `ml` and quietly print `h(t)`, which is the credit spelling and looks wrong to
   the field the node is written for. Adding the alias costs one line and is exactly the
   review moment wanted.
   **The checker does not parse node bodies.** Matching alias strings against TeX is not
   reliable, since `\lambda` occurs inside `\lambda(t)`, `v` inside `\varphi`, and every short
   alias inside something longer; a tokeniser would be needed and it would still guess at the
   maths-and-prose boundary. Declaring what a node spends is exact, costs the author one line,
   and is the discipline actually wanted. Whether the body honours the declaration is a review
   responsibility.
2. **Symbol uniqueness within a domain.** No two objects claim the same rendering inside one
   domain.
3. **Referential integrity and acyclicity.** Every `requires` id resolves to a node, and the
   graph is acyclic.
4. **Path teachability.** For every path, each node's prerequisites appear earlier in that
   same path, or anywhere in a path reachable through `builds_on`. This is the check that makes
   a path teachable rather than merely ordered.
5. **Publishable citations.** Every id in `vault_sources` resolves to a vault register entry
   that is `confidentiality: public-free`, or `public-paid` carrying a `publication_waiver`.
   Anything else fails. Purchased material can therefore inform a node through
   `vault_articles` and can never be quoted in it.
6. **Gap closure.** No node carries `status: reviewed` while an open gap-ledger entry lists
   it in `needed_by`. Both ledger files are read, and an id held in both is reported, since
   their two copies then disagree over whether the document still needs acquiring.
7. **Generated artefacts are current.** `notation/symbols.md` matches what `objects.yaml`
   would generate. A committed build artefact needs this, or it drifts silently.
8. **`taught_in` resolves.** Every non-null `taught_in` names a lecture source that exists at
   `lectures/<value>.qmd`. Phase 4 lands lectures one at a time against nodes already
   written, so a node marked taught before its lecture renders publishes a dead link from its
   own page and from every path listing it. Skips where `lectures/` is absent.
9. **Ledger references resolve.** Every id in every `needed_by` in either ledger file
   resolves to a node. Check 6 looks each id up and moves on where it finds nothing, which is
   right for its own rule and useless as a guard, so without rule 9 a single mistyped id
   disables gap enforcement for that node silently and permanently. Reading one file and not
   the other would reopen that same silence for everything the unread file names, so both
   rules skip only where neither file exists.

Rules 8 and 9 were added in the Phase 0 fix wave rather than at design time. Both are about
ten lines, and both close a hole no test could see, which is the class of defect this corpus
is most exposed to at four figures of nodes.

Check 5 reads the vault, which is a separate private repo. Its location comes from
`ALCHEMIST_VAULT`, defaulting to `~/Documents/Repos/vault`. Where no vault is present it
reports skipped rather than failing. Measured with `ALCHEMIST_VAULT=/nonexistent`, checks 5
and 11 are the two rules that skip, since both read the vault: check 6 reads the gap
ledger, which lives in this repo rather than the vault, so somebody who clones
this public repo still runs nine of the eleven. The checks are enforced where it matters,
meaning on your machine and in CI, and they never make the corpus unverifiable for a reader.

## 6. Repo layout

```
alchemist/
├── CLAUDE.md
├── docs/superpowers/specs/        # this file and its successors
├── nodes/<id>.md                 # frontmatter graph + tier-1 page
├── paths/<id>.yaml               # ordered node ids + preamble
├── notation/
│   ├── objects.yaml              # canonical objects + per-domain aliases
│   └── symbols.md                # generated, never hand-edited
├── sources/wanted.yaml           # the gap ledger: documents to acquire
├── sources/to-ingest.yaml        # the gap ledger: documents the vault holds
├── lectures/<ID>_<slug>.qmd      # flat; the ID prefix already encodes the track
├── lectures/figures/<stem>/
├── notes/                        # per-lecture structure notes and citation registers
├── scripts/
│   ├── check.py                  # the eleven checks above
│   ├── build_site.py             # index, path pages, graph SVGs
│   ├── render_lecture.sh         # Quarto wrapper, vendored KaTeX
│   ├── html_to_pdf.sh            # headless Chrome printer
│   ├── inline_assets.py          # post-render, makes one self-contained file
│   └── convert_credit_data.py    # converts the downloaded CSV to parquet
├── vendor/katex/                 # committed js, css, fonts
├── assets/lecture.css            # one stylesheet, carried from the trunk repo
├── data/                         # gitignored; public downloads only
└── index.html                    # generated
```

Track prefixes carry over from `actuarial_deep_learning/credit_lectures/`, so the existing
`S`, `R`, `C`, `D`, and `F` tracks keep their meaning and the numbered `01` to `12` sequence
keeps mirroring the ETH course. The directory stays flat, because the prefix already encodes
the track and sorts on it, whereas a per-track subdirectory would deepen every relative path to
`assets/` and `data/` for no gain. The trunk repo holds seventeen lectures flat today.

## 7. Build pipeline

**Tier 1.** `check.py` gates, then `build_site.py` generates `index.html`, one page per path,
and a static SVG dependency view per domain through graphviz. The graph therefore prints, and
needs no JavaScript.

The stylesheet needs no font work, which is worth recording because the obvious assumption is
wrong. `actuarial_deep_learning/lectures/lecture.css` resolves its three families to system
stacks (`'Iowan Old Style', Palatino` and the rest), carries no `@font-face` and no `@import`,
and never reaches `fonts.googleapis.com`. Consequently the sheet has no network dependency to
remove, and the corpus needs no embedded typeface. The `guides` stylesheet does load a web
font, and it is the one being retired.

**Tier 2.** The chain from `actuarial_deep_learning` carries across with one change.
`render_lecture.sh` calls Quarto with `html-math-method: katex` pointed at `vendor/katex/`,
then `scripts/inline_assets.py` inlines the stylesheet and the KaTeX pair, then
`html_to_pdf.sh` prints through headless Chrome.

Quarto's own `embed-resources: true` is deliberately **not** used, despite being the obvious
route to a single file. It inlines Quarto's theme assets too, and `render_lecture.sh` removes
those by matching `<link>` and `<script>` tags that point into `_files/libs/`, so inlining
defeats the strip the stylesheet depends on. Rendering with `embed-resources: false`, stripping
as now, and then inlining only our own three assets reaches the same single-file result and
keeps a working script working. Removing the
CDN removes the silent raw-TeX failure, because printing no longer waits on a network
round trip. Grading through `writing-guidelines-grader` stays a precondition for landing a
lecture, and a lecture is unfinished until its PDF sits beside it.

Two traps carried over from the trunk repo's own notes. Chrome writes the PDF and then
declines to exit, and macOS ships no `timeout(1)`, so the script waits for the file to settle
and then terminates the browser itself, checking for a `%%EOF` trailer rather than trusting a
file that merely stopped growing. And generated HTML must never be formatted: `.prettierignore`
covers `lectures/**/*.html`, naming the glob rather than the directory, because Prettier reads
gitignore semantics where excluding a directory stops the walk and a later negation is inert.

**Publishing.** A GitHub Pages workflow with an allow-list step, as in the trunk repo. It
publishes `index.html`, the node and path pages, the graph SVGs, `lectures/**/*.html`, the
PDFs, `lectures/figures/`, and `assets/`. It leaves `notes/`, the grading reports, and the
`.qmd` sources off the site. Note what the allow-list does and does not buy: on a public repo
those files are readable on github.com regardless, so the list shapes the site rather than
protecting anything.

## 8. Licence and confidentiality constraints

The repo is public, so assume anything committed is published the moment it lands.

- Nothing from a Gini engagement enters the repo, and no example borrows a client's
  parameters or figures.
- `data/` is gitignored. Only public datasets are used, and none is committed as a binary.
  The Bondora loan book is a manual public download, and `scripts/convert_credit_data.py`
  converts it into the typed parquet tables the lectures read. The script does not fetch: the
  public-reports page is not a stable direct-download URL, so the download stays a human step
  and only the conversion is automated.
- Purchased material informs and is never quoted, enforced by check 5.
- **The ETH summer-school material is licensed CC BY-NC 4.0.** Reuse, remix, and adaptation
  are permitted for non-commercial purposes only, with attribution and a statement of
  changes. A corpus deriving from it therefore stays non-commercial. Should the corpus ever
  become fee-earning, the ETH-derived nodes need re-sourcing to the peer-reviewed papers
  behind the slides, which is cheap now and awkward at scale.

## 9. Phases and gates

| Phase          | Work                                                                                                                                                                                                                                                                                                                                                                                                              | Output                                                                                       | Gate                                                                        |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| 0. Foundations | Scaffold the repo, seed`notation/objects.yaml`, write `check.py`, carry the render and print scripts across with KaTeX vendored, write `CLAUDE.md`, hand-build one exemplar node page and re-render `S1_credit-survival-bridge`                                                                                                                                                                           | A working pipeline and two exemplars                                                         | You read the schema, the object table, and both exemplars                   |
|                | **The exemplar doubles as the KaTeX compatibility probe.** The existing seventeen lectures were authored against MathJax, and KaTeX supports a strict subset, so a MathJax-only macro or a bare `\begin{align}` anywhere in them is a Phase 0 discovery rather than a Phase 4 surprise. Phase 0 therefore sweeps all seventeen `.qmd` files for unsupported constructs and records what needs rewriting | A compatibility report                                                                       | Read alongside the exemplars                                                |
| 1. Skeleton    | Transcribe 20 published anchor bodies into stub nodes: ASSA F107 and F207, IFoA CS1, CS2, CM1, CM2, CB2, CP1 and SP1, SP2, SP5, SP6, SP7, SP8, SP9, BCBS d424, IFRS 9, the twelve ETH lectures, and the two University of Pretoria programmes recorded in `notes/uni-programme-anchors.md`, which replace the chosen floors for financial engineering, data engineering and the GLM level with real anchors and add a claims-reserving braid. One agent per body writing into a staging directory, then a merge and reconcile step. Staging is what makes a shared node work: CS2 and F107 both produce `survival-function`, and an agent writing straight into `nodes/` would clobber the other's record and drop its anchor silently | 1,100 to 1,400 stub nodes with `requires` and `anchor` populated, ten path files, four further notation objects, a seeded gap ledger, and a single generated review document | You read the review document once, rather than a thousand files. Cheapest moment to fix a mistake |
| 2. Attach      | Per node, find covering vault articles and record them; where the vault has nothing, write a gap-ledger entry naming the primary source.                                                                                                                                                                                                                                                                        | A populated graph and a gap ledger                                                           | You read the gap ledger, since acquisition is your call                     |
| 2a. Sourcing   | Acquire the ledger's sources, into`vault/raw/`, then `doc-to-markdown` and `kb-ingest`                                                                                                                                                                                                                                                                                                                      | Vault articles for the gaps                                                                  | Per the vault's own workflow                                                |
| 3. Pages       | One agent per batch of nodes writes tier-1 pages against the locked template, with`check.py` as a hard gate                                                                                                                                                                                                                                                                                                     | Every node carrying a written page body rather than a stub                                   | You spot-read for voice; the checker owns structure                         |
| 4. Lectures    | The existing per-lecture discipline, one at a time, starting with the survival braid across life, general insurance, and credit, extending`S1` through `S3`                                                                                                                                                                                                                                                   | Lectures on the trunk and the junctions                                                      | Every lecture, as now                                                       |

Phase 1 exists as a distinct phase because a wrong skeleton is cheap to fix while it is a
thousand lines of records and ruinous once a thousand files hang off it. Separating it from
Phase 2 keeps the two failure modes apart: a wrong node is a schema edit, and a wrong
attachment is a citation corrected in place.

Gate 2 is the phase's whole justification, so it has to be a gate a reader can actually pass
through. A thousand markdown files cannot be read once, which is why the output above names a
generated review document: nodes grouped by path, one line each carrying id, title, domains,
`requires` count and anchor, with the grain distributions and the merge report at its head and
every node belonging to no path listed at its foot. Note what `check.py` contributes here and
what it does not. It verifies referential integrity, acyclicity, path teachability and symbol
resolution, and it verifies nothing about whether an anchor points at a section that exists in
the document it names, whether grain is consistent across bodies, or whether `requires` is
pedagogically ordered rather than merely acyclic. Those three are what the review document and
the reconcile numbers exist to put in front of you.

## 10. Model routing

Per `~/.claude/CLAUDE.md`, planning runs on Opus and implementation on Sonnet.

| Phase                        | Model                                               | Reason                                                              |
| ---------------------------- | --------------------------------------------------- | ------------------------------------------------------------------- |
| Spec and implementation plan | Opus                                                | Planning                                                            |
| 0. Foundations               | Sonnet                                              | Implementation, with judgement                                      |
| 1. Skeleton                  | Sonnet, Haiku for document reads                    | Transcription needs granularity judgement                           |
| 2. Attach                    | Sonnet deciding, Haiku searching the vault          | Retrieval with a fixed schema                                       |
| 3. Pages                     | To be measured                                      | The only phase with the volume for a per-token difference to matter |
| 4. Lectures                  | Opus for the structure note, Sonnet for the`.qmd` | Highest quality per file                                            |

**The Phase 3 model is decided by measurement rather than by preference.** Write ten nodes
from the survival braid with Fable 5.1 and ten with Sonnet, grade all twenty through
`writing-guidelines-grader`, and pick on the grades.

One operational constraint. The session workflow-size guideline is medium, capping a workflow
at fifteen agents, while Phases 2 and 3 cover hundreds of nodes. Batch roughly forty nodes per
agent, which is better practice anyway, since an agent that reads the notation contract once
should spend it on more than one node. Forty per agent does not fit inside the cap in one go:
Phase 2's 1,560 nodes come to thirty-nine agents, so the batches run as three sequential waves
of thirteen. Phase 3 will need the same arithmetic.

## 11. Out of scope

Deliberately excluded, so that a later "while we are here" has to argue for itself.

- No migration of the 719 `guides` lectures. They are a hint channel and then retired.
- No interactive graph explorer. The static SVG per domain is the graph view. An interactive
  one is a separate request, and it would need JavaScript.
- No exercise sets, flashcard decks, or slide renders. A third tier was considered and
  rejected during brainstorming.
- No change to `actuarial_deep_learning`. It keeps its seventeen lectures, its site, and its
  scope. Alchemist re-renders copies rather than moving originals.
- No new tests directory. Correctness here is `check.py` plus a lecture that renders.
