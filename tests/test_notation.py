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
