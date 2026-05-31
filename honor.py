"""Local honor-flag derivation. Not security-critical (the oracle enforces real
attacks); the pledge is a ritual. Derived from the repo id + a public constant,
so the value a student gets locally matches what grade.py expects in CI."""
import hashlib
import hmac
import os
import subprocess

_HONOR_SALT = b"spellbreaker-honor-v1"


def repo_id() -> str:
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


def honor_flag() -> str:
    h = hmac.new(_HONOR_SALT, repo_id().encode(), hashlib.sha256).hexdigest()[:24]
    return f"CECS378{{honor_{h}}}"
