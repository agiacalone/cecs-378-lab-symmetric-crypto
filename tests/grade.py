#!/usr/bin/env python3
"""Autograder entry point — run one ward and check the recovered flag.

Usage: ``python tests/grade.py wardN`` (run from the repo root).

Gate: the honor flag must be present in ``student/WRITEUP.md`` or every ward
fails. Then the student's ``student/exploitN.py`` is executed and its stdout is
searched for the per-student flag (computed in the SAME environment, so in CI's
real mode this is the real flag — a hardcoded practice flag won't match).
"""
import os
import subprocess
import sys
from pathlib import Path

from oracle import _seed

ROOT = Path(__file__).resolve().parents[1]
# Student dir is overridable so tests can grade an isolated fixture dir without
# touching the tracked student/ scaffolds.
STUDENT = Path(os.environ.get("SPELLBREAKER_STUDENT_DIR", ROOT / "student"))


def honor_ok():
    writeup = STUDENT / "WRITEUP.md"
    return writeup.exists() and _seed.honor_flag() in writeup.read_text()


def main():
    ward = sys.argv[1]                 # e.g. "ward2"
    num = ward[-1]                     # "2"
    if not honor_ok():
        print(f"FAIL {ward}: honor flag missing or incorrect in student/WRITEUP.md")
        return 1
    expected = _seed.ward_flag(ward)
    exploit = STUDENT / f"exploit{num}.py"
    if not exploit.exists():
        print(f"FAIL {ward}: {exploit} not found")
        return 1
    proc = subprocess.run(
        [sys.executable, str(exploit)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=60,
    )
    if expected in proc.stdout:
        print(f"PASS {ward}")
        return 0
    print(f"FAIL {ward}: expected flag not found in exploit output")
    sys.stderr.write(proc.stdout + proc.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
