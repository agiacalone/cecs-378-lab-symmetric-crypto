```
        ╔═══════════════════════════════════════════════════╗
        ║   S P E L L B R E A K E R                          ║
        ║   the vault sealed by four flawed wards            ║
        ╚═══════════════════════════════════════════════════╝
```

# CECS 378 Lab: Spellbreaker

**The Tower drinks the world dry.**

For a century the Company has sunk its wells into the planet's veins and pumped
the raw magic up into its Tower. Bottling the lifeblood of the world as
**Materia**, crystallized spellfire, it sells back to the very cities it has
dimmed. What the Company guards most jealously isn't gold, and isn't territory.
It's *memory*: the ledgers, the keys, the proof of everything it has taken. All
sealed in the **Vault** beneath the Tower, behind four arcane **wards**.

You are a **Spellbreaker**. The operative a resistance cell sends in once brute
force has already failed. The Vault was never built to be forced. It was built
to be *outsmarted*.

Those wards were woven by the Company's chief enchanter, **Archmage Sephira**, 
a prodigy who was certain no one alive could unravel her craft. She was right
about her own brilliance and wrong about almost everything else. She socketed
the **same Materia** into every seal so she'd never stoop to recharging them.
She let her **patterns show**, trusting that nobody would look closely. She
bound a ward that will **answer any question** you put to it, never dreaming of
a thief who would ask the right ones. Every shortcut she took is a real
cryptographic sin — a reused key, a deterministic cipher, an oracle that leaks —
and every one of them is a door she left ajar.

> In CECS 326 you learned to *weave* a cipher. Here you learn that anything
> woven can be **unwoven**. While the fantasy element is a costume, the four
> attacks beneath it are exactly how real systems fall — and exactly how real
> organizations get owned.

## `[--[ THE FOUR WARDS ]--]`

Four guardians stand between you and the Vault, each bound to one of Sephira's
shortcuts. The deeper you descend, the less they forgive.

| Boss | Spell | The flaw | Difficulty |
| --- | --- | --- | --- |
| **I · The Wisp** | *Sense* | ECB determinism (detection) | trivial |
| **II · The Rune Golem** | *Fire→Firaga* | ECB byte-at-a-time recovery | the real fight |
| **III · The Mirror Knight** | *Alter* | CBC malleability (bit-flipping) | hard |
| **IV · OMEGA WARD** | *Ultima* | CBC padding oracle | Ω — top players only |

- **The Wisp** barely counts as a guardian. Cast *Sense* and its repeating
  pattern flickers into the open.
- **The Rune Golem** is your first true fight: pry its secret loose one rune at
  a time until the whole word stands bare.
- **The Mirror Knight** answers only to a sigil of passage. So forge one it
  cannot tell from the real thing.
- **OMEGA WARD** is Sephira's masterpiece and her worst mistake. It will confirm
  or deny any guess you make, and that, patiently, is all you need.

Wards I–III are the climb. **OMEGA WARD is an optional superboss**. Clear it
for glory.

## `[--[ HOW TO BEGIN ]--]`

1. Accept the GitHub Classroom assignment (you're reading its repo).
2. Set up Python and the crypto library:
   ```sh
   pip install -r requirements.txt
   ```
   Full setup (virtualenv, troubleshooting): `docs/setup.md`.
3. The four wards live in `oracle/vault.py`. **Open it. Read it. Take it
   apart.** Studying exactly how a ward is built is the first half of breaking
   it — that *is* cryptanalysis. Reading the lock will never hand you the key,
   though: each ward's flag is derived from a secret that exists only inside the
   grading vault, so the one and only way to claim a flag is to genuinely defeat
   the ward. Write your attack in `student/exploitN.py`.
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

## `[--[ BEHIND THE CURTAIN ]--]`

Curious how the Vault tells *your* wards from everyone else's? Open
`oracle/_seed.py`. Every key, IV, and flag is derived with **SHA-256** from your
repository's name — a cryptographic hash pressed into service as a
*key-derivation function*. That one move buys three properties at once:

- **Determinism** — the same repo always hashes to the same wards, so grading is
  repeatable.
- **Uniqueness** — no two repositories hash alike, so your wards (and flags) are
  yours alone; a borrowed exploit recovers nothing.
- **One-wayness** — you can't run a flag back through the hash to forge its key.

You spend this lab attacking four ways symmetric crypto goes *wrong*. The
machinery that makes the lab fair is crypto done *right* — reused keys, ECB,
padding oracles, and now **hashing as a KDF**: applied symmetric crypto from
both sides of the blade.

## `[--[ HONOR CODE ]--]`

Read everything: public tutorials, the oracle source, the docs, each other's
*ideas*. Curiosity is the whole job. What you may **not** do is submit an
exploit you didn't write and understand. And you couldn't coast on a
classmate's even if you tried: their wards aren't yours — the flags differ — and
a borrowed exploit recovers nothing. Write your own. It's the only thing that
works.

```
[--EOF--]
```
