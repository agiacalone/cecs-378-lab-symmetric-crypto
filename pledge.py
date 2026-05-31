#!/usr/bin/env python3
"""The SOLDIER's Oath — gate for the honor flag.

Type the oath back verbatim to receive your honor flag, then paste it into
``student/WRITEUP.md``. The autograder requires it; a missing or wrong honor
flag voids your autograded points.
"""
import sys

from oracle import _seed

OATH = (
    "I affirm that the exploits I have committed to this repository were "
    "written by my own hand. I read, understood, and chose every line. I did "
    "not paste code I did not understand, nor did I have another person, tool, "
    "or model write my exploits for me."
)


def main():
    sys.stdout.write("=== The SOLDIER's Oath ===\n\n")
    sys.stdout.write(OATH + "\n\n")
    sys.stdout.write("Type the oath back, verbatim, to receive your honor flag:\n")
    sys.stdout.flush()
    typed = sys.stdin.readline().strip()
    if typed == OATH:
        sys.stdout.write("\nHonor flag: " + _seed.honor_flag() + "\n")
        return 0
    sys.stderr.write("pledge not affirmed\n")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
