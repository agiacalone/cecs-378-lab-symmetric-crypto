# Setup

You need Python 3.10+ and one library.

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

## Practice vs. real mode

Locally you attack a **practice** oracle: deterministic, repeatable, and its
flag is derivable — perfect for development. When you push, CI runs your same
exploit against the **real** oracle whose secret only exists in CI, so you
cannot shortcut by hardcoding the practice flag. Write a real attack and it
works in both.

## Troubleshooting

- `ModuleNotFoundError: No module named 'oracle'` — you're not in the repo
  root, or you bypassed the scaffold's `sys.path` line. Run from the root.
- `ModuleNotFoundError: No module named 'Crypto'` — `pip install -r
  requirements.txt` (the package is `pycryptodome`).
