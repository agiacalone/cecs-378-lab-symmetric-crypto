---
# Paste your flags here. The autograder reads this file.
honor: CECS378{honor_PASTE_FROM_pledge.py}
ward1: CECS378{ward1_...}
ward2: CECS378{ward2_...}
ward3: CECS378{ward3_...}
ward4: CECS378{ward4_...}   # optional — OMEGA WARD (Ω stretch)
---

# Grimoire of the Spellbreaker

> Every Spellbreaker keeps a grimoire — a record of how each ward fell, so the
> next break comes faster. This one is yours. Write an entry for every ward you
> defeated: comment your exploit code, cite at least one source, and tell me
> *how* the ward broke, not merely that it did. "I ran the attack" earns
> nothing; "the ward leaked X, which let me do Y" earns everything.

## The Oath

Speak the SOLDIER's Oath — run `python pledge.py` — and paste the honor flag it
yields into the frontmatter above. No honor flag, no marks: a Spellbreaker who
won't sign their work doesn't get paid.

## Ward I — The Wisp (ECB detection)

- **How I made the pattern flicker:**
- **The real-world sin this is (name the CVE class):**

## Ward II — The Rune Golem (ECB byte-at-a-time)

- **The block size I measured, and how I measured it:**
- **How prying one rune at a time recovers the whole word:**
- **Where this same flaw bites real systems:**

## Ward III — The Mirror Knight (CBC bit-flipping)

- **Which ciphertext byte(s) I flipped, and what each plaintext byte became:**
- **Why CBC let me forge a sigil the ward couldn't question:**
- **Where this same flaw bites real systems:**

## Ward IV — OMEGA WARD (CBC padding oracle)  *(optional Ω stretch)*

- **What the one leaked bit told me, and how it cascades into full plaintext:**
- **The real-world reckoning (POODLE / Lucky 13):**

## Behind the curtain  *(optional — for the curious)*

- **Read `oracle/_seed.py`: which hash turns your repo name into your
  per-student keys and flags, and why does its one-wayness keep those flags
  unforgeable?**

## Sources

-
