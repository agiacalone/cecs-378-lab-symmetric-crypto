"""Local honor-flag derivation. Not security-critical (the oracle enforces real
attacks); the pledge is a ritual. Derived from the repo id + a public constant,
so the value a student gets locally matches what grade.py expects in CI."""
import hashlib
import hmac
import os
import subprocess

_HONOR_SALT = b"spellbreaker-honor-v1"


def _normalize_remote_url(url: str) -> str:
    """Reduce a git remote URL to the canonical owner/repo form.

    GitHub Actions and Codespaces both set GITHUB_REPOSITORY to owner/repo,
    but a student's local clone only has a remote URL. We map common forms
    (scp-like, https, ssh) to owner/repo so the local flag matches CI.
    """
    s = url.strip()
    if s.endswith(".git"):
        s = s[: -len(".git")]
    if "://" in s:
        # drop the scheme, then drop the host up to the first slash
        s = s.split("://", 1)[1]
        s = s.split("/", 1)[1] if "/" in s else s
    elif "@" in s and ":" in s:
        # scp-like: git@host:owner/repo
        s = s.split(":", 1)[1]
    return s.strip("/")


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
            return _normalize_remote_url(url)
    except Exception:
        pass
    return "local/practice"


def honor_flag() -> str:
    h = hmac.new(_HONOR_SALT, repo_id().encode(), hashlib.sha256).hexdigest()[:24]
    return f"CECS378{{honor_{h}}}"
