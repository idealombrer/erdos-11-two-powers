# STEP51 — Chantiers A & B (Fable), avec les énoncés EXACTS testés (comme il l'exige).

**Date :** 2026-07-05. Réponse à la critique méthodologique de Fable (fermer un lead contre sa VRAIE
formulation, avec l'inéquation/mesure qui bloque, consignée). Scripts `chantierB_occupation.py`,
`chantierA_moments.py`.

## Chantier B — RÉOUVERTURE propre du lead #1 (larger sieve), contre son objet correct

**Énoncé exact testé :** occupation ν(q)=#{classes mod q occupées par les ENTIERS M=1+2^β−2^γ−2^δ,
β,γ,δ∈[0,L]}, pour q premier ≤50. (STEP49 testait les *premiers non-Sidon* = mauvais objet ; Fable a
raison.)

**Table brute (transmise à Fable pour validation) :** ν(q) = q pour TOUT q≤50, y compris petits ordres :
q=3(ord2), 5(ord4), 7(ord3), 31(ord5), 47(ord23) → tous ν/q = **1.00**. `Σ_{q≤50} log q/ν(q) = 2.42`
contre `log(range M ≈ 2^{L+1}) = 42.3` ⟹ dénominateur du larger sieve massivement < 0.

**Inéquation qui bloque (fermeture propre) :** le sumset signé **1+H−H−H d'un sous-groupe mult. H remplit
Z/q même pour |H| minuscule** (sum-product ; vérifié même |H|=2 mod 3 remplit). Donc les M(δ) SATURENT
toutes les classes ⟹ le larger sieve n'a rien à exploiter. Lead #1 MORT contre sa vraie formulation, pour
la bonne raison documentée (≠ STEP49 qui testait le mauvais objet ET STEP44 range exponentiel).
**Contre l'intuition de Fable** (« 2^k prend peu de valeurs → M contraint ») : faux, le sumset triple
remplit. [Verdict final déféré à Fable, table brute fournie.]

## Chantier A — moments de C(n) via indépendance CRT. Amélioration RÉELLE mais CONDITIONNELLE.

**Erreur d'abord corrigée :** v1 mesurait Σ N_p (mauvaise quantité). Le C(n) du papier (l.741) est
**C(n)=Σ_p N_p(N_p−1)** (compte de collisions), avec Σ N_p ≤ π(L²)+C(n). E[C]=Σ Δ_p/p² = 0.445, 0.452,
0.539, 0.983 (L=16..28) = **retrouve le C̄ du papier (0.44,0.43,0.51,0.96)** ✓ bonne quantité.

**Mesure :** Var[C]/E[C] = 2.08→2.89 (borné, L=16..36), maxX_p=6→12. Chebyshev bat Markov de 50–160×
(croissant) ⟹ **numériquement O(1/(L³logL))**, facteur L² vs Markov O(1/(L logL)).

**Inéquation qui bloque l'inconditionnalité (fermeture propre du côté « inconditionnel ») :**
Var[C]=Σ_p Var[N_p(N_p−1)] ≤ Σ_p Δ_p M_p²/p² ≤ **M_max²·C̄**. Avec le seul bound trivial M_p≤L+1
(≤1 paire par valeur de l) : Var[C]≤L²·C̄=O(L³) ⟹ Chebyshev O(1/L) = PIRE que Markov. Le gain L² EXIGE
M_max=o(L), i.e. un contrôle du 4ᵉ moment Σ_p p^{−2}Σ_r[c_r(c_r−1)]² — crible du carré d'ordre supérieur,
**même difficulté que (M″)/(TB)**. 

**⟹ Fable a tort sur « publiable INCONDITIONNEL O(L^{−A}) ».** L'indépendance CRT factorise les moments
(exact), mais borner leur SOMME asymptotique n'est PAS « trivialement bornable » — c'est le crible du
carré. Seul le 1er moment (Markov) est inconditionnel. (Je fais à Chantier A ce que Fable a fait à
Stepanov : exhiber l'inéquation. Var[C]≤M_max²C̄, M_max≤L trivial ⟹ pas de gain.) Le mur (B) (N_p∈{0,1}
quasi-Bernoulli) est plus plausiblement inconditionnel au 2ᵉ moment, non poursuivi.

**Papier corrigé (honnêtement) :** remarque « higher moments » réécrite (gain CONDITIONNEL sur M_max=o(L)/
4ᵉ moment, pas inconditionnel) ; phrase du corollaire idem. La densité INCONDITIONNELLE reste
O(1/(L logL)) (Markov + amélioration mur-B ηL²). Pas de faux théorème introduit.

## Bilan salve Fable (mis à jour)

- Corrections rigueur (Lemme K, pont CRT) : faites, justes.
- Amélioration gratuite mur-B (Markov ηL²) : O(1/logL)→O(1/(L logL)) INCONDITIONNEL. Réelle.
- Lead #1 larger sieve : MORT (Chantier B, objet correct : M(δ) saturent Z/q).
- Lead #4 réduction p-adique : PARTIELLE (STEP50).
- Chantier A (moments) : gain CONDITIONNEL (M_max=o(L)), PAS inconditionnel. Fable trop optimiste.
- Non faits : #3 Cilleruelo (biblio, Fable prend), #5 corps de fonctions (build), #6 digits (reformulation).

Voir [[project_erdos11_fable_leads]], [[project_erdos11_twopow_status]].

---
*Chantier B : lead #1 mort contre son vrai objet (M(δ) saturent ν(q)=q, sum-product remplit Z/q ; table
brute à Fable). Chantier A : C(n)=ΣN_p(N_p−1) (E[C] match papier) ; Chebyshev num. O(1/(L³logL)) MAIS
conditionnel M_max=o(L) (Var≤M_max²C̄, trivial M_max≤L ⟹ nul) = 4ᵉ moment/crible carré, PAS inconditionnel.
Fable corrigé. Papier : remarque higher-moments honnête, densité inconditionnelle reste O(1/(L logL)).*
