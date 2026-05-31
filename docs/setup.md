# Setup — sharpening your tools

No Spellbreaker walks into the Vault unarmed. Yours is a short bench: Python
3.10+ and one crypto library.

## Quick start

```sh
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running an exploit

Always run from the repo root so `import oracle` resolves:

```sh
python student/exploit1.py
```

The scaffolds insert the repo root on `sys.path` for you — leave that boilerplate.

## Running the reference tests (optional)

The instructor's reference attacks live in `tests/` and double as a sanity
check that the wards behave:

```sh
pytest -v
```

## Practice wards vs. the real Vault

Locally you face **practice** wards: deterministic, repeatable, and their flags
are derivable — perfect for honing an attack. When you push, the grader runs
your same exploit against the **real** wards, whose secret lives only in the
grading vault, so hardcoding the practice flag gets you nowhere. Write a true
attack and it breaks both.

## Troubleshooting

- `ModuleNotFoundError: No module named 'oracle'` — you're not in the repo
  root, or you bypassed the scaffold's `sys.path` line. Run from the root.
- `ModuleNotFoundError: No module named 'Crypto'` — `pip install -r
  requirements.txt` (the package is `pycryptodome`).
