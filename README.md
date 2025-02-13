# CECS 378 Lab: Symmetric Cryptography (Spring 2025 Update)

## Assignment Description

## Overview

This lab introduces you to **basic cryptanalysis** by focusing on simple substitution ciphers. By the end of the assignment, you should:

1. Understand the mechanics of a **simple-substitution cipher** (sometimes called a monoalphabetic cipher).  

2. Write a **brute-force or heuristic-based decryption** program that attempts to crack an encrypted message **without** prior knowledge of the key.  

3. Write two smaller programs: one that **encrypts** a plaintext message given a key, and one that **decrypts** a cipher text message given the same key.

**Important**: Your solution must make an honest attempt at cryptanalysis—**hard-coding** the decrypted phrases or any attempt of falsifying your results or assignment is grounds for receiving **zero credit**.

---

You are given the following **four** quotes, each encrypted with a **simple substitution cipher** (where each letter in the alphabet is replaced by another letter). Your job is to programmatically **recover** the original text using a **brute-force** or **analytical** approach (letter frequency, dictionary lookups, etc.). You may use any programming language to accomplish the task that you feel comfortable with.

1. `FNCNJ LQNAB JANAJ CQNAP XXMJC VJPRL HXDTW XF`
   
2. `NUCDM AHJVG JDHHU IEAJF JPNBE AKRJQ MHHRJ QCHRU FJBIU PHTOE KTHEA KOUPM AXEON UCPJQ PMFJM AXDUC PMKJU CBMAX AJFJP LCEHN UCDMA DUSJU CHMIE AAJPY CBHRE ZJSJ`

3. `HTEBG RMAJH TMBUP PMHTJ PTMXM GPUQR JSITE DTIMB HTEBS UBHUO HTJGJ UGRJR EFEAK UAEHI JPJCA TMGGN OUPGP JHHNS CDTUO HTJHE SJSMA NBURC HEUAB IJPJB CKKJB HJXOU PHTEB GPUQR JSQCH SUBHU OHTJB JIJPJ RMPKJ RNDUA DJPAJ XIEHT HTJSU FJSJA HUOBS MRRKP JJAGE JDJBU OGMGJ PITED TIMBU XXQJD MCBJU AHTJI TURJE HIMBA HHTJB SMRRK PJJAG EJDJB UOGMG JPHTM HIJPJ CATMG GN`

4. `EAHTE BTUCP EXUAU HQJRE JFJHT MHMAN XMPZA JBBIE RRJAX CPJ`

Your **decryption** program should:
- Attempt to recover the **original English** text.  
- Output your best guess for each line.  
- Explain in comments or a detailed write-up **how** you arrived at your guess (e.g., letter-frequency analysis, known word matching, etc.).
- Run in a reasonable time (seconds, minutes, not hours or days).

---

## Part 2: Simple Substitution Cipher Tools

For the second part of this assignment, you will create **two small programs** (they can be in the same file or separate, as long as it’s clear what each does):

1. **Encrypter**  
   - Takes in **two arguments**:  
     1. A **plaintext** string.  
     2. A **key** in the form of a **modified alphabet** (i.e., a permutation of the 26 English letters).  
   - Outputs the **encrypted** version of the plaintext using that key.

2. **Decrypter**  
   - Takes in **two arguments**:  
     1. An **encrypted** string.  
     2. The **key** (same format, a modified alphabet).  
   - Outputs the **decrypted** (plaintext) version of that ciphertext.

### Test Phrases to Encrypt & Decrypt

Use your **Encrypter** and **Decrypter** on the **three** quotes below. For each:
1. Provide the **key** (permutation of the alphabet) you used.  
2. Provide the **resulting ciphertext**.  
3. Demonstrate that your Decrypter can transform that ciphertext **back** into plaintext.

**Phrase A**: 
> He who fights with monsters should look to it that he himself does not become a monster. And if you gaze long into an abyss, the abyss also gazes into you.

**Phrase B**:  
> There is a theory which states that if ever anybody discovers exactly what the Universe is for and why it is here, it will instantly disappear and be replaced by something even more bizarre and inexplicable. There is another theory which states that this has already happened.

**Phrase C**:  
> Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people's hats off - then, I account it high time to get to sea as soon as I can.

---

## Submission Guidelines

1. **Source Code**: Submit all scripts or files needed to run your programs.  
   - Include a detailed README.md (writeup) if your code requires compilation instructions. You may replace this file with your own (it's okay...I have a backup copy!).
2. **Decrypted Text**: For Part 1, submit the **original text** you recovered.  
3. **Keys and Ciphertext**: For Part 2, provide your chosen keys, the resulting **encrypted** text, and proof of successful **decryption**.  
4. **No Pre-Programmed Solutions**: If your code merely embeds the decrypted text or uses direct mappings that skip genuine cryptanalysis, you will receive **zero** points for the submission.  
5. **No Compression**: Don’t compress your files: it's bad practice to compress files in a git repository.
6. **Commenting**: Important code sections must be **commented** to explain your approach and logic.

---

## Grading Criteria and Deliverables

1. **Cryptanalysis Effort** (40%)  
   - Code must genuinely attempt to decipher the Part 1 quotes.  
2. **Accuracy of Decryption** (20%)  
   - Correctness (or near correctness) in revealing the original text.  
3. **Encrypter & Decrypter** (20%)  
   - Both tools must work properly with any given key.  
4. **Organization & Comments** (10%)  
   - Code is reasonably structured and explained.  
5. **Submission Format** (10%)  
   - Correct files submitted with no compression, following the instructions above.

Kudos if you can tell me who said these quotes without searching the Internet for them!

### Deliverables

Submit your source code and documentation or detailed writeup (well-commented source code can be substituted for a writeup, but it must be detailed, through, and describe your thought process) through your git repository along with the decrypted phrases in `*.txt` format.
