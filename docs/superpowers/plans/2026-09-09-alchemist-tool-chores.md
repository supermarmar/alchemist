# Alchemist deferred tool chores implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close the five tool chores Phase 1 deferred, so the merge tool, check 10 and the three
new path preambles are sound before Phase 2 runs agents against them.

**Architecture:** Five independent changes to existing files. Three cover the merge tool
(`scripts/alchemist/merges.py` and `scripts/merge_nodes.py`): two refusal arms that carry no
test, one CLI validation arm that carries no test, and one ordering defect where a note prints
before the refusal that makes it meaningless. The fourth teaches check 10's proper-name list to
hold phrases rather than only words. The fifth varies the cadence of the three path preambles
written at gate 2, which all open on a noun phrase and a colon.

**Tech Stack:** Python 3.14, pytest, PyYAML. Python is always `.venv/bin/python`, never a system
`python3`.

**Spec:** `docs/superpowers/specs/2026-09-09-alchemist-phase-2-attach-design.md`, section 13,
which sequences these ahead of Phase 2 and states why they take their own branch. The residual
defects themselves are recorded in
`.superpowers/sdd/2026-09-08-alchemist-phase-1-close-out/progress.md:115` and as G23 and G24 in
`notes/phase-1-close-out-report-2026-09.md`.

## Global constraints

- **Branch:** `fix/phase-1-tool-chores`, cut from `main` **after PR #4 merges**. Do not start on
  `feat/phase-1-close-out`; that would put two concerns in one pull request.
- **Python is `.venv/bin/python`.** Never a system `python3`.
- **The pre-commit hook runs `check.py` on every commit** and validates the working tree rather
  than the index. Wire it up once per clone with `git config core.hooksPath .githooks`.
- **Never self-merge, never force-push `main` or `develop`, never `--no-verify`.**
- **Conventional Commits**, imperative and lowercase, no trailing period, ending with
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
- **Explicit paths on `git add`.** Never `git add -A` or `git add .`.
- **British English throughout, and no em or en dashes as punctuation**, in code comments, test
  names, prose and commit messages alike.
- **This repo is public.** Nothing from a Gini engagement enters it.
- The suite stands at **218 passed** at `c215e12`. Every task below adds tests, so the count
  rises and never falls.

---

### Task 1: Test the two merge refusal arms that carry none

The `merges.py` guards all work today. Two of their arms have no test, so a regression would
reach Phase 2 unseen. Backfilling coverage of working code cannot follow red-then-green
honestly, therefore each test here is followed by a **mutation check**: break the guard, watch
the test go red, restore the guard. That is what proves the test is load-bearing rather than
merely passing.

**Files:**
- Modify: `tests/test_merges.py` (append; the file ends at the `capsys` test around line 162)
- Read only: `scripts/alchemist/merges.py:32-46` (the `merged_record` blocker) and
  `scripts/alchemist/merges.py:111-116` (the missing-file arm)

**Interfaces:**
- Consumes: `write_node`, `write_path` and the `repo` fixture already defined at the head of
  `tests/test_merges.py`; `merge_pair(root, absorbed_id, survivor_id)` from
  `scripts.alchemist.merges`.
- Produces: nothing later tasks depend on.

- [ ] **Step 1: Write the two failing tests**

Append to `tests/test_merges.py`:

```python
def test_a_drafted_record_is_not_absorbed(repo):
    """The status arm on its own. The taught_in and spends arms have their own
    tests, so this one carries no taught_in and no spends and still refuses."""
    write_node(repo / "nodes", "d", status="drafted")
    with pytest.raises(ValueError, match="carries status"):
        merge_pair(repo, "d", "a")
    assert (repo / "nodes" / "d.md").exists()


def test_a_missing_absorbed_file_names_the_pair(repo):
    """The loop checks the absorbed file first, so its arm is reached only by an
    absorbed id with no file. test_a_missing_survivor_names_the_pair covers the
    other half of the same loop."""
    with pytest.raises(ValueError, match="no such node ghost"):
        merge_pair(repo, "ghost", "a")
```

- [ ] **Step 2: Run them and confirm they pass against the working guards**

Run: `.venv/bin/python -m pytest tests/test_merges.py::test_a_drafted_record_is_not_absorbed tests/test_merges.py::test_a_missing_absorbed_file_names_the_pair -v`

Expected: 2 passed. They pass because the guards work; step 3 proves the tests would catch it if
they stopped working.

- [ ] **Step 3: Mutation check the status arm**

In `scripts/alchemist/merges.py`, temporarily change:

```python
    elif absorbed.status != "stub":
        blocker = "status"
```

to:

```python
    elif False:
        blocker = "status"
```

Run: `.venv/bin/python -m pytest tests/test_merges.py::test_a_drafted_record_is_not_absorbed -v`

Expected: FAIL with `DID NOT RAISE <class 'ValueError'>`. **Then restore the two lines exactly as
they were** and re-run to confirm PASS.

- [ ] **Step 4: Mutation check the missing-absorbed-file arm**

In `scripts/alchemist/merges.py`, temporarily change:

```python
    for missing_id, file in ((absorbed_id, absorbed_file), (survivor_id, survivor_file)):
```

to:

```python
    for missing_id, file in ((survivor_id, survivor_file),):
```

Run: `.venv/bin/python -m pytest tests/test_merges.py::test_a_missing_absorbed_file_names_the_pair -v`

Expected: FAIL. The absorbed file is gone, so `parse_node` raises something other than the
`ValueError` the test matches. **Then restore the line exactly** and re-run to confirm PASS.

- [ ] **Step 5: Run the whole suite**

Run: `.venv/bin/python -m pytest -q`
Expected: 220 passed.

- [ ] **Step 6: Confirm the working tree is clean of the mutations**

Run: `git diff --stat scripts/alchemist/merges.py`
Expected: **no output.** Any output means a mutation from step 3 or 4 was not restored. Restore it
before committing.

- [ ] **Step 7: Commit**

```bash
git add tests/test_merges.py
git commit -m "test(merges): cover the status and missing-absorbed refusal arms

Both guards worked and neither had a test, so a regression would have
reached Phase 2 unseen. Each test was mutation-checked against its own
guard rather than trusted for passing.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 2: Test `merge_nodes.py`'s line validation

The CLI rejects a pairs file whose line does not hold exactly two tokens, and returns exit code
2. That arm has no test. The test must run against a temporary root through `--root`, never
against the real corpus: the Phase 1 review found a sequencer test that would have rewritten
`paths/credit-trunk.yaml` had its guard regressed, and the same trap applies here.

**Files:**
- Modify: `tests/test_cli.py` (append)
- Read only: `scripts/merge_nodes.py:28-37` (the token check)

**Interfaces:**
- Consumes: `scripts/merge_nodes.py`'s `main()` via `subprocess`, with `--pairs` and `--root`.
- Produces: nothing later tasks depend on.

- [ ] **Step 1: Read how the existing CLI tests invoke a script**

Run: `sed -n '1,40p' tests/test_cli.py`

Follow whatever invocation idiom is already there (`subprocess.run` with `sys.executable`, or a
direct `main()` call with patched `sys.argv`). Match it rather than introducing a second style.
The test below uses `subprocess.run`; adapt it if the file does something else.

- [ ] **Step 2: Write the failing test**

Append to `tests/test_cli.py`:

```python
def test_merge_nodes_rejects_a_line_that_is_not_a_pair(tmp_path):
    """Exit 2 and name the line, before any merge runs. The empty root proves
    it: a merge attempt would fail on the missing nodes directory instead."""
    pairs = tmp_path / "merges.txt"
    pairs.write_text("# a comment\n\nalpha beta gamma\n")
    result = subprocess.run(
        [sys.executable, "scripts/merge_nodes.py",
         "--pairs", str(pairs), "--root", str(tmp_path)],
        capture_output=True, text=True, cwd=REPO,
    )
    assert result.returncode == 2
    assert "merges.txt:3: expected 'absorbed survivor'" in result.stderr
    assert "'alpha beta gamma'" in result.stderr


def test_merge_nodes_skips_comments_and_blank_lines(tmp_path):
    """A one-token line is also a failure, and the line number counts the
    comment and the blank that precede it rather than the pairs alone."""
    pairs = tmp_path / "merges.txt"
    pairs.write_text("# header\n\n\nlonely\n")
    result = subprocess.run(
        [sys.executable, "scripts/merge_nodes.py",
         "--pairs", str(pairs), "--root", str(tmp_path)],
        capture_output=True, text=True, cwd=REPO,
    )
    assert result.returncode == 2
    assert "merges.txt:4:" in result.stderr
```

If `tests/test_cli.py` lacks them, add `import subprocess`, `import sys` and a `REPO =
Path(__file__).resolve().parents[1]` constant at the top, matching the file's existing imports.

- [ ] **Step 3: Run them and confirm they pass**

Run: `.venv/bin/python -m pytest tests/test_cli.py -k merge_nodes -v`
Expected: 2 passed.

- [ ] **Step 4: Mutation check the arm**

In `scripts/merge_nodes.py`, temporarily change `if len(tokens) != 2:` to `if False:`.

Run: `.venv/bin/python -m pytest tests/test_cli.py -k merge_nodes -v`
Expected: FAIL on the return code, which becomes 1 or raises rather than 2. **Restore the line
exactly** and re-run to confirm PASS.

- [ ] **Step 5: Confirm the tree is clean and the suite green**

Run: `git diff --stat scripts/merge_nodes.py && .venv/bin/python -m pytest -q`
Expected: no diff output, then 222 passed.

- [ ] **Step 6: Commit**

```bash
git add tests/test_cli.py
git commit -m "test(cli): cover merge_nodes.py line validation against a temp root

The arm returns 2 and names the offending line number, counting comments
and blanks. Both tests run against --root tmp_path so a regression cannot
rewrite the corpus, which is the trap the Phase 1 sequencer test hit.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 3: Print the longer-body note only once the merge is going ahead

This one is a genuine defect rather than missing coverage, so it runs red-then-green properly.
`merge_pair` prints "read both before Phase 3" at `merges.py:119-126` and only then calls
`merged_record`, which is what refuses a drafted or taught record. Consequently a refused merge
still advises the operator to read both bodies, which is advice about a merge that never happens.

**Files:**
- Modify: `scripts/alchemist/merges.py:117-129`
- Modify: `tests/test_merges.py` (append one test)

**Interfaces:**
- Consumes: `merged_record(survivor, absorbed) -> Node` and `render(node) -> str`, both already
  in `scripts/alchemist/merges.py`.
- Produces: `merge_pair`'s behaviour is unchanged on every path that merges. Only the stderr
  ordering on a refused merge changes.

- [ ] **Step 1: Write the failing test**

Append to `tests/test_merges.py`:

```python
def test_a_refused_merge_prints_no_longer_body_note(repo, capsys):
    """The note advises reading both bodies before Phase 3, which is advice
    about a merge that is not going to happen. It printed anyway, because the
    note came before the protected-record check."""
    write_node(repo / "nodes", "long", status="drafted", body="one two three four five")
    write_node(repo / "nodes", "short", body="one")
    with pytest.raises(ValueError, match="carries status"):
        merge_pair(repo, "long", "short")
    assert capsys.readouterr().err == ""
```

- [ ] **Step 2: Run it to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_merges.py::test_a_refused_merge_prints_no_longer_body_note -v`
Expected: FAIL. The assertion on stderr finds `note: long's body (5 words) is longer than short's
(1); read both before Phase 3`.

- [ ] **Step 3: Hoist the merge computation above the note**

In `scripts/alchemist/merges.py`, replace this block:

```python
    a_words, s_words = len(absorbed.body.split()), len(survivor.body.split())
    if a_words > s_words:
        print(
            f"note: {absorbed_id}'s body ({a_words} words) is longer than "
            f"{survivor_id}'s ({s_words}); read both before Phase 3",
            file=sys.stderr,
        )

    touched: list[Path] = []
    survivor_file.write_text(render(merged_record(survivor, absorbed)))
```

with:

```python
    # merged_record refuses a drafted, taught or symbol-spending record, so it
    # runs before the note. The note advises reading both bodies before Phase 3,
    # and that is advice about a merge which is going ahead.
    merged = merged_record(survivor, absorbed)

    a_words, s_words = len(absorbed.body.split()), len(survivor.body.split())
    if a_words > s_words:
        print(
            f"note: {absorbed_id}'s body ({a_words} words) is longer than "
            f"{survivor_id}'s ({s_words}); read both before Phase 3",
            file=sys.stderr,
        )

    touched: list[Path] = []
    survivor_file.write_text(render(merged))
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_merges.py::test_a_refused_merge_prints_no_longer_body_note -v`
Expected: PASS.

- [ ] **Step 5: Confirm the note still prints on a merge that goes ahead**

Run: `.venv/bin/python -m pytest tests/test_merges.py -v`
Expected: all pass, `test_a_longer_absorbed_body_prints_a_note` included. That test is what proves
the hoist did not delete the note outright.

- [ ] **Step 6: Run the whole suite and the checks**

Run: `.venv/bin/python -m pytest -q && .venv/bin/python scripts/check.py`
Expected: 223 passed, then all ten rules ok at `1560 nodes, 13 paths, 0 failures`.

- [ ] **Step 7: Commit**

```bash
git add scripts/alchemist/merges.py tests/test_merges.py
git commit -m "fix(merges): refuse a protected record before advising on its body

The longer-body note printed ahead of merged_record's refusal, so a
refused merge still told the operator to read both bodies before Phase 3.
Hoisting merged_record above the note also removes the nested call in the
write.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 4: Give check 10 a phrase-level proper-name list (G23)

`PROPER_NAMES` at `checks.py:382-389` holds single words, so a defined term of several words has
to admit each word globally. Seventeen of its thirty-eight entries exist only to support one such
term, and each therefore licenses that word anywhere in any title. `Capital`, for instance, is
admitted across all 1,560 titles so that `Capital Requirements Regulation` passes.

The fix masks a known phrase to lower case before the word loop runs. Masking preserves the word
count and every word position, so the loop's `title.split()[1:]` still skips exactly the first
word, which a deletion-based strip would break for a phrase sitting at the start of a title.

The seven phrases and the seventeen words were measured against the corpus rather than guessed.
Every word below appears in exactly one title, and only inside its phrase.

**Files:**
- Modify: `scripts/alchemist/checks.py:382-406` (`PROPER_NAMES` and `_capitalised_off_list`)
- Modify: `tests/test_checks_titles.py` (append)

**Interfaces:**
- Consumes: nothing from earlier tasks.
- Produces: `PROPER_PHRASES: tuple[str, ...]` and `_mask_phrases(title: str) -> str` in
  `scripts/alchemist/checks.py`. `_capitalised_off_list(title: str) -> list[str]` keeps its
  signature and its return type, so `check_titles_sentence_case` needs no change.

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_checks_titles.py`:

```python
def test_a_phrase_passes_as_a_phrase():
    assert _capitalised_off_list("Capital Requirements Regulation") == []
    assert _capitalised_off_list("Business Indicator Component") == []
    assert _capitalised_off_list("Internal Loss Multiplier") == []
    assert _capitalised_off_list("Economic history since the Great Depression") == []
    assert _capitalised_off_list("World Trade Organization") == []


def test_a_phrase_word_outside_its_phrase_is_an_offender():
    """The point of the change. Capital was admitted everywhere so that
    Capital Requirements Regulation would pass, which licensed it in any
    title at all."""
    assert _capitalised_off_list("Sources of Capital for a bank") == ["Capital"]
    assert _capitalised_off_list("Reporting the Loss distribution") == ["Loss"]
    assert _capitalised_off_list("An Internal model") == ["Internal"]
    assert _capitalised_off_list("The Great moderation") == ["Great"]


def test_a_standalone_proper_name_still_passes():
    """These stay in PROPER_NAMES because each is a name in its own right
    rather than half of a defined term."""
    assert _capitalised_off_list("Compound Poisson distribution") == []
    assert _capitalised_off_list("Duration dependent Markov process") == []
    assert _capitalised_off_list("Black-Scholes martingale approach") == []
    assert _capitalised_off_list("Bolzano-Weierstrass and Heine-Borel theorems") == []
    assert _capitalised_off_list("Basel III redefinition of Tier 1 and Tier 2 capital") == []


def test_masking_preserves_word_positions():
    """A phrase at the head of a title must not shift which word counts as
    first. Deleting the phrase instead of masking it would make Requirements
    the first word and skip it for the wrong reason."""
    assert _mask_phrases("Capital Requirements Regulation") == "capital requirements regulation"
    assert _mask_phrases("Shortcomings of the Basel Accord") == "Shortcomings of the basel accord"
    assert _mask_phrases("A title with no phrase") == "A title with no phrase"
```

Add `_capitalised_off_list` and `_mask_phrases` to the file's import from
`scripts.alchemist.checks`.

- [ ] **Step 2: Run them to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_checks_titles.py -k "phrase or standalone or masking" -v`

Expected: FAIL. `test_masking_preserves_word_positions` fails with `ImportError` or `NameError` on
`_mask_phrases`, and `test_a_phrase_word_outside_its_phrase_is_an_offender` fails because
`_capitalised_off_list("Sources of Capital for a bank")` returns `[]` today.

- [ ] **Step 3: Add the phrase list and the mask, and trim the word list**

In `scripts/alchemist/checks.py`, replace the `PROPER_NAMES` block and `_capitalised_off_list`
with:

```python
# Single words that are proper names in their own right, wherever they appear.
PROPER_NAMES = frozenset({
    "American", "Basel", "Bayes", "Black", "Bolzano", "Borel", "Brace",
    "Brownian", "Euclidean", "Gatarek", "Greeks", "Heine", "Laplace", "Lloyd",
    "Markov", "Musiela", "Pareto", "Poisson", "Scholes", "Tier", "Weierstrass",
})

# Defined terms of more than one word. Each of these used to cost the word list
# an entry per word, and every such entry licensed that word across all 1,560
# titles: "Capital" was admitted everywhere so that "Capital Requirements
# Regulation" would pass. Ordered longest first, so a phrase containing another
# masks before the shorter one can match inside it.
PROPER_PHRASES = (
    "Capital Requirements Regulation",
    "Business Indicator Component",
    "Internal Loss Multiplier",
    "World Trade Organization",
    "Great Depression",
    "Basel Accord",
    "Monte Carlo",
)
ROMAN = re.compile(r"^(?:I|II|III|IV|V|VI|VII|VIII|IX|X)$")


def _mask_phrases(title: str) -> str:
    """Lower-case every known phrase in place, leaving the word count alone.

    Masking rather than deleting is load-bearing. `_capitalised_off_list` skips
    `title.split()[1:]`, so removing a phrase that opens a title would promote
    the phrase's second word to first and skip it for the wrong reason.
    """
    masked = title
    for phrase in PROPER_PHRASES:
        masked = masked.replace(phrase, phrase.lower())
    return masked


def _capitalised_off_list(title: str) -> list[str]:
    """Words after the first that carry a capital the rule does not allow."""
    offenders: list[str] = []
    for word in _mask_phrases(title).split()[1:]:
        for part in word.split("-"):
            core = part.strip("(),:;\"'").removesuffix("'s")
            if not core or not core[0].isupper():
                continue
            if len(core) == 1 or sum(ch.isupper() for ch in core) >= 2:
                continue
            if ROMAN.match(core) or core in PROPER_NAMES:
                continue
            offenders.append(part)
    return offenders
```

Note that `ROMAN` moves up with the block; do not leave a second definition behind.

- [ ] **Step 4: Run the tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_checks_titles.py -v`
Expected: all pass, the pre-existing title tests included.

- [ ] **Step 5: Run check 10 over the whole corpus**

Run: `.venv/bin/python scripts/check.py`

Expected: all ten rules ok at `1560 nodes, 13 paths, 0 failures`. This is the step that matters:
seventeen words left the list, so any title relying on one of them outside its phrase now fails.
Should a title fail, do not put the word back. Read the title, and either add a genuine phrase to
`PROPER_PHRASES` or correct the title's casing in the record, which is what D4 rules.

- [ ] **Step 6: Run the suite**

Run: `.venv/bin/python -m pytest -q`
Expected: 227 passed.

- [ ] **Step 7: Update `CLAUDE.md`'s title-casing section**

In `CLAUDE.md`, in the "Title casing" section, replace:

```
Check 10 enforces
it against the `PROPER_NAMES` list in `checks.py`, so a genuine name the list lacks is added
there by name, and a source's title case is corrected in the record. Ruled at gate 2 (D4).
```

with:

```
Check 10 enforces it against two lists in `checks.py`:
`PROPER_NAMES` for single words that are names in their own right, and `PROPER_PHRASES` for a
defined term of several words, which is masked as a phrase so that its words are not admitted
anywhere else. A genuine name the lists lack is added to whichever fits, and a source's title
case is corrected in the record. Ruled at gate 2 (D4); the phrase list is G23.
```

- [ ] **Step 8: Commit**

```bash
git add scripts/alchemist/checks.py tests/test_checks_titles.py CLAUDE.md
git commit -m "feat(checks): admit proper names as phrases rather than words

Seventeen of PROPER_NAMES' thirty-eight entries existed only to support
one defined term of several words, and each licensed that word across all
1,560 titles. PROPER_PHRASES now masks the seven terms to lower case
before the word loop, so Capital passes inside Capital Requirements
Regulation and fails outside it. Masking rather than deleting keeps the
word positions, which a phrase opening a title depends on. Closes G23.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 5: Vary the cadence of the three gate 2 path preambles (G24)

The three paths drawn at gate 2 under D2 all open the same way: a noun phrase, a colon, then a
long list. Read together they announce a template, and the colon does a full stop's job, which
`~/.claude/rules/chat-voice.md` and `01 Guidelines/_craft.md` both budget at roughly one per
piece. The nine older preambles do not share the shape, so the three new ones stand out.

This task rewrites three `preamble` fields and touches nothing else. Every fact in each preamble
is preserved: the same topics, the same node counts, the same `builds_on` reasoning.

**Files:**
- Modify: `paths/enterprise-risk-and-regulation.yaml` (the `preamble` block only)
- Modify: `paths/banking-and-financial-management.yaml` (the `preamble` block only)
- Modify: `paths/economics.yaml` (the `preamble` block only)

**Interfaces:**
- Consumes: nothing from earlier tasks.
- Produces: nothing later tasks depend on. `parse_path` reads `preamble` as an opaque string, so
  no signature changes.

- [ ] **Step 1: Read all twelve preambles together**

Run: `for f in paths/*.yaml; do echo "=== $f"; sed -n '/^preamble:/,/^nodes:/p' "$f" | head -3; done`

Confirm before editing that the three named files open on a noun phrase and a colon and that the
other nine do not. Rewrite only where the shape is actually shared; if a fourth file turns out to
share it, report that rather than widening the task.

- [ ] **Step 2: Rewrite the enterprise risk and regulation preamble**

In `paths/enterprise-risk-and-regulation.yaml`, replace the whole `preamble: >` block with:

```yaml
preamble: >
  A regulated financial firm has to identify, measure, and govern its risk, and it has to
  satisfy a supervisor that it does. This path covers both halves. It opens on the risk
  management function and its committees, risk appetite, the three lines of defence, and model
  risk management, then turns to the Basel capital and liquidity framework from Basel I through
  the 2017 finalisation, taking in the leverage ratio, the output floor, the liquidity coverage
  and net stable funding ratios, the capital buffers, and the internal capital and liquidity
  adequacy assessment processes. Hedge accounting, conduct risk, insurance regulation, and
  recovery and resolution sit alongside. It builds on the credit trunk because the internal
  ratings-based rules regulate the parameters the trunk estimates, and on the life and general
  insurance paths, which supply the prerequisites its CP1 principles nodes draw on.
```

- [ ] **Step 3: Rewrite the banking and financial management preamble**

In `paths/banking-and-financial-management.yaml`, replace the whole `preamble: >` block with:

```yaml
preamble: >
  Before a bank is a portfolio of risks it is a business, and this path treats it as one. It
  works through the balance sheet and income statement, deposit taking and wholesale funding,
  the funds transfer pricing regimes that price liquidity between businesses, and the capital,
  return, and liquidity metrics a treasury and an asset-liability committee manage. The path
  also carries the ASSA banking papers' material on operational risk data and loss modelling,
  pension obligation risk, and the enterprise risk management vocabulary of appetite, culture,
  and reporting, together with the strategy and case-study material the papers end on. It
  builds on the enterprise risk and regulation path because the ratios and buffers it manages
  are the ones that path defines, and on the credit trunk because the loan book is the asset
  being funded.
```

- [ ] **Step 4: Rewrite the economics preamble**

In `paths/economics.yaml`, replace the whole `preamble: >` block with:

```yaml
preamble: >
  The banking material assumes a reader who already holds the economics, and this path supplies
  it. On the macroeconomic side it covers the circular flow, aggregate demand and supply,
  growth, unemployment and inflation, money and monetary policy, fiscal policy, interest and
  exchange rates, and trade; on the microeconomic side, the market structures from perfect
  competition to monopoly. Economic history since the Great Depression sits here too, alongside
  the strategic material on how a bank fares through the cycle, because net interest income is
  conditional on the economy. It builds on the banking path for the balance-sheet vocabulary
  and on financial engineering for the instruments the economy moves.
```

- [ ] **Step 5: Confirm no fact moved and no dash crept in**

Run: `git diff paths/ | grep -E "^[-+].*(—|–)"`
Expected: no output.

Then read the diff in full: `git diff paths/`. Every topic named in the old preamble has to appear
in the new one. The economics rewrite keeps its one colon, which now separates two genuine halves
of a contrast rather than unpacking a summarising clause, and that is the single permitted use.

- [ ] **Step 6: Run the checks and the suite**

Run: `.venv/bin/python scripts/check.py && .venv/bin/python -m pytest -q`
Expected: all ten rules ok at `1560 nodes, 13 paths, 0 failures`, then 227 passed. Check 4 reads
the `nodes` list rather than the preamble, so a green run here confirms nothing else was
disturbed.

- [ ] **Step 7: Rebuild the site and confirm the preambles render**

Run: `.venv/bin/python scripts/build_site.py`

Then check `git status --short site/` and confirm only the three path pages changed. Should
`build_site.py` complain that `dot` is missing, install graphviz with `brew install graphviz`
and re-run.

- [ ] **Step 8: Commit**

```bash
git add paths/enterprise-risk-and-regulation.yaml paths/banking-and-financial-management.yaml paths/economics.yaml site/
git commit -m "docs(paths): vary the cadence of the three gate 2 preambles

All three opened on a noun phrase and a colon, so read together they
announced a template, and the colon did a full stop's job. Each now opens
on a sentence and keeps every topic, node count and builds_on reason it
had. Closes G24.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 6: Open the pull request

**Files:** none.

- [ ] **Step 1: Confirm the branch state**

Run: `git status --short && .venv/bin/python scripts/check.py && .venv/bin/python -m pytest -q`
Expected: clean tree, ten rules ok, 227 passed.

- [ ] **Step 2: Push and open the pull request**

```bash
git push -u origin fix/phase-1-tool-chores
gh pr create --base main --head fix/phase-1-tool-chores \
  --title "fix: close the five deferred Phase 1 tool chores" \
  --body-file <body saved to a file first>
```

The body should name the five chores, the two mutation-checked refusal arms, the ordering defect,
G23's seventeen words folded into seven phrases, and G24's three preambles, and it should end with
`🤖 Generated with [Claude Code](https://claude.com/claude-code)`.

- [ ] **Step 3: Stop**

**Never self-merge.** Hand the pull request to Mario and wait.

---

## Self-review

**Spec coverage.** Section 13 of the spec names three chores: G23's phrase-level proper names
(Task 4), the merge tool's three untested refusal arms (Tasks 1 and 2, which together cover the
status arm, the missing-absorbed-file arm and `merge_nodes.py`'s line validation, exactly the
three recorded at `progress.md:115`), and G24's preamble cadence (Task 5). Task 3 adds the
ordering defect recorded in the same ledger line, because it sits in the file Task 1 already
touches and would otherwise stay a residual nobody owns. Task 6 opens the pull request.

**Placeholders.** None. Every code step carries the literal code, every run step the literal
command and its expected output, and the two lists in Task 4 were measured against the corpus
rather than proposed.

**Type consistency.** `_capitalised_off_list(title: str) -> list[str]` keeps its signature, so
`check_titles_sentence_case` is untouched. `_mask_phrases(title: str) -> str` and
`PROPER_PHRASES: tuple[str, ...]` are new and are used only inside `checks.py` and its tests.
`merged_record(survivor, absorbed) -> Node` is called once in Task 3 where it was called once
before, and `render` takes the same `Node`. Test counts run 218, 220, 222, 223, 227, 227 across
the tasks, which is consistent with two, two, one and four tests added and none removed.

**One risk worth naming.** Task 4's step 5 is the only step that can fail on data rather than on
code. Seventeen words leave the word list, and a title relying on one outside its phrase will
fail check 10. That is the change working as intended, so the repair is a new phrase or a
corrected title, never restoring the word.
