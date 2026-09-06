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


def _orphan_section(review: str) -> str:
    """The document's own last section, from the `## Orphan nodes` heading to
    its end. It never needs a following `## ` heading to bound it, unlike
    `_path_section`, because nothing else renders after it.
    """
    heading = "## Orphan nodes"
    assert heading in review, f"{heading!r} is missing from the review"
    return review[review.index(heading):]


def test_the_review_lists_every_node_under_its_path():
    corpus = two_path_corpus()
    review = render_review(corpus)
    for path in corpus.paths.values():
        section = _path_section(review, path)
        for node_id in path.nodes:
            assert f"`{node_id}`" in section
        for node_id in set(corpus.nodes) - set(path.nodes):
            assert f"`{node_id}`" not in section


def test_the_review_orders_paths_and_their_nodes():
    """`render_review`'s docstring commits to two orders: paths in the
    alphabetical order of their id, and a path's own nodes in the order its
    node list declares. This checks both, rather than merely that everything
    is present somewhere."""
    corpus = two_path_corpus()
    review = render_review(corpus)
    maths_path = corpus.paths["maths-stats-prerequisites"]
    survival_path = corpus.paths["survival-braid"]
    assert review.index(f"## {maths_path.title}") < review.index(f"## {survival_path.title}")
    section = _path_section(review, survival_path)
    positions = [section.index(f"`{node_id}`") for node_id in survival_path.nodes]
    assert positions == sorted(positions)


def test_the_review_carries_the_counts_at_its_head():
    corpus = two_path_corpus()
    review = render_review(corpus)
    head = review.split("## ", 1)[0]
    assert str(len(corpus.nodes)) in head
    assert str(len(corpus.paths)) in head


def test_the_head_labels_bind_to_the_right_count():
    """A fixture with a different node count and path count, so swapping the
    two figures between the `Nodes:` and `Paths:` labels could not still print
    a line that happens to carry the right digit by coincidence."""
    corpus = two_path_corpus()
    review = render_review(corpus)
    head = review.split("## ", 1)[0]
    nodes_line = next(l for l in head.splitlines() if l.startswith("- Nodes:"))
    paths_line = next(l for l in head.splitlines() if l.startswith("- Paths:"))
    assert f"**{len(corpus.nodes)}**" in nodes_line
    assert f"**{len(corpus.paths)}**" in paths_line


def test_the_head_carries_each_further_count_against_its_own_label():
    """A fixture where prerequisite edges, multi-anchored nodes and chosen
    nodes take four different values from each other and from the node and
    path counts, so a renderer that mixed the three up, or printed one
    borrowed value for all three, could not still match by coincidence.

    n2 carries two anchors from two different registered bodies (`bcbs.d424`
    and `ifoa.cs2`) and is the one node the "anchored by more than one body"
    count should include. n5 carries two anchors from the same body
    (`ifoa.cs2` twice, as `survival-function` does in the real corpus) and
    must not be: counting anchor entries rather than resolved bodies is
    exactly the bug this fixture exists to catch."""
    nodes = {
        n.id: n
        for n in (
            _node("n1", requires=(), anchor=("chosen",)),
            _node("n2", requires=("n1",), anchor=("bcbs.d424.irb.para-1", "ifoa.cs2.1.1")),
            _node("n3", requires=("n1", "n2"), anchor=("chosen",)),
            _node("n4", requires=("n1", "n2", "n3"), anchor=("bcbs.d424.irb.para-2",)),
            _node("n5", requires=(), anchor=("ifoa.cs2.1.1", "ifoa.cs2.4.1-3")),
        )
    }
    corpus = Corpus(nodes=nodes, paths={})
    review = render_review(corpus)
    head = review.split("## ", 1)[0]

    def _line(prefix: str) -> str:
        return next(l for l in head.splitlines() if l.startswith(prefix))

    assert "**6**" in _line("- Prerequisite edges:")
    assert "**1**" in _line("- Nodes anchored by more than one body:")
    assert "**2**" in _line("- Nodes anchored `chosen`")


def test_the_per_domain_line_names_each_domain_with_its_own_count():
    """A fixture where each domain's node count differs from the others, so a
    placeholder, or a count swapped between two domains, could not still
    match by coincidence."""
    nodes = {
        n.id: n
        for n in (
            _node("n1", domains=("maths",)),
            _node("n2", domains=("stats", "credit")),
            _node("n3", domains=("stats", "credit")),
            _node("n4", domains=("credit",)),
        )
    }
    corpus = Corpus(nodes=nodes, paths={})
    review = render_review(corpus)
    head = review.split("## ", 1)[0]
    domain_line = next(l for l in head.splitlines() if l.startswith("Nodes per domain:"))
    assert "maths 1" in domain_line
    assert "stats 2" in domain_line
    assert "credit 3" in domain_line


def test_the_review_lists_orphans_separately():
    """A node in no path is a judgement for gate 2 and no check rejects one,
    so the review is the only place it becomes visible."""
    corpus = corpus_with_an_orphan("ruin-theory")
    review = render_review(corpus)
    assert "ruin-theory" in _orphan_section(review)


def test_the_review_groups_orphans_by_domain_set():
    """Orphans group by their domain set, largest group first and rows
    alphabetical within a group, so a reader can dispatch a large
    single-domain block in one judgement instead of reading each row."""
    corpus = two_path_corpus()
    corpus.nodes["orphan-b"] = _node("orphan-b", domains=("fin-man",))
    corpus.nodes["orphan-a"] = _node("orphan-a", domains=("fin-man",))
    corpus.nodes["orphan-c"] = _node("orphan-c", domains=("eco",))
    review = render_review(corpus)
    section = _orphan_section(review)
    assert "### fin-man" in section
    assert "### eco" in section
    assert section.index("### fin-man") < section.index("### eco")
    fin_man_group = section[section.index("### fin-man"):section.index("### eco")]
    assert fin_man_group.index("`orphan-a`") < fin_man_group.index("`orphan-b`")


def test_a_node_line_carries_its_anchor_and_prerequisite_count():
    corpus = two_path_corpus()
    review = render_review(corpus)
    node = corpus.nodes["hazard-rate"]
    line = next(l for l in review.splitlines() if l.startswith(f"| `{node.id}`"))
    assert node.anchor[0] in line
    assert f"| {len(node.requires)} " in line


def test_the_reqs_column_counts_requires_length():
    """A fixture node with two requires and one anchor, so rendering the
    anchor count in the Reqs column instead of the requires count prints a
    different, and therefore wrong, digit."""
    node = _node("triple-check", requires=("a", "b"), anchor=("chosen",))
    corpus = Corpus(nodes={node.id: node}, paths={"solo": _path("solo", (node.id,))})
    review = render_review(corpus)
    line = next(l for l in review.splitlines() if l.startswith(f"| `{node.id}`"))
    assert f"| {len(node.requires)} " in line


def test_a_missing_node_id_renders_missing():
    """A path can name a node id absent from the corpus, though check 4, path
    teachability, catches that in the committed corpus before it ever reaches
    this renderer. A fixture is the only way to exercise the MISSING row."""
    corpus = two_path_corpus()
    path = _path("phantom-path", ("does-not-exist",))
    corpus.paths[path.id] = path
    review = render_review(corpus)
    section = _path_section(review, path)
    assert "| `does-not-exist` | **MISSING** | | | |" in section


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
