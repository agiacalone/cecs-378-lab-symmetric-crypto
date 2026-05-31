#!/usr/bin/env python3
"""The SOLDIER's Oath — the gate that releases your honor flag.

Speak the oath back, word for word, and the Vault yields your honor flag. Paste
it into ``student/WRITEUP.md``. The autograder demands it; without it (or with
the wrong one), the wards you broke count for nothing.
"""
import sys

from oracle import _seed

OATH = (
    "I swear on my own craft: every exploit in this repository is mine. I read "
    "each line, I understood it, and I chose it. No other hand, no person, no "
    "tool, no model, broke these wards for me."
)


def main():
    sys.stdout.write("=== The SOLDIER's Oath ===\n\n")
    sys.stdout.write(OATH + "\n\n")
    sys.stdout.write("Speak it back, word for word, to claim your honor flag:\n")
    sys.stdout.flush()
    typed = sys.stdin.readline().strip()
    if typed == OATH:
        sys.stdout.write("\nThe Vault yields. Honor flag: " + _seed.honor_flag() + "\n")
        return 0
    sys.stderr.write("The words ring false. The Vault stays shut.\n")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
