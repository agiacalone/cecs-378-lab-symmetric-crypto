# Setup -- sharpening your tools

No Spellbreaker walks into the Vault unarmed. Yours is a short bench: Python
3.10+, one crypto library, and Docker (for the practice oracle).

## Setup in Codespaces (one-click)

The fastest bench is the one you don't have to build. Accept the Classroom
assignment, then on your assignment repo click the green **Code** button ->
**Codespaces** -> **Create codespace on main**. The first build takes about 2 to
4 minutes while the forge warms up.

When the terminal attaches, the practice oracle is **already running** and
`$SPELLBREAKER_ORACLE` is **already set** for you. There is no `docker compose
up`, no venv, and no exports to do in a Codespace. Just cast:

```sh
python student/exploit1.py
```

In a Codespace you attack the local **practice** oracle: open test mode, public
key, no secrets. Grading is a separate ritual that runs in GitHub Actions
against the remote **grading** oracle. Pasting a hardcoded proof you saw locally
fails grading, so write a true attack.

### Codespaces hygiene -- save your quota

Codespaces are billable cloud VMs. GitHub Education gives you ~180
core-hours/month, which is plenty for this lab if you stop yours when you walk
away. It is *not* infinite if you forget.

> **STOP, don't DELETE.**
>
> *Stop* pauses the VM with the disk intact: zero quota while stopped, instant
> resume next session, all your uncommitted work still there.
>
> *Delete* wipes everything: next session = fresh rebuild, AND any uncommitted
> edits are gone forever.
>
> The button labelled "Delete" is for when you want to start over from scratch.
> It is not for "I'm done for the day." If you walk away from the lab, hit
> **Stop**.

Habits that keep you in the safe zone:
- **Stop when you walk away.** Codespaces auto-suspend after about 30 minutes
  idle, but stopping explicitly is faster. `gh codespace stop` (interactive
  picker) or right-click in the GitHub Codespaces panel -> Stop. Never click
  Delete unless you actually want a clean rebuild.
- **A long attack run counts as active time.** A full OMEGA WARD padding-oracle
  grind (Ward IV) can churn for a while, and every minute it runs is billed
  active time. Let it finish, then stop the codespace when you step away.
- **`git commit && git push` is your save button.** If a Codespace ever gets
  deleted (by you, a quota cap, or a platform hiccup), pushed commits live on
  GitHub and survive. Push every meaningful step.
- **Watch your usage.** `gh codespace list` shows what you have running. Quota
  detail: <https://github.com/settings/billing/summary>.
- **One Codespace per student per assignment.** Don't share. Your repo id seeds
  your per-student oracle, so a classmate's Codespace has different ward secrets
  and a different honor flag, and the honor code is real.

If you run out of quota mid-assignment: switch to local Docker (below) or wait
for the monthly reset.

## Quick start

Prefer your own machine? You'll need Python 3.10+, one crypto library, and
Docker for the practice oracle.

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
