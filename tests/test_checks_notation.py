from scripts.alchemist.checks import (
    check_declared_symbols_resolve,
    check_symbol_uniqueness_within_domain,
)
from scripts.alchemist.model import (
    Alias, Corpus, MathObject, Node, Objects, Spend,
)
from pathlib import Path


def node(node_id: str, domains, spends) -> Node:
    return Node(
        id=node_id, title=node_id, domains=tuple(domains), status="stub",
        requires=(), spends=tuple(spends), anchor=(), vault_articles=(),
        vault_sources=(), taught_in=None, body="", path=Path(f"nodes/{node_id}.md"),
    )


HAZARD = MathObject(
    id="obj.hazard", name="Hazard", canonical="h(t)", definition="d",
    aliases=(Alias("life", r"\mu_x", "force of mortality"),
             Alias("gi", r"\lambda", "claim intensity")),
)
INTENSITY_CLASH = MathObject(
    id="obj.other", name="Other", canonical="z", definition="d",
    aliases=(Alias("gi", r"\lambda", "something else"),),
)


def test_a_resolvable_spend_passes():
    corpus = Corpus(nodes={"n": node("n", ["life"], [Spend("obj.hazard", "life")])}, paths={})
    assert check_declared_symbols_resolve(corpus, Objects({"obj.hazard": HAZARD})).failures == []


def test_an_unknown_object_fails():
    """Asserts the message prefix, not just the object id. A bare
    `except LookupError` would also mention obj.ghost, because KeyError is a
    LookupError subclass, so an id-substring assertion passes under the very bug
    the explicit `not in objects.by_id` guard exists to prevent."""
    corpus = Corpus(nodes={"n": node("n", ["life"], [Spend("obj.ghost", "life")])}, paths={})
    result = check_declared_symbols_resolve(corpus, Objects({"obj.hazard": HAZARD}))
    assert len(result.failures) == 1
    assert "spends unknown object" in result.failures[0]
    assert "obj.ghost" in result.failures[0]


def test_spending_an_object_in_an_undeclared_domain_fails():
    """Covers check 1's third branch. Without this test, deleting the
    domain-membership guard leaves every other test green."""
    corpus = Corpus(nodes={"n": node("n", ["credit"], [Spend("obj.hazard", "life")])}, paths={})
    result = check_declared_symbols_resolve(corpus, Objects({"obj.hazard": HAZARD}))
    assert len(result.failures) == 1
    assert "not among its own domains" in result.failures[0]


def test_a_domain_with_no_alias_fails():
    corpus = Corpus(nodes={"n": node("n", ["credit"], [Spend("obj.hazard", "credit")])}, paths={})
    result = check_declared_symbols_resolve(corpus, Objects({"obj.hazard": HAZARD}))
    assert len(result.failures) == 1 and "no alias" in result.failures[0]


def test_two_spends_rendering_the_same_symbol_in_one_node_fails():
    corpus = Corpus(
        nodes={"n": node("n", ["gi"], [Spend("obj.hazard", "gi"), Spend("obj.other", "gi")])},
        paths={},
    )
    result = check_declared_symbols_resolve(
        corpus, Objects({"obj.hazard": HAZARD, "obj.other": INTENSITY_CLASH})
    )
    assert len(result.failures) == 1 and "both render" in result.failures[0]


def test_one_object_spelled_alike_in_two_domains_is_not_a_collision():
    """obj.survival is S(t) in both statistics and credit. That is one meaning,
    so keying the collision map on the symbol alone would fail a correct node."""
    twin = MathObject(
        id="obj.survival", name="Survival", canonical="S(t)", definition="d",
        aliases=(Alias("stats", "S(t)", "survival function"),
                 Alias("credit", "S(t)", "survival function")),
    )
    corpus = Corpus(
        nodes={"n": node("n", ["stats", "credit"],
                         [Spend("obj.survival", "stats"), Spend("obj.survival", "credit")])},
        paths={},
    )
    assert check_declared_symbols_resolve(corpus, Objects({"obj.survival": twin})).failures == []


def test_a_domain_with_one_symbol_on_two_objects_fails_globally():
    result = check_symbol_uniqueness_within_domain(
        Objects({"obj.hazard": HAZARD, "obj.other": INTENSITY_CLASH})
    )
    assert len(result.failures) == 1 and "gi" in result.failures[0]


def test_the_same_symbol_in_different_domains_is_fine():
    twin = MathObject(
        id="obj.twin", name="Twin", canonical="z", definition="d",
        aliases=(Alias("life", r"\lambda", "different domain"),),
    )
    assert check_symbol_uniqueness_within_domain(
        Objects({"obj.hazard": HAZARD, "obj.twin": twin})
    ).failures == []
