# Alchemist: design

A comprehensive quantitative syllabus, held as a dependency graph and rendered as a
teaching corpus. Credit risk is the trunk, life and general insurance run alongside it
throughout, and the roots reach down into mathematics, statistics, financial engineering,
data engineering, feature engineering, machine learning, and actuarial science.

- **Status:** approved 3 September 2026, pending implementation plan.
- **Repo:** `~/Documents/Repos/alchemist`, public, published at
  `https://supermarmar.github.io/alchemist/`.
- **Trunk material:** the seventeen credit lectures in
  `~/Documents/Repos/actuarial_deep_learning/credit_lectures/`.

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

| Repo | Role in Alchemist |
|---|---|
| `vault` | The sole source of truth for citations. A node cites vault wiki articles, and vault source-register ids where it quotes primary text. |
| `actuarial_deep_learning` | Origin of the trunk. Its seventeen credit lectures, its Quarto render chain, its PDF printer, and its stylesheet come across. It keeps the ETH authors' own material and stays as it is. |
| `guides` | A hint channel, read once during Phase 2 and then dropped. Its 719 lectures and 175 wiki files carry no citation weight in Alchemist, and its Notion-purple stylesheet is retired. |

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
   "Comprehensive" needs a stopping rule you can point at. Expected size is 400 to 600 nodes.
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
objects: [obj.hazard, obj.survival]  # notation objects this node may spend
anchor: [ifoa.cs2.2.1]               # external syllabus reference, or the literal `chosen`
vault_articles: [methods/exponential-dispersion-family-and-glm]
vault_sources: [dl-actuarial-2026-l02-glm]
taught_in: credit/S1_credit-survival-bridge   # null until a lecture covers it
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
  `fin-eng`, `actuarial`, `life`, `gi`, `credit`, and `regulation`. The vocabulary has to be
  closed because check 2 below is scoped to a domain, and an open one would make it
  meaningless.
- **`taught_in`** points forward from node to lecture. The lecture never claims nodes, which
  keeps one direction of truth.
- **`anchor`** records which published syllabus put the node in the corpus. The literal
  `chosen` marks a node whose depth you selected, which is honest about where the stopping
  rule is yours rather than external.
- **`vault_articles`** takes vault wiki slugs. **`vault_sources`** takes vault source-register
  ids and is used only where the node quotes primary text.

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

The collisions this exists to resolve are real, and the seed set covers at least these:

| Object | Canonical | Life | General insurance | Credit | Statistics and ML |
|---|---|---|---|---|---|
| Hazard | `h(t)` | `\mu_x` | `\lambda` | `h(t)` | `\lambda(t)` |
| Survival function | `S(t)` | `{}_tp_x` | | `S(t)` | `S(t)` |
| Lifetime distribution | `F(t)` | `{}_tq_x` | | `F(t)` | `F(t)` |
| Standard normal CDF | `\Phi(\cdot)` | | | `N(\cdot)` | `\Phi(\cdot)` |
| Standard normal quantile | `\Phi^{-1}(\cdot)` | | | `G(\cdot)` | `\Phi^{-1}(\cdot)` |
| Asset correlation | `\rho` | | | `R` | `\rho` |
| Response mean | `\mu` | | `\mu` | | `\mu = E[Y]` |
| Dispersion | `\varphi` | | `\varphi` | | `\varphi` |
| Regularisation weight | `\lambda` | | | | `\lambda` |
| Exposure | `v` | | `v_i` | `EAD` | offset |
| Discount factor | `v` | `v = 1/(1+i)` | | | |
| Regression coefficients | `\beta` | | `\beta` | `\beta` | `\theta` |

Two entries in that table deserve their own note, since they are the cases a single global
symbol table cannot survive. `\lambda` carries three unrelated meanings, and `v` is the
actuarial discount factor in life and the exposure weight in the Wuthrich general-insurance
notation. Neither can be renamed without making the corpus look wrong to a practitioner in
the field it borrows from.

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

One file, `sources/wanted.yaml`. Each entry names a source the corpus needs and the vault
does not hold.

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

The ledger drains rather than accumulates, because **no node reaches `status: reviewed` while
it carries an open gap.** Acquisition runs through the vault's existing route: into
`vault/raw/`, then `doc-to-markdown`, then `kb-ingest`, under the vault's `curation-workflow`
rule that every file entering `raw/` yields either a wiki article or a recorded exclusion.

`acquisition: purchased-personal` is a last resort, for the F107 study notes and university
summaries on the other laptop. Where the ledger records one, it also records the public
primary source those notes were distilled from, and that primary source is what the node
eventually cites.

## 5. Checks

`scripts/check.py` enforces seven rules and blocks a commit that breaks any of them. Rules 1
to 4 are the reason the schema is worth carrying, rules 5 and 6 follow from the repo being
public, and rule 7 keeps a committed build artefact honest.

1. **Symbol declaration.** Every symbol appearing in a node's mathematics resolves to the
   canonical rendering or a domain alias of an object listed in that node's `objects`.
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
6. **Gap closure.** No node carries `status: reviewed` while an open `sources/wanted.yaml`
   entry lists it in `needed_by`.
7. **Generated artefacts are current.** `notation/symbols.md` matches what `objects.yaml`
   would generate. A committed build artefact needs this, or it drifts silently.

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
├── sources/wanted.yaml           # the gap ledger
├── lectures/<track>/<ID>_<slug>.qmd
├── lectures/figures/
├── notes/                        # per-lecture structure notes and citation registers
├── scripts/
│   ├── check.py                  # the six checks above
│   ├── build_site.py             # index, path pages, graph SVGs
│   ├── render_lecture.sh         # Quarto wrapper, vendored KaTeX
│   ├── html_to_pdf.sh            # headless Chrome printer
│   └── fetch_*.py                # public data rebuilders
├── vendor/katex/                 # committed js, css, fonts
├── assets/lecture.css            # one stylesheet, carried from the trunk repo
├── data/                         # gitignored; public downloads only
└── index.html                    # generated
```

Track prefixes carry over from `actuarial_deep_learning/credit_lectures/`, so the existing
`S`, `R`, `C`, `D`, and `F` tracks keep their meaning and the numbered `01` to `12` sequence
keeps mirroring the ETH course.

## 7. Build pipeline

**Tier 1.** `check.py` gates, then `build_site.py` generates `index.html`, one page per path,
and a static SVG dependency view per domain through graphviz. The graph therefore prints, and
needs no JavaScript.

The typeface is embedded in `assets/lecture.css` as base64 rather than fetched from
`fonts.googleapis.com`, for the same durability reason as KaTeX. Consequently the stylesheet
carries no network dependency of any kind.

**Tier 2.** The chain from `actuarial_deep_learning` carries across with one change.
`render_lecture.sh` calls Quarto with `html-math-method: katex` pointed at `vendor/katex` and
`embed-resources: true`, then `html_to_pdf.sh` prints through headless Chrome. Removing the
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
- `data/` is gitignored. Only public datasets are used, and each is rebuilt by a script from
  its public URL.
- Purchased material informs and is never quoted, enforced by check 5.
- **The ETH summer-school material is licensed CC BY-NC 4.0.** Reuse, remix, and adaptation
  are permitted for non-commercial purposes only, with attribution and a statement of
  changes. A corpus deriving from it therefore stays non-commercial. Should the corpus ever
  become fee-earning, the ETH-derived nodes need re-sourcing to the peer-reviewed papers
  behind the slides, which is cheap now and awkward at scale.

## 9. Phases and gates

| Phase | Work | Output | Gate |
|---|---|---|---|
| 0. Foundations | Scaffold the repo, seed `notation/objects.yaml`, write `check.py`, carry the render and print scripts across with KaTeX vendored, write `CLAUDE.md`, hand-build one exemplar node page and re-render `S1_credit-survival-bridge` | A working pipeline and two exemplars | You read the schema, the object table, and both exemplars |
| 1. Skeleton | Transcribe published syllabi into stub nodes: ASSA F107, IFoA CM1, CM2, CS1, CS2, SP, the Basel and IFRS structure, the twelve ETH lectures, plus chosen floors for data engineering, feature engineering, and financial engineering. One agent per syllabus document, then a reconcile step | 400 to 600 stub nodes with `requires` and `anchor` populated, plus the initial path files | You read the node list and the paths once. Cheapest moment to fix a mistake |
| 2. Attach | Per node, find covering vault articles and record them; where the vault has nothing, write a gap-ledger entry naming the primary source. Read `guides` once as hints, then drop it | A populated graph and a gap ledger | You read the gap ledger, since acquisition is your call |
| 2a. Sourcing | Acquire the ledger's sources, into `vault/raw/`, then `doc-to-markdown` and `kb-ingest` | Vault articles for the gaps | Per the vault's own workflow |
| 3. Pages | One agent per batch of nodes writes tier-1 pages against the locked template, with `check.py` as a hard gate | Every node carrying a written page body rather than a stub | You spot-read for voice; the checker owns structure |
| 4. Lectures | The existing per-lecture discipline, one at a time, starting with the survival braid across life, general insurance, and credit, extending `S1` through `S3` | Lectures on the trunk and the junctions | Every lecture, as now |

Phase 1 exists as a distinct phase because a wrong skeleton is cheap to fix while it is five
hundred lines of records and ruinous once five hundred files hang off it. Separating it from
Phase 2 keeps the two failure modes apart: a wrong node is a schema edit, and a wrong
attachment is a citation corrected in place.

## 10. Model routing

Per `~/.claude/CLAUDE.md`, planning runs on Opus and implementation on Sonnet.

| Phase | Model | Reason |
|---|---|---|
| Spec and implementation plan | Opus | Planning |
| 0. Foundations | Sonnet | Implementation, with judgement |
| 1. Skeleton | Sonnet, Haiku for document reads | Transcription needs granularity judgement |
| 2. Attach | Sonnet deciding, Haiku searching the vault | Retrieval with a fixed schema |
| 3. Pages | To be measured | The only phase with the volume for a per-token difference to matter |
| 4. Lectures | Opus for the structure note, Sonnet for the `.qmd` | Highest quality per file |

**The Phase 3 model is decided by measurement rather than by preference.** Write ten nodes
from the survival braid with Fable 5.1 and ten with Sonnet, grade all twenty through
`writing-guidelines-grader`, and pick on the grades.

One operational constraint. The session workflow-size guideline is medium, capping a workflow
at fifteen agents, while Phases 2 and 3 cover hundreds of nodes. Batch roughly forty nodes per
agent, which fits inside the cap and is better practice anyway: an agent that reads the
notation contract once should spend it on more than one node.

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
