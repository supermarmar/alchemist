import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def run(*args):
    return subprocess.run([sys.executable, str(REPO / "scripts" / "build_manifest.py"), *args],
                          capture_output=True, text=True, cwd=REPO)


def test_an_existing_manifest_is_never_overwritten_without_force(tmp_path):
    """Phase 3 batches the stubs, and the stubs shrink as waves land, so a
    rebuild mid-phase renumbers every remaining batch from 1 and `stray_writes`
    then checks a wave against the wrong owners. The manifest a wave ran from is
    the record, so a second write needs saying twice."""
    out = tmp_path / "manifest.yaml"
    assert run("--phase", "3", "--order", "depth", "--out", str(out)).returncode == 0
    first = out.read_text()
    refused = run("--phase", "3", "--order", "depth", "--out", str(out))
    assert refused.returncode == 2 and "--force" in refused.stderr
    assert out.read_text() == first
    assert run("--phase", "3", "--order", "depth", "--out", str(out), "--force").returncode == 0
