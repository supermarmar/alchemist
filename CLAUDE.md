# Alchemist

## Project overview

Alchemist is a comprehensive quantitative syllabus, held as a dependency graph and rendered
as a teaching corpus. Credit risk is the trunk, life and general insurance run alongside it
throughout, and the roots reach down into mathematics, statistics, financial engineering,
data engineering, feature engineering, machine learning, economics, financial management and
actuarial science. The corpus has one job, stated in full in section 1 of the spec: teach
this material to somebody else, now and in twenty years, without the teacher present. That
single sentence drives every schema decision below, so read it before touching a check or a
generator.

This is a **personal teaching project, not a Gini deliverable**. Consequently several Gini
engineering conventions are relaxed, and the relaxations are stated below rather than left to
inference, following the pattern set in `../actuarial_deep_learning/CLAUDE.md`.

The repo lives at `~/Documents/Repos/alchemist`, is public, and publishes to
`https://supermarmar.github.io/alchemist/`. Its trunk material is copied, never moved, from
the seventeen credit lectures in `~/Documents/Repos/actuarial_deep_learning/credit_lectures/`.

## The two tiers

Every node produces a reference page: a markdown file at `nodes/<id>.md` whose YAML
frontmatter is the graph and whose body is the tier-1 prose. Trunk nodes and branch
junctions additionally produce a full lecture, rendered from a Quarto `.qmd` source through
the chain described under Build commands below. A node is at tier 2 exactly when its
`taught_in` field is non-null; there is no separate tier field to let the two disagree.

A uniform full-lecture standard for the 1,500-odd nodes the corpus holds would take
years and leave the graph unwritten meanwhile, which is why the second tier exists only where
a node is either on the trunk or the point two branches meet.

## Schemas: read the spec, not this file

The node record, the notation contract, the path file and the gap ledger are specified in
full, with worked examples, in
`docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md`, sections 4.1 to 4.4. That
document is the source of truth for field names, types and the reasoning behind each one
(why `unlocks` is derived rather than stored, why there is no tier field, why paths are
first-class and node ids carry no ordinal). Restating it here would only give it a second
place to drift out of step; read it there.

## Closed domain vocabulary

`domains` draws on a closed vocabulary, because check 2 is scoped to a single domain and an
open vocabulary would make that check meaningless. The list enforced by
`scripts/alchemist/model.py`'s `DOMAINS` constant is:

`maths`, `stats`, `ml`, `data-eng`, `fin-eng`, `actuarial`, `life`, `gi`, `credit`,
`regulation`, `eco`, `fin-man`.

It carried ten until Phase 1 Task 2, which added `eco` and `fin-man` and so closed the
divergence from spec section 4.1, which has listed twelve since design time. Adding a domain
means updating `DOMAINS` and this list together, in the same commit.

## Anchor grammar

`anchor` records which published syllabus put a node in the corpus, or the literal `chosen`
where the depth was your own call. Every anchor other than `chosen` follows a fixed grammar,
enforced by `model.py`'s `ANCHOR` pattern:

```
<body>.<subject>.<section>[.<item>]
```

lowercase and dot-separated, three or four segments: `ifoa.cs2.3.2`, `assa.f107.4.1`,
`bcbs.d424.irb.para-220`, `ucsc.dl-actuarial-2026.l02`. Phase 1 populates this field across 20
anchor bodies in parallel, so the grammar is stated here rather than left to each transcriber
to invent.

A body numbering three levels deep hyphenates its third level into the item segment, because
the grammar allows four segments at most: CS2 item 1.1.5 is `ifoa.cs2.1.1-5`, following the
precedent `bcbs.d424.irb.para-220` sets for a composite final segment. Each body maps into the
grammar differently, and the per-body table is in `notes/transcription-brief.md`.

## Title casing

Titles are sentence case: a capital on the first word, on proper names, and on a body's own
defined term where the term is the node (Capital Requirements Regulation). Check 10 enforces
it against two lists in `checks.py`:
`PROPER_NAMES` for single words that are names in their own right, and `PROPER_PHRASES` for a
defined term of several words, which is masked as a phrase so that its words are not admitted
anywhere else. A genuine name the lists lack is added to whichever fits, and a source's title
case is corrected in the record. Ruled at gate 2 (D4); the phrase list is G23.

## The eleven checks

`scripts/check.py` enforces eleven rules over the whole corpus and exits non-zero on any
failure, and **it runs on every commit** through `.githooks/pre-commit`, which each clone
wires up once with `git config core.hooksPath .githooks`. That command is not committed,
because `core.hooksPath` lives in `.git/config`; the README's clone recipe carries it. The
rules, in the order `check.py` reports them, are: declared symbols resolve; symbol uniqueness
within a domain; referential integrity and acyclicity of `requires`; path teachability across
`builds_on`; publishable citations in `vault_sources`; gap closure against
`sources/wanted.yaml`; generated-artefact currency for `notation/symbols.md`; every non-null
`taught_in` naming a lecture source at `lectures/<value>.qmd`; and every `needed_by` id in
the gap ledger resolving to a node. Rule 10, added at gate 2, is that every title is sentence
case. Rule 11, added for Phase 2, is that every attached vault article resolves to a real
wiki file and is public-free or public-paid. The first seven are argued for in spec section 5,
including why the checker declares rather than parses a node's spent symbols. Rules 8 and 9
arrived in the Phase 0 fix wave, each closing a hole no test could see: a node marked taught
before its lecture renders publishes a dead link, and a mistyped `needed_by` id disables
check 6 for that node silently and permanently.

Check 5 reads the vault, a separate **private** repository, at the path in `ALCHEMIST_VAULT`
or `~/Documents/Repos/vault` by default, and reports **skipped** rather than failing where no
vault is present. Measured with `ALCHEMIST_VAULT=/nonexistent`, checks 5 and 11 are the two
rules that skip, since both read the vault: check 6 reads `sources/wanted.yaml`, which lives
in this repo rather than the vault, so a clone with no vault still gets nine of the eleven
and the hook still protects it. See the README for what that means for a stranger cloning the
repo.

The hook validates the **working tree** rather than the index, so a broken node staged and
then fixed in the worktree commits clean, and a good node staged and then broken does not. A
`git stash`-based fix is deliberately not attempted, because Phase 1 runs agents that stage
subsets of their work and a stash inside a hook is its own hazard.

## Build commands

```bash
.venv/bin/python scripts/check.py                          # the eleven checks
.venv/bin/python scripts/build_site.py                      # index, path pages, node pages, graph SVGs
bash scripts/render_lecture.sh lectures/<id>.qmd            # Quarto, KaTeX vendored, no CDN
bash scripts/html_to_pdf.sh lectures/<id>.html              # headless Chrome, watchdog, %%EOF check
.venv/bin/python -m pytest                                  # the test suite
```

Python is always `.venv/bin/python`, never a system `python3`. A lecture is unfinished until
its PDF sits beside its HTML: rendering is two steps because printing is downstream of
rendering by one, and re-rendering after an edit means running both again in order.

`build_site.py` shells out to graphviz's `dot` for the per-domain graph SVGs. Install it with
`brew install graphviz` if `site.py` raises complaining that it is not on `PATH`.

## Public-repo rules

The repo is public, so assume anything committed is published the moment it lands.

- Nothing from a Gini engagement enters this repo: no client parameters, no client figures,
  no purchased material quoted (`vault_sources` enforces the last of these at check 5).
- `data/` is gitignored. Only public datasets are used, and none is committed as a binary.
  The Bondora loan book is a manual download from
  <https://www.bondora.com/en/public-reports>, which `scripts/convert_credit_data.py` then
  converts into the typed parquet tables the lectures read. The script fetches nothing, which
  is why it is named for what it does.
- **The Università Cattolica summer-school material this corpus derives from is licensed CC BY-NC 4.0.**
  Reuse, remix and adaptation are permitted for non-commercial purposes only, with
  attribution and a statement of changes, both carried in the README. The corpus therefore
  stays non-commercial; should it ever become fee-earning, the summer-school-derived nodes need
  re-sourcing to the peer-reviewed papers behind the slides.
- No em dashes or en dashes as punctuation, and British English throughout, in every file
  including this one, `README.md`, node bodies and commit messages.
- **Write currency with the unit word, never a bare dollar sign**, in a node body and in a
  `.qmd` alike: "between 1 million and 2 million euro", not "between $1m & $2m". Every `$` on
  the page is a maths delimiter. A line carrying two amounts extracts the text between them
  as a maths span, and an `&` sitting there is a KaTeX error, so the page publishes red error
  text and the sweep fails on prose that was never mathematics. The rule lives here rather
  than in `scripts/katex_sweep.py` because a Phase 3 agent writing node prose will never open
  that file.

## Shared team standards

The general Gini standards live in `~/.claude/rules/`. `git-conventions.md` (Conventional
Commits, branch naming, PR rules) and `google-dev-style.md` (docstring and CLI-help register)
apply here unchanged. `coding-standards.md` and `testing.md` apply with the specific
relaxations named below.

## What is suspended here, and why

The Gini standards in `~/.claude/rules/` and `~/.claude/CLAUDE.md` assume a client
engagement or a production codebase. In this repo:

- **Workspace routing does not apply.** There is no OneDrive, Notion or DocuSign leg: every
  artefact here is code, markdown or generated HTML, and all of it lives in this GitHub repo.
- **Client isolation does not apply.** There is no client. The vault dependency (check 5)
  exists to keep purchased and confidential material out of a public repo, which is the same
  goal client isolation serves, reached by a different mechanism.
- **No Notion Issue/Feature Log.** Work is tracked in `docs/superpowers/plans/` and
  `docs/superpowers/specs/`, which double as the issue log for a project with one author and
  no client stakeholder to report status to.
- **`coding-standards.md`'s one-public-function-per-file convention is suspended** for
  `scripts/alchemist/`. The package is split by concern (`model.py` for typed records and
  loaders, `checks.py` for the eleven rules, `site.py` for every generated artefact) rather
  than by function, because the dataclasses and the loaders that fill them are tightly
  coupled and splitting them further would fragment rather than clarify. Type annotations are
  **not** suspended and are present throughout.
- **`coding-standards.md`'s Google-style Args/Returns/Raises docstrings are relaxed to
  prose.** A docstring here states why a function exists or what trap it avoids, since the
  type signature already carries the what. `check_generated_current`'s one-line docstring,
  "A committed build artefact drifts unless something checks it," is the pattern to follow.
- **`testing.md`'s mirrored source-and-test tree is relaxed.** `tests/` holds one module per
  checks group plus `test_model.py`, `test_site.py`, `test_cli.py` and the others, rather than
  a `tests/scripts/alchemist/test_checks.py`-shaped mirror, because the checks are one
  cohesive rule set best tested together. Everything else in `testing.md` stands: the suite
  passes, network-touching tests (`tests/test_render_chain.py`) skip cleanly where Quarto or
  Chrome is absent rather than failing, and nothing here makes a network call.
- **`~/.claude/rules/html-design.md` is suspended for `assets/lecture.css`**, which
  deliberately departs into a warm-paper, oxblood-accent reading register in the Tufte style,
  chosen for long-form study rather than for client delivery. The deviation is stated a
  second time at the sheet's own head, in the comment above its token block, so a reader who
  opens the CSS directly still finds the reason without coming back here.

Everything else in `~/.claude/rules/` and `~/.claude/CLAUDE.md` stands, British English and
the dash ban above all.
