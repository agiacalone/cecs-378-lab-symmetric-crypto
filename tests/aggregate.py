#!/usr/bin/env python3
"""Aggregate the four ward outcomes + honor status into ``grading/result.json``.

This emits the machine-readable *recon contract* consumed by lectern's
``reg-lab-recon``. It is published as the ``grading-result`` CI run artifact (a
durable, Classroom-independent home that students cannot delete).

Usage (from the workflow, after the ward steps):
    python tests/aggregate.py "$WARD1" "$WARD2" "$WARD3" "$WARD4"
where each arg is the GitHub Actions step ``outcome`` ("success"/"failure"/...).
The in-workflow ``outcome`` expression is authoritative — unlike the jobs-API
step ``conclusion``, which ``continue-on-error: true`` masks to "success".
"""
from __future__ import annotations
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

ASSIGNMENT = "spellbreaker"
POINTS = {"ward1": 10, "ward2": 35, "ward3": 15, "ward4": 10}
MAX_TOTAL = 100  # wards (70) + grimoire writeup (30, graded manually)


def honor_ok() -> bool:
    """True iff the student's WRITEUP.md carries this repo's honor flag."""
    try:
        import honor
        w = ROOT / "student" / "WRITEUP.md"
        return w.exists() and honor.honor_flag() in w.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return False


def build(outcomes: list[str]) -> dict:
    keys = ["ward1", "ward2", "ward3", "ward4"]
    by_key = dict(zip(keys, outcomes + [""] * (len(keys) - len(outcomes))))
    ok = honor_ok()
    challenges = {}
    for k in keys:
        passed = ok and by_key.get(k) == "success"  # honor gate voids all wards
        pts = POINTS[k]
        challenges[k] = {"pass": passed, "points": pts if passed else 0, "max": pts}
    total = sum(c["points"] for c in challenges.values())
    return {
        "schema": 1,
        "assignment": ASSIGNMENT,
        "commit": os.environ.get("GITHUB_SHA", ""),
        "honor_ok": ok,
        "challenges": challenges,
        "points": total,
        "max": MAX_TOTAL,
    }


def main(argv: list[str]) -> int:
    result = build(argv)
    out = ROOT / "grading" / "result.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
