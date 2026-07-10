# Le pire-cas de la plage $(L,L^2]$ se DISSOUT : borne déterministe via $M_p$

**Date :** 2026-06-23. Suite de `STEP12` (où l'argument CRT pour le pire-cas a été réfuté, mais
le « presque tout $n$ » obtenu). **Avancée majeure : pour la plage de premiers $(L,L^2]$ — le
gros de R2 — le problème du pire-cas $n$ DISPARAÎT.** Il se réduit à une borne de
*multiplicité additive* $M_p$ **indépendante de $n$**, empiriquement $=o(L^2)$ une fois sommée.

## 1. L'idée : borner $N_p(n)$ par son max sur $n$

$M_p:=\max_n N_p(n)=\max_n\#\{(i,j):2^i+2^j\equiv n\ (p^2)\}$ = **multiplicité additive maximale**
de l'ensemble géométrique $A=\{2^l\bmod p^2:l\le L\}$. C'est une quantité **purement
arithmétique, sans $n$**. Pour TOUT $n$ :
$$R2\big|_{(L,L^2]}=\sum_{p\in(L,L^2]}N_p(n)\ \le\ \sum_{p\in(L,L^2]}M_p.$$
**Si $\sum_p M_p=o(L^2)$, alors la plage $(L,L^2]$ contribue $o(L^2)$ à R2 pour TOUT $n$,
déterministiquement — plus aucun problème de pire-cas.**

## 2. Donnée : $M_p$ borné, $\sum_p M_p=o(L^2)$ (jusqu'à $L=40$)

| $L$ | 16 | 20 | 24 | 28 | 32 | 36 | 40 |
|---|---|---|---|---|---|---|---|
| $\max_{p\in(L,L^2]}M_p$ (ordonné) | 6 | 6 | 6 | 6 | 6 | 8 | 8 |
| $\sum_{p\in(L,L^2]}M_p$ | 122 | 178 | 236 | 318 | 394 | 490 | 590 |
| $\sum_p M_p/L^2$ | 0.477 | 0.445 | 0.410 | 0.406 | 0.385 | **0.378** | **0.369** |

- **$\max_p M_p$ borné** (6, puis 8) — croissance ultra-lente ($O(1)$ ou au plus $O(\log L)$, et
  seulement pour de rares premiers non-Sidon).
- **$\sum_p M_p/L^2$ décroît comme $\sim1/\ln L$** (0.48→0.37) ⟹ $\sum_p M_p=O(L^2/\ln L)=o(L^2)$.
  Raison : la majorité des $p\in(L,L^2]$ sont **Sidon** mod $p^2$ ($M_p=2$, sommes $2^i+2^j$
  distinctes), donc $\sum_p M_p\approx 2\,\pi(L^2)=L^2/\ln L=o(L^2)$ ; les premiers non-Sidon
  (rares, près de $L$) ajoutent un excès $o(L^2)$.

**Donc, modulo le Lemme M ci-dessous, $R2|_{(L,L^2]}=o(L^2)$ pour tout $n$ — le pire-cas de la
plage dominante est dissous.**

## 3. Structure prouvable de $M_p$ (le levier quadratique)

> **Observation (racines quadratiques).** Si $2^i+2^j\equiv n\ (p^2)$, alors $x=2^i,y=2^j$ sont
> les deux racines de $T^2-nT+2^{i+j}\equiv0\ (p^2)$. Pour $p$ impair, ce trinôme a **$\le2$
> racines** mod $p^2$ (Hensel). Donc, à $s=i+j$ fixé, il y a **au plus une représentation
> non-ordonnée** $\{2^i,2^j\}$. D'où
> $$M_p^{\text{unord}}\ \le\ \#\{s\in[0,2L]:\ T^2-nT+2^s\ \text{a ses deux racines dans }\{2^l\bmod p^2\}\}.$$

C'est un vrai handle : $M_p$ compte des valeurs $s=i+j$ telles qu'un trinôme explicite a ses deux
racines *powers of 2*. Combiné au fait que les min-exposants des représentations sont distincts
(prouvé en `STEP6`), on a une voie élémentaire plausible vers **$M_p\le C$** (constante absolue,
$\le3$ non-ordonné empiriquement). C'est un énoncé de type **équation en S-unités mod $p^2$**
(« combien de fois $n$ s'écrit somme de deux puissances de 2 mod $p^2$ »).

## 4. Décomposition complète de R2 et ce qui reste (état le plus raffiné)

$R2=\sum_{p\in(L,\sqrt n]}N_p(n)$ se découpe en trois :

| Plage de $p$ | Contribution | Statut |
|---|---|---|
| **$(L,L^2]$** (le gros) | $\le\sum_p M_p=o(L^2)$ | **déterministe, pire-cas dissous** — modulo Lemme M ($M_p$ borné) |
| **$(\sqrt{n/2},\sqrt n]$** (très haut) | $\le2\#\{(i,j):n-2^i-2^j=\square\}=O(L)$ | **FAIT** (Kalinin Thm 4, carrés parfaits) |
| **$(L^2,\sqrt{n/2}]$** (moyen-haut) | $\#\{(i,j):n-2^i-2^j\ \text{a un facteur }p^2\in(L^4,n/2)\}$ | **LE MUR** (densité squarefree de la suite structurée) |

**Ce qu'il reste à prouver pour la preuve complète :**

- **(A) Lemme M :** $\displaystyle\sum_{p\in(L,L^2]}M_p=o(L^2)$ (ou $\max_p M_p=O(1)$). *Énoncé
  déterministe, sans $n$*, sur la multiplicité additive de $\{2^l\bmod p^2\}$. Empiriquement
  solide ($O(L^2/\ln L)$), structure quadratique disponible (§3). **Plausibilité élémentaire
  ~50-60 %** — c'est le morceau le plus prometteur jamais isolé, et il *supprime* le problème
  du pire-cas pour la plage dominante.
- **(B) Plage moyenne-haute :** $\#\{(i,j):n-2^i-2^j\ \text{divisible par }p^2,\ p\in(L^2,\sqrt{n/2}]\}=o(L^2)$
  pour tout $n$. *Le mur d'équidistribution irréductible*, mais désormais **confiné à
  $p\in(L^2,\sqrt{n/2}]$** (ni les petits, ni le très-haut). **Plausibilité élémentaire
  ~10-15 %, spécialiste ~40-50 %.**

## 5. Verdict honnête

**Progrès réel et net cette session :** le pire-cas $n$ — qui bloquait tout depuis plusieurs
sessions — **n'est plus un problème pour la plage dominante $(L,L^2]$** : il se dissout en une
borne de multiplicité $M_p$ *indépendante de $n$*, empiriquement $o(L^2)$, avec une structure
quadratique qui rend le Lemme M plausiblement élémentaire. Le très-haut est déjà fait (Kalinin).
**Le mur d'équidistribution est maintenant confiné à une seule plage : $p\in(L^2,\sqrt{n/2}]$.**

**Ce n'est pas encore une preuve complète**, mais la cartographie est désormais :
- petits premiers ($\le L$) : **FAIT** (Lemme K + R1, `STEP6`) ;
- $(L,L^2]$ : **réduit au Lemme M déterministe** (A), pire-cas dissous, ~50-60 % élémentaire ;
- $(\sqrt{n/2},\sqrt n]$ : **FAIT** (Kalinin) ;
- $(L^2,\sqrt{n/2}]$ : **le seul mur restant** (B), équidistribution, ~10-15 % élémentaire.

Deux maillons nommés, dont un (A) probablement élémentaire et qui élimine le pire-cas. C'est
l'état le plus avancé et le mieux cartographié de toute l'investigation.

---
*Scripts : $M_p=\max_n N_p(n)$ par convolution mod $p^2$ ; $\max_p M_p$ et $\sum_p M_p$ sur
$(L,L^2]$ jusqu'à $L=40$ (tasks `btdzw8yps`, `bz72k2k1y`). Observation quadratique : élémentaire
(Hensel). Améliore `STEP12` : le pire-cas de la plage dominante est dissous (déterministe), le
mur réduit à $(L^2,\sqrt{n/2}]$.*
