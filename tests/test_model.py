from pathlib import Path

import pytest

from scripts.alchemist.model import DOMAINS, Spend, parse_node, parse_path

VALID = """---
id: hazard-rate
title: Hazard rate
domains: [stats, credit]
status: stub
requires: [survival-function]
spends:
  - {object: obj.hazard, domain: credit}
anchor: [ifoa.cs2.3.2]
vault_articles: [methods/exponential-dispersion-family-and-glm]
vault_sources: []
taught_in: null
---

The instantaneous rate of default.
"""


def write(tmp_path: Path, name: str, text: str) -> Path:
    target = tmp_path / name
    target.write_text(text)
    return target


def test_parses_a_valid_node(tmp_path):
    node = parse_node(write(tmp_path, "hazard-rate.md", VALID))
    assert node.id == "hazard-rate"
    assert node.domains == ("stats", "credit")
    assert node.spends == (Spend("obj.hazard", "credit"),)
    assert node.taught_in is None
    assert node.body.strip() == "The instantaneous rate of default."


def test_rejects_a_filename_that_disagrees_with_the_id(tmp_path):
    with pytest.raises(ValueError, match="does not match id"):
        parse_node(write(tmp_path, "hazard.md", VALID))


def test_rejects_a_domain_outside_the_vocabulary(tmp_path):
    bad = VALID.replace("[stats, credit]", "[stats, insurance]")
    with pytest.raises(ValueError, match="unknown domains"):
        parse_node(write(tmp_path, "hazard-rate.md", bad))


def test_rejects_a_malformed_anchor(tmp_path):
    bad = VALID.replace("[ifoa.cs2.3.2]", "[CS2 section 3.2]")
    with pytest.raises(ValueError, match="malformed anchor"):
        parse_node(write(tmp_path, "hazard-rate.md", bad))


def test_domain_vocabulary_is_closed():
    assert "regulation" in DOMAINS and "insurance" not in DOMAINS


VALID_PATH = """id: survival-braid
title: Survival analysis across life, general insurance and credit
builds_on: [maths-stats-prerequisites]
preamble: One object under four names.
nodes: [survival-function, hazard-rate]
"""


def test_parses_a_valid_path(tmp_path):
    target = tmp_path / "survival-braid.yaml"
    target.write_text(VALID_PATH)
    path = parse_path(target)
    assert path.id == "survival-braid"
    assert path.builds_on == ("maths-stats-prerequisites",)
    assert path.nodes == ("survival-function", "hazard-rate")


def test_a_path_defaults_builds_on_and_preamble_when_absent(tmp_path):
    target = tmp_path / "bare.yaml"
    target.write_text("id: bare\ntitle: Bare\nnodes: []\n")
    path = parse_path(target)
    assert path.builds_on == () and path.preamble == "" and path.nodes == ()


def test_a_path_filename_that_disagrees_with_the_id_is_rejected(tmp_path):
    target = tmp_path / "wrong.yaml"
    target.write_text(VALID_PATH)
    with pytest.raises(ValueError, match="does not match id"):
        parse_path(target)
