# STEP31 — L'extrême de Poisson du Type B SUFFIT (le loglog !) et le Type B est SOUS-Poisson. Le vrai résidu = approximation de Poisson des fibres génériques.

**Date :** 2026-07-02. Script `poisson_extreme.py`. Idée (GPT) : l'extrême de Poisson borne-t-il le
Type B ? **Résultat : OUI — l'arithmétique corrigée (avec le loglog) SUFFIT, maxM_B suit log L/loglog L,
et le Type B est SOUS-Poisson (corrélation négative confirmée). La queue super-Poisson ×500 de STEP24
était un artefact du Type A. Le vrai résidu se clarifie : prouver que les fibres GÉNÉRIQUES sont
Poisson-approximables (= input d'équidistribution/somme d'exponentielles), PAS le mur max-vs-énergie
avec queue lourde.**

## L'arithmétique corrigée : le loglog fait tout

$$M''=\underbrace{\sum_{A}(M_p-1)}_{\le\,\sum\lfloor L/e\rfloor+O(1)\#A\,=\,o(L^2)\ \text{[STEP26-lit]}}
+\underbrace{\sum_{B}(M_p-1)}_{\le\,(\max_B M_p-1)\cdot\pi(L^2)}.$$
Extrême de Poisson sur N=π(L²) : max_B M_p = **O(log N/loglog N) = O(log L/loglog L)**. Donc
$$\sum_B(M_p-1)\le O\!\Big(\tfrac{\log L}{\log\log L}\Big)\cdot O\!\Big(\tfrac{L^2}{\log L}\Big)
=O\!\Big(\tfrac{L^2}{\log\log L}\Big)=o(L^2).\ \checkmark$$
**Le slip de GPT** : écrire O(L²·logL/logL)=O(L²) LAISSE TOMBER le loglog. Avec lui, c'est o(L²). Le
facteur **loglog L** est exactement ce qui sépare « pas assez » de « assez ».

## Vérification empirique (décisive)

| L | #B | maxM_B | logL/loglogL | ratio | SB=Σ_B(M_p−1) | SB/L² | #(B,M≥2) |
|---|---|---|---|---|---|---|---|
| 60 | 448 | 3 | 2.90 | 1.03 | 51 | 0.0142 | 47 |
| 100 | 1141 | 4 | 3.02 | 1.33 | 127 | 0.0127 | 117 |
| 180 | 3328 | 4 | 3.15 | 1.27 | 330 | 0.0102 | 303 |
| 260 | 6521 | 4 | 3.24 | 1.23 | 565 | 0.0084 | 525 |
| 300 | 8467 | 5 | 3.28 | 1.53 | 700 | **0.0078** | 651 |

- **maxM_B ≈ (1.0–1.5)·log L/loglog L** : suit la prédiction de l'extrême de Poisson. ✓
- **SB/L² = 0.0142 → 0.0078, décroissance nette → 0** : Σ_B(M_p−1)=o(L²) confirmé. ✓
- excès moyen Type B ≈ SB/#(B,M≥2) ≈ 1.08 (borné). #(B,M≥2) ≈ 0.08·π(L²) = Θ(L²/log L).

## Le Type B est SOUS-Poisson (la corrélation négative de GPT, confirmée)

Histogramme agrégé Type B (e_p>L) vs Poisson, L=120 :

| k | obs (Type B) | Poisson | ratio |
|---|---|---|---|
| 1 | 11 645 096 | 11 643 378 | 1.00 |
| 2 | 18 474 | 19 018 | **0.97** |
| 3 | 657 | 822 | **0.80** |
| 4 | 27 | 56 | **0.48** |

**Queue PLUS LÉGÈRE que Poisson (ratios <1, décroissants).** C'est exactement la corrélation
négative/sous-Poisson espérée. **Contraste avec STEP24** (queue globale super-Poisson ×500) : cette
queue lourde était **entièrement portée par le Type A** (order-driven). Le Type B générique est
propre — mieux : sous-Poisson (les collisions ne se regroupent PAS, car l'involution qui clusterise
le Type A est box-exclue en Type B, STEP30). **L'obstruction « queue lourde » n'existe pas pour B.**

## Ce que ça change (vrai progrès)

Le résidu de #11 se reformule PROPREMENT :
- Type A (structuré) : Σ⌊L/e⌋=o(L²) **acquis** + excès O(1) (ι_p≤2, STEP30). Compris.
- Type B (générique) : Σ_B(M_p−1) ≤ maxM_B·π(L²), et **maxM_B = O(log L/loglog L) suffit** ⟹ o(L²).
  Le Type B étant SOUS-Poisson, l'extrême est CONTRÔLÉ (pas de queue lourde). ✓ empirique, marge↑.

**Le vrai verrou n'est PLUS « max-vs-énergie avec queue super-Poisson »** (ça, c'était le Type A, réglé
autrement). C'est : **prouver que les fibres génériques {2^a+2^b mod p²} sont Poisson-approximables**
(⟹ extrême O(log/loglog)). C'est un énoncé d'ÉQUIDISTRIBUTION, pas d'énergie. Il se ramène aux bornes
de sommes d'exponentielles |S_p(t)|=|Σ_{k≤L} e_{p²}(t·2^k)| ≪ L·p^{−δ} (GPT harmonic PDF, STEP17/24) :
si les 2^k sont équidistribués mod p² (Poisson-approximation à la Chen-Stein), alors sous-Poisson
prouvé et extrême borné.

## Honnêteté sur le « même mur ? »

GPT anticipait « ça risque de buter sur max-vs-énergie en langage probabiliste ». **Partiellement
faux, et c'est la bonne nouvelle** : le mur max-vs-énergie venait de la queue SUPER-Poisson, qui est
un phénomène Type A. Le Type B est SOUS-Poisson ⟹ l'énergie n'y est PAS l'obstruction (max ≈
prédiction Poisson, pas ≫). Ce qui reste n'est pas « borner le max par l'énergie » (impossible) mais
« établir l'approximation de Poisson » (équidistribution/Chen-Stein/Janson + input somme d'exp.). Ça
NE bute PAS sur le même mur — c'est un objectif analytique différent et mieux posé.

## Verdict

- **Extrême de Poisson borné ?** Empiriquement OUI : maxM_B ~ log L/loglog L (ratio 1.0–1.5).
- **Suffit-il ?** OUI, avec le loglog : Σ_B(M_p−1) ≤ maxM_B·π(L²) = O(L²/loglog L) = o(L²). Le slip
  de GPT (O(L²)) venait d'avoir laissé tomber le loglog.
- **Variables négativement corrélées ?** OUI, CONFIRMÉ : Type B SOUS-Poisson (ratios 0.97,0.80,0.48).
- **Même mur max-vs-énergie ?** NON pour le Type B : la queue lourde (obstruction énergie) était un
  artefact Type A ; Type B propre. Le résidu = approximation de Poisson (équidistribution), pas énergie.
- **STATUT :** M″=o(L²) réduit à : [Type A : acquis Σ⌊L/e⌋ + ι_p≤2] + [Type B : maxM_B=O(logL/loglogL),
  = Poisson-approximation des fibres génériques, empiriquement sous-Poisson, marge croissante]. **Le
  Type B est un objectif analytique PROPRE (somme d'exponentielles/Chen-Stein), pas le mur énergie.**
  Reste ouvert mais reformulé favorablement. Piste de GPT = la bonne, arithmétique validée.

---
*Script poisson_extreme.py. L'extrême de Poisson (avec loglog !) SUFFIT pour Type B ; maxM_B~logL/loglogL,
Type B SOUS-Poisson (queue légère, ≠ super-Poisson global qui était Type A). Résidu = Poisson-approx
des fibres génériques (équidistribution/somme d'exp), PAS max-vs-énergie. PAPER intact.*
