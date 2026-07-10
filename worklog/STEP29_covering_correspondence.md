# STEP29 — κ_p vs covering systems (Granville–Soundararajan) : RAFFINEMENT STRICT (marginale orthogonale, pas équivalence).

**Date :** 2026-07-02. Script `covering_test.py`. Test de classification théorique : κ_p est-il un
objet de covering system (GS/Hough), ou nouveau ? **Verdict : le CADRE est un covering system 2D
tronqué (classique, déjà invoqué STEP17) ; mais κ_p est la marginale CONCENTRATION, ORTHOGONALE à
la marginale DENSITÉ que GS contrôlent. RAFFINEMENT STRICT : ni équivalence (autre marginale), ni
objet neuf ex nihilo (cadre covering classique). Le contenu ouvert/dur (κ_p) est HORS du cadre GS.**

## 1. La correspondance canonique fibres ↔ covering (existe, explicite)

n mauvais ⟺ ∀(l,m)∈[0,L]², ∃p : p²|n−2^l−2^m ⟺ les **B_p(n)={(l,m):p²|n−2^l−2^m} RECOUVRENT
[0,L]²**. C'est un **système de recouvrement 2D tronqué** sur le réseau des exposants. Chaque
B_p(n) est une **union de classes de congruence** : (l,m)∈B_p(n) ⟺ l−m≡δ (mod e_p) pour un δ admissible
ET m≡f(l) (mod d_p). Vérifié (p=127, pire n≡2797) : B_p(n) = **κ_p=2 classes** (l−m≡1 mod 7 : 4 paires ;
l−m≡6 mod 7 : 8 paires). Donc **κ_p = nombre de classes de congruence de p se superposant au pire n**
= la **multiplicité de covering du premier p** en ce point.

## 2. Deux marginales du MÊME covering — GS contrôle l'une, κ_p est l'autre

L'incidence (l,m)×p a (cf. STEP22, 3 marginales) une marginale **DENSITÉ** et une marginale **PIC** :

| Marginale | Quantité | Ce qu'elle mesure | Qui la contrôle |
|---|---|---|---|
| **DENSITÉ** (union) | ρ(n)=Σ_p\|B_p(n)\|/#paires, E[ρ]=Σ_p 1/p² | le covering est-il assez dense (≥1) ? | **GS/Hough** (Σ1/m≥1, module min.) |
| **CONCENTRATION** (pic) | M_p=max_n\|B_p(n)\|, κ_p | un seul p peut-il empiler ses congruences ? | **κ_p (ce travail)** — hors GS |

**Obstruction GS = marginale densité :** Σ_{p≥3}1/p²=**0.2022 < 1** ⟹ pas de recouvrement plein ⟹
presque tout n bon (= STEP17, « almost all n »). **C'est EXACTEMENT le résultat GS**, déjà acquis.

## 3. Pour (L,L²], le covering est SOUS-CRITIQUE ⟹ GS ne dit rien sur κ_p

Densité du covering portée par les GRANDS premiers (L,L²] : **Σ_{p>L}1/p² = 0.0054 (L=40), 0.0022
(L=80) → 0.** La densité (GS) vient des PETITS premiers p≤L (0.20). Donc dans (L,L²] :
- **Marginale densité → 0** : négligeable, GS-triviale (STEP17 : premier moment O(1/log L)).
- **Marginale concentration = κ_p** : un grand premier a densité ~1/p²≈0 MAIS peut concentrer
  ⌊L/e_p⌋+κ_p paires sur UN n. **C'est toute la question « every n ».**

**κ_p décorrélé de la densité (vérifié) :** 1/p² monotone ↓ en p, κ_p NON (p=8191 densité 1.5e-8,
κ=2 ; p=101 densité 9.8e-5, κ=5). **κ_p ⊥ densité GS.** GS contrôlent la densité ; la concentration
worst-case dans un régime SOUS-CRITIQUE (densité<1) **n'est pas dans leur cadre** (GS/Hough : théorie
des coverings à densité ≥1, module minimal, non tronqués).

## 4. La contrainte a+δ≤L = troncature DIAGONALE (non-standard covering)

Chaque classe de congruence l−m≡δ (mod e), m≡f (mod d_p) est une DROITE infinie sur ℤ². La boîte
{0≤l,m≤L} la tronque à ⌊L/e_p⌋+1 points — troncature **diagonale couplant l,m**. Les covering
systems GS sont **non tronqués** (recouvrement de ℤ entier). La troncature finie + le couplage
diagonal = exactement la « boîte » que STEP28 a montrée invisible à l'énergie multiplicative. GS
n'ont pas d'outil pour la concentration d'un covering tronqué sous-critique.

## 5. Verdict de classification (trichotomie demandée)

- **Équivalence ?** NON. La marginale densité (Σ1/p²) EST du GS (et déjà exploitée : almost all n).
  Mais κ_p est la marginale CONCENTRATION, décorrélée de la densité. GS ne bornent PAS le pic.
- **Objet nouveau ex nihilo ?** NON. Le cadre (covering 2D tronqué sur les exposants) est classique,
  et le lien Σ1/p²<1 était déjà identifié (STEP17). Rien n'est inventé from scratch.
- **RAFFINEMENT STRICT ?** **OUI.** κ_p = **marginale concentration/multiplicité d'un covering
  sous-critique tronqué** — un objet légitimement DIFFÉRENT de la densité GS, adressant précisément
  l'écart « almost all n » (densité, GS, fait) → « every n » (concentration, κ_p, ouvert). C'est un
  vrai progrès structurel : on sait maintenant que le verrou n'est PAS un problème de covering-densité
  (GS le règle : densité→0 dans la plage), mais de covering-CONCENTRATION, question orthogonale que
  la théorie GS ne touche pas.

## 6. Pourquoi ça éclaire la difficulté (et boucle avec STEP28)

GS/covering = « le covering est-il assez DENSE ? » (2ᵉ moment/union). κ_p = « un seul premier peut-il
CONCENTRER ses congruences tronquées ? » (pic/max). C'est **le même clivage densité-vs-pic que
max-vs-énergie** (STEP19-28) : les outils de densité (GS, énergie, covering-Σ1/m) voient l'union/le
2ᵉ moment ; κ_p est le pic sous troncature additive. **Covering systems ⊂ outils de densité ⟹ ne
peuvent pas fermer κ_p**, exactement comme l'énergie (STEP28). Cohérent : c'est un mur d'outil, pas
un manque d'effort. Le résidu κ_p=O(1) est la concentration d'un covering sous-critique — objet
d'additive-combinatorics (grande déviation), pas de covering-théorie.

## Sortie

- **Application fibres→covering :** construite (B_p(n)=κ_p classes de congruence ; vérifié p=127).
- **κ_p exprimable en covering ?** OUI comme **multiplicité de covering du premier p** (nb de ses
  congruences superposées), PAS comme densité/module (marginale orthogonale).
- **Où apparaît a+δ≤L :** troncature diagonale du covering au carré [0,L]² (couple l,m).
- **Équivalent à un covering tronqué ?** La STRUCTURE oui ; la QUESTION (concentration sous-critique)
  non — hors cadre GS (densité≥1, non tronqué).
- **Conclusion : RAFFINEMENT STRICT.** Cadre covering classique (densité = GS = almost all n, acquis) ;
  κ_p = marginale concentration orthogonale, = le contenu ouvert, non couvert par GS. Même clivage
  densité/pic que max-vs-énergie ⟹ covering systems ne ferment pas κ_p (mur d'outil, STEP28-cohérent).

---
*Script covering_test.py. #11 = covering 2D tronqué sur les exposants ; densité=Σ1/p²=GS (almost all,
acquis) ; κ_p=marginale concentration, ⊥ densité (décorrélé vérifié), sous-critique dans (L,L²],
troncature diagonale — HORS cadre GS. Raffinement strict, pas équivalence. PAPER intact.*
