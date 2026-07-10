/-
  Erdős problem #11 — two-powers squarefree variant.
  FORMALLY VERIFIED elementary lemmas underpinning the UNCONDITIONAL parts of the reduction.

  These are the statements that are proved "for all n / all p" (not merely checked on finite data).
  What is NOT here (because it is empirical or conditional, not proved for all n):
    * the factorial-moment bound  E_k^tot ≤ C^k E_k^null  (hypothesis TB);
    * the extreme bound  max_p M_p = o(log L)  (the genuine open lock);
    * the every-n theorem.
  Those remain conjectural. This file locks down only the rigorously true elementary lemmas.

  Compiles with 0 `sorry` against Mathlib v4.30 via
     cd ~/mathematics_in_lean && ~/.elan/bin/lake env lean Erdos11_verified.lean
-/
import Mathlib

open Finset

namespace Erdos11

/-- **Involution identity** (STEP26). In any commutative semiring, if `x ^ e = 1` and `δ ≤ e`, then
`x ^ δ * (1 + x ^ (e - δ)) = 1 + x ^ δ`. Taking `x = 2` in `ZMod p` with `e = ord_p(2)` (so
`x ^ e = 1`), this is exactly `1 + 2 ^ (e-δ) ≡ 2^(-δ) (1 + 2^δ)`: the gap-values `1 + 2^δ` and
`1 + 2^(e-δ)` lie in the same coset of `⟨2⟩ mod p`. This is the algebraic identity behind the
arithmetic-progression structure of the fibers of `{2^a + 2^b mod p²}`. -/
theorem involution {R : Type*} [CommSemiring R] (x : R) (e δ : ℕ)
    (he : x ^ e = 1) (hδ : δ ≤ e) :
    x ^ δ * (1 + x ^ (e - δ)) = 1 + x ^ δ := by
  have key : x ^ δ * x ^ (e - δ) = 1 := by
    rw [← pow_add, Nat.add_sub_cancel' hδ, he]
  rw [mul_add, mul_one, key, add_comm]

/-- **Order lower bound / convergence input** (used for `∑_p 1/ord_p(2) < ∞`). Any prime `p`
dividing `2 ^ e - 1` (in particular `e = ord_p(2)`, for which `2 ^ e ≡ 1 (mod p)`) satisfies
`p < 2 ^ e`. Hence `ord_p(2) > log₂ p`, the bound that makes `∑_p 1/ord_p(2)` converge by comparison
with `∑ 1/(p log p)`. -/
theorem prime_lt_two_pow_of_dvd {p e : ℕ} (he : 0 < e) (hdvd : p ∣ 2 ^ e - 1) :
    p < 2 ^ e := by
  have h2 : 2 ≤ 2 ^ e := by
    calc 2 = 2 ^ 1 := (pow_one 2).symm
      _ ≤ 2 ^ e := Nat.pow_le_pow_right (by norm_num) he
  have hpos : 0 < 2 ^ e - 1 := by omega
  calc p ≤ 2 ^ e - 1 := Nat.le_of_dvd hpos hdvd
    _ < 2 ^ e := by omega

/-- Product of a finite set of distinct primes, each dividing `N`, divides `N`
(distinct primes are pairwise coprime). -/
private theorem prod_dvd_of_primes {N : ℕ} :
    ∀ (S : Finset ℕ), (∀ p ∈ S, p.Prime) → (∀ p ∈ S, p ∣ N) → S.prod id ∣ N := by
  intro S
  induction S using Finset.induction with
  | empty => intro _ _; simp
  | @insert a s ha ih =>
    intro hp hdvd
    rw [Finset.prod_insert ha]
    have hpa : a.Prime := hp a (Finset.mem_insert_self a s)
    have hda : a ∣ N := hdvd a (Finset.mem_insert_self a s)
    have hps : s.prod id ∣ N :=
      ih (fun p hp' => hp p (Finset.mem_insert_of_mem hp'))
         (fun p hp' => hdvd p (Finset.mem_insert_of_mem hp'))
    have hcop : Nat.Coprime a (s.prod id) := by
      apply Nat.Coprime.prod_right
      intro p hp'
      have hpp : p.Prime := hp p (Finset.mem_insert_of_mem hp')
      have hne : a ≠ p := fun h => ha (h ▸ hp')
      exact (Nat.coprime_primes hpa hpp).mpr hne
    exact Nat.Coprime.mul_dvd_of_dvd_of_dvd hcop hda hps

/-- **Order-sum key lemma** (STEP26-lit; the *new* unconditional bound, and the reason the Type-A
"order sum" `∑_{p∈(L,L²]} ⌊L/ord_p(2)⌋` is `O(L²/log L) = o(L²)`).

If `S` is a finite set of distinct primes, each `> L`, all dividing `N > 0`, then
`(L+1) ^ |S| ≤ N`. Applied with `N = 2^k - 1`: the number of primes `p > L` dividing `2^k - 1`
is at most `log_{L+1}(2^k)`, i.e. `< k · log 2 / log L`. Summing `⌊L/ord_p(2)⌋ = #{k ≤ L : ord_p(2) ∣ k}`
over `p` and using `ord_p(2) ∣ k ↔ p ∣ 2^k - 1` yields the `O(L²/log L)` bound.

The gain over the trivial count comes **entirely** from `p > L`. -/
theorem card_large_prime_divisors_le {N L : ℕ} (S : Finset ℕ)
    (hp : ∀ p ∈ S, p.Prime) (hL : ∀ p ∈ S, L < p) (hdvd : ∀ p ∈ S, p ∣ N) (hN : 0 < N) :
    (L + 1) ^ S.card ≤ N := by
  have hprod : S.prod id ∣ N := prod_dvd_of_primes S hp hdvd
  have h1 : (L + 1) ^ S.card ≤ S.prod id := by
    rw [← Finset.prod_const]
    apply Finset.prod_le_prod'
    intro p hp'
    exact hL p hp'
  exact le_trans h1 (Nat.le_of_dvd hN hprod)

/-- **Order ↔ divisibility bridge** (additive-order form, `sorry`-free): for `x` in a monoid,
`x ^ k = 1 ↔ orderOf x ∣ k`. Applied with `x = (2 : (ZMod p)ˣ)` this turns
`⌊L/ord_p(2)⌋ = #{k ≤ L : ord_p(2) ∣ k}` into `#{k ≤ L : x^k = 1}`, the count used in the order sum.
(We state the clean monoid form to keep the file self-contained and fully verified.) -/
theorem pow_eq_one_iff_order_dvd {M : Type*} [Monoid M] (x : M) (k : ℕ) :
    x ^ k = 1 ↔ orderOf x ∣ k :=
  (orderOf_dvd_iff_pow_eq_one).symm

/-- **Function-field degree obstruction** (the reason the `F_q[t]` analogue of hypothesis (TB) is a
theorem while over `ℤ` it is a genuine open estimate).

A nonzero polynomial `D` of degree `< 2·deg P` cannot be divisible by `P²`. In the sieve over `F_q[t]`,
a nontrivial coincidence `∑ t^{a_i} ≡ ∑ t^{b_i} (mod P²)` makes `D = ∑ t^{a_i} - ∑ t^{b_i}` a nonzero
polynomial of degree `≤ L`; for `deg P > L/2` this lemma forbids `P² ∣ D`, so there are no nontrivial
coincidences and (TB) holds by a pure degree count — no exponential-sum input.

Over `ℤ` the analogue **fails**: a nonzero `2^a + 2^b - 2^c - 2^d` can still be squarefull, because
integer size gives no bound on its square divisors. This is exactly the *archimedean* obstruction
isolated in the paper (powers of `2` carry, monomials do not). -/
theorem no_sq_divisor_of_small_degree {F : Type*} [Field F] {P D : Polynomial F}
    (hD : D ≠ 0) (hdeg : D.natDegree < 2 * P.natDegree) : ¬ (P ^ 2 ∣ D) := by
  intro h
  have hle := Polynomial.natDegree_le_of_dvd h hD
  rw [Polynomial.natDegree_pow] at hle
  omega

end Erdos11

-- Axiom audit: each proved statement depends only on the standard axioms
-- (propext, Classical.choice, Quot.sound) — NO `sorryAx`, confirming a complete proof.
#print axioms Erdos11.involution
#print axioms Erdos11.prime_lt_two_pow_of_dvd
#print axioms Erdos11.card_large_prime_divisors_le
#print axioms Erdos11.pow_eq_one_iff_order_dvd
#print axioms Erdos11.no_sq_divisor_of_small_degree
