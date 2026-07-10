# STEP42 — Universalité + robustification : le phénomène est GÉNÉRIQUE (toutes bases), le signal de congruence était un ARTEFACT DE MOYENNE. Corrige STEP41.

**Date :** 2026-07-04. Script `universality.py`. Tests ChatGPT : (a) base 2 spéciale ? (b) robustifier
le signal de congruence par le TAUX (pas la moyenne). **Résultat : (1) le phénomène d'outliers E₂ est
UNIVERSEL — g=2,3,5,6,7,10 l'ont tous, comparable ; base 2 PAS spéciale. (2) Le signal « p mod 16 »
(STEP41) était largement un ARTEFACT DE MOYENNE : le taux d'outliers est ~plat (0.7-3.4%), mildement
élevé pour des résidus base-dépendants (g=2: p≡1,13 ; g=3: p≡3). Il n'y a PAS de structure de
congruence propre à extraire. Deuxième auto-correction : les outliers sont une QUEUE GÉNÉRIQUE, pas une
structure explicite.**

## UNIVERSALITÉ : phénomène générique (base 2 non spéciale)

| g | #Type B | #(ρ>10) | max ρ2 | moy ρ2 | ΣΔ_out/E₂ |
|---|---|---|---|---|---|
| 2 | 1143 | 17 | 444 | 1.04 | 0.096 |
| 3 | 1149 | 21 | 255 | 1.40 | 0.067 |
| 5 | 1139 | 14 | 468 | 0.99 | 0.037 |
| 6 | 1144 | 19 | 185 | 1.09 | 0.058 |
| 7 | 1147 | 15 | 105 | 0.81 | 0.053 |
| 10 | 1143 | 20 | 283 | 1.05 | 0.055 |

**Tous comparables** (#ρ>10 ~14-21, max ~100-468, contribution 4-10%). **La base 2 n'est PAS spéciale**
(g=5 a max ρ2=468 > 444). ⟹ **phénomène GÉNÉRIQUE de « sumset de progression géométrique mod p² »**,
additif-combinatoire, pas une arithmétique-spéciale de 2. (Info : la preuve, si elle existe, sera
base-INDÉPENDANTE ⟹ méthode GÉNÉRALE, pas un truc base-2.)

## ROBUSTIFICATION : le signal congruence était un ARTEFACT DE MOYENNE (corrige STEP41)

Taux d'outliers (ρ>10) par p mod 16, g=2 (robuste, ≠ moyenne) :

| p mod 16 | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 |
|---|---|---|---|---|---|---|---|---|
| taux % | **3.1** | 0.7 | 0.7 | 1.4 | 0.7 | 2.0 | **3.4** | 0.0 |

- Moyenne globale ~1.5%. p≡1 et p≡**13** mildement élevés (~2×), pas 4× (le mean ρ2=4.2 de STEP41
  était tiré par quelques extrêmes DANS la classe p≡1, pas un taux élevé). **Signal réel mais MILD (~2×),
  pas dominant.** La plupart des outliers sont RÉPARTIS sur les résidus.
- g=3 : taux élevé sur p≡**3** mod 16 (5%), pas p≡1 ⟹ **base-dépendant** (cohérent avec « g résidu de
  puissance », mais faible et bruité).

⟹ **Mon STEP41 « congruence p mod 16 = vraie variable » était SURINTERPRÉTÉ** (artefact de moyenne).
Le taux robuste est ~plat ; l'effet de congruence est réel mais mineur (~2×) et base-dépendant.

## Conséquence : pas de « struct » explicite à extraire

La décomposition E₂=diag+struct+err (STEP41, philosophie ChatGPT) supposait un terme structuré
EXTRACTIBLE (congruence explicite). **Les outliers sont en fait une QUEUE GÉNÉRIQUE** (toutes bases,
taux ~plat, pas de congruence dominante) — PAS une structure séparable. On ne peut pas peler E₂^struct :
c'est la queue lourde de la distribution générique d'énergie des sumsets de PG. ⟹ la décomposition ne
simplifie pas ; il faut contrôler la distribution ENTIÈRE (queue incluse).

## Recadrage stratégique (double négatif, positif net)

- **Réfuté :** base 2 spéciale ; structure de congruence propre extractible (STEP41).
- **Établi :** le phénomène (générique + queue lourde) est le MÊME pour toute PG {g^k} ⟹ la conjecture
  E_k^tot ≤ C^k E_k^null est un énoncé **général sur les énergies additives des sumsets de progressions
  géométriques mod p²**, base-indépendant.
- **Implication outil :** ⟹ la voie est une méthode GÉNÉRALE (grand crible à modules carrés pour le
  sumset, ou un résultat général d'énergie de PG mod q), PAS un truc base-2 ni une extraction de
  structure. Ceci RE-CENTRE (sans « incontournable ») sur le grand crible/méthode générale : les
  alternatives « extraire le structuré » (ChatGPT) sont réfutées faute de structure propre.

## Note d'honnêteté (deux auto-corrections consécutives)

STEP40 (outliers ~20, <1%, petit index) → corrigé STEP41 (~L²/logL, ~10%, congruence) → corrigé
STEP42 (queue générique, congruence = artefact de moyenne mild). **Leçon : les signaux par-premier/
outlier sont bruités et tirés par la moyenne ; je les ai sur-lus deux fois.** L'image robuste, stable :
**pseudo-aléatoire générique + queue lourde générique, base-indépendante, sans structure propre
extractible.** C'est la conclusion honnête et elle CLÔT la ligne « extraire la structure ».

## Verdict (format demandé)

- **Base 2 spéciale ?** **NON** — phénomène universel (g=2,3,5,6,7,10 comparables).
- **Signal congruence robuste ?** **NON** (mild ~2×, base-dépendant, artefact de moyenne en grande
  partie ; STEP41 surinterprété).
- **Struct extractible (décomposition ChatGPT) ?** **NON** — queue générique, pas structure séparable.
- **STATUT : RESTE OUVERT, recadré.** La conjecture est un énoncé GÉNÉRAL (base-indépendant) sur
  l'énergie des sumsets de PG mod p² ⟹ méthode générale (grand crible à modules carrés). Les voies
  « base-2-spéciale » et « extraire la congruence » sont réfutées. Le générique est proche du hasard
  (ChatGPT avait raison là-dessus), mais la queue est générique aussi (pas extractible).

---
*Script universality.py. Phénomène UNIVERSEL (g=2..10 comparables, base 2 non spéciale). Signal
congruence = artefact de moyenne (taux plat ~1.5%, mild ~2× base-dépendant). Corrige STEP41. Outliers =
queue générique, pas structure extractible ⟹ décomposition diag+struct+err ne simplifie pas. Recadre
sur méthode générale (grand crible modules carrés). PAPER/Lean non touchés.*
