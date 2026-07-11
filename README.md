# The two-powers squarefree variant of Erdős Problem #11

**Problem.** Erdős #11 asks whether every large $n$ is $k+2^m$ with $k$ squarefree. This note
studies the relaxation *"every odd $n>1$ is $k+2^l+2^m$ with $k$ squarefree and $l,m\ge0$"*
(the Lean statement `erdos_11.variants.two_pow_two`). Paper: [`PAPER.tex`](PAPER.tex) /
[`PAPER.pdf`](PAPER.pdf).

This repository contains the paper, a **Lean 4 verification of the five elementary lemmas**
(`0 sorry`), and the scripts backing every numerical claim.

## Results (in ten lines)

- **Unconditional, self-contained:** the variant holds for **almost all $n$** (density
  $1-O(1/(L\log L))$, $L=\lfloor\log_2 n\rfloor$), on every prime range.
- **Type A (unconditional):** a García–Voloch bound gives $\sum_{\text{Type A}}M_p=O(L^{8/3}/\log L)$
  — short of the target $o(L^2)$ by exactly $L^{2/3}$.
- **Type B is closed by circularity:** Bourgain–Chang gives the additive sup-norm
  unconditionally, but the moment bound that would convert it into the Type-B hypothesis (TB)
  *equals* the additive energy, i.e. (TB) itself. So (TB) is a genuine open estimate, not a
  missing reference.
- **Function-field model:** the $\mathbb F_q[t]$ analogue of (TB) is proved by a degree count,
  and the mechanism does not transpose — diagnosing the obstruction over $\mathbb Z$ as
  *archimedean* (powers of $2$ carry; monomials do not).
- **Machine-checked:** the five elementary lemmas underpinning the unconditional results are
  formally verified in Lean 4 / Mathlib. → [`lean/`](lean/)

## Build

- **Paper:** `tectonic PAPER.tex` (or `pdflatex PAPER.tex`, run twice). Self-contained; the
  bibliography is inline. Compiled `PAPER.pdf` included.
- **Lean:** see [`lean/README.md`](lean/README.md). Five lemmas, `0 sorry`, axiom audit
  `[propext, Classical.choice, Quot.sound]` → [`lean/axiom_audit.txt`](lean/axiom_audit.txt).
- **Scripts:** `python3` with `numpy`, `sympy`. All are path-independent (run from `scripts/`).

## Formal verification (`lean/Erdos11_verified.lean`, 5 lemmas, 0 `sorry`)

| Lemma | Role in the paper |
|---|---|
| `involution` | involution identity, §5.3 |
| `prime_lt_two_pow_of_dvd` | order lower bound behind the convergence Prop., §2 |
| `card_large_prime_divisors_le` | order-sum bound $O(L^2/\log L)$, §5.2 |
| `pow_eq_one_iff_order_dvd` | order ↔ divisibility bridge |
| `no_sq_divisor_of_small_degree` | degree obstruction, (TB) over $\mathbb F_q[t]$, §8 |

## Numerical claims → scripts

Each script prints the figures quoted in the paper. Run from `scripts/`.

| Paper claim | script(s) |
|---|---|
| pivot constant $0.3205\ldots$, order sum $O(L^2/\log L)$ | `orders.py`, `sum_ord.py` |
| energy $E_2$, $E_k^{\text{tot}}/E_k^{\text{null}}$ sub-multinomial table | `lemmaE2.py`, `heath_brown_e2.py` |
| fibre / per-class structure, $\kappa_p$ | `verify_structure.py`, `kappa_structure.py` |
| residual / Lemma M | `verify_residual.py` |
| García–Voloch $r_p(b)\le 4e_p^{2/3}$ ($b\ne0$), degenerate $b=0$ | `typeA_garcia_voloch_check.py` |
| exceptional band $p\in(L,L^{4/3})$ absorbed | `typeA_exceptional_band.py` |
| Bourgain–Chang sup-norm $\max|S(\xi)|/(L+1)=0.37,0.31,0.24$ | `typeB_supnorm_check.py` |
| $\mathrm{EM}(L)\approx1.3$, geometric decay of $\#\{M_p\ge k\}$ | `geometric_decay.py`, `typeB_moments_conditional_check.py` |
| $k=2$ inventory: $p^2\mid N$ doubles are all Mersenne squares | `typeB_k2_inventory.py` |
| wall (B) first moment, exceptional fraction | `typeB_wall_first_moment.py` |
| base-independence / universality of the mechanism | `universality.py` |
| larger-sieve / occupation / digit checks (landscape) | `larger_sieve_test.py`, `landscape_occupation_test.py`, `landscape_digit_weight_check.py` |

## Layout

```
PAPER.tex / .pdf     the paper
EXPLAINER.md         plain-language explanation (English)
lean/                Erdos11_verified.lean + build instructions + axiom_audit.txt
scripts/             the scripts backing every numerical claim (header docstrings)
certificates/        the Lean axiom audit (this problem's certificate is the Lean proof)
worklog/             chronological research log (STEP01–56, consolidation_notes.md,
                     PAPER_DEBUTANT.md) — includes dead ends and corrected errors,
                     kept for transparency
```

## Methodology

Produced in a human-directed workflow with AI assistants in distinct executor and validator
roles: proposing tools and computations, locating and cross-checking references, and deriving
and refuting bounds, under a standing rule that **no theorem enters the paper without a written
proof or a formal (Lean) verification**, and **every numerical assertion names the script that
produces it** (the table above). The mathematical judgements, and the responsibility for
errors, are the author's. The `worklog/` retains the full record, corrected errors included.
