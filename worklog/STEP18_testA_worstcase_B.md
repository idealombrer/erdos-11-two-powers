# STEP18 — TEST A : le pire-cas du mur B reste O(1) (ne grandit PAS avec L)

**Date :** 2026-06-24. Test A demandé : $\sup_n B(n)$ où
$B(n)=\#\{(l,m),0\le l\le m\le L;\ p\in(L^2,\sqrt{n/2}]\ \text{premier}:\ p^2\mid n-2^l-2^m\ge1\}$
(non-ordonné ; ×2 pour ordonné). Question : reste-t-il $o(L^2)$ ou explose-t-il ?

## Méthode
Crible inverse sur une fenêtre de $W=4\times10^6$ entiers en haut de chaque bloc dyadique
$[2^{kk},2^{kk+1})$ (donc $L=kk$ fixe) : pour chaque $p\in(L^2,\sqrt{n/2}]$ et chaque paire,
on marque les $n\equiv2^l+2^m\ (p^2)$. Max sur la fenêtre. Script `testA.py`.

## Résultat (lignes propres, L=22..26 ; L=21 écartée car fenêtre déborde sous $2^{21}$)

| $L$ | max $B$ (non-ord.) | argmax $n$ | #{n: B>0} / 4M | $L^2$ | max$B/L^2$ |
|---|---|---|---|---|---|
| 22 | **5** | 5972483 | 117396 | 484 | 0.0103 |
| 23 | **3** | 12816017 | 125915 | 529 | 0.0057 |
| 24 | **4** | 32303595 | 131922 | 576 | 0.0069 |
| 25 | **4** | 65537281 | 133644 | 625 | 0.0064 |
| 26 | **4** | 132964089 | 133061 | 676 | 0.0059 |

## Lecture
- **Le pire-cas de B est PLAT (~3–5 non-ordonné, soit ~6–10 ordonné) tandis que $L^2$ double
  (484→676).** Aucune croissance. $\max B/L^2\to0$ (0.010→0.006).
- Cohérent avec le premier-moment $O(1/\log L)$ (STEP17) : non seulement la moyenne mais le
  **pire-cas** de B semble $O(1)$, donc $o(L^2)$ très largement.
- La fraction de $n$ avec $B>0$ est stable (~3.3 % de la fenêtre), elle aussi sans explosion.

## Portée / réserves
- **Borne inférieure du vrai $\sup$** : fenêtre de 4M par bloc, pas le bloc entier ($2^{kk}$
  valeurs). Mais 4M est grand et le max est stable → signal fort.
- Non-ordonné (×2 pour la convention du papier). Sans incidence sur « $o(L^2)$ ».

## Conséquence
**Forte évidence empirique que B n'est PAS un vrai mur, même en pire-cas :** $\sup_n B(n)=O(1)$
observé. Si confirmé/prouvé, $R2|_{(L^2,\sqrt{n/2}]}=O(1)=o(L^2)$ pour TOUT $n$, et le seul
obstacle restant au « tout $n$ » deviendrait **(M″) seul** sur $(L,L^2]$. À prouver : une
borne déterministe sur le nombre de paires à facteur carré $>L^2$ simultané — du type
$\le$ (multiplicité additive) × (rareté des grands carrés), pas encore élémentaire mais
beaucoup plus modeste que l'équidistribution qu'on craignait.

---
*Script `testA.py`. Le pire-cas de B est plat (3–5) sur L=22→26 ; corrige l'idée que B serait
le mur dominant — en pire-cas il est $O(1)$, c'est (M″) le vrai dernier verrou.*
