import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def test_the_report_prints_every_figure_the_gate_reads():
    result = subprocess.run(
        [sys.executable, "scripts/build_pages_report.py"],
        capture_output=True, text=True, cwd=REPO,
    )
    assert result.returncode == 0, result.stderr
    for line in ("Pages by status:", "Written pages by domain:", "Display blocks per written page:",
                 "Words per written page:", "'rather than' across written pages:",
                 "Written pages naming none of their unlocks in the closing section:"):
        assert line in result.stdout
    assert "stub" in result.stdout and "drafted" in result.stdout
