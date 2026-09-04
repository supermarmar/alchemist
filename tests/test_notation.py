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
        "a node spending both objects in ml would fail check 1 with no remedy"
    )
    assert note("obj.discount-factor", "actuarial").endswith(
        "which is why exposure is canonically e_i here"
    )
    assert note("obj.coefficients", "ml").endswith(
        "where beta would imply linearity"
    )


def test_the_hazard_carries_an_ml_alias():
    """Deep survival models are machine learning, and check 1 has no fallback
    to the canonical rendering, so an ml node spending the hazard fails without
    this alias."""
    objects = load_objects(REPO)
    assert objects.rendering(Spend("obj.hazard", "ml")) == "h(t)"


def test_the_regularisation_note_survived_its_commas():
    """Three notes were truncated at their first comma before load_objects
    started rejecting unknown alias keys. This one lost the reason it existed."""
    objects = load_objects(REPO)
    alias = objects.by_id["obj.regularisation"].for_domain("ml")
    assert "hazard" in alias.note
    assert len(alias.note) > 60


RESERVING = {
    "obj.cohort-index": {"gi": "i", "credit": "i"},
    "obj.development-index": {"gi": "j", "credit": "j"},
    "obj.development-factor": {"gi": "f_j", "credit": "r_j"},
    "obj.ultimate": {"gi": "U_i", "credit": "U_i"},
}


@pytest.mark.parametrize("object_id,expected", sorted(RESERVING.items()))
def test_the_reserving_vocabulary_is_seeded(object_id, expected):
    """The twelve seeded objects came from the ETH course's modelling frame,
    which is not a reserving frame, so this vocabulary was missing entirely.
    Pinning the symbol as well as the domain matters here: f_j against r_j is
    exactly why the credit alias differs from the general-insurance one, and a
    typo of one for the other would still resolve, still pass check 1 and
    check 2, and still regenerate cleanly through check 7."""
    objects = load_objects(REPO)
    assert object_id in objects.by_id
    for domain, symbol in expected.items():
        assert objects.rendering(Spend(object_id, domain)) == symbol


def test_the_contract_carries_at_least_seventeen_objects():
    """A floor rather than an exact count. Step 4 tells the implementer to seed
    whatever the vocabulary sweep justifies, so a fixed count would turn a
    correct judgement into a red test. The four reserving objects are pinned
    by name above."""
    assert len(load_objects(REPO).by_id) >= 17
