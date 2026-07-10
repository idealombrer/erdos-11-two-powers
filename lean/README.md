# Lean verification (`Erdos11_verified.lean`)

Five elementary lemmas underpinning the paper's unconditional results, formally verified against
Mathlib, `0 sorry`:

| Lemma | Role |
|---|---|
| `involution` | the involution identity $1+2^{e-\delta}\equiv 2^{-\delta}(1+2^\delta)$ |
| `prime_lt_two_pow_of_dvd` | $p\mid 2^e-1\Rightarrow p<2^e$ (order lower bound) |
| `card_large_prime_divisors_le` | distinct primes $>L$ dividing $N>0$ give $(L+1)^{|S|}\le N$ (order sum) |
| `pow_eq_one_iff_order_dvd` | $x^k=1\iff \mathrm{ord}(x)\mid k$ |
| `no_sq_divisor_of_small_degree` | a nonzero polynomial of degree $<2\deg P$ is not divisible by $P^2$ (the $\mathbb F_q[t]$ degree obstruction, §8) |

## Build

The file depends only on Mathlib. From a Mathlib-enabled Lean 4 project (with the file placed
in it):

```bash
lake env lean Erdos11_verified.lean
```

The file ends with `#print axioms` for all five lemmas; the type-check prints the axiom audit —
each lemma depends only on `[propext, Classical.choice, Quot.sound]` (no `sorryAx`). The saved
output is in [`axiom_audit.txt`](axiom_audit.txt).

To set up a fresh project, create a Mathlib project (`lake new … math`, then `lake exe cache
get`), copy this file in, and run the command above with a toolchain matching the project's
`lake-manifest.json`.
