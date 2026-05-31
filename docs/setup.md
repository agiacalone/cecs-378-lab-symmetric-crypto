# Setup -- sharpening your tools

No Spellbreaker walks into the Vault unarmed. Yours is a short bench: Python
3.10+, one crypto library, and Docker (for the practice oracle).

## Quick start

```sh
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run the practice oracle

The wards are a service, not a local library. Start a practice oracle with
Docker before running any exploit:

```sh
docker compose up -d
```

The image is pulled automatically on first run. Confirm it is ready:

```sh
curl localhost:8000/healthz
# -> {"ok":true,"mode":"test"}
```

The oracle runs in open test mode (no token required, public test key). By
default, `$SPELLBREAKER_ORACLE` is `http://localhost:8000`, so no extra export
is needed. If you run the oracle on a different host or port, set the variable:

```sh
export SPELLBREAKER_ORACLE=http://localhost:8000
```

## Running an exploit

Always run from the repo root so `from spellbreaker_oracle import Oracle`
resolves. Each exploit talks to the practice oracle over HTTP and prints its
proof on the last line:

```sh
python student/exploit1.py
```

The scaffolds insert the repo root on `sys.path` for you; leave that boilerplate.

## Running the reference tests (optional)

The instructor's reference attacks live in `tests/` and double as a sanity
check that the wards behave. They require a running practice oracle:

```sh
docker compose up -d
pytest -v
```

## Practice oracle vs. the grading oracle

Locally you attack the **practice** oracle: open test mode, no token, repeatable
sessions. When you push, the autograder runs your same exploit against the
**grading** oracle, whose secret lives only on the server. A hardcoded proof from
a local session fails against the grading oracle -- write a true attack and it
breaks both.

## Troubleshooting

- `ModuleNotFoundError: No module named 'spellbreaker_oracle'` -- you are not
  in the repo root, or you bypassed the scaffold's `sys.path` line. Run from
  the root.
- `ModuleNotFoundError: No module named 'Crypto'` -- `pip install -r
  requirements.txt` (the package is `pycryptodome`).
- `ConnectionRefusedError` or `requests.exceptions.ConnectionError` -- the
  practice oracle is not running. Run `docker compose up -d` first.
