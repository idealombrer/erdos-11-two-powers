# STEP26-lit — Σ 1/ord_p(2) sur (L,L²] : PAS besoin de la littérature. Borne ÉLÉMENTAIRE inconditionnelle o(L). M″ réduit au seul bound per-premier (STEP26).

**Date :** 2026-07-02. Script `sum_ord.py`. Objectif : la réduction M″ ⟸ Σ_{p∈(L,L²]} 1/ord_p(2)=o(L)
(STEP26) est-elle couverte par la littérature (Pappalardi/Kurlberg-Pomerance/Hooley/GRH) ?
**Réponse : question RÉGLÉE, et la littérature est INUTILE — la somme est élémentairement o(L),
sans GRH ni Artin. Ceci CORRIGE le pessimisme de STEP26 (« Θ(L²) »). Il ne reste QUE le bound
per-premier structurel M_p ≤ ⌊L/ord_p⌋+O(1) (STEP26).**

## Le résultat principal — borne ÉLÉMENTAIRE, INCONDITIONNELLE

**Lemme (élémentaire).** Pour tout k, les premiers p>L divisant 2^k−1 ont un produit ≤ 2^k−1<2^k.
Si m d'entre eux, alors L^m < 2^k, donc
$$\#\{p>L:\ p\mid 2^k-1\}\ <\ \frac{k\log 2}{\log L}.$$
(Vérifié numériquement : ratio cnt/borne ≤ 0.81 (L=50), 0.95 (L=100). VALIDE.)

**Corollaire (⋆).** Puisque ⌊L/d⌋=#{k≤L : d|k} et ord_p(2)|k ⟺ p|2^k−1 :
$$(\star)=\!\!\sum_{p\in(L,L^2]}\!\!\Big\lfloor\frac{L}{\mathrm{ord}_p(2)}\Big\rfloor
=\sum_{k\le L}\#\{p\in(L,L^2]:p\mid 2^k-1\}
<\sum_{k\le L}\frac{k\log2}{\log L}=\frac{\log2}{\log L}\cdot\frac{L(L+1)}2
=O\!\Big(\frac{L^2}{\log L}\Big)=o(L^2).$$

**Corollaire (somme réciproque).**
$$\sum_{p\in(L,L^2]}\frac1{\mathrm{ord}_p(2)}
=\underbrace{\sum_{\mathrm{ord}>L}}_{<\,\pi(L^2)/L=O(L/\log L)}
+\underbrace{\sum_{\mathrm{ord}\le L}}_{<\,\sum_{k\le L}(1/k)\cdot k\log2/\log L=O(L/\log L)}
=O\!\Big(\frac{L}{\log L}\Big)=o(L).$$

**Aucune hypothèse (GRH, Artin) n'est utilisée.** Le facteur log L gagné vient ENTIÈREMENT de la
contrainte p>L (bas de l'intervalle). C'est la correction de STEP26, qui bornait #{ord=d}≤d sans
utiliser p>L, d'où un faux Θ(L²).

## ÉTAPE 2 — croissance empirique (bien meilleure que la borne)

| L | #p | S=Σ1/ord | S/L | S/log L | (⋆)=Σ⌊L/ord⌋ | (⋆)/L² | (⋆)/(L²/logL) |
|---|---|---|---|---|---|---|---|
| 20 | 70 | 1.76 | .088 | .59 | 14 | .035 | .11 |
| 40 | 239 | 2.12 | .053 | .58 | 33 | .021 | .076 |
| 60 | 486 | 2.49 | .041 | .61 | 68 | .019 | .077 |
| 80 | 812 | 2.64 | .033 | .60 | 89 | .014 | .061 |
| 100 | 1204 | 2.83 | .028 | .62 | 130 | .013 | .060 |

- **S(L) ≈ 0,60·log L = Θ(log L)** (S/log L stable à 0,58-0,62). Bien plus petit que la borne
  O(L/log L). S/L → 0 net.
- Repères (L=100) : Σ1/ord=2,83 ; Σ1/p=0,68 (~log2, Mertens sur (L,L²]) ; Σ1/√p=23,6 (~L/log L).
  ⟹ Σ1/ord entre les deux, **échelle log L** : la partie ord~p donne O(1) (Σ1/p) ; les petits
  ordres ajoutent le Θ(log L).
- (⋆)/(L²/log L) ≈ 0,06 décroissant ⟹ (⋆)=O(L²/log L), constante ~0,06 (bien sous log2/2=0,35).

## ÉTAPE 4 — décomposition Type A (ord≤L) / Type B (ord>L)

| L | S_A (ord≤L) | S_B (ord>L) | S_B/L |
|---|---|---|---|
| 40 | 1.06 | 1.06 | .027 |
| 100 | 1.52 | 1.31 | .013 |

Les deux moitiés sont o(L). Type B (générique) trivialement (<π(L²)/L). Type A (petits ordres,
= premiers p|2^k−1) : ~1,5, croissance ~log L. Aucune ne menace o(L).

## ÉTAPE 1 — littérature (pour mémoire ; NON nécessaire)

- **Romanoff (1934)** : {p+2^k} de densité positive ; son argument repose sur la petitesse de
  sommes de réciproques d'ordres (second moment ∝ Σ 1/lcm(ord_p,ord_q)). Confirme l'ordre d'idées
  mais on n'en a pas besoin ici.
- **Artin/Hooley (1967, GRH)** : 2 est racine primitive (ord_p(2)=p−1) pour une proportion positive
  de p ⟹ pour eux 1/ord=1/(p−1), Σ~Σ1/p=O(1). Donnerait AUSSI o(L), mais conditionnel et superflu.
- **Pappalardi, Kurlberg–Pomerance, Murty–Séguin–Stewart** : étudient ord_p(2) en moyenne / la
  conjecture d'Artin quantitative. Pertinents pour l'asymptotique fine de Σ1/ord_p(2) (≈ log L ici),
  mais **la borne o(L) dont M″ a besoin est bien en-deçà et purement élémentaire**.

**Conclusion ÉTAPE 1 :** la réduction ne dépend d'AUCUN résultat difficile ; c'est un comptage de
diviseurs. La « question de littérature » n'existe pas.

## Impact sur M″ (l'essentiel)

M_p−1 ≤ ⌊L/ord_p⌋ + (M_p−1−⌊L/ord_p⌋). En sommant, avec le bound STEP26 M_p ≤ ⌊L/ord_p⌋+C :
$$M''=\!\!\sum_{p\in(L,L^2]}\!\!(M_p-1)\ \le\ (\star)+C\cdot\#\{p:M_p\ge2\}
\ \le\ O(L^2/\log L)+C\cdot\pi(L^2)=O(L^2/\log L)=o(L^2).$$
Le terme additif est absorbé : #{M_p≥2}≤π(L²)=O(L²/log L), et **il suffit même que l'excès
C=M_p−⌊L/ord_p⌋ soit o(log L)** (couvre un extrême de Poisson pour le Type B) pour garder o(L²).

**Donc : le maillon "somme d'ordres" est FERMÉ (inconditionnel, élémentaire). M″=o(L²) est
maintenant réduit au SEUL énoncé per-premier de STEP26 :**
$$\boxed{\ M_p\ \le\ \big\lfloor L/\mathrm{ord}_p(2)\big\rfloor + o(\log L)\quad(\forall p\in(L,L^2]).\ }$$

## Verdict (format demandé)

- **Croissance empirique de Σ1/ord_p(2) sur (L,L²) ?** **Θ(log L)** (≈0,60 log L), S/L→0.
- **Résultat dans la littérature ?** Contexte Romanoff/Pappalardi/Hooley existe, mais **NON requis** :
  la borne est un comptage de diviseurs élémentaire.
- **Sous GRH : o(L) prouvable ?** Oui trivialement (Hooley), mais **inutile**.
- **Inconditionnel : quelle borne ?** **Σ1/ord=O(L/log L), (⋆)=O(L²/log L). PROUVÉ, élémentaire.**
- **Décomposition Type A/B : Type B o(L) ?** Oui (<π(L²)/L). Type A aussi (~log L). Les deux o(L).
- **M″ prouvé si littérature couvre ?** La littérature n'est pas le maillon. **M″=o(L²) est
  INCONDITIONNELLEMENT réduit** au bound per-premier M_p≤⌊L/ord_p⌋+o(log L) (STEP26). Ce bound reste
  empirique (C≤4 stable, L≤160).
- **STATUT :**
  - **PROUVÉ (inconditionnel, élémentaire) :** (⋆)=Σ⌊L/ord_p⌋=O(L²/log L)=o(L²) ; Σ1/ord=o(L).
    Correction du Θ(L²) de STEP26.
  - **CONDITIONNEL (au bound per-premier STEP26) :** M″=o(L²).
  - **RESTE OUVERT (unique maillon) :** l'énoncé structurel M_p≤⌊L/ord_p⌋+o(log L) — la borne
    de multiplicité par l'ordre (involution + PA, STEP26). Plus « littérature d'ordres ».

---
*Script `sum_ord.py`. La somme d'ordres réciproques n'est PAS un obstacle : élémentairement o(L)
(comptage de diviseurs, p>L). M″=o(L²) réduit au SEUL bound per-premier de STEP26. PAPER intact.*
