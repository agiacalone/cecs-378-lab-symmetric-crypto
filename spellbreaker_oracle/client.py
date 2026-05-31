"""HTTP client the student exploit imports. Reads $SPELLBREAKER_ORACLE (URL),
$SPELLBREAKER_ORACLE_TOKEN (grading only), and $GITHUB_REPOSITORY (repo id).
The same code talks to a local test oracle and the remote grading oracle."""
import os

import requests


class Oracle:
    def __init__(self, base: str | None = None, token: str | None = None, repo: str | None = None):
        self.base = (base or os.environ.get("SPELLBREAKER_ORACLE", "http://localhost:8000")).rstrip("/")
        self.token = token or os.environ.get("SPELLBREAKER_ORACLE_TOKEN")
        self.repo = repo or os.environ.get("GITHUB_REPOSITORY", "local/practice")
        self._session = requests  # overridable in tests with a FastAPI TestClient

    def _post(self, path: str, body: dict) -> dict:
        headers = {"X-Grading-Token": self.token} if self.token else {}
        r = self._session.post(f"{self.base}{path}",
                               json={**body, "repo": self.repo}, headers=headers, timeout=30)
        r.raise_for_status()
        return r.json()

    # Ward I
    def ward1_challenge(self) -> list[str]:
        return self._post("/spellbreaker/ward1/challenge", {})["ciphertexts"]

    # Ward II
    def ward2_encrypt(self, data: bytes) -> bytes:
        return bytes.fromhex(self._post("/spellbreaker/ward2/encrypt", {"data": data.hex()})["ct"])

    # Ward III
    def ward3_token(self, userdata: bytes) -> bytes:
        return bytes.fromhex(self._post("/spellbreaker/ward3/token", {"userdata": userdata.hex()})["token"])

    # Ward IV
    def ward4_challenge(self) -> tuple[bytes, bytes]:
        r = self._post("/spellbreaker/ward4/challenge", {})
        return bytes.fromhex(r["iv"]), bytes.fromhex(r["ct"])

    def ward4_padding(self, iv: bytes, ct: bytes) -> bool:
        return self._post("/spellbreaker/ward4/padding", {"iv": iv.hex(), "ct": ct.hex()})["valid"]

    # Verify (proof type depends on the ward)
    def verify(self, challenge: str, proof: str) -> bool:
        return self._post("/spellbreaker/verify", {"challenge": challenge, "proof": proof})["pass"]
