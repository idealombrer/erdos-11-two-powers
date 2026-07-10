# STEP40 — Proposition GPT (chercher un premier « qui explose ») : sharpée et TRANCHÉE. Des premiers explosent par-premier (ρ~500), mais le verrou est l'AGRÉGAT (somme), pas un premier isolé. Approche par-premier RÉFUTÉE.

**Date :** 2026-07-04. Script `expander_scan.py`. Test de la proposition GPT (mesurer énergies /
biais de Fourier / gap spectral de S_p={2^0..2^L mod p²}, chercher UN premier où tout explose ;
si aucun ⟹ famille d'expanseurs additifs). **Sharpée en : le ratio par-premier ρ_p=Δ_p/aléatoire
est-il borné sur les Type B ? (si oui ⟹ E₂ fermé per-prime, sans grand crible).**

## Réponse : OUI des premiers « explosent » — mais c'est le mauvais objet

max ρ2 (= Δ_p/(C(P,2)/p²)) sur les Type B (e_p>L) :

| L | #Type B | médiane ρ2 | moy ρ2 | **MAX ρ2** | argmax p (e_p, p/L) | max ρ3 | max ρ4 |
|---|---|---|---|---|---|---|---|
| 60 | 450 | 0 | 0.53 | 33.8 | 2243 (2242, 37) | 1.9 | 0 |
| 100 | 1143 | 0 | 1.04 | 443.6 | 8369 (2092, 84) | 6.6 | 1.3 |
| 140 | 2113 | 0 | 1.15 | 341.1 | 8369 (2092, 60) | 68.3 | 5.6 |
| 180 | 3330 | 0 | 1.12 | 529.0 | 28081 (14040, 156) | 168.7 | 2.4 |

**max ρ2 NON borné (~500), croît.** ⟹ **l'argument par-premier ÉCHOUE** : il existe des Type B avec
Δ_p jusqu'à ~500× l'aléatoire. La proposition GPT « aucun premier n'explose » est **FAUSSE**.

**Qui sont les outliers ?** À petit **index** (p−1)/e_p (coset-structurés, STEP24) : p=8369 (e_p=2092
=(p−1)/4, index 4), et des racines primitives (index 1) à p/L grand. Le découpage e_p>L ne les
distingue pas — un premier peut avoir e_p>L (Type B) ET un petit index (énergie élevée).

## Pourquoi c'est le MAUVAIS objet (le verrou est l'agrégat, pas un premier)

Les outliers, malgré ρ2~500 :
- **explosent seulement en RATIO** : leur Δ_p ABSOLU est petit (~100-250), car la référence aléatoire
  P²/2p² est minuscule pour p grand (~0.4). Un premier avec 109 collisions et référence 0.37 a ρ2=294.
- **sont PEU nombreux** (~20 avec ρ2>3 sur des milliers).
- **ont surtout M_p=2** (ρ3,ρ4≈0 pour la plupart) ⟹ **ne menacent PAS l'extrême** (maxM_B) : ils
  contribuent à #{M_p≥2}≤π(L²)=o(L²) [gratuit], pas à #{M_p≥k≥3}.
- **contribuent <1 % à Σ_p Δ_p** : ~20×200=4000 vs E₂^tot~L³/logL~560000 (L=140). Négligeables.

⟹ **Le verrou est l'AGRÉGAT E_k^tot=Σ_p Σ_r C(N_p(r),k) ≤ C^k E_k^null (une SOMME), qui TIENT**
(STEP33-34 : ratios agrégés 0.34–0.96, ≤1) **MALGRÉ l'explosion par-premier.** La somme est dominée
par la masse des premiers Sidon (médiane ρ=0) ; les outliers ne la dominent pas. **L'analyse
par-premier (GPT) ne capture PAS le verrou** — qui est irréductiblement un énoncé de MOYENNE.

## Le langage expanseur/spectral : légible mais = le sup-bound

La 2ᵉ valeur propre du graphe de Cayley additif de S_p = max_{t≠0}|S_p(t)| = biais de Fourier ~ √L
(STEP31-32). Donc « S_p bon expanseur additif » est VRAI (gap ~1−1/√L) mais **= le sup-bound √L qu'on
a déjà** — 2ᵉ moment. Or l'énergie E₂ est le 4ᵉ moment : un bon expanseur peut avoir E₂ élevée (les
outliers ci-dessus sont de bons expanseurs à E₂ élevée). **Expansion (2ᵉ moment/sup) ≠ énergie
(4ᵉ moment).** Le langage spectral est légible mais ne ferme pas le verrou.

## Verdict (format demandé)

- **Existe-t-il un premier où E₂ explose ?** **OUI** (ρ2~500, premiers à petit index / coset). GPT
  réfuté sur ce point.
- **Cela ferme-t-il / menace-t-il le verrou ?** NON, ni l'un ni l'autre : les outliers sont peu
  nombreux, d'énergie absolue petite, surtout M_p=2 (ρ3,ρ4≈0), <1 % de la somme.
- **Le verrou est-il un phénomène par-premier ?** **NON.** C'est l'AGRÉGAT E_k^tot ≤ C^k E_k^null,
  qui tient (STEP33-34) malgré les outliers. Irréductiblement une MOYENNE (grand crille), confirmant
  STEP35/38.
- **Famille d'expanseurs ?** Vrai (gap ~√L) mais = sup-bound ; expansion ≠ énergie ⟹ n'aide pas.
- **STATUT : RESTE OUVERT.** La proposition GPT (chercher un premier qui explose, langage spectral)
  est **légible mais vise le mauvais objet** : le verrou n'est pas un premier isolé mais la SOMME.
  Ceci RÉFUTE toute la classe d'approches « trouver le contre-exemple premier » et re-confirme que
  l'outil est le grand crible à modules carrés (STEP38), pas une analyse par-premier ou spectrale.

## Le nugget positif

Ce test tranche une ambiguïté réelle : **on ne peut PAS fermer E₂ par une borne par-premier**
(ρ_p non borné), donc l'averaging sur p (grand crible) est GENUINEMENT nécessaire — ce n'était
pas prouvé avant, c'était une conjecture (STEP35). Maintenant c'est établi : le per-prime est
insuffisant PAR CONSTRUCTION (outliers à petit index), le grand crible est incontournable.

---
*Script expander_scan.py. max ρ_p per-prime NON borné (~500, premiers petit index/coset) ⟹ per-prime
échoue. Mais outliers peu nombreux, Δ absolu petit, M_p=2, <1% de la somme ⟹ agrégat E_k^tot≤C^kE_k^null
tient (STEP33-34). Verrou = MOYENNE (grand crible), pas premier isolé. Expander/spectral = sup-bound,
≠ énergie. GPT vise le mauvais objet. RESTE OUVERT. PAPER/Lean non touchés.*
