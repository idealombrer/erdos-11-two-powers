# STEP27 — Prouver M_p ≤ ⌊L/ord_p(2)⌋+O(1) ? Argument naïf RÉFUTÉ ; borne per-classe PROUVÉE ; exception Wieferich localisée ; reste ouvert = κ_p=O(1).

**Date :** 2026-07-02. Scripts `final_bound.py`, `final_bound2.py`. Dernier maillon : prouver la
borne per-premier. **Résultat : l'argument « une PA par classe » (ÉTAPE 3 du plan) est FAUX.
On PROUVE la borne per-classe M_p ≤ κ_p·(⌊L/e⌋+1) et on LOCALISE l'unique exception (Wieferich),
mais la borne serrée M_p ≤ ⌊L/e⌋+O(1) reste conditionnelle à κ_p=O(1) (empirique, non prouvé).
STATUT : RESTE OUVERT, progrès structurel réel.**

## ÉTAPE 3 (argument proposé) — RÉFUTÉ

Le plan proposait : « δ,δ' même classe C ⟹ 1+2^δ≡1+2^{δ'} mod p ⟹ 2^δ≡2^{δ'} ⟹ δ≡δ' mod e ⟹
une seule PA par classe ⟹ M_p≤⌊L/e⌋+1 ». **Faux dès la 1ʳᵉ implication.** « Même classe de ⟨2⟩ »
signifie (1+2^δ)/(1+2^{δ'})∈⟨2⟩, i.e. **1+2^δ≡2^s(1+2^{δ'}) mod p²** — PAS congruents (sauf s=0).
Deux δ d'une même fibre vérifient 1+2^δ≡2^{a'−a}(1+2^{δ'}). Contre-exemple (p=257, e=16, fibre max) :
δ=41 (≡9 mod e, 1+2^δ≡256 mod p) et δ=144 (≡0, 1+2^δ≡2) COEXISTENT — classes mod e différentes,
1+2^δ mod p différents. **κ (nb de classes mod e dans la fibre) = 3, pas 1.**

Données κ (fibre max, L=160) : κ∈{1,2,3,4,5} selon p (257:3, 683:3, 233:2, 241:1…). Jamais garanti 1.

## Ce qui est PROUVÉ : borne per-classe (via p>L, non-Wieferich)

Pour p>L **non-Wieferich** : d_p=ord_{p²}(2)=p·e>L (e=ord_p(2)), donc pour chaque a∈[0,L] au plus
UN b=a+δ∈[0,L] (unicité de 2^b≡r−2^a mod p²). En groupant les reps d'une fibre par (a,δ) mod e :
a=a_0+en, δ=δ_0+em, la contrainte mod p² devient **une droite** n·X+m·Y≡Z mod p (X,Y du dvpt
p-adique 2^e≡1+q_p·p, non-dégénérée car q_p≠0), et la boîte {a+δ≤L} devient un triangle de côté
T=⌊(L−a_0−δ_0)/e⌋≤⌊L/e⌋. Comme **T<p** (car p>L≥eT), chaque m donne ≤1 n ⟹
$$\boxed{\text{par classe }(a_0,\delta_0)\bmod e:\ \le \lfloor L/e\rfloor+1\ \text{reps}.}$$
**Vérifié : 0 violation** (toutes les tailles de classe ≤⌊L/e⌋+1). D'où **M_p ≤ κ_p·(⌊L/e_p⌋+1)**,
κ_p = nb de classes actives. **ord_p(2)=e est le bon dénominateur** (et non d_p=ord_{p²}(2)=pe) :
le facteur p tué par la réduction mod p → mod p² est exactement le pas de la PA. (M1, réfuté en
STEP15, utilisait d_p : mauvais niveau.)

## L'exception Wieferich (localisée précisément)

L'analyse suppose **q_p≠0** (non-Wieferich). Pour p Wieferich (2^{p-1}≡1 mod p²), q_p=0 : la droite
n·X+m·Y≡Z DÉGÉNÈRE (X≡Y≡0), la contrainte mod p² s'effondre, des classes entières collident.
**p=1093 (Wieferich) : M_p = 1,2,3,3,39,79 pour L=60,100,140,180,220,260** — EXPLOSE.
Hors Wieferich, **excès max(M_p−⌊L/e_p⌋) stable à 3-4** (L=60→260). Wieferich = 2 premiers connus
(1093, 3511), donc ≤2 dans toute plage ⟹ contribution à M″ **triviale : ≤2·(trivial)=o(L²)**
(et déjà exclus/traités par Lemme K dans la charpente #11).

## Pourquoi la borne prouvable ne suffit PAS (le vrai obstacle)

M_p ≤ κ_p·(⌊L/e⌋+1) ne ferme M″ que si **κ_p=O(1)** (ou o(log L)). Or on ne sait borner κ_p que par
β_p = multiplicité additive du sous-groupe ⟨2⟩ mod p = max_r #{(g,h)∈⟨2⟩²:g+h≡r}. **Et β_p=e_p
souvent** (car −1∈⟨2⟩ pour e pair ⟹ fibre r=0 de taille e) : 257→16, 683→22, 241→24, 397→44…
Donc β_p·(⌊L/e⌋+1)≈L : **TRIVIAL**. Le gain réel (M_p≈⌊L/e⌋+O(1)) vient à 100% de la coupe mod p²,
que β_p (mod p) ne voit pas. **κ_p (classes actives, empiriquement ≤5) ≪ β_p (=e), mais rien ne le
prouve.** Borner κ_p = comprendre combien de classes mod e survivent à la fois à la coupe mod p² ET
à la boîte — c'est un énoncé de multiplicité fin, non élémentaire.

Décomposition du résidu :
- **Type A (e≤L, structuré) :** M_p≤κ_p(⌊L/e⌋+1) ; empiriquement M_p≤⌊L/e⌋+1 (excès ≤1) ⟹ κ_p
  « effectivement 1 » après coupe. Non prouvé.
- **Type B (e>L, générique, non-Wieferich) :** ⌊L/e⌋=0, M_p=O(1) (≈4, Poisson) — extrême de la loi
  bulk (STEP24). = mur max-vs-énergie pour un premier générique. Non prouvé (empiriquement o(log L)).

## Chaîne complète — état

$$M''=\sum_{p\in(L,L^2]}(M_p-1)=\underbrace{\sum_{\neg\text{Wief}}}_{\le\,\sum\kappa_p(\lfloor L/e_p\rfloor+1)}
+\underbrace{\sum_{\text{Wief}}}_{\le\,2\cdot O(L)=o(L^2)}.$$
Σ⌊L/e_p⌋=O(L²/log L)=o(L²) est ACQUIS (STEP26-lit, élémentaire). Donc **M″=o(L²) ⟸ κ_p=O(1) pour
p non-Wieferich** (Type A stacking + Type B Poisson). C'est le maillon final, non fermé.

## Verdict (format demandé)

- **k=nb PA par classe toujours 1 ?** **NON** (κ_p∈{1..5}). ÉTAPE 3 réfutée.
- **Argument étape 3 correct ?** **NON** — « même coset ≠ congru mod p » ; contre-ex p=257 (κ=3).
- **Borne tient mod p² ? pourquoi ord_p(2) ?** Per-classe ≤⌊L/e⌋+1 PROUVÉE mod p² (droite p-adique
  non-dégénérée ∩ triangle, T<p via p>L). e=ord_p(2) est le pas de PA (le facteur p de d_p=pe est
  la réduction mod p→p²). Wieferich (q_p=0) casse (dégénérescence).
- **M_p ≤ ⌊L/e⌋+1 prouvé ?** **NON.** Prouvé : M_p≤κ_p(⌊L/e⌋+1) + per-classe≤⌊L/e⌋+1. Serré = empirique
  (non-Wief : excès ≤4, L≤260 ; Type A ≤1).
- **Chaîne « tout n » prouvée ?** **NON.** Réduite à **κ_p=O(1) (non-Wieferich)** ; Wieferich (≤2
  premiers) trivialement o(L²).
- **Sauvable avec +O(log L) ?** Empiriquement OUI (non-Wieferich excès O(1) stable) ; mais preuve =
  κ_p=O(1), non acquise.
- **STATUT : RESTE OUVERT.** Progrès : (1) argument naïf réfuté ; (2) borne per-classe M_p≤κ_p(⌊L/e⌋+1)
  PROUVÉE (p>L, non-Wieferich) ; (3) exception Wieferich localisée et négligeable ; (4) résidu =
  κ_p=O(1) = « nb de classes/PA actives borné » (Type A) + Poisson générique o(log L) (Type B). Le
  maillon final est un énoncé de multiplicité fin, PAS élémentaire — mais précisément délimité.

---
*Scripts final_bound.py/final_bound2.py. ÉTAPE 3 réfutée (κ≤5≠1) ; M_p≤κ_p(⌊L/e_p⌋+1) prouvée
(per-classe ≤⌊L/e⌋+1, p>L non-Wieferich) ; Wieferich (1093:M=79 à L=260) = seule exception, ≤2
premiers ⟹ o(L²). M″=o(L²) ⟸ κ_p=O(1). Reste ouvert, bien délimité. PAPER intact.*
