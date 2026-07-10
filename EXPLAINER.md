# Understanding the #11 paper — a plain-language guide

*Companion document to "Elementary reductions for the two-powers squarefree variant of
Erdős Problem #11." Same purpose as `COMPRENDRE_273.md`: to make clear what the paper claims,
how it's proved (in broad strokes), what remains open, and how to answer questions about it.*

---

## 1. The problem, from scratch

### 1.1 What does "squarefree" mean?

An integer is **squarefree** if no perfect square > 1 divides it. Equivalently: in its prime
factorization, every prime appears at most once.

- 10 = 2 × 5 → squarefree ✓
- 15 = 3 × 5 → squarefree ✓
- 12 = 2² × 3 → NOT squarefree (divisible by 4) ✗
- 45 = 3² × 5 → NOT squarefree (divisible by 9) ✗

This is a *common* property: about 61% of integers are squarefree (the exact proportion is
6/π²). This matters: we're looking for something common, not rare — that's what makes the
problem plausible.

### 1.2 Erdős's Problem #11, and our variant

**The original Problem #11** (open): can every sufficiently large integer be written as
n = k + 2^m, with k squarefree and 2^m a power of 2?

**Our "two-powers" variant**: can every odd integer n > 1 be written as
n = k + 2^l + 2^m, with k squarefree?

Example: n = 23. Try 2^1 + 2^2 = 6 → k = 17, prime hence squarefree ✓. Found on the first try
— and that's typical: there are *many* choices of pairs (l, m), and it only takes ONE giving
a squarefree k.

Giving two powers instead of one should make the problem easier (more attempts allowed); a
remark attributed to Erdős suggests he thought this relaxation "might be easy." Our paper
shows it isn't — but that it can be pushed very far, and precisely locates where it blocks.
The variant is recorded as `erdos_11.variants.two_pow_two` in Lean formalized-conjectures
repositories; to our knowledge, nobody had studied it.

### 1.3 Machine-verified up to 50 million

Before any theory: the variant was tested for all odd n up to 5 × 10⁷. No exceptions. This
proves nothing (there are infinitely many integers), but it says that if a counterexample
exists, it is large.

---

## 2. The strategy: counting failures

### 2.1 The trial budget

For a given n, let L be the number of bits of n (precisely L = ⌊log₂ n⌋). The possible pairs
(l, m) with 2^l + 2^m < n number about **T = (L+1)²**. For n around a billion, L ≈ 30: about
960 trials.

**The paper's master idea fits in one sentence**: instead of searching for a pair that WORKS,
count the pairs that FAIL. A pair fails when k = n − 2^l − 2^m is divisible by a square p²
(p prime). If we prove the total number of failures is **strictly less than T**, then at
least one pair succeeds — and the problem is solved for that n. The whole battle is bounding
the failures, prime by prime.

### 2.2 Splitting by prime size

Each prime p can "sabotage" certain pairs (those where p² divides k). How many? It depends on
the size of p. The paper splits the primes into zones:

| Zone | Final status |
|---|---|
| Small primes (p ≤ L+1) | **CLOSED** for every n — the heart of the paper (Lemma K + Prop. R1) |
| Middle zone (L < p ≤ L²) | closed for *almost all* n; for *every* n, this is THE lock (two sub-cases, see §4) |
| Large zone (L² < p ≤ √(n/2)) | closed for almost all n; open for every n ("wall B") |
| Very large (near √n) | closed (a perfect-square argument) |

### 2.3 Lemma K: the dominant term cancels EXACTLY

The biggest danger comes from small primes (3, 5, 7 sabotage many pairs). The paper proves
their contribution can be computed **exactly** via a "character sum" cancellation — an
algebraic identity, not an estimate. Result: small primes sabotage at most ≈ 32% of the pairs
(the paper's constant 0.3205), for EVERY n, with no hypothesis at all.

A curiosity along the way: this cancellation requires that p not be a "Wieferich prime" (an
extremely rare property: only two are known in the entire universe of numbers, 1093 and
3511). The paper shows these two exceptions cost a negligible amount — and, importantly, our
argument does NOT depend on the open conjecture about infinitely many Wieferich primes.

---

## 3. The main theorem: true for "almost all" n

### 3.1 What it says

> **Corollary 6.9 (unconditional).** The proportion of odd n for which the variant could fail
> tends to 0 (at rate ≈ 1/(L log L)). In other words: for almost all odd integers,
> n = squarefree + 2^l + 2^m, and this is PROVED, with no hypothesis whatsoever.

"Almost all" has a precise mathematical meaning here: the set of possible exceptions has a
density that shrinks to zero. This is not "every n" (see §4), but it is a real theorem,
complete, self-contained (no unverified external result is used), and it is the paper's
central result.

### 3.2 The idea of the proof (the casino picture)

For the middle and large zones, we cannot control the WORST n — but we can control the
AVERAGE n. The argument is probabilistic: we compute the average number of failures over all
n in a range, show it is small, and Markov's inequality (an elementary principle: if average
spending is small, few people spend a lot) bounds the proportion of "unlucky" n. Unlucky ones
may exist, but they are rare, and increasingly rare as n grows.

---

## 4. What blocks "EVERY n" — the locks, explained

To go from "almost all n" to "every n," one would need to control the worst case of the
middle zone (L < p ≤ L²) and of the large zone. The paper shows everything reduces to ONE
question: in the middle zone, how many different pairs can give the same residue modulo p²?
(The "multiplicity.") This question splits in two depending on how the number 2 behaves
modulo p:

### 4.1 Type A — a real partial result, with a measured gap

For primes where powers of 2 "spin fast" modulo p, we found a tailor-made theorem in the
literature (García–Voloch, 1988, via the Stepanov method) that directly bounds the
multiplicity. Unconditional result of the paper: the Type A contribution is at most ≈ L^{8/3},
whereas L² would be needed. **Exactly one factor of L^{2/3} is missing** — the gap is measured
to the decimal, and the open question is cleanly stated (can a special symmetry of our sums,
the "involution," be exploited to close the gap?).

### 4.2 Type B — closed "by circularity" (the most subtle result)

For the other primes, the bound we'd need is called (TB). The paper proves two surprising
things:

1. A powerful theorem of Bourgain–Chang (2006) applies to our sums and gives genuine
   cancellation — we checked this against the source texts AND numerically. Apparent good
   news.
2. BUT: converting this cancellation into the bound (TB) requires another bound… which is
   mathematically EQUAL to (TB) itself. The snake eats its own tail: the missing ingredient
   IS the intended conclusion.

This is what's called **closure by circularity**: (TB) is not "a result awaiting its
reference in the literature," it is a genuine open estimate, at the research front.
Documenting it precisely spares anyone who tries again months of work.

### 4.3 The final diagnosis: the culprit is CARRIES

The paper tests the entire architecture in a parallel world: polynomials (replacing the
number 2 with the variable t). There, the analogue of (TB) is proved in three lines. Why?
Because monomials never "carry": t^a + t^a = 2·t^a, always of degree a. Whereas for integers,
2^a + 2^a = 2^{a+1}: binary addition PROPAGATES CARRIES, exactly like doing addition by hand
in school. This carrying phenomenon is precisely what prevents bounding the coincidences
modulo p². The paper's conclusion: the difficulty of the #11 variant is not a lack of
cancellation (it exists, we proved it), it is an "archimedean" phenomenon — the carries of
binary notation. Locating a wall at this level of precision is a contribution in itself.

### 4.4 Two classic pitfalls avoided (good to know for the FAQ)

- **Wieferich**: our proof does NOT need the open conjecture about Wieferich primes — only to
  exclude the two known ones (negligible cost).
- **Crocker**: the cousin problem with a PRIME instead of a squarefree number
  (n = p + 2^a + 2^b) is FALSE (disproved in 1971 by a congruence trick). The paper explains
  why that trick cannot apply here: "composite" can be forced by a congruence, "not
  squarefree" cannot (squarefree numbers are too common in any progression). Our variant
  remains plausible where its cousin is false.

---

## 5. Machine verification (Lean)

Five elementary lemmas carrying the unconditional results have been formalized and verified
in the Lean 4 proof assistant (file `Erdos11_verified.lean`, zero `sorry` — i.e. zero proof
gaps). The analytic and conditional parts are deliberately NOT formalized: their conjectural
status is thus visible in the repository's very structure. Nobody needs to take our word for
the basic building blocks: the machine checked them.

---

## 6. FAQ — if you're asked

**"Did you solve the variant?"** — No. Proved for almost all n (unconditionally); for every
n, it is conditional on (TB) plus two softer inputs, and the paper pinpoints exactly why
(TB) is currently out of reach.

**"What about the original Problem #11?"** — Not touched. We study a relaxation; our
techniques don't carry back to the one-power problem. In fact the paper shows that the lock
(TB), looked at closely, is itself a cousin of #11 — the difficulty isn't bypassed by
relaxing, it concentrates.

**"Why trust the computations?"** — Every numerical claim points to a named script; the five
basic lemmas are Lean-verified; the external theorems (García–Voloch, Bourgain–Chang,
Heath-Brown) are cited with their exact conditions, collated against the sources — and the
paper itself flags the one place an unverified external dependency remains (Kalinin's
preprint, used only in the conditional part; the main theorem no longer depends on it).

**"What's the contribution if nothing is resolved?"** — An unconditional theorem (almost all
n), a partial result with a measured gap (Type A), a documented closure by circularity
(Type B), a structural diagnosis (the carries), and two open questions stated to the
millimeter. This is the transformation of a vague problem into a precise one — exactly the
material the next researcher needs.

---

## 7. Small glossary (complementing #273's)

- **Squarefree**: no square > 1 divides it (≈ 61% of integers).
- **L**: the number of bits of n; **T = (L+1)²**: the number of trial pairs.
- **N_p(n)**: the number of pairs sabotaged by prime p (those where p² divides
  n − 2^l − 2^m).
- **Character sum**: a sum of complex exponentials whose cancellation reflects a perfectly
  balanced distribution; Lemma K proves an EXACT cancellation.
- **Wieferich**: a prime p such that p² divides 2^{p−1} − 1; two known (1093, 3511),
  infinitude open — our proof does not depend on it.
- **Type A / Type B**: middle-zone primes according to whether the order of 2 modulo p is
  small (≤ L) or large (> L).
- **(TA), (TB), (B)**: the three named open statements; (TB) is the central lock, closed by
  circularity.
- **Circularity**: a situation where the ingredient missing to prove X is logically
  equivalent to X — a sign of being at the research front, not behind on the literature.
- **Almost all n**: all but a set of exceptions of density tending to 0 (a precise
  mathematical sense, not a figure of speech).
- **Function field / F_q[t]**: the "parallel world" of polynomials where the architecture is
  tested; monomials have no carries.
- **Archimedean**: relating to the actual size of numbers (here: the binary carrying
  phenomenon), as opposed to divisibility properties.
