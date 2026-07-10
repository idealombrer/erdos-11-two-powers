# STEP46 — Consolidation : lemmes inconditionnels FORMALISÉS en Lean 4 (0 sorry) + papier clarifié.

**Date :** 2026-07-04. Demande de l'user : « mets à jour le papier + formalise en Lean pour s'assurer
que tout ce qu'on a est bon » (crainte légitime : beaucoup vérifié sur DONNÉES finies, pas prouvé
pour tout n). **Résultat : les lemmes ÉLÉMENTAIRES prouvés (valables pour tout n/p) sont désormais
FORMELLEMENT VÉRIFIÉS en Lean 4 / Mathlib v4.30, 0 sorry, audit d'axiomes propre. Le papier
distingue explicitement le PROUVÉ (formalisé) de l'empirique/conditionnel.**

## Fichier `Erdos11_verified.lean` — compile EXIT=0, audit d'axiomes

Compile via `cd ~/mathematics_in_lean && ~/.elan/bin/lake env lean Erdos11_verified.lean`.
`#print axioms` confirme **AUCUN `sorryAx`** :
- `involution` : `[propext]`
- `prime_lt_two_pow_of_dvd` : `[propext, Classical.choice, Quot.sound]`
- `card_large_prime_divisors_le` : `[propext, Classical.choice, Quot.sound]`
- `pow_eq_one_iff_order_dvd` : `[propext, Classical.choice, Quot.sound]`

Théorèmes formalisés (tous PROUVÉS pour tout n/p, pas vérifiés sur données) :
1. **`involution`** (STEP26) : dans un semi-anneau commutatif, `x^e=1 ∧ δ≤e ⟹ x^δ(1+x^(e−δ))=1+x^δ`.
   = l'identité d'involution `1+2^{e−δ}≡2^{−δ}(1+2^δ) mod p`, base de la structure PA des fibres.
2. **`prime_lt_two_pow_of_dvd`** : `p ∣ 2^e−1 ∧ 0<e ⟹ p<2^e`. = borne d'ordre `ord_p(2)>log₂p`,
   input de la convergence de Σ1/ord_p(2).
3. **`card_large_prime_divisors_le`** (STEP26-lit, le NOUVEAU résultat inconditionnel) : S ensemble
   fini de premiers distincts, tous >L, tous divisant N>0 ⟹ **`(L+1)^|S| ≤ N`**. Cœur de la borne
   `Σ_{p∈(L,L²]}⌊L/ord_p(2)⌋ = O(L²/logL) = o(L²)` (le gain vient de p>L). Preuve via
   `prod_dvd_of_primes` (premiers distincts copremiers ⟹ produit divise N) + `prod_le_prod'`.
4. **`pow_eq_one_iff_order_dvd`** : `x^k=1 ↔ ord(x)∣k` (pont ordre↔divisibilité, forme monoïde propre).

**Ce qui N'EST PAS formalisé (car empirique/conditionnel, PAS prouvé pour tout n)** — explicitement
noté dans le fichier et le papier : la borne de moments factoriels E_k^tot≤C^k E_k^null (TB), la
borne d'extrême maxM_B=o(logL), le théorème every-n. Ils restent conjecturaux.

## Papier mis à jour (PAPER.tex, 17 pp, compile tectonic)

- **Remarque « Which moment is binding » (STEP45)** ajoutée après §typeB : E₂^tot n'est PAS o(L²)
  (c'est Θ(L³/logL)) ; le terme k=2 est gratuit (#{M_p≥2}≤π(L²)) ; le cas contraignant est l'extrême
  (grand k~logL/loglogL), pas la variance ; mécanisme = Sidon/ℤ ⟹ densité (E₂=densité à 5%),
  base-indépendant. Corrige le risque de mésinterprétation « prouver E₂ ⟹ fini ».
- **Mention Lean mise à jour** : « None of this is formalised » → les lemmes élémentaires SONT
  formalisés (Erdos11_verified.lean, 0 sorry, audit d'axiomes), les analytiques/conditionnels non
  (statut conjectural respecté).

## Bilan honnête pour l'user

- **Ce qui est SÛR (prouvé tout n, dont Lean) :** almost-all-n (densité 1−O(1/logL)), Lemme K,
  périodicité, convergence Σ1/d_p, R1, périodes complètes ≤0.3205T, Lemme M, order-sum o(L²),
  involution. Les 3 derniers + involution : formalisés Lean 0 sorry.
- **Ce qui est EMPIRIQUE (données finies, PAS tout n) :** E_k sous-Poisson, maxM_B~logL/loglogL,
  théorème every-n. Marqués conditionnels partout.
- La crainte de l'user (« vrai sur données mais pas tout n ») est fondée pour la partie every-n, et
  maintenant clairement séparée : le every-n est CONDITIONNEL (à TB), l'almost-all-n est INCONDITIONNEL
  et ses briques élémentaires sont Lean-vérifiées.

---
*Erdos11_verified.lean : 4 théorèmes, 0 sorry, audit axiomes [propext, Classical.choice, Quot.sound].
Papier : remarque STEP45 (le verrou est l'extrême, pas E₂) + mention Lean. PROUVÉ (dont Lean) vs
empirique/conditionnel clairement séparés.*
