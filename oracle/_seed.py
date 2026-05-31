"""Per-student parameter derivation for the Spellbreaker lab.

Two derivation regimes:

* **Ward secrets / flags** are salted by a MASTER key. In CI (real mode) the
  master comes from the ``SPELLBREAKER_MASTER`` Actions secret, so the real
  flag cannot be computed locally — the student's exploit must actually run
  the attack against the oracle. Locally (practice mode) the master falls back
  to a public constant, giving a deterministic practice flag to develop
  against.

* **The honor flag** derives from the repo id ONLY (no master), so the value a
  student obtains locally via ``pledge.py`` matches what CI expects.

The per-student identity is the repository ("owner/name"): ``GITHUB_REPOSITORY``
in CI, the git ``remote.origin.url`` locally, else ``local/practice``.
"""
import hashlib
import os
import subprocess

PRACTICE_MASTER = b"spellbreaker-practice-master-v1"


def repo_id():
    rid = os.environ.get("GITHUB_REPOSITORY")
    if rid:
        return rid.strip()
    try:
        url = subprocess.check_output(
            ["git", "config", "--get", "remote.origin.url"],
            stderr=subprocess.DEVNULL,
        ).decode().strip()
        if url:
            return url
    except Exception:
        pass
    return "local/practice"


def _master():
    m = os.environ.get("SPELLBREAKER_MASTER")
    return m.encode() if m else PRACTICE_MASTER


def is_real_mode():
    return bool(os.environ.get("SPELLBREAKER_MASTER"))


def _digest(*parts, master=True):
    h = hashlib.sha256()
    if master:
        h.update(_master())
    h.update(repo_id().encode())
    for p in parts:
        h.update(b"|")
        h.update(p if isinstance(p, bytes) else p.encode())
    return h.digest()


def ward_key(ward):
    return _digest("key", ward)[:16]


def ward_iv(ward):
    return _digest("iv", ward)[:16]


def ward_index(ward, n):
    return _digest("index", ward)[0] % n


def ward_flag(ward):
    return f"CECS378{{{ward}_{_digest('flag', ward).hex()[:24]}}}"


def honor_flag():
    return f"CECS378{{honor_{_digest('honor', master=False).hex()[:24]}}}"
