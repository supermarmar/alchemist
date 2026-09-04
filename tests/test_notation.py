import pytest

from scripts.alchemist.model import REPO, Spend, load_objects


@pytest.fixture(scope="module")
def objects():
    return load_objects(REPO)


def test_a_domain_alias_wins_over_the_canonical(objects):
    assert objects.rendering(Spend("obj.hazard", "life")) == r"\mu_x"
    assert objects.rendering(Spend("obj.hazard", "credit")) == "h(t)"


def test_an_object_with_no_alias_for_the_domain_is_a_lookup_error(objects):
    with pytest.raises(LookupError, match="no alias"):
        objects.rendering(Spend("obj.discount-factor", "credit"))


def test_an_unknown_object_is_a_key_error(objects):
    with pytest.raises(KeyError):
        objects.rendering(Spend("obj.nonsense", "credit"))


def test_the_seeded_collisions_are_all_present(objects):
    assert {"obj.hazard", "obj.exposure", "obj.discount-factor"} <= objects.by_id.keys()


def test_bare_lambda_is_never_the_regularisation_weight(objects):
    """The collision the contract exists to prevent: lambda is the intensity."""
    assert objects.rendering(Spend("obj.regularisation", "ml")) != r"\lambda"
    assert objects.rendering(Spend("obj.hazard", "gi")) == r"\lambda"


CONTRACT = """- id: obj.thing
  name: Thing
  canonical: 't'
  definition: A thing.
  aliases:
    - {domain: stats, symbol: 't', name: thing, note: %s}
"""


def write_contract(tmp_path, note: str):
    (tmp_path / "notation").mkdir()
    (tmp_path / "notation" / "objects.yaml").write_text(CONTRACT % note)
    return tmp_path


def test_a_quoted_note_containing_a_comma_survives_whole(tmp_path):
    """The three notes that carry the corpus's hardest notation decisions all
    contain a comma. Quoting is what keeps them, so assert the tail rather than
    the head: a truncating parse keeps the head and drops exactly the reasoning.
    """
    root = write_contract(tmp_path, '"kept deliberately, because the tail is the reason"')
    alias = load_objects(root).by_id["obj.thing"].aliases[0]
    assert alias.note == "kept deliberately, because the tail is the reason"


def test_an_unquoted_note_containing_a_comma_is_rejected(tmp_path):
    """The detection half. Before this guard the loader read `note` alone and
    never looked at the bare key YAML made of the remainder, so the truncated
    text reached the published symbol table with nothing complaining.
    """
    root = write_contract(tmp_path, "kept deliberately, because the tail is the reason")
    with pytest.raises(ValueError, match="unknown alias keys"):
        load_objects(root)
    with pytest.raises(ValueError, match="obj.thing"):
        load_objects(root)


def test_every_note_in_the_real_contract_survives_the_parse(objects):
    """Guards the data rather than the loader. All three of these were truncated
    at their first comma in the committed file, and each assertion below is on
    the fragment that was lost.
    """
    def note(object_id: str, domain: str) -> str:
        return objects.by_id[object_id].for_domain(domain).note

    assert note("obj.regularisation", "ml").endswith(
        "because bare lambda is the claim intensity and the hazard"
    )
    assert note("obj.discount-factor", "actuarial").endswith(
        "which is why exposure is canonically e_i here"
    )
    assert note("obj.coefficients", "ml").endswith(
        "where beta would imply linearity"
    )
