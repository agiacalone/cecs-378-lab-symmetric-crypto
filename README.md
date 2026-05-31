```
                        ·  ✦  ·
                      ▄▄█████▄▄
                   ▄██▓▓▒▒▒▒▓██▄
                ✧ ▟█▓▒▒░░░░▒▒▓██▙ ·
                 ██▓▒░░░░░░░▒▓████
                 █▓▒░░░░░░░▒▒▓████
                 █▓▒▒░░░░░▒▒▓▓████
                 ██▓▒▒░░░▒▒▓▓█████
                · ▜██▓▓▒▒▒▓▓▓████▛ ✧
                   ▀██▓▓▓▓▓▓███▀
                      ▀▀█████▀▀
                        ·  ✦  ·

            S  P  E  L  L  B  R  E  A  K  E  R
              the vault sealed by four flawed wards
```

# CECS 378 Lab: Spellbreaker

**The Tower drinks the world dry.**

For a century [the Company](https://finalfantasy.fandom.com/wiki/Shinra_Electric_Power_Company) has sunk its wells into the planet's veins and pumped
the raw magic up into its Tower. Bottling [the lifeblood of the world](https://finalfantasy.fandom.com/wiki/Lifestream) as
[**Materia**](https://finalfantasy.fandom.com/wiki/Materia_%28Final_Fantasy_VII%29), crystallized spellfire, it sells back to the very cities it has
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
cryptographic sin: a [reused key](https://en.wikipedia.org/wiki/Key_%28cryptography%29), a [deterministic cipher](https://en.wikipedia.org/wiki/Deterministic_encryption), an oracle that leaks.
And every one of them is a door she left ajar.

> In CECS 326 you learned to *weave* a cipher. Here you learn that anything
> woven can be **unwoven**. The fantasy element is costume; the four
> attacks beneath it are exactly how real systems fall and exactly how real
> organizations get owned.

## `[--[ THE FOUR WARDS ]--]`

Four guardians stand between you and the Vault, each bound to one of Sephira's
shortcuts. The deeper you descend, the less they forgive.

| Boss | Spell | The flaw | Difficulty |
| --- | --- | --- | --- |
| **I · The Wisp** | [*Sense*](https://finalfantasy.fandom.com/wiki/Sense_%28Final_Fantasy_VII%29) | ECB determinism (detection) | trivial |
| **II · The Rune Golem** | [*Fire→Firaga*](https://finalfantasy.fandom.com/wiki/Fire_%28ability%29) | ECB byte-at-a-time recovery | the real fight |
| **III · The Mirror Knight** | [*Manipulate*](https://finalfantasy.fandom.com/wiki/Manipulate_%28Final_Fantasy_VII%29) | CBC malleability (bit-flipping) | hard |
| **IV · OMEGA WARD** | [*Ultima*](https://finalfantasy.fandom.com/wiki/Ultima_%28ability%29) | CBC padding oracle | Ω == top players only |

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
2. Set up Python and start the practice oracle:
   ```sh
   pip install -r requirements.txt
   docker compose up -d
   ```
   Full setup (virtualenv, oracle healthcheck, troubleshooting): `docs/setup.md`.
3. The four wards are a **network service**. Your exploit calls the oracle over
   HTTP using `from spellbreaker_oracle import Oracle`. The oracle runs the
   crypto server-side; you probe it, observe how it responds, and use those
   responses to recover the secret. Studying how each ward leaks, via the
   published oracle source and the reading list below, is the first half of
   breaking it. The one and only way to claim a proof is to genuinely run the
   attack. Write your attack in `student/exploitN.py`.
4. Develop locally against the **practice** oracle (test mode, no token,
   repeatable sessions). When you push, the autograder runs your same exploit
   against the **grading** oracle, whose secret lives only on the server. A
   hardcoded proof from a local session fails against the grading oracle -- a
   true attack breaks both.

## `[--[ DELIVERABLES ]--]`

| Path | What goes here |
| --- | --- |
| `student/exploit1.py … exploit4.py` | one attack per ward (Ward IV optional) |
| `student/WRITEUP.md` | the grimoire (template provided; honor flag goes in frontmatter) |
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

The **honor flag is a hard gate.** Run `python pledge.py`, affirm the [SOLDIER](https://finalfantasy.fandom.com/wiki/SOLDIER)'s
Oath, paste the flag into your grimoire. Missing or wrong honor flag voids the
autograded points.

## `[--[ BEHIND THE CURTAIN ]--]`

Curious how the Vault keeps your wards distinct from everyone else's? The
grading oracle holds a secret key server-side. Every proof it accepts is bound
to that key and to the specific ward you attacked. The oracle's source is
published alongside the image you pull for local practice; read it the same way
you'd audit a real cryptosystem. The one-way properties that protect the oracle's
secrets are the same [key-derivation](https://en.wikipedia.org/wiki/Key_derivation_function) and [cryptographic hash](https://en.wikipedia.org/wiki/Cryptographic_hash_function) ideas you will
study this semester.

- **[Determinism](https://en.wikipedia.org/wiki/Deterministic_algorithm)**: the oracle always accepts the same correct proof for a given
  ward, so grading is repeatable.
- **Uniqueness**: your proof for Ward II is not a valid proof for Ward III, and
  a borrowed proof from someone else's session fails.
- **[One-wayness](https://en.wikipedia.org/wiki/One-way_function)**: you can't reverse a proof to forge the oracle's key.

You spend this lab attacking four ways symmetric crypto goes *wrong*. The
machinery that makes the lab fair is crypto done *right*.

## `[--[ THE SPELLBREAKER'S LIBRARY ]--]`

Each ward is a real, named attack, and the honor code says *read everything*, so
here's where to start. These four are a curated walk through the
[Cryptopals challenges](https://cryptopals.com/); the lab is their Spellbreaker
retelling.

- **I · The Wisp**: ECB detection · [Block cipher modes](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation) · [Cryptopals 1·8](https://cryptopals.com/sets/1/challenges/8)
- **II · The Rune Golem**: ECB byte-at-a-time · [Cryptopals 2·12](https://cryptopals.com/sets/2/challenges/12)
- **III · The Mirror Knight**: CBC bit-flipping · [Cryptopals 2·16](https://cryptopals.com/sets/2/challenges/16)
- **IV · OMEGA WARD**: CBC padding oracle · [Padding oracle attack](https://en.wikipedia.org/wiki/Padding_oracle_attack) · [POODLE](https://en.wikipedia.org/wiki/POODLE) / [Lucky 13](https://en.wikipedia.org/wiki/Lucky_Thirteen_attack) · [Cryptopals 3·17](https://cryptopals.com/sets/3/challenges/17)
- **Behind the curtain**: the oracle architecture · [Key derivation function](https://en.wikipedia.org/wiki/Key_derivation_function)

## `[--[ HONOR CODE ]--]`

Read everything: public tutorials, the oracle source, the docs, each other's
*ideas*. Curiosity is the whole job. What you may **not** do is submit an
exploit you didn't write and understand. And you couldn't coast on a
classmate's even if you tried: their wards aren't yours, and the flags differ. A
borrowed exploit recovers nothing. Write your own. It's the only thing that
works.

```
[--EOF--]
```
