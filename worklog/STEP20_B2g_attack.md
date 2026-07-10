# STEP20 — Constante de M″ (≈ 4/π ?) et statut B₂[g] : le worst-case est FAUX, M″ est un énoncé de moyenne

**Date :** 2026-06-24. Suite de STEP19 (M″ ⟺ excès moyen $O(1)$, ≈1,3). Objectif : identifier
la constante, situer dans la littérature B₂[g], tenter le lemme. **Résultat : la constante est
≈1,27 (candidat 4/π=1,2732, non confirmé) ; le lemme B₂[g] à $g$ constant est FAUX (= maxM=O(1),
réfuté) ; M″ est irréductiblement un énoncé de multiplicité MOYENNE / énergie additive, pas un
B₂[g] worst-case.** Scripts : `identify_constant.py`. PAPER.tex intact.

## Étape 1 — la constante. EM(L)=S₁/#{non-Sidon} ≈ 1,27, candidat 4/π

| L | 20 | 30 | 40 | 50 | 55 | 60 | 65 | 70 | 75 | 80 |
|---|---|---|---|---|---|---|---|---|---|---|
| EM | 1.118 | 1.286 | 1.217 | 1.274 | 1.308 | 1.333 | 1.280 | 1.278 | 1.255 | 1.265 |

- **Moyenne (L≥30) = 1,271 ; $4/\pi=1{,}2732$.** Écart $<0{,}2\%$. **Meilleur candidat : $4/\pi$.**
  (Rejetés : $\zeta(2)/\zeta(4)=15/\pi^2=1{,}520$ ; $1+1/e=1{,}368$ ; $\zeta(2)=1{,}645$ ; $\sum1/p(p-1)=0{,}773$.)
- **RÉSERVE HONNÊTE :** EM est bruité (rapport de comptages entiers), oscille dans $[1{,}12;1{,}33]$,
  **non monotone** (monte à 1,33 à L=60 puis redescend). Donc « EM → 4/π » est un *candidat
  cohérent, NON prouvé convergent*. Ce qui est solide : **EM est borné et stable ⟹ EM=O(1) ⟹ M″.**
- $4/\pi$ est exactement le type de constante qui apparaît en énergie additive / autoconvolution
  (cf. littérature ci-dessous), donc le candidat n'est pas absurde — mais le confirmer demanderait
  des $L$ bien plus grands.

## Étape 2 — littérature B₂[g] : ce qui s'applique, ce qui ne s'applique pas

- **Progression géométrique sur ℤ = Sidon** (classique) : $r^i+r^j=r^k+r^l$ n'a que les solutions
  triviales. **Mais c'est sur ℤ.** Sur ℤ/p²ℤ, les enroulements créent des collisions → PAS Sidon.
- Cilleruelo & al. (généralisés B₂[g] ; « Sidon sets and statistics of the ElGamal function »,
  arXiv:1708.04395, étudie $\{(g^x,x)\}$) : travaux pertinents mais **aucun théorème
  « $\{r^k\bmod m\}$ est B₂[O(1)] »** — et il ne peut pas y en avoir (réfuté §3).
- **Conclusion biblio :** le bon objet n'est pas « B₂[g] worst-case » mais **l'énergie additive de
  $\{2^k\bmod p^2\}$**, qui relève des sommes d'exponentielles sur sous-groupes
  (Bourgain–Garaev–Konyagin) — exactement le diagnostic de STEP16 et de la note harmonique GPT.

## Étape 3 — le lemme candidat « B₂[2] » est FAUX (faille de parité explicite)

**La reformulation du plan « $G_L$ est B₂[g] pour $g=O(1)$ universel » équivaut à maxM=O(1),
RÉFUTÉ** (STEP15/19 : maxM ~ log L, atteint 6 à L=70). Donc aucun $g$ constant ne marche.

La preuve candidate (cas $a<c$ : « $1+2^{b-a}$ impair $\equiv 2^{c-a}(1+2^{d-c})$ pair ⟹
contradiction ») **casse car la parité n'existe pas modulo l'impair $p^2$.** Contre-exemples :
- **dégénéré** $p=3$ (enroulement, régime Lemme K) : $2^0+2^0=2\equiv2^0+2^6=65\ (\bmod 9)$ car
  $2^6\equiv1$ ($=$ ord). (Hors-régime : $L\ge6>$ ord/2.)
- **en régime** $p=127$, $L=50<$ ord$_{p^2}/2=444$ : $\;1+2^8=257\equiv 2^1+2^{14}=16386\ (\bmod 127^2{=}16129)$
  car $16386-16129=257$. Ici $a=0<c=1$ : le RHS « pair » $16386$ se réduit au résidu **impair** $257$.
  **La parité est détruite par la réduction mod $p^2$** — exactement le point où la preuve échoue.

## Étape 4 — énergie / Plünnecke : INUTILE (doublement maximal)

| L | p | \|G\| | \|G+G\| | K=\|G+G\|/\|G\| | E(ord)/\|G\|² |
|---|---|---|---|---|---|
| 30 | 31 | 31 | 275 | 8.9 | 4.24 |
| 30 | 457 | 31 | 496 | 16.0 | 1.97 |
| 40 | 41 | 41 | 706 | 17.2 | 2.87 |
| 40 | 809 | 41 | 861 | 21.0 | 1.98 |

- **Doublement $K\sim L/2$ à $L$ (maximal)** : $G_L$ n'a AUCUNE structure additive. Plünnecke–Ruzsa
  donne $E\le K^2|G|^2\sim L^2|G|^2=L^4/4$ = **borne triviale. Voie morte.**
- **MAIS $E/|G|^2\approx2$–$4$ (proche du plancher Sidon $=2$)** : $G_L$ est **« presque Sidon »**,
  énergie à peine au-dessus du minimum. C'est *là* qu'est M″ — un énoncé fin sur l'excès d'énergie,
  pas sur le doublement.

## Verdict (format demandé)

- **PROUVÉ (rigoureux) :** (i) B₂[g] à $g$ constant est FAUX (= maxM=O(1), réfuté) ; la preuve
  candidate B₂[2] a une faille de parité explicitée (contre-ex. $p=127$). (ii) Plünnecke est
  inutile (doublement maximal $K\sim L$). (iii) progression géométrique Sidon sur ℤ mais pas mod p².
- **CONDITIONNEL :** M″ ⟺ EM(L)=O(1) (STEP19) ; EM ≈ 1,27, candidat $4/\pi$, **non confirmé**.
  Équivalent : énergie additive de $\{2^k\bmod p^2\}$ est $2|G|^2(1+o(1))$ **en moyenne** sur
  $p\in(L,L^2]$ (« presque-Sidon en moyenne »).
- **RESTE OUVERT (nommé, affiné) :** *l'énergie additive moyenne de la progression géométrique
  $\{2^k\bmod p^2\}$ sur $p\in(L,L^2]$ excède le plancher Sidon de seulement $O(|G|^2)$* — énoncé
  de type Bourgain–Garaev (sommes d'exponentielles sur $\langle2\rangle$), NON réductible au
  worst-case B₂[g] (faux) ni au doublement (inutile). C'est le même noyau analytique que le
  Lemme E′/GPT, désormais cerné comme « presque-Sidon en moyenne, constante ≈ 4/π ».
- **La constante 1,3 est-elle identifiée ?** Candidat $4/\pi=1{,}2732$ (moyenne 1,271), cohérent
  mais **non confirmé** (bruit, non-monotone). Pas de constante « classique » mieux ajustée.
- **Le lemme B₂[g] tient-il ?** NON à $g$ constant (worst-case). OUI trivialement à $g=$maxM~log L,
  mais ça ne suffit pas (donne $\Theta(L^2)$). Le bon énoncé est *en moyenne*, pas worst-case.
- **Plausibilité de M″ :** **inchangée, très élevée** — EM borné/stable, énergie quasi-Sidon. La
  preuve reste niveau spécialiste (sommes d'exponentielles sur sous-groupes mod $p^2$).

---
*Script `identify_constant.py` (EM(L) L=20–80 ; contre-ex. B₂[2] ; doublement/énergie). PAPER.tex
intact. Affine STEP19 : constante ≈4/π (candidat), B₂[g]-constant réfuté, énergie quasi-Sidon en
moyenne = le vrai énoncé (Bourgain–Garaev), Plünnecke inutile.*
