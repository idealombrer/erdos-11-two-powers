# STEP35 — Crible de Heath-Brown sur E_2 : le gain vient de l'averaging (confirmé), MAIS le terme d'erreur (sommes de caractères ~L, queue lourde) n'est PAS trivialement contrôlé. E_2 au bon ordre, preuve NON immédiate.

**Date :** 2026-07-03. Script `heath_brown_e2.py`. Test du crible du carré / averaging sur E_2.
**Résultat : (1) le gain O(L³/logL) vient BIEN de l'averaging sur p (moyenne Δ_p/aléatoire=1.75
bornée), pas du per-prime (qui donne O(L⁴/logL)). (2) MAIS deux pièges confirmés : les sommes de
caractères Σχ(2^j) atteignent ~0.8L (PAS O(1) — argument ÉTAPE 4 réfuté), et la distribution de Δ_p
a une queue lourde (outliers à 421× l'aléatoire = premiers Type A). Donc le crible est au bon ordre
mais sa mise en œuvre rigoureuse n'est PAS immédiate : le terme d'erreur exige un vrai grand crible.
CONDITIONNEL, outil identifié, non clos.**

## ÉTAPE 2a — E_2^tot ~ L³/logL (avec dérive de constante)

| L | 30 | 40 | 50 | 60 | 70 |
|---|---|---|---|---|---|
| E_2^tot·logL/L³ | 0.136 | 0.141 | 0.148 | 0.163 | 0.170 |

Légèrement croissant ⟹ E_2^tot = Θ(E_2^null) solide (STEP34, ratio ~0.95), mais la constante
asymptotique dérive (facteur lentement croissant possible). Caveat mineur sur « exactement L³/logL ».

## ÉTAPE 2b — le gain est l'AVERAGING sur p (confirmé), mais queue lourde

Δ_p/aléatoire(P²/2p²), tous premiers, L=60 : **moyenne 1.75, médiane 0.00, max 421, %(>2)=7%.**
- La plupart des p ont Δ_p ≤ aléatoire (souvent 0). **Moyenne bornée (1.75)** ⟹ Σ_p Δ_p = 1.75·Σ
  aléatoire = O(L³/logL). **Le facteur L de gain vient de l'averaging** (per-prime : sup-bound donne
  Δ_p=O(L²) ⟹ Σ=O(L⁴/logL) ; l'averaging le corrige).
- **MAIS queue lourde : outliers à 421× l'aléatoire.** Ce sont les premiers à petit ordre (Type A).
  Pour Type B seul, ratio ≤1 (STEP34) — propre. Mais une PREUVE de la moyenne bornée doit absorber
  ces outliers (contrôle du 2ᵉ moment Σ Δ_p²), non trivial.

## ÉTAPE 4 — sommes de caractères : piège 1 CONFIRMÉ (PAS O(1))

max_χ |Σ_{j≤L} χ(2^j)|, p Type B, L=80 :

| p | e_p | #{χ:χ(2)=1} | max\|Σ\| | /√p | /L |
|---|---|---|---|---|---|
| 211 | 210 | 1 | 62.6 | 4.31 | 0.78 |
| 409 | 204 | 2 | 61.6 | 3.04 | 0.77 |
| 809 | 404 | 2 | 75.8 | 2.66 | 0.95 |
| 1279 | 639 | 2 | 78.9 | 2.21 | 0.99 |

**max|Σχ(2^j)| ~ 0.8L**, PAS O(1) ni O(√p). Les caractères **quasi-triviaux** (χ(2)=e(m/e), m petit)
ont Σ ~ L (somme géométrique partielle non annulée). ⟹ **l'argument ÉTAPE 4 (« seul χ trivial
contribue O(L), les autres O(1) ») est RÉFUTÉ.** Il y a ~L caractères à somme ~L. Le terme d'erreur
du crible de Heath-Brown n'est donc PAS trivialement borné par le seul caractère trivial.

## Pourquoi le crible ne clôt pas immédiatement (honnête)

Le crible du carré / grand crible ramène Σ_p Δ_p à :
- un TERME PRINCIPAL Σ_p (L+1)⁴/p² ~ L³/logL (le bon ordre, = aléatoire) ; **acquis** ;
- un TERME D'ERREUR = sommes de caractères Σ_{t≠0} (structure des 2^j mod p²). Empiriquement ces
  sommes atteignent ~L (piège 1), et la contribution par-premier Δ_p a des outliers ~421× (queue).
  Un grand crible RIGOUREUX doit montrer que ces erreurs se compensent en moyenne — vrai
  empiriquement (moyenne 1.75 bornée) mais **PAS une application en une ligne** : il faut contrôler
  le 2ᵉ moment / les grandes déviations des sommes de caractères, ce qui est le cœur analytique.

## Verdict (format demandé)

- **Borne de crible sur E_2 au bon ordre O(L³/logL) ?** OUI empiriquement (averaging, moyenne
  Δ_p/aléatoire=1.75 bornée). Le gain du facteur L vient de l'averaging sur p, pas du per-prime.
- **Terme d'erreur (sommes de Weil/caractères) contrôlé ?** **NON trivialement** : max|Σχ(2^j)|~0.8L
  (piège 1 confirmé), queue lourde de Δ_p (outliers 421×). Contrôlé EN MOYENNE (empirique) mais pas
  par une borne simple ⟹ exige un vrai grand crible (2ᵉ moment des sommes de caractères).
- **Itération à k≥3 correcte et fermée ?** NON testée en détail — hériterait des mêmes obstructions
  (erreurs de caractères, queue), amplifiées. Pas fermée.
- **E_k^tot ≤ C^k E_k^null prouvé ?** **NON.** Au bon ORDRE empirique (E_k/E_k^null ≤1), mais la
  preuve via crible bute sur le terme d'erreur non trivial.
- **M″ prouvé ?** **NON.**
- **STATUT : CONDITIONNEL, PAS un mur, mais preuve NON immédiate.**
  - **Confirmé :** E_2 au bon ordre ; le gain est l'averaging sur p (structurellement correct).
  - **Obstruction identifiée :** terme d'erreur du crible = sommes de caractères ~L (pas O(1)) +
    queue lourde de Δ_p ⟹ nécessite un grand crible fin (contrôle du 2ᵉ moment), non élémentaire.
  - **RESTE OUVERT :** E_k^tot ≤ C^k E_k^null. L'outil (crible/grand crible) est le bon et donne le
    bon ordre, mais le rendre rigoureux = contrôler les sommes de caractères en moyenne quadratique.
    Ce n'est plus « quel outil » mais « exécuter le grand crible » — un travail analytique standard
    mais réel.

## Recommandation

Après STEP34-35, le diagnostic est stable : E_2 (et E_k) sont au bon ordre, le crible est le bon
outil, mais le terme d'erreur (sommes de caractères de la suite lacunaire {2^j mod p²}, ~L et non
O(1)) exige un grand crible fin — le même cœur analytique que Bourgain-Garaev, désormais sous forme
« moyenne quadratique des sommes de caractères », pas « sup ». **Le livrable mûr est le THÉORÈME
CONDITIONNEL (piste 6)** : énoncer #11-every-n conditionnellement à E_k^tot ≤ C^k E_k^null (ou à la
borne de grand crible équivalente), avec Type A / Wieferich / order-sum inconditionnels. Cela isole
l'unique input analytique en une phrase standard et capitalise toute la réduction (STEP19-35).

---
*Script heath_brown_e2.py. Averaging sur p donne le bon ordre (moyenne Δ_p/aléatoire=1.75 bornée),
MAIS sommes de caractères Σχ(2^j)~0.8L (piège 1 confirmé, ÉTAPE 4 réfutée) + queue lourde de Δ_p ⟹
terme d'erreur non trivial ⟹ crible non clos, exige un grand crible fin. E_k au bon ordre, preuve
non immédiate. Recommandation : théorème conditionnel. PAPER intact.*
