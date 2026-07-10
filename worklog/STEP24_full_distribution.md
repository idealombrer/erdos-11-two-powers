# STEP24 — Distribution COMPLÈTE des multiplicités (piste GPT « mauvais invariant ? ») — RÉFUTÉE, mais diagnostic net

**Date :** 2026-07-02. Scripts `checkdist.py`, `checkdist2.py`. Piste ChatGPT : et si tout était
centré sur le mauvais invariant — le max M_p au lieu de la **loi entière** {N_p(r)} ? Étude
systématique de l'histogramme complet des multiplicités de somme
`N_p(r)=#{(a,b),0≤a≤b≤L:2^a+2^b≡r mod p²}` (correction de notation : GPT écrivait `#{k:2^k≡r}`,
trivial car déterminé par d_p ; l'objet réel de la preuve est la multiplicité de **somme**).

**Verdict : hypothèse RÉFUTÉE.** Le max n'est PAS la valeur extrême d'une loi universelle. Mais
la piste produit une caractérisation SHARP du mur max-vs-énergie, jamais faite avant.

## Découverte centrale : loi = BULK Poisson universel + QUEUE super-Poisson non-universelle

Histogramme agrégé `#{(p,r):N_p(r)=k}` vs prédiction Poisson `Σ_p p²·e^{-λ}λ^k/k!` (λ=P/p²,
P=(L+1)(L+2)/2), L=80 :

| k | observé | Poisson-attendu | ratio |
|---|---|---|---|
| 1 | 2 668 751 | 2 674 609 | **1.00** |
| 2 | 10 999 | 10 114 | **1.09** |
| 3 | 1 313 | 547 | 2.40 |
| 4 | 234 | 39.5 | 5.92 |
| 5 | 100 | 2.75 | 36.3 |
| 6 | 88 | 0.18 | **500.8** |

- **Le bulk (k=1,2) EST Poisson** (à ~9 %). Or les doubles k=2 = l'énergie Δ_p. Donc **la partie
  universelle de la loi ne redonne QUE l'énergie** — l'invariant que toutes les méthodes contrôlent
  déjà, et qui donne Θ(L²) (STEP19-22). Rien de neuf de ce côté.
- **La queue (k≥3) est massivement super-Poisson** (×2.4 → ×500). Queue-ratios Pr(N≥t)/Pr(N≥t−1) :
  0.005, 0.14, 0.24, 0.45, 0.47 — **croissants** : queue plus lourde que géométrique, a fortiori que
  Poisson (qui donnerait λ/t décroissant). C'est là que vit M_p.

## Pourquoi ça RÉFUTE « M_p = valeur extrême d'une loi universelle » (l'espoir de GPT)

1. **Aucune stat simple ne détermine M_p** (corrélations, L=80, 812 premiers) :
   √Δ_p 0.92 (mais facteur ~18 lâche, STEP21), Δ_p 0.70, λ_p 0.67, entropie −0.75, var 0.61,
   1/d_p 0.61. Le meilleur (√Δ_p) reste une borne d'énergie, déjà réfutée comme voie.
2. **La queue est HÉTÉROGÈNE, pas une loi** : les M_p≥3 ont e_p=ord_p(2) médian 36, min 7
   (127=Mersenne), **max 210=p−1** (p=211,197,139,107,101 : 2 racine primitive !). Donc gros M_p
   **≠** petit ordre exclusivement (confirme STEP23 : corr 0.71 non exclusive). corr(M_p,⌊L/e_p⌋+1)
   =0.70 seulement, prédicteur naïf faux (p=101 e_p=100 → M_p=4).
3. **L'universalité par-premier est bruitée** : Δ_p/Δ_Poisson oscille 0 → 11.65 selon λ. Le match
   Poisson des doubles est un effet d'**agrégation** sur ~800 premiers, pas une loi par-premier
   exploitable pour une grande déviation.
4. **Mécanisme des top-fibres (EXP8) = arithmétique, pas probabiliste** : p=257=2⁸+1 (Fermat),
   fibre max = (0,8),(16,24),(32,40),(48,56),(64,72) : b−a≡8 constant, a en PA de pas 16=ord_p(2)
   [car 2^a(1+2⁸)≡0]. p=127,89 : a+b en PA de pas ord_p(2). Structure déterministe pour
   Fermat/Mersenne — donc PAS tirée d'une loi aléatoire universelle.

## Décomposition de M″ = Σ(M_p−1)

| L | S1=Σ(M_p−1) | M_p=2 (doubles, part Poisson) | M_p≥3 (queue arithm.) | % queue |
|---|---|---|---|---|
| 60 | 96 | 54 prem → 54 | 18 prem → 42 | 44 % |
| 80 | 148 | 98 prem → 98 | 19 prem → 50 | 34 % |
| 100 | 219 | 135 prem → 135 | 32 prem → 84 | 38 % |

**M″ ≈ 60 % bulk-Poisson (= énergie, déjà comprise) + ~40 % queue arithmétique** portée par
~20-30 premiers exceptionnels hétérogènes. C'est exactement la partie NON-universelle qui résiste.

## Réponse à la question principale de GPT

« Existe-t-il une propriété robuste de la distribution ENTIÈRE plus stable que M_p ? »
- **OUI, mais inutile :** le bulk (doubles) est stablement Poisson — mais ce n'est QUE l'énergie
  Δ_p ≈ P²/2p², l'invariant que 4-5 outils contrôlent déjà et qui plafonne à Θ(L²).
- **NON pour ce qui compte :** M_p vit dans une queue super-Poisson non-universelle et hétérogène.
  Il n'est PAS la valeur extrême d'une loi unique ⟹ **pas de réduction à une grande déviation
  probabiliste.** La stratégie n'est donc PAS « centrée sur le mauvais invariant » : le max EST
  intrinsèquement l'objet dur, et la loi entière le confirme en le SÉPARANT du bulk universel.

## Le même mur, vu plus net (apport réel de la session)

Nouveau diagnostic du mur max-vs-énergie (STEP19-22), plus précis que « EM≈1.3 » :
> La loi de multiplicité additive de {2^a+2^b mod p²} = **bulk Poisson universel (= l'énergie,
> contrôlable, Θ(L²)) + queue super-Poisson non-universelle et arithmétique (order-driven pour
> Fermat/Mersenne, mais aussi présente pour racines primitives) où vit M_p.** Aucun moment, aucune
> entropie, aucune borne d'énergie ne capture cette queue (meilleur correlate √Δ_p à 0.92 encore
> ×18 lâche). C'est POURQUOI les méthodes d'énergie voient k=2 (universel) mais ratent le max.

## Verdict (format demandé)

- **Loi universelle avec M_p = extrême ?** **NON, RÉFUTÉ.** Bulk Poisson (redonne l'énergie),
  queue super-Poisson non-universelle/hétérogène (où vit M_p). Pas de loi limite unique.
- **Stat simple qui détermine M_p ?** **NON.** √Δ_p 0.92 mais ×18 lâche ; entropie/var/λ/1/d_p
  toutes 0.6-0.75. Aucune ne le capture (toutes = énergie déguisée).
- **Corrélations arithmétiques ?** gros M_p corrèle faiblement avec petit ordre (1/d_p à 0.61)
  mais **non exclusif** (racines primitives p=101,211 ont M_p=4). Pas de signature unique.
- **Réduit-il M″ / ouvre-t-il une voie ?** **NON — même mur.** ~40 % de M″ est la queue
  arithmétique non-universelle, hors de portée des arguments de loi/moment.
- **RÉFUTÉE** comme piste vers un nouvel invariant, **MAIS** cristallise le mur : distribution =
  Poisson (énergie) ⊕ queue arithmétique (max). Cohérent avec « on tombe sur le même mur ».
- **Plausibilité M″ :** inchangée, élevée (S1/L²↓). Preuve = contrôle de la queue arithmétique
  hétérogène, non probabiliste — niveau spécialiste, confirmé sous un 6ᵉ angle.

---
*Scripts `checkdist.py` (8 exp : moments, Poisson-fit, queue, universalité, corrélations, entropie,
régimes d_p, géométrie fibres), `checkdist2.py` (mécanisme ordre, universalité bulk, décomp. M″).
Réfute « loi universelle → M_p extrême » ; le bulk Poisson = énergie (connue), le max vit dans une
queue arithmétique non-universelle. PAPER.tex/PDF intacts (cf. feedback).*
