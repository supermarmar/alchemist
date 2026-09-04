from pathlib import Path

from scripts.alchemist.checks import check_generated_current
from scripts.alchemist.model import Alias, Corpus, MathObject, Node, Objects, Spend
from scripts.alchemist.site import render_node_page, render_symbols

HAZARD = MathObject(
    id="obj.hazard", name="Hazard rate", canonical="h(t)",
    definition="The instantaneous rate of the event.",
    aliases=(Alias("life", r"\mu_x", "force of mortality", "age-indexed"),
             Alias("gi", r"\lambda", "claim intensity")),
)
OBJECTS = Objects({"obj.hazard": HAZARD})


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
