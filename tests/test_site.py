from pathlib import Path

from scripts.alchemist.checks import check_generated_current
from scripts.alchemist.model import Alias, MathObject, Objects
from scripts.alchemist.site import render_symbols

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


def test_the_output_is_stable_across_calls():
    assert render_symbols(OBJECTS) == render_symbols(OBJECTS)


def test_check_7_passes_when_the_file_matches(tmp_path):
    (tmp_path / "notation").mkdir()
    (tmp_path / "notation" / "symbols.md").write_text(render_symbols(OBJECTS))
    assert check_generated_current(OBJECTS, tmp_path).failures == []


def test_check_7_fails_when_the_file_has_drifted(tmp_path):
    (tmp_path / "notation").mkdir()
    (tmp_path / "notation" / "symbols.md").write_text("# stale\n")
    result = check_generated_current(OBJECTS, tmp_path)
    assert len(result.failures) == 1 and "build_site" in result.failures[0]


def test_check_7_fails_when_the_file_is_missing(tmp_path):
    (tmp_path / "notation").mkdir()
    result = check_generated_current(OBJECTS, tmp_path)
    assert len(result.failures) == 1 and "missing" in result.failures[0]
