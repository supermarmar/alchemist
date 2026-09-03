from pathlib import Path

import pytest

from scripts.inline_assets import inline

PAGE = """<!doctype html>
<html><head>
<link rel="stylesheet" href="../vendor/katex/katex.min.css">
<link rel="stylesheet" href="../assets/lecture.css">
<script defer src="../vendor/katex/katex.min.js"></script>
</head><body><p>$x$</p></body></html>
"""


def fake_repo(tmp_path: Path) -> Path:
    (tmp_path / "vendor" / "katex").mkdir(parents=True)
    (tmp_path / "assets").mkdir()
    (tmp_path / "lectures").mkdir()
    (tmp_path / "vendor" / "katex" / "katex.min.css").write_text(".katex{}")
    (tmp_path / "vendor" / "katex" / "katex.min.js").write_text("var katex={};")
    (tmp_path / "assets" / "lecture.css").write_text("body{}")
    (tmp_path / "lectures" / "L.html").write_text(PAGE)
    return tmp_path


def test_all_three_assets_are_inlined(tmp_path):
    root = fake_repo(tmp_path)
    assert inline(root / "lectures" / "L.html", root) == 3


def test_no_external_reference_survives(tmp_path):
    root = fake_repo(tmp_path)
    inline(root / "lectures" / "L.html", root)
    out = (root / "lectures" / "L.html").read_text()
    assert "href=" not in out and "src=" not in out
    assert ".katex{}" in out and "body{}" in out and "var katex={}" in out


def test_it_is_idempotent(tmp_path):
    root = fake_repo(tmp_path)
    target = root / "lectures" / "L.html"
    inline(target, root)
    once = target.read_text()
    assert inline(target, root) == 0
    assert target.read_text() == once


def test_a_missing_asset_raises_rather_than_silently_skipping(tmp_path):
    """Raising is half the property. The other half is that nothing was written:
    a half-inlined lecture that also raised would leave a corrupt file for the
    next step in the chain to print."""
    root = fake_repo(tmp_path)
    target = root / "lectures" / "L.html"
    before = target.read_text()
    (root / "assets" / "lecture.css").unlink()
    with pytest.raises(FileNotFoundError, match="lecture.css"):
        inline(target, root)
    assert target.read_text() == before


def test_a_stylesheet_carrying_its_own_closing_tag_raises(tmp_path):
    """A `</style>` inside the stylesheet ends the element the moment the browser
    reads it, and the remainder of the CSS renders as page text. Nothing in the
    chain exits non-zero, which is the failure class it exists to remove. As with
    the missing-asset case, assert that nothing was written either."""
    root = fake_repo(tmp_path)
    target = root / "lectures" / "L.html"
    before = target.read_text()
    (root / "assets" / "lecture.css").write_text("body{}\n</style><p>spill</p>")
    with pytest.raises(ValueError, match="</style>"):
        inline(target, root)
    assert target.read_text() == before


def test_a_script_carrying_its_own_closing_tag_raises(tmp_path):
    """The same hazard on the script side, where a string literal holding
    `</script>` is the realistic way in."""
    root = fake_repo(tmp_path)
    target = root / "lectures" / "L.html"
    before = target.read_text()
    (root / "vendor" / "katex" / "katex.min.js").write_text(
        'var end = "</script>";'
    )
    with pytest.raises(ValueError, match="</script>"):
        inline(target, root)
    assert target.read_text() == before
