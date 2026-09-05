from pathlib import Path

from scripts.alchemist.checks import check_generated_current
from scripts.alchemist.model import (
    Alias,
    Corpus,
    MathObject,
    Node,
    Objects,
    Spend,
    TeachingPath,
)
from scripts.alchemist.site import render_node_page, render_review, render_symbols

HAZARD = MathObject(
    id="obj.hazard", name="Hazard rate", canonical="h(t)",
    definition="The instantaneous rate of the event.",
    aliases=(Alias("life", r"\mu_x", "force of mortality", "age-indexed"),
             Alias("gi", r"\lambda", "claim intensity")),
)
OBJECTS = Objects({"obj.hazard": HAZARD})


def _node(node_id: str, *, title=None, domains=("credit",), requires=(), anchor=("chosen",)) -> Node:
    return Node(
        id=node_id, title=title or node_id.replace("-", " ").capitalize(),
        domains=domains, status="stub", requires=requires, spends=(), anchor=anchor,
        vault_articles=(), vault_sources=(), taught_in=None, body="A stub.",
        path=Path(f"nodes/{node_id}.md"),
    )


def _path(path_id: str, nodes: tuple[str, ...], *, builds_on=()) -> TeachingPath:
    return TeachingPath(
        id=path_id, title=path_id.replace("-", " ").capitalize(),
        builds_on=builds_on, preamble=f"The {path_id} path.", nodes=nodes,
    )


def two_path_corpus() -> Corpus:
    """Two paths, four nodes, every node placed. The baseline the review renders."""
    nodes = {
        n.id: n
        for n in (
            _node("conditional-probability", domains=("maths", "stats")),
            _node("survival-function", domains=("stats", "credit")),
            _node("hazard-rate", title="Hazard rate", domains=("stats", "credit"),
                  requires=("survival-function",), anchor=("ifoa.cs2.2.1-3",)),
            _node("discrete-time-hazard", requires=("hazard-rate",)),
        )
    }
    paths = {
        "maths-stats-prerequisites": _path(
            "maths-stats-prerequisites", ("conditional-probability",)
        ),
        "survival-braid": _path(
            "survival-braid",
            ("survival-function", "hazard-rate", "discrete-time-hazard"),
            builds_on=("maths-stats-prerequisites",),
        ),
    }
    return Corpus(nodes=nodes, paths=paths)


def corpus_with_an_orphan(node_id: str) -> Corpus:
    """The baseline plus one node in no path, which no check rejects and only the
    review document makes visible."""
    corpus = two_path_corpus()
    corpus.nodes[node_id] = _node(node_id, domains=("gi",))
    return corpus


def shared_node_corpus(node_id: str) -> Corpus:
    """One node earning a place in two paths, which spec section 4.3 permits
    outright and the review must therefore show under both."""
    corpus = two_path_corpus()
    braid = corpus.paths["survival-braid"]
    corpus.paths["credit-trunk"] = _path(
        "credit-trunk", (node_id,), builds_on=("maths-stats-prerequisites",)
    )
    assert node_id in braid.nodes, "the fixture only means anything if the node is in both"
    return corpus


def test_the_table_carries_the_object_its_domains_and_its_note():
    out = render_symbols(OBJECTS)
    assert "Hazard rate" in out
    assert r"$\mu_x$" in out and "force of mortality" in out
    assert "age-indexed" in out
    assert "generated" in out.lower()


def test_objects_are_rendered_in_id_order():
    """Asserts the ordering itself rather than merely that two calls agree.
    Within one process a dict walks in insertion order deterministically, so a
    calls-agree assertion passes with `sorted()` removed, which is the mutation
    this test exists to catch."""
    later = MathObject(
        id="obj.zeta", name="Zeta", canonical="z", definition="d",
        aliases=(Alias("stats", "z", "zeta"),),
    )
    unsorted = Objects({"obj.zeta": later, "obj.hazard": HAZARD})
    out = render_symbols(unsorted)
    assert out.index("Hazard rate") < out.index("Zeta")


def test_check_7_passes_when_the_file_matches(tmp_path):
    (tmp_path / "notation").mkdir()
    (tmp_path / "notation" / "symbols.md").write_text(render_symbols(OBJECTS))
    assert check_generated_current(OBJECTS, tmp_path).failures == []


def test_check_7_fails_when_the_file_has_drifted(tmp_path):
    (tmp_path / "notation").mkdir()
    (tmp_path / "notation" / "symbols.md").write_text("# stale\n")
    result = check_generated_current(OBJECTS, tmp_path)
    assert len(result.failures) == 1
    # "drifted", not "build_site": both messages name build_site.py, so matching
    # on that would pass even if the drifted case emitted the missing message.
    assert "drifted" in result.failures[0]


def test_check_7_fails_when_the_file_is_missing(tmp_path):
    (tmp_path / "notation").mkdir()
    result = check_generated_current(OBJECTS, tmp_path)
    assert len(result.failures) == 1 and "missing" in result.failures[0]


def test_a_node_body_keeps_its_tex_through_markdown():
    r"""CommonMark reads `\,` as an escaped comma and eats the backslash, so a
    plain markdown render corrupts the thin space before any typesetter sees it.
    """
    body = Node(
        id="a", title="A", domains=("stats",), status="stub", requires=(),
        spends=(), anchor=(), vault_articles=(), vault_sources=(),
        taught_in=None, body="Then $P(A \\mid B)\\,P(B)$ follows.\n",
        path=Path("nodes/a.md"),
    )
    out = render_node_page(body, Corpus({"a": body}, {}), Objects({}))
    assert r"\,P(B)" in out
    assert r",P(B)" not in out.replace(r"\,P(B)", "")


def test_a_node_page_loads_katex_and_typesets_it():
    """A page showing raw TeX is not a reference page. Assert both the assets and
    the call, since either alone leaves the mathematics unset."""
    body = Node(
        id="a", title="A", domains=("stats",), status="stub", requires=(),
        spends=(), anchor=(), vault_articles=(), vault_sources=(),
        taught_in=None, body="$$x$$\n", path=Path("nodes/a.md"),
    )
    out = render_node_page(body, Corpus({"a": body}, {}), Objects({}))
    assert "../../vendor/katex/katex.min.css" in out
    assert "../../vendor/katex/katex.min.js" in out
    assert "../../vendor/katex/auto-render.min.js" in out
    assert "renderMathInElement" in out


def test_the_alias_table_typesets_its_symbols_rather_than_showing_raw_tex():
    r"""The alias table is built outside `MD`, so a bare `$\mu_x$` reaching the
    page would leave the `\(...\)`/`\[...\]` delimiters `render_node_page`
    configures for auto-render with nothing to match, exactly the gap the
    hazard-rate page surfaced once the body's own maths started typesetting.
    """
    body = Node(
        id="a", title="A", domains=("life", "gi"), status="stub", requires=(),
        spends=(Spend("obj.hazard", "life"), Spend("obj.hazard", "gi")),
        anchor=(), vault_articles=(), vault_sources=(), taught_in=None, body="",
        path=Path("nodes/a.md"),
    )
    out = render_node_page(body, Corpus({"a": body}, {}), OBJECTS)
    assert '<span class="math inline">\\(\\mu_x\\)</span>' in out
    assert "<td>$\\mu_x$</td>" not in out


def test_raw_html_in_a_node_body_is_escaped():
    """Bodies are author text on a public site, and markdown-it defaults to
    html=True."""
    body = Node(
        id="a", title="A", domains=("stats",), status="stub", requires=(),
        spends=(), anchor=(), vault_articles=(), vault_sources=(),
        taught_in=None, body="Text <script>alert(1)</script> more.\n",
        path=Path("nodes/a.md"),
    )
    out = render_node_page(body, Corpus({"a": body}, {}), Objects({}))
    assert "<script>alert(1)</script>" not in out


def _path_section(review: str, path: TeachingPath) -> str:
    """The stretch of the review between one path's `## ` heading and the next.

    A node dropped from its path still turns up in the orphan table at the
    foot, so a check against the whole document passes regardless of where the
    node landed. Slicing to the path's own section is what makes the check
    mean what its name says.
    """
    heading = f"## {path.title}"
    assert heading in review, f"{heading!r} is missing from the review"
    body = review[review.index(heading):].split("\n", 1)[1]
    end = body.find("\n## ")
    return body if end == -1 else body[:end]


def test_the_review_lists_every_node_under_its_path():
    corpus = two_path_corpus()
    review = render_review(corpus)
    for path in corpus.paths.values():
        section = _path_section(review, path)
        for node_id in path.nodes:
            assert f"`{node_id}`" in section
        for node_id in set(corpus.nodes) - set(path.nodes):
            assert f"`{node_id}`" not in section


def test_the_review_carries_the_counts_at_its_head():
    corpus = two_path_corpus()
    review = render_review(corpus)
    head = review.split("## ", 1)[0]
    assert str(len(corpus.nodes)) in head
    assert str(len(corpus.paths)) in head


def test_the_review_lists_orphans_separately():
    """A node in no path is a judgement for gate 2 and no check rejects one,
    so the review is the only place it becomes visible."""
    corpus = corpus_with_an_orphan("ruin-theory")
    review = render_review(corpus)
    assert "ruin-theory" in review.rsplit("Orphan", 1)[-1]


def test_a_node_line_carries_its_anchor_and_prerequisite_count():
    corpus = two_path_corpus()
    review = render_review(corpus)
    node = corpus.nodes["hazard-rate"]
    line = next(l for l in review.splitlines() if l.startswith(f"| `{node.id}`"))
    assert node.anchor[0] in line
    assert f"| {len(node.requires)} " in line


def test_a_node_in_two_paths_appears_under_both():
    """Checked against each path's own section rather than a whole-document
    count, so a row missing from one path and duplicated in the other could
    not pass by coincidence."""
    corpus = shared_node_corpus("hazard-rate")
    review = render_review(corpus)
    carrying = [path for path in corpus.paths.values() if "hazard-rate" in path.nodes]
    assert len(carrying) >= 2
    for path in carrying:
        assert "`hazard-rate`" in _path_section(review, path)
