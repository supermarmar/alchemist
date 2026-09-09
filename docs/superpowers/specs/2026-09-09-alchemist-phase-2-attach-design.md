# Alchemist Phase 2 Attach: design

**Status:** design, awaiting review
**Date:** 9 September 2026
**Supersedes:** nothing. Expands section 9's Phase 2 row of
`docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md`, which gives the phase one
table row and leaves its mechanics undesigned.
**Precondition:** PR #4 (`feat/phase-1-close-out`) merged, and the four execution rulings
recorded in `notes/phase-1-close-out-report-2026-09.md` confirmed. Mario confirmed all four on
9 September 2026, together with the D5 and D7 positional reading, so the corpus is settled at
1,560 nodes.

## 1. What Phase 2 changes

Phase 2 attaches the corpus to the vault. For every node it finds the vault wiki articles that
cover the node's subject and records their slugs in `vault_articles`, and where the vault holds
nothing it records the document that would close the gap in `sources/wanted.yaml`. The phase
writes no prose, so a node's `status` stays `stub` throughout and Phase 3 remains the first
phase that puts words on a page.

The phase exists as its own step because attachment and drafting fail differently. A wrong
attachment is a citation corrected in place, whereas a page drafted from the wrong article is a
page rewritten. Consequently the cheap check runs first, and the gate below is what makes it
cheap.

## 2. The measured starting position

Every figure here was measured against the tree at `c215e12` on 9 September 2026 rather than
carried forward from an earlier note.

All 1,560 nodes carry `vault_articles: []`, so Phase 2 covers the whole corpus rather than a
remainder. The `guides` field that section 9 describes as a hint source does not exist on any
node, so the hint step in that row has nothing to read and drops out.

The vault wiki holds 477 articles. They sit 247 in `regulation`, 150 in `methods`, 52 in
`concepts`, 24 in `ai-agents`, 2 in `synthesis`, and 2 in `entities`. The corpus, by contrast,
is largest in the domains the vault covers least:

| Corpus domain | Nodes | Vault position |
|---|---:|---|
| `fin-man` | 450 | Thin. Banking and financial management is not the vault's subject. |
| `stats` | 373 | Partial. `methods/` covers the credit-modelling subset well and CS1 barely. |
| `regulation` | 327 | Strong. The vault's largest section by some distance. |
| `fin-eng` | 285 | Thin. |
| `credit` | 258 | Strong. The vault's original purpose. |
| `life` | 206 | Very thin. |
| `actuarial` | 177 | Very thin. |
| `eco` | 144 | Very thin. |
| `maths` | 120 | Absent in practice. |
| `gi` | 115 | Very thin. |
| `ml` | 66 | Partial, through `methods/` and `ai-agents/`. |
| `data-eng` | 38 | Partial, through the engineering articles. |

Therefore most nodes will come back uncovered, and the phase has to stay useful when they do.
The gap ledger is what carries them, and section 8 measures how large it can grow.

The confidentiality position is clean. Of the 477 articles, 434 are `public-free` and 9 are
`public-paid`, none carries a non-empty `client_scope`, and 34 carry no `confidentiality` field
at all. Those 34 are the AI and software-engineering material, which the corpus has little call
for. Hence no client-confidential article sits in the wiki, and attaching a vault slug to a
record in this public repo raises no client-isolation question.

The ledger currently holds four entries, seeded by Phase 1.

## 3. Decisions taken

Four choices were settled with Mario on 9 September 2026 before this document was written.

**D2.1 Sweep all 1,560 nodes, and keep the ledger per document.** Every node is searched. An
uncovered node does not spawn its own ledger entry, because `sources/wanted.yaml` is already one
entry per document carrying a `needed_by` list of node ids, so the uncovered nodes collapse into
the documents that would cover them.

**D2.2 The cover bar is "enough to write the page from".** An article attaches to a node only
where it treats that node's subject directly enough that a Phase 3 writer could draft the page
from it, meaning the article is about that thing or gives it a substantive section. A passing
mention does not attach. A regulatory article that genuinely treats fifteen nodes attaches to
all fifteen, and one that merely touches them attaches to none.

**D2.3 Candidates come from a generated index, read once per agent.** A build step reads the
frontmatter of all 477 articles and emits an index of slug, title, type, topics, and
confidentiality. Each agent reads that index once and then opens only the articles it wants to
test. The `topics` list is what makes this work: all 477 articles carry it, and it is a far
better matching signal than a title alone.

**D2.4 Nodes are written directly, the ledger is staged, and a new check 11 guards the slugs.**
Batches hold disjoint sets of node files, so an agent writes `vault_articles` straight into
frontmatter and no staging directory is needed for nodes. Only `sources/wanted.yaml` is shared,
so only the ledger stages. Check 11 then fails the build on any `vault_articles` slug that does
not resolve to a real wiki file, which removes a fabricated slug mechanically rather than
trusting a reviewer to spot it.

Two further calls were made in the same conversation and are recorded here because a later
reader would otherwise have to infer them.

**`vault_sources` stays empty this phase.** That field means the node quotes primary text, and
no node carries prose until Phase 3. Populating it now would put check 5 to work against
quotations that do not exist.

**The generated index is gitignored rather than committed.** The slugs reach the public repo
anyway through node frontmatter, and check 5's docstring already sanctions that. Committing the
index as well would additionally publish 477 vault article titles and topic lists, which
describes the shape of Gini's research base for no benefit, given the index rebuilds in seconds
from the vault.

## 4. The vault index

`scripts/build_vault_index.py` walks `<vault>/wiki/`, parses each article's frontmatter, and
writes `data/vault-index.yaml`. The vault root comes from `vault_root()` in
`scripts/alchemist/checks.py`, which already reads `ALCHEMIST_VAULT` and falls back to
`~/Documents/Repos/vault`, so the index builder introduces no second way to find the vault.

Each index entry carries the slug, the title, the type, the topics list, and the confidentiality
value. `wiki/README.md` and everything under `wiki/_meta/` are skipped, since neither is an
article.

An article whose frontmatter carries no `confidentiality` field is excluded from the index and
listed in a `skipped` block at its foot, with the reason. Consequently the 34 unclassified
articles cannot be attached to a node by an agent that never sees them, and the exclusion stays
visible rather than silent. Classifying them is a vault chore rather than a Phase 2 one, and it
is logged as G25 below.

No `.gitignore` change is needed for the index, because `/data/` is already ignored whole. The
staging directory does need one: `.gitignore` ignores `.superpowers/` today and says nothing
about `.staging/`, so Phase 2 adds it. Any agent or script that needs the index builds it first.

## 5. Batching and the agent contract

The 1,560 node ids are sorted and sliced into 39 batches of 40, recorded in
`.staging/phase-2/manifest.yaml` as an explicit id list per batch. Slicing a sorted list makes a
rerun reproducible, and naming the ids rather than the slice bounds means a manifest read later
still describes the same work after the corpus changes.

Thirty-nine agents exceed the session's fifteen-agent workflow guideline, so the batches run as
three sequential waves of thirteen. Section 12 records this as an amendment to the parent spec,
whose section 10 states that forty nodes per agent fits inside the cap.

Each agent receives its batch's node ids, the cover-bar rule of D2.2 verbatim, and the path to
the index. It then works one node at a time and does three things. It matches the node against
the index on title and topics to draw up candidates. It opens each candidate article and tests
it against the cover bar, which is why the phase cannot be done from the index alone. It writes
the surviving slugs to `vault_articles` in the node's own file, sorted alphabetically so that a
rerun is byte-identical, and writes nothing else in that file.

The agent also writes two fragments and never touches a shared file. `.staging/phase-2/ledger-
<NN>.yaml` names the documents its uncovered nodes need, each with the node ids that need it,
the claim the document would support, and a proposed `acquisition` and `expected_tier` following
the vocabulary in the ledger's own header comment. `.staging/phase-2/report-<NN>.md` records, per
node, the candidates considered, the ones attached, and one sentence on any rejection, which is
the evidence the gate's spot-reads draw on.

**A ledger fragment names the node's own anchor document by default.** This rule is what bounds
the ledger, so it belongs in the agent contract rather than only in section 8's arithmetic. An
agent proposes a document other than the node's anchor only where the anchor genuinely cannot
cover the node, and then it says why in the report fragment. Thirty-nine agents inventing
document names independently is the unbounded case, and the two existing non-anchor entries in
the seeded ledger show how readily it happens.

An agent that finds nothing for a node leaves `vault_articles: []` and records the node in its
ledger fragment under the document that would cover it. Where no document plausibly would, it
says so in the report fragment and the node reaches the gate as genuinely uncovered.

## 6. The ledger merge

`scripts/merge_ledger.py` reads every fragment, unions them into `sources/wanted.yaml`, and is
the only writer of that file in this phase.

Entries union by document id. Two agents proposing the same document produce one entry whose
`needed_by` is the sorted union of both node lists, and whose remaining fields come from the
first fragment to name them, with any disagreement recorded as a complaint rather than resolved
silently. The four seeded entries are preserved, and a fragment naming one of them extends its
`needed_by` and leaves every other field alone.

A malformed fragment becomes a reported complaint and never a stack trace, following the
precedent `_ledger_entries` sets in `scripts/alchemist/checks.py`, whose docstring records the
three shapes that used to crash. The tool refuses to write at all where any fragment is
malformed, so a partial ledger cannot reach the gate wearing the appearance of a complete one.

The merge step also compares the working-tree diff against the manifest. An agent that modified
a node file outside its own batch is reported and the merge refuses, which catches a stray write
rather than trusting every agent to have stayed inside its assignment.

## 7. Check 11, and what it does not gate

Check 11 is "attached vault articles resolve and are publishable". For every node, each slug in
`vault_articles` has to resolve to a file at `<vault>/wiki/<slug>.md`, and that file's
`confidentiality` has to be `public-free` or `public-paid`. A slug that resolves to nothing is a
fabrication or a stale rename, and either way the corpus should not carry it.

The two failure modes carry distinct messages, because a future debugging session should not
have to guess which one fired. A slug resolving to no file reports that it does not resolve,
naming the path it looked for, whereas a slug whose article carries no `confidentiality` field
reports exactly that. The second fires where an article loses its classification in the vault
after attachment, which is correct behaviour and reads as a reclassification rather than a
rename.

`public-paid` passes deliberately. Check 5's docstring already states the rule: purchased
material can inform a node through `vault_articles`, because the article stays in the private
vault and the node's own prose is original, whereas `vault_sources` means the node quotes the
primary text and there `public-paid` needs a waiver. Check 11 therefore guards resolution and
classification, and check 5 keeps guarding quotation.

**Check 11 cannot gate CI, and the spec says so plainly rather than implying otherwise.** It
follows check 5's pattern and sets `result.skipped` when no vault sits at `vault_root()`. GitHub
Actions has no vault, so the deploy workflow will report check 11 as skipped on every run. The
gate that does bite is the pre-commit hook on a machine with the vault mounted, which is the
machine the attachment was written on. A reader who assumes the build catches a fabricated slug
would be wrong, and this paragraph exists to stop that assumption.

## 8. The gate

Mario reads two artefacts, and both are generated rather than hand-written.

`notes/phase-2-coverage-2026-09.md` reports coverage by domain and by anchor document, the count
of nodes attached against uncovered, the distribution of attachments per node, and the twenty
nodes with the most attachments. The per-anchor-document view is the one that matters for
acquisition, because it turns "1,100 nodes are uncovered" into "these documents would cover
them".

`sources/wanted.yaml` is the acquisition list, and it is Mario's call per section 9 of the parent
spec. Its size is bounded rather than hoped for. The whole corpus points at 59 distinct anchor
documents, led by `assa.f107` on 306 nodes, `assa.f207` on 177, `bcbs.d424` on 143, and
`ifoa.sp6` on 139, and only two nodes carry the literal `chosen`. Since an uncovered node's
ledger entry names the document its own anchor already points at, the ledger caps at roughly 59
entries however many nodes go uncovered. Twenty-two of the 59 are `up.*` Pretoria course codes,
where the acquisition question is hardest, and the coverage report names them explicitly so the
decision is put rather than buried.

## 9. Failure handling and reproducibility

A batch that fails leaves its nodes untouched, because an agent writes a node file only once it
has settled that node's attachments. The manifest names the batch's ids, so the batch re-runs
against the same forty nodes without recomputing the slice.

A rerun of a completed batch is idempotent. The agent recomputes the same candidates from the
same index and writes the same sorted slug list, and the ledger merge unions rather than appends.

Where the vault changes mid-phase, the index goes stale and check 11 catches the consequence: a
renamed article breaks resolution on the nodes that cite it. Rebuilding the index and re-running
the affected batch is the repair, and the coverage report records the index's build timestamp so
the staleness is visible.

## 10. Testing

The three new pieces are test-driven, and each test goes red under its named bug before the fix
lands, which is the discipline `notes/phase-1-close-out-report-2026-09.md` records the Phase 1
fix waves failing at first.

The index builder is tested against a temporary vault root injected through `ALCHEMIST_VAULT`,
covering an article with full frontmatter, one with no `confidentiality` field, one whose
frontmatter does not parse, and the `README.md` and `_meta/` exclusions.

The ledger merge is tested for the union of two fragments naming one document, the preservation
of a seeded entry, a field disagreement becoming a complaint, a malformed fragment blocking the
whole write, and a node written outside its manifest batch being caught.

Check 11 is tested for a resolving `public-free` slug, a resolving `public-paid` slug, a slug
resolving to nothing, a slug whose article has no `confidentiality` field, and the clean skip
when no vault is present.

## 11. Out of scope

Phase 2 does not draft prose, does not set `status: drafted`, does not populate `vault_sources`,
and does not acquire anything. Acquisition is Phase 2a and runs through the vault's own workflow.
Placing the sixteen no-path nodes named in the close-out report is Phase 2 work, and it is out of
scope for this design. Attachment edits node frontmatter whereas placement edits path files, the
two share no tooling, and placement needs its own reasoning about where each node belongs.
Consequently it gets its own design and its own branch, after this one.

## 12. Amendments to the parent spec

Two lines in `docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md` need correcting
when this design is accepted.

Section 10's operational constraint states that forty nodes per agent "fits inside the cap".
Forty nodes per agent across 1,560 nodes is thirty-nine agents against a fifteen-agent
guideline, so the sentence should say that forty nodes per agent runs as three sequential waves
of thirteen.

Section 9's Phase 2 row instructs the phase to "read `guides` once as hints, then drop it". No
node carries a `guides` field, so the instruction should be struck rather than left for a future
reader to hunt for.

`CLAUDE.md` needs one correction in the same wave. Its "The ten checks" section states that
check 5, "measured with `ALCHEMIST_VAULT=/nonexistent`, is the only rule that skips". Check 11
skips on the same condition, so the sentence has to name both, and the section's title and its
count of the rules move from ten to eleven.

## 13. Order of work

The deferred tool chores go first, on their own branch once PR #4 merges, because each is small,
each touches a tool Phase 2 relies on, and bundling them into the Phase 2 branch would put two
concerns in one pull request. They are G23's phrase-level proper-name list for check 10, the
merge tool's three untested refusal arms, and G24's cadence fix on the three new path preambles.

Phase 2 then runs in the order the sections above describe, with one ordering constraint that is
easy to get wrong. The `.staging/` entry in `.gitignore` lands **first**, ahead of the index
builder, because thirteen agents write fragments there and the pre-commit hook runs on every
commit, so a wave starting before that entry exists would dirty the tree. After it come the
index builder and check 11 with their tests, then the manifest, wave one, the ledger merge, waves
two and three, and finally the coverage report. The gate closes the phase.

## 14. Backlog this design adds

- **G25:** Classify the 34 vault wiki articles carrying no `confidentiality` field. A vault
  chore, and until it is done those articles cannot be attached to any node.
- **G26:** Enable GitHub Pages on `supermarmar/alchemist`. Both merges to `main` so far failed
  at the deploy step with `HttpError: Not Found`, while every check and the build passed.
- **G27:** Add a checks workflow triggered on `pull_request`, keeping the deploy on `main`. The
  ten checks and the 218 tests currently gate no pull request, so the pre-commit hook is the
  only gate. Adding `pull_request` to `pages.yml` would be the wrong fix, since it would attempt
  a deploy from a branch.
