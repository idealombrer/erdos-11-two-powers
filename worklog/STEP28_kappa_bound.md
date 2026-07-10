# STEP28 — κ_p=O(1) via énergie additive/multiplicative : APPROCHE RÉFUTÉE (l'énergie est box-aveugle). κ_p=O(1) reste ouvert.

**Date :** 2026-07-02. Script `kappa_energy.py`. Objectif : prouver κ_p=O(1) (dernier verrou,
STEP27) via l'énergie multiplicative du sous-groupe ⟨2⟩ (Heath-Brown–Konyagin, Shkredov).
**Résultat : l'approche énergie est STRUCTURELLEMENT INADAPTÉE — elle est aveugle à la contrainte
de boîte {a+δ≤L}, qui est précisément ce qui fait M_p ≪ occupation-coset. Mur pour l'outil (pas
"c'est difficile"). κ_p=O(1) reste empiriquement vrai (≤6, L≤220) mais hors de portée de l'énergie.**

## Le mur : l'énergie multiplicative de ⟨2⟩ est BOX-AVEUGLE

Objets : S={1+2^δ mod p² : δ≤L}, H=⟨2⟩ mod p². m*(p)=max occupation d'un coset de H par S
(=max_v #{δ:(1+2^δ)^{d_p}≡v}, car x∈coset ⟺ x^{d_p} fixé). m* MAJORE M_p mais **ignore la boîte**.

**ÉTAPE 4 — contre-exemple décisif p=101 (racine primitive, e=100=p−1, index 1) :**

| L | m*(occupation coset) | M_p | κ_p |
|---|---|---|---|
| 40 | 41 (=L+1) | 2 | 2 |
| 80 | 80 (≈L+1) | 4 | 4 |
| 160 | 159 (≈L+1) | 5 | 5 |

**⟨2⟩ = tout le groupe ⟹ S entier dans UN SEUL coset ⟹ m*=|S|=L+1, quelle que soit la valeur de
M_p.** L'occupation-coset (donc E×, énergie) est MAXIMALE et **constante en M_p** : elle ne contient
littéralement aucune information sur M_p. Le facteur L+1 → M_p=O(1) est fait **à 100% par la boîte**
`a+δ≤L` (contrainte additive sur les exposants), invisible à la structure multiplicative des cosets.

**⟹ Aucune borne M_p ≤ f(E×, m*, ν_p) monotone ne peut marcher** pour Type B : les quantités
d'énergie sont saturées (=|S|²,|S|) tandis que M_p est minimal. C'est une réfutation structurelle,
pas un manque de finesse. (Réfute aussi l'ÉTAPE 4 du plan « κ_p=1 pour Type B » : faux, κ_p=M_p=4-5 ;
la prémisse "chaque coset ≤1 δ" suppose index grand, or les Type B à M_p≥2 sont quasi-racines-primitives, index petit.)

## Surcomptage aussi en Type A (ÉTAPE 2/3)

| p | e | L | M_p | κ_p | m* | E×(S,H) | ν_p |
|---|---|---|---|---|---|---|---|
| 127 | 7 | 160 | 12 | 2 | 46 | 6877 | 2 |
| 257 | 16 | 160 | 11 | 3 | 40 | 4261 | 4 |
| 683 | 22 | 160 | 8 | 3 | 29 | 2891 | 4 |
| 281 | 70 | 220 | ≥4 | 6 | — | — | 22 |

- **m* ≈ 2–4× M_p** même en Type A (box-aveugle partout, moins catastrophique).
- **Borne Cauchy-Schwarz κ_p ≤ E×/(L/e)²** (ÉTAPE 2) : p=257 donne 4261/100=42.6 ≫ κ_p=3
  (×14) ; p=127 : 6877/522=13.2 ≫ 2 (×6). **Inutilisable** (E× box-aveugle).
- **ν_p = max_r #{g∈⟨2⟩ mod p : 1+g∈rH}** (comptage sous-groupe mod p, éq. García-Voloch/HBK) :
  ν_p ≫ κ_p (p=281 : 22 vs 6 ; p=101 : 99 vs 5). La borne d'énergie mod p **surcompte κ_p** ×4–20.

**ÉTAPE 3 — Heath-Brown–Konyagin / Shkredov, régime :** leurs bornes donnent
ν_p = #{x+y=1 : x,y∈⟨2⟩} = O(e_p^{2/3}) (e_p<p^{2/3}). Or (i) c'est mod p, box-aveugle, ⟹ borne
κ_p pas M_p ; (ii) même comme borne de κ_p : M_p ≤ ν_p(⌊L/e⌋+1) ≤ e^{2/3}(L/e+1)~L·e^{−1/3}, et
sommée Σ_{e≤L} e^{2/3}(L/e)·#{e_p=e} avec #{e_p=e}≤e log2/logL donne O(L^{8/3}/logL) ≫ L². **Trop
faible d'un facteur polynomial.** Les bornes de sous-groupe ne franchissent pas l'écart.

## κ_p empirique : petit, lentement croissant (mais l'énergie ne l'atteint pas)

max_p κ_p (M_p≥4, hors Wieferich) : **4, 4, 4, 5, 6** pour L=60,100,140,180,220. Petit, croissance
lente (~log L ?), **≪ ν_p** (la borne énergie). Donc κ_p=O(1) plausible empiriquement, mais l'outil
énergie donne au mieux ν_p=O(e^{2/3}) ≫ κ_p — **il ne peut pas prouver κ_p=O(1)**.

## Pourquoi c'est le MÊME mur (max-vs-énergie), un niveau plus bas

Depuis STEP19, tous les outils butent car ils contrôlent l'ÉNERGIE (2ᵉ moment, occupation,
collisions) mais M″ veut le MAX (multiplicité de pic). Ici, exactement pareil pour κ_p :
- Énergie multiplicative E×(S,⟨2⟩) / occupation m* = « combien de S dans le même coset » (2ᵉ moment
  multiplicatif) — **saturée, box-aveugle**.
- κ_p / M_p = pic sous contrainte de boîte — **ce qu'on veut, invisible à l'énergie**.
La boîte {a+δ≤L} est une condition ADDITIVE sur les exposants ; l'énergie de sous-groupe est
MULTIPLICATIVE. L'outil est dans le mauvais registre. Récurrence exacte du mur STEP19-23.

## Verdict (format demandé)

- **E×(S,H) empirique, croissance en L ?** Croît ~ quadratiquement en L (Σ occupation² ; p=127 :
  1731→6877 pour L=80→160). Mais **box-aveugle** ⟹ ne mesure pas M_p.
- **Borne de Shkredov applicable mod p² ?** Elle borne ν_p (mod p) = O(e^{2/3}) ; box-aveugle ET
  trop faible (sommée : L^{8/3}≫L²). Non concluante.
- **Type B : κ_p=1 prouvé (étape 4) ?** **NON, RÉFUTÉ.** p=101 : m*=L+1 mais M_p=κ_p=4-5. La boîte,
  pas le coset, borne M_p ; l'argument étape 4 (prémisse "1 δ/coset") est faux pour les Type B actifs.
- **Type A : κ_p borné comment ?** Empiriquement ≤6 ; par l'énergie seulement κ_p≤ν_p=O(e^{2/3})
  (surcompte ×4–20, insuffisant sommé).
- **κ_p=O(1) global : prouvé/conditionnel/réfuté ?** **NON prouvé.** L'APPROCHE ÉNERGIE est **RÉFUTÉE**
  (box-aveugle, mur structurel). κ_p=O(1) reste une conjecture empirique (≤6, L≤220).
- **M″ résolu si κ_p=O(1) ?** Oui (M″≤Σκ_p(⌊L/e⌋+1)=o(L²) via STEP26). Mais κ_p=O(1) non acquis.
- **STATUT : RESTE OUVERT.** Réfutation de l'outil énergie (structurelle : additif vs multiplicatif,
  box-aveugle). Le verrou κ_p=O(1) exige un argument SENSIBLE À LA BOÎTE (comptage de solutions de
  2^a+2^b≡r dans le triangle {a+δ≤L}, niveau p-adique 2ᵉ ordre) — hors de portée de l'énergie de
  sous-groupe. Même mur max-vs-énergie, récurrent, maintenant au niveau κ_p.

---
*Script `kappa_energy.py`. L'énergie multiplicative de ⟨2⟩ est box-aveugle (p=101 : m*=L+1, M_p=5) ⟹
ne peut prouver κ_p=O(1). ν_p (HBK/Shkredov, O(e^{2/3})) surcompte κ_p et est trop faible sommé.
κ_p=O(1) reste empirique (≤6). Mur max-vs-énergie récurrent. PAPER intact.*
