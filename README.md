```
        ╔═══════════════════════════════════════════════════╗
        ║   S P E L L B R E A K E R                          ║
        ║   the vault sealed by four flawed wards            ║
        ╚═══════════════════════════════════════════════════╝
```

# CECS 378 Lab: Spellbreaker

A careless megacorp sealed its Vault with four magical **wards**, each woven
from **Materia** — crystallized magic. Their archmage made the oldest mistakes
in the book: he socketed the **same Materia** into every seal, left his
**patterns showing**, and never imagined anyone would **probe** his wards.

You are the **Spellbreaker**. You break in by exploiting exactly those
blunders. In CECS 326 you learned to *cast* a cipher; here you learn to
*unweave* one.

> Every "ward" is a real symmetric-crypto flaw with a real-world body count.
> Reused keys, ECB mode, and padding oracles are how actual companies get
> owned. The fantasy is the wrapper; the attacks are the lesson.

## `[--[ THE FOUR WARDS ]--]`

| Boss | Spell | The flaw | Difficulty |
| --- | --- | --- | --- |
| **I · The Wisp** | *Sense* | ECB determinism (detection) | trivial |
| **II · The Rune Golem** | *Fire→Firaga* | ECB byte-at-a-time recovery | the real fight |
| **III · The Mirror Knight** | *Alter* | CBC malleability (bit-flipping) | hard |
| **IV · OMEGA WARD** | *Ultima* | CBC padding oracle | Ω — top players only |

Wards I–III are the climb. **OMEGA WARD is an optional superboss** — clear it
for glory.

## `[--[ HOW TO BEGIN ]--]`

1. Accept the GitHub Classroom assignment (you're reading its repo).
2. Set up Python and the crypto library:
   ```sh
   pip install -r requirements.txt
   ```
   Full setup (virtualenv, troubleshooting): `docs/setup.md`.
3. Each ward is a black box in `oracle/vault.py`. **Do not read its
   internals** — that's the answer key. Attack it from `student/exploitN.py`.
4. Develop locally against the **practice** oracle (deterministic). When you
   push, the autograder re-runs your exploit against the **real** ward and
   checks the flag you recover.

## `[--[ DELIVERABLES ]--]`

| Path | What goes here |
| --- | --- |
| `student/exploit1.py … exploit4.py` | one attack per ward (Ward IV optional) |
| `student/WRITEUP.md` | the grimoire (template provided; flags go in frontmatter) |
| `student/screenshots/` | a terminal shot of each flag you recovered |

Comment your code. Cite at least one source in your grimoire.

## `[--[ GRADING ]--]`

| Component | Points | How |
| --- | --- | --- |
| Ward I — The Wisp | 10 | autograded |
| Ward II — The Rune Golem | 35 | autograded |
| Ward III — The Mirror Knight | 15 | autograded |
| OMEGA WARD (Ω stretch) | 10 | autograded |
| Grimoire (writeup) | 30 | instructor |

Wards I–III + a thoughtful grimoire ≈ 90%. OMEGA WARD is the stretch.

The **honor flag is a hard gate.** Run `python pledge.py`, affirm the SOLDIER's
Oath, paste the flag into your grimoire. Missing or wrong honor flag voids the
autograded points.

## `[--[ HONOR CODE ]--]`

You may read public tutorials on these attacks. **You will write your own
exploit.** Your wards are not your classmate's wards — their flags differ from
yours, so a borrowed exploit recovers nothing. Sharing is wasted typing.

```
[--EOF--]
```
