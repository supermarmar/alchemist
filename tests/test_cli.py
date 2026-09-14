import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from scripts.merge_ledger import FLOW_LIST_MAX_ITEMS
from scripts.alchemist.model import (
    Alias, Corpus, MathObject, Node, Objects, Spend, TeachingPath,
)
from scripts.alchemist.site import (
    render_domain_dot, render_index, render_node_page, render_path_page,
)

REPO = Path(__file__).resolve().parents[1]

# Matches double-quoted attributes only. Every asset tag the generators emit is
# written with double quotes, in `HEAD`, `NODE_HEAD` and the link builders, and
# that is the convention this regex relies on: a single-quoted href would slip
# past it unchecked.
LOCAL_REF = re.compile(r'(?:href|src)="(?!https?:|//|#|data:)([^"#?]+)')


def node(node_id: str, requires=(), domains=("stats",), taught_in=None) -> Node:
    return Node(
        id=node_id, title=node_id.replace("-", " ").capitalize(), domains=domains,
        status="stub", requires=tuple(requires), spends=(), anchor=(),
        vault_articles=(), vault_sources=(), taught_in=taught_in, body="",
        path=Path(f"nodes/{node_id}.md"),
    )


def test_the_index_lists_every_path_and_counts_the_nodes():
    """The corpus holds three nodes while the path lists two, so the per-path count
    and the summary total are different strings. With them equal, deleting the
    per-path count entirely still passes, because the summary sentence supplies
    the same text. The third node also covers the "taught in full" figure, which
    otherwise has no test at all."""
    corpus = Corpus(
        {
            "a": node("a"),
            "b": node("b", ["a"]),
            "c": node("c", taught_in="S1_credit-survival-bridge"),
        },
        {"p": TeachingPath("p", "A path", (), "Why.", ("a", "b"))},
    )
    out = render_index(corpus)
    assert "A path" in out
    assert "2 nodes" in out                      # the path's own count
    assert "3 nodes" in out                      # the corpus summary
    assert "1 of them taught in full" in out


def test_one_node_and_one_path_read_as_singular():
    corpus = Corpus(
        {"a": node("a")}, {"p": TeachingPath("p", "P", (), "", ("a",))}
    )
    out = render_index(corpus)
    assert "1 node," in out and "1 nodes" not in out
    assert "1 path." in out and "1 paths" not in out


def test_a_path_page_lists_its_nodes_in_order_and_marks_the_taught_ones():
    corpus = Corpus(
        {"a": node("a", taught_in="S1_credit-survival-bridge"), "b": node("b", ["a"])},
        {"p": TeachingPath("p", "A path", (), "Why.", ("a", "b"))},
    )
    out = render_path_page(corpus.paths["p"], corpus)
    assert out.index("../nodes/a.html") < out.index("../nodes/b.html")
    assert "S1_credit-survival-bridge" in out


def test_a_node_page_carries_the_body_the_aliases_and_what_it_unlocks():
    hazard = MathObject(
        id="obj.hazard", name="Hazard rate", canonical="h(t)", definition="d",
        aliases=(Alias("life", r"\mu_x", "force of mortality"),
                 Alias("credit", "h(t)", "default hazard")),
    )
    root = Node(
        id="survival-function", title="Survival function", domains=("life", "credit"),
        status="drafted", requires=(), spends=(Spend("obj.hazard", "life"),
                                              Spend("obj.hazard", "credit")),
        anchor=(), vault_articles=("methods/deep-learning-credit-scoring",),
        vault_sources=(), taught_in=None, body="## Definition\n\nThe probability of no event.\n",
        path=Path("nodes/survival-function.md"),
    )
    corpus = Corpus({"survival-function": root, "hazard-rate": node("hazard-rate", ["survival-function"])}, {})
    out = render_node_page(root, corpus, Objects({"obj.hazard": hazard}))
    assert "The probability of no event." in out
    assert "force of mortality" in out and "default hazard" in out
    assert "hazard-rate" in out
    assert "methods/deep-learning-credit-scoring" in out


def test_a_node_page_omits_the_alias_table_where_one_domain_is_spent():
    hazard = MathObject(
        id="obj.hazard", name="Hazard rate", canonical="h(t)", definition="d",
        aliases=(Alias("credit", "h(t)", "default hazard"),),
    )
    only = Node(
        id="a", title="A", domains=("credit",), status="stub", requires=(),
        spends=(Spend("obj.hazard", "credit"),), anchor=(), vault_articles=(),
        vault_sources=(), taught_in=None, body="x\n", path=Path("nodes/a.md"),
    )
    out = render_node_page(only, Corpus({"a": only}, {}), Objects({"obj.hazard": hazard}))
    assert "One object, several names" not in out


def test_the_alias_table_covers_only_objects_spent_in_more_than_one_domain():
    """The table's heading claims one object under several names, so its trigger
    is one object spanning domains rather than the node spanning them. Here the
    hazard spans life and credit while the survival function is spent in credit
    alone, so the second belongs nowhere in the table. Under the old
    domain-count trigger it rendered a row of its own, giving two rows labelled
    `credit` carrying different symbols under that heading.
    """
    hazard = MathObject(
        id="obj.hazard", name="Hazard rate", canonical="h(t)", definition="d",
        aliases=(Alias("life", r"\mu_x", "force of mortality"),
                 Alias("credit", "h(t)", "default hazard")),
    )
    survival = MathObject(
        id="obj.survival", name="Survival function", canonical="S(t)", definition="d",
        aliases=(Alias("credit", "S(t)", "survival function"),),
    )
    both = Node(
        id="a", title="A", domains=("life", "credit"), status="stub", requires=(),
        spends=(Spend("obj.hazard", "life"), Spend("obj.hazard", "credit"),
                Spend("obj.survival", "credit")),
        anchor=(), vault_articles=(), vault_sources=(), taught_in=None,
        body="", path=Path("nodes/a.md"),
    )
    out = render_node_page(
        both, Corpus({"a": both}, {}),
        Objects({"obj.hazard": hazard, "obj.survival": survival}),
    )
    table = out[out.index("One object, several names"):]
    assert "force of mortality" in table and "default hazard" in table
    assert "Hazard rate" in table          # the object column, so a row says whose
    assert "survival function" not in table
    assert "Survival function" not in table


def test_the_alias_table_is_absent_where_no_object_spans_two_domains():
    """Two domains, two objects, one domain each. The node is not a bridge, so
    a table headed "one object, several names" would be about nothing. This is
    the case the old domain-count trigger got wrong in the other direction.
    """
    hazard = MathObject(
        id="obj.hazard", name="Hazard rate", canonical="h(t)", definition="d",
        aliases=(Alias("life", r"\mu_x", "force of mortality"),),
    )
    survival = MathObject(
        id="obj.survival", name="Survival function", canonical="S(t)", definition="d",
        aliases=(Alias("credit", "S(t)", "survival function"),),
    )
    spread = Node(
        id="a", title="A", domains=("life", "credit"), status="stub", requires=(),
        spends=(Spend("obj.hazard", "life"), Spend("obj.survival", "credit")),
        anchor=(), vault_articles=(), vault_sources=(), taught_in=None,
        body="", path=Path("nodes/a.md"),
    )
    out = render_node_page(
        spread, Corpus({"a": spread}, {}),
        Objects({"obj.hazard": hazard, "obj.survival": survival}),
    )
    assert "One object, several names" not in out
    assert "force of mortality" not in out


def test_the_dot_graph_carries_one_edge_per_prerequisite():
    """Asserts the count, which is what "one edge per prerequisite" claims. The
    old assertion was that one edge existed, so a generator emitting it twice
    passed, and a duplicated entry in a node's `requires` would do exactly that.
    Three prerequisites across the corpus means three edges and no more.
    """
    corpus = Corpus(
        {"a": node("a"), "b": node("b", ["a"]), "c": node("c", ["a", "b"])}, {}
    )
    dot = render_domain_dot(corpus, "stats")
    assert dot.startswith("digraph")
    assert dot.count('"a" -> "b"') == 1
    assert dot.count('"a" -> "c"') == 1
    assert dot.count('"b" -> "c"') == 1
    assert dot.count(" -> ") == 3


def test_a_node_whose_only_prerequisite_sits_in_another_domain_is_not_drawn():
    corpus = Corpus(
        {"a": node("a", domains=("life",)), "b": node("b", ["a"], domains=("stats",))},
        {},
    )
    dot = render_domain_dot(corpus, "stats")
    assert '"b"' not in dot and '"a" -> "b"' not in dot


def test_a_member_with_an_in_domain_edge_is_drawn_and_a_lone_member_is_not():
    corpus = Corpus({"a": node("a"), "b": node("b", ["a"]), "c": node("c")}, {})
    dot = render_domain_dot(corpus, "stats")
    assert '"a"' in dot and '"b"' in dot and '"a" -> "b"' in dot
    assert '"c"' not in dot


def test_author_supplied_text_is_escaped():
    """"PD < 1%" is ordinary prose in this corpus and the repo is public, so an
    unescaped title corrupts the page the first time real content lands."""
    corpus = Corpus(
        {"a": node("a")},
        {"p": TeachingPath("p", "PD < 1% & rising", (), "See <b>this</b>.", ("a",))},
    )
    index = render_index(corpus)
    page = render_path_page(corpus.paths["p"], corpus)
    assert "PD &lt; 1% &amp; rising" in index
    assert "PD < 1% & rising" not in index
    assert "&lt;b&gt;this&lt;/b&gt;" in page
    assert "<b>this</b>" not in page


def test_a_quote_in_a_title_does_not_break_the_dot_label():
    """A DOT label is a quoted string, so an unescaped double quote ends the
    label early and `dot` fails on the rest of the line."""
    quoted = Node(
        id="a", title='The "ultimate" claim', domains=("stats",), status="stub",
        requires=(), spends=(), anchor=(), vault_articles=(), vault_sources=(),
        taught_in=None, body="", path=Path("nodes/a.md"),
    )
    dot = render_domain_dot(Corpus({"a": quoted, "b": node("b", ["a"])}, {}), "stats")
    assert '\\"ultimate\\"' in dot


def test_pages_below_site_reach_the_repo_root():
    """A page in site/paths/ is two levels below the root, so ../assets/ would
    resolve to site/assets/, which nothing ever creates."""
    corpus = Corpus(
        {"a": node("a", taught_in="S1_credit-survival-bridge")},
        {"p": TeachingPath("p", "P", (), "", ("a",))},
    )
    page = render_path_page(corpus.paths["p"], corpus)
    assert "../../assets/lecture.css" in page
    assert "../../lectures/S1_credit-survival-bridge.html" in page


def test_check_py_exits_zero_on_the_real_repo():
    done = subprocess.run(
        [sys.executable, "scripts/check.py"], cwd=REPO, capture_output=True, text=True
    )
    assert done.returncode == 0, done.stdout + done.stderr


def test_check_py_exits_non_zero_when_a_rule_fails(tmp_path):
    (tmp_path / "nodes").mkdir()
    (tmp_path / "paths").mkdir()
    (tmp_path / "notation").mkdir()
    (tmp_path / "nodes" / "b.md").write_text(
        "---\nid: b\ntitle: B\ndomains: [stats]\nstatus: stub\nrequires: [ghost]\n---\n\nx\n"
    )
    (tmp_path / "notation" / "objects.yaml").write_text("[]\n")
    (tmp_path / "notation" / "symbols.md").write_text("wrong\n")
    done = subprocess.run(
        [sys.executable, str(REPO / "scripts" / "check.py"), "--root", str(tmp_path)],
        capture_output=True, text=True, cwd=REPO,
    )
    assert done.returncode == 1 and "ghost" in done.stdout


# All three of these are COPIED, never symlinked. `nodes/` and `paths/` are
# read-only inputs, but `build()` WRITES `notation/symbols.md`, which is the
# whole reason the old test repaired a drift mid-suite: symlink `notation/` and
# the write resolves straight back into the working tree and the bug returns.
# The trees below carry no generated file, so they are symlinked rather than
# copied, which saves 936 kB of vendored KaTeX per test run.
BUILD_INPUTS = ("nodes", "paths", "notation")
LINKED_TREES = ("assets", "vendor", "lectures")


@pytest.mark.skipif(shutil.which("dot") is None, reason="graphviz not installed")
def test_every_link_a_generated_page_emits_resolves_on_disk(tmp_path):
    """Both site defects found in Phase 0 were dangling links that no test could
    see: the index pointed at `paths/` while the pages were written to
    `site/paths/`, and the path page pointed at a lecture HTML that gitignore
    kept out of the tree. Walk what the generators actually emit instead.

    Builds into `tmp_path` rather than into `REPO`. Building into the working
    tree made pytest a writer: it regenerated `notation/symbols.md` mid-suite,
    which silently repaired the drift check 7 exists to catch. The three input
    directories are copied so the build's writes land in the temporary tree; the
    three asset trees are symlinked, because a link to
    `../../vendor/katex/katex.min.js` is a claim about repo content and
    `Path.resolve()` follows the symlink to check it.

    Skipped where graphviz is absent. `build()` shells out to `dot` for the
    domain graph SVGs whatever root it is given, so without the guard this test
    fails rather than skips, and a contributor with no graphviz cannot run the
    unit suite at all. Definition-of-done criterion 1 promises no test skips
    other than on an absent Quarto or Chrome, so the honest reading is that
    graphviz joins that list rather than that the failure is documented as an
    exception.
    """
    from scripts.alchemist.site import build

    for name in BUILD_INPUTS:
        shutil.copytree(REPO / name, tmp_path / name)
    for name in LINKED_TREES:
        (tmp_path / name).symlink_to(REPO / name, target_is_directory=True)

    written = build(tmp_path)
    pages = [p for p in written if p.suffix == ".html"]
    assert pages, "the build wrote no HTML pages, so this test proves nothing"

    missing: list[str] = []
    for page in pages:
        for ref in LOCAL_REF.findall(page.read_text()):
            target = (page.parent / ref).resolve()
            if not target.exists():
                missing.append(f"{page.relative_to(tmp_path)} -> {ref}")
    assert missing == [], "dangling links:\n" + "\n".join(missing)


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


def test_merge_ledger_refuses_to_write_a_malformed_fragment(tmp_path):
    """A partial ledger reaching the gate wearing the appearance of a complete
    one is worse than no ledger, so the seeded file must survive untouched."""
    sources = tmp_path / "sources"
    sources.mkdir()
    ledger_before = (
        "# Sources the corpus needs and the vault does not hold.\n"
        "#\n"
        "# acquisition: public-download | regulator | journal | purchased-personal\n"
        "# status:      wanted | located | in-raw | ingested\n"
        "- id: seeded-entry\n"
        "  needed_by: [some-node]\n"
        "  claim: A seeded claim.\n"
        "  document: A seeded document.\n"
        "  expected_tier: T4\n"
        "  acquisition: journal\n"
        "  status: wanted\n"
    )
    (sources / "wanted.yaml").write_text(ledger_before)
    staging = tmp_path / "staging"
    staging.mkdir()
    (staging / "ledger-01.yaml").write_text("- just a string\n")

    result = subprocess.run(
        [sys.executable, "scripts/merge_ledger.py",
         "--root", str(tmp_path), "--staging", str(staging)],
        capture_output=True, text=True, cwd=REPO,
    )
    assert result.returncode == 2
    assert "malformed" in result.stderr
    assert "ledger-01" in result.stderr
    assert (sources / "wanted.yaml").read_text() == ledger_before


def test_merge_ledger_dry_run_with_no_fragments_is_the_identity(tmp_path):
    """The property the real repo's own dry-run rests on, exercised here
    against a small tmp ledger rather than the four seeded Phase 1 entries."""
    sources = tmp_path / "sources"
    sources.mkdir()
    ledger_before = (
        "# header comment\n"
        "- id: seeded-entry\n"
        "  needed_by: [some-node]\n"
        "  claim: A seeded claim.\n"
        "  document: A seeded document.\n"
        "  expected_tier: T4\n"
        "  acquisition: journal\n"
        "  status: wanted\n"
    )
    (sources / "wanted.yaml").write_text(ledger_before)
    staging = tmp_path / "staging"
    staging.mkdir()

    result = subprocess.run(
        [sys.executable, "scripts/merge_ledger.py",
         "--root", str(tmp_path), "--staging", str(staging), "--dry-run"],
        capture_output=True, text=True, cwd=REPO,
    )
    assert result.returncode == 0
    assert "would write 1 entries (1 seeded)" in result.stdout
    assert (sources / "wanted.yaml").read_text() == ledger_before


def _run_merge_ledger(root: Path, staging: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "scripts/merge_ledger.py",
         "--root", str(root), "--staging", str(staging)],
        capture_output=True, text=True, cwd=REPO,
    )


def test_merge_ledger_over_the_real_ledger_keeps_folded_claims_and_flow_lists(tmp_path):
    """A bare yaml.safe_dump turns every folded claim into a quoted flow
    scalar and every flow needed_by into a block sequence: content survives,
    readability does not. Run against a copy of the real ledger, never the
    repo's own sources/wanted.yaml, so this proves the restored styles hold on
    the file the gate actually reads rather than on a toy fixture.

    The styles are counted rather than matched literally, because a flow list
    at the ledger's width wraps across lines and a literal single-line match
    would fail on any entry naming more than a handful of nodes."""
    real_ledger = (REPO / "sources" / "wanted.yaml").read_text()
    sources = tmp_path / "sources"
    sources.mkdir()
    (sources / "wanted.yaml").write_text(real_ledger)
    staging = tmp_path / "staging"
    staging.mkdir()

    result = _run_merge_ledger(tmp_path, staging)
    assert result.returncode == 0

    written = (sources / "wanted.yaml").read_text()
    header = real_ledger[: real_ledger.index("- id:")]
    assert written.startswith(header)
    # Derived from the input rather than a literal count, so this keeps
    # checking the style rather than the content once tasks 8/9 grow the
    # ledger past today's four entries.
    assert written.count("claim: >") == real_ledger.count("claim: >")
    assert written.count("needed_by: [") == real_ledger.count("needed_by: [")
    # Flow style below the boundary, block style above it, checked against the
    # entries themselves rather than asserted absent. The ledger held four
    # entries of one to three ids when this test was written, so block style
    # never appeared; Phase 2's merge took it to 135 entries, one of which
    # names 177 nodes, and that is the case FLOW_LIST_MAX_ITEMS exists for.
    merged = yaml.safe_load(written)
    short = [e for e in merged if len(e["needed_by"]) <= FLOW_LIST_MAX_ITEMS]
    assert written.count("needed_by: [") == len(short)
    assert written.count("needed_by:\n") == len(merged) - len(short)


def test_merge_ledger_run_twice_is_byte_identical(tmp_path):
    """The property every later diff depends on: a merge over its own output
    changes nothing, so a real ledger update is never buried in reformatting
    noise. Run against a copy of the real ledger, never the repo's own
    sources/wanted.yaml."""
    real_ledger = (REPO / "sources" / "wanted.yaml").read_text()
    header = real_ledger[: real_ledger.index("- id:")]
    # Deliberately de-styled input: a plain safe_dump drops every folded claim
    # and flow list, which is the state the first merge has to restore. The
    # real ledger is itself merge output now that Phase 2 has written it, so
    # feeding it in directly would make the first merge a no-op and the guard
    # below vacuous.
    destyled = header + yaml.safe_dump(yaml.safe_load(real_ledger), sort_keys=False)
    sources = tmp_path / "sources"
    sources.mkdir()
    (sources / "wanted.yaml").write_text(destyled)
    staging = tmp_path / "staging"
    staging.mkdir()

    first = _run_merge_ledger(tmp_path, staging)
    assert first.returncode == 0
    first_bytes = (sources / "wanted.yaml").read_bytes()
    assert first_bytes != destyled.encode()

    second = _run_merge_ledger(tmp_path, staging)
    assert second.returncode == 0
    second_bytes = (sources / "wanted.yaml").read_bytes()
    assert second_bytes == first_bytes


def test_merge_ledger_run_twice_is_byte_identical_on_a_block_style_needed_by(tmp_path):
    """The same guarantee as above, exercised on the path the real ledger
    cannot: every needed_by seeded there today holds one to three ids, so
    the test above never touches block style. A 200-id needed_by is well
    inside the corpus's own design bound (roughly 1,100 uncovered nodes
    across about 59 anchor documents, with assa.f107 alone anchoring 274
    of them), so this is the shape idempotency has to hold for."""
    entry = {
        "id": "assa-f107-2026",
        "needed_by": [f"node-{i:03d}" for i in range(200)],
        "claim": "A long claim.",
        "document": "ASSA F107, 2026",
        "expected_tier": "T4",
        "acquisition": "purchased-personal",
        "status": "wanted",
    }
    sources = tmp_path / "sources"
    sources.mkdir()
    (sources / "wanted.yaml").write_text(
        "# header\n" + yaml.safe_dump([entry], sort_keys=False)
    )
    staging = tmp_path / "staging"
    staging.mkdir()

    first = _run_merge_ledger(tmp_path, staging)
    assert first.returncode == 0
    written = (sources / "wanted.yaml").read_text()
    assert "needed_by:\n" in written  # confirms block style actually fired
    first_bytes = written.encode()

    second = _run_merge_ledger(tmp_path, staging)
    assert second.returncode == 0
    assert (sources / "wanted.yaml").read_bytes() == first_bytes
