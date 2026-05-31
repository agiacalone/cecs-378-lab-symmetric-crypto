#!/usr/bin/env python3
"""Autograder entry -- run one ward's exploit, submit its proof to the oracle.

Usage: ``python tests/grade.py wardN`` from the repo root.

Gate: the honor flag must be present in WRITEUP.md or every ward fails. Then the
student's exploitN.py is run; its last stdout line is the proof; that proof is
submitted to the oracle's /verify. The oracle (not this script) decides pass/fail,
so a fake proof or a printed 'PASS' fails."""
import os
import subprocess
import sys
from pathlib import Path

import honor
from spellbreaker_oracle import Oracle

ROOT = Path(__file__).resolve().parents[1]
STUDENT = Path(os.environ.get("SPELLBREAKER_STUDENT_DIR", ROOT / "student"))


def honor_ok() -> bool:
    w = STUDENT / "WRITEUP.md"
    return w.exists() and honor.honor_flag() in w.read_text()


def main() -> int:
    ward = sys.argv[1]            # e.g. "ward2"
    num = ward[-1]
    if not honor_ok():
        print(f"FAIL {ward}: honor flag missing or incorrect in student/WRITEUP.md")
        return 1
    exploit = STUDENT / f"exploit{num}.py"
    if not exploit.exists():
        print(f"FAIL {ward}: {exploit} not found")
        return 1
    proc = subprocess.run([sys.executable, str(exploit)], cwd=ROOT,
                          capture_output=True, text=True, timeout=600)
    lines = [ln for ln in proc.stdout.splitlines() if ln.strip()]
    if not lines:
        print(f"FAIL {ward}: exploit produced no output")
        sys.stderr.write(proc.stderr)
        return 1
    proof = lines[-1].strip()
    if Oracle().verify(ward, proof):
        print(f"PASS {ward}")
        return 0
    print(f"FAIL {ward}: oracle rejected the submitted proof")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
