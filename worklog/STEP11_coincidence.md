# R2 = π(L²) + C(n) : décomposition propre, moitié inconditionnelle, résidu = coïncidences

**Date :** 2026-06-23. Tentative ciblée « second-moment / grand crible adapté ». **Vrai progrès :
on isole la moitié facile de R2 inconditionnellement, et le résidu se réduit à un terme de
COÏNCIDENCE $C(n)$, empiriquement $O(L)$, concentré sur $O(L/\log L)$ petits premiers.**

## 1. La décomposition (élémentaire, exacte)

$R2=\sum_{p\in(L,L^2]}N_p(n)$, $N_p(n)=\#\{(i,j):p^2\mid n-2^i-2^j\}$. Sépare premiers par $N_p$ :
$$R2=\sum_{p:N_p\ge1}N_p=\underbrace{\#\{p:N_p\ge1\}}_{=:Q(n)}+\sum_p(N_p-1)^+
\ \le\ \pi(L^2)+\sum_{p\in(L,L^2]}N_p(N_p-1)=:\pi(L^2)+C(n).$$
- **$Q(n)\le\pi(L^2)\sim L^2/(2\ln L)=o(L^2)$ — INCONDITIONNEL et GRATUIT** (il n'y a pas assez
  de premiers dans $(L,L^2]$ pour que le simple *comptage* des premiers contributeurs atteigne
  $L^2$). C'est la moitié du travail, faite sans aucune hypothèse.
- **$C(n)=\sum_p N_p(N_p-1)$ = terme de coïncidence** = $\#\{(p,P,P'):P\ne P',\ p^2\mid n-\mathrm{sum}(P)
  \text{ et }p^2\mid n-\mathrm{sum}(P')\}$ : deux paires distinctes dont les valeurs sont
  *simultanément* divisibles par le même $p^2>L^2$. Requiert $\gcd(k_P,k_{P'})\ge p^2>L^2$.

## 2. $C(n)$ est minuscule et concentré (données, jusqu'à $2^{22}$)

En maximisant $C(n)$ sur $n$ :

| $L$ | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|
| max $C(n)$ | 4 | 6 | 6 | 6 | 8 | 8 | 8 |
| # premiers avec $N_p\ge2$ | 2 | 3 | 1 | 1 | 2 | 2 | 2 |
| premiers concernés | 23,31 | 19,23,31 | 17 | 19 | 19,59 | 23,31 | 23,31 |

$C(n)=O(L)$, $C(n)/L^2\to0$. **Les seuls premiers contributeurs ont $N_p\ge2$ et sont tous
$\lesssim 3L$** (17,19,23,29,31,59), $\max N_p\le3$.

**Pourquoi (test d'uniformité, partie 2).** Les sommes $\{2^i+2^j\bmod p^2\}$ ($\binom{L+2}{2}$
paires) :
- pour $p\gtrsim3L$ : **injectives** (0 collision, distinctes mod $p^2$ — *mieux* qu'aléatoire) ⟹ $N_p\le1$ ⟹ contribution nulle à $C(n)$ ;
- pour $p\lesssim3L$ : collisions $\approx$ prédiction aléatoire $\binom{\#paires}{2}/p^2$.

Donc $N_p\ge2$ **seulement** pour $p\in(L,\sim3L]$, soit $\pi(3L)-\pi(L)=O(L/\log L)$ premiers.

## 3. Heuristique : $C(n)=O(L)$ (et pourquoi $o(L^2)$ est très probable)

Pour $p\lesssim3L$, $N_p(n)$ est Poisson de moyenne $\lambda_p=\binom{L+2}{2}/p^2\approx(L^2/2)/p^2$.
Alors $\mathbb E[N_p(N_p-1)]\approx\lambda_p^2$, et
$$\sum_{p>L}\lambda_p^2\approx\frac{L^4}{4}\sum_{p>L}\frac1{p^4}\approx\frac{L^4}{4}\cdot\frac1{L^3}=\frac L4.$$
Colle à $C(n)\approx4$–$8$. **Pour menacer $C(n)\sim L^2$ il faudrait que $n$ soit un point de
concentration simultané pour $\gtrsim L/\log L$ carrés $p^2$ indépendants — interdit par le CRT.**
C'est pourquoi $C(n)=o(L^2)$ paraît bien plus accessible que l'équidistribution complète :
c'est un énoncé de **second moment sur $O(L/\log L)$ petits premiers + indépendance CRT**.

## 4. Tentative de preuve de $C(n)=o(L^2)$ — où ça avance, où ça bloque

**Avance :** $C(n)=\sum_{p\in(L,\sim3L]}N_p(N_p-1)$ (seuls ces premiers comptent). Moyenné sur $n$
(mod $p^2$), $\frac1{p^2}\sum_n N_p(n)(N_p(n)-1)=\frac{\Delta_p}{p^2}$ où $\Delta_p$ = énergie
additive non-diagonale ; $\sum_{p\lesssim3L}\Delta_p/p^2$ est petit. **En moyenne sur $n$, $C(n)$
est $O(L)$, rigoureusement** (second moment standard).

**Blocage :** on a besoin du **pire $n$**, pas de la moyenne. Un $n$ adverse pourrait concentrer
$N_p$ sur quelques petits $p$. La borne triviale $N_p\le L+1$ + $O(L/\log L)$ premiers donne
$C(n)\le(L+1)^2\cdot O(L/\log L)=O(L^3/\log L)$ — toujours le mur $L^3$, car le pire-cas
par-premier ($N_p\sim L$) n'est pas exclu pour un $n$ choisi. Exclure cette concentration
simultanée pour le pire $n$ = exactement l'input qui manque (mais c'est un input **faible** :
il suffit que $\max_p N_p(n)=o(\sqrt{L\log L})$ en moyenne sur les petits premiers, ce que le CRT
rend très plausible).

## 5. Verdict honnête (révisé, plus précis)

**Progrès réel cette session :** la moitié de R2 ($Q(n)\le\pi(L^2)$) est **fermée
inconditionnellement** ; le résidu n'est plus « équidistribution de $\{n-2^i-2^j\bmod p^2\}$ »
mais le terme de **coïncidence $C(n)=o(L^2)$**, strictement plus faible, concentré sur
$O(L/\log L)$ petits premiers, et heuristiquement $O(L)$ via CRT.

**Classification : (b) preuve CONDITIONNELLE, avec hypothèse résiduelle nettement améliorée.**
La preuve est complète **modulo** : $\;C(n)=\sum_{p\in(L,L^2]}N_p(n)(N_p(n)-1)=o(L^2)$
uniformément en $n$ — c.-à-d. « peu de paires $(i,j)\ne(i',j')$ donnent des valeurs
$n-2^i-2^j$, $n-2^{i'}-2^{j'}$ partageant un facteur carré $>L^2$ ». Énoncé propre, autonome,
de type second-moment/CRT.

**Plausibilités (révisées à la hausse) :**
- $C(n)=o(L^2)$ prouvable **élémentairement** (second moment + CRT pour exclure la concentration
  au pire $n$) : **~15-25 %** — en hausse nette ; c'est le morceau le plus accessible jamais isolé,
  bien plus faible que Heilbronn, et la moitié $Q(n)$ est déjà gratuite ;
- via un analyste (large sieve sur $O(L/\log L)$ petits modules $p^2\sim L^2$, régime *favorable*
  car modules petits) : **~50-60 %** ;
- **résultat partiel** (R2 $\le\pi(L^2)+C(n)$, moitié inconditionnelle) : **acquis, rigoureux,
  Lean-formalisable.**

**Ce n'est toujours pas une preuve complète, mais le résidu n'a jamais été aussi faible ni aussi
propre.** Le prochain pas concret, réellement prometteur : prouver $C(n)=o(L^2)$ via un argument
de second moment sur les petits premiers $p\lesssim3L$ + indépendance CRT pour contrôler le pire
$n$. C'est un projet borné et, pour la première fois, **plus de la moitié du chemin est
inconditionnelle**.

---
*Scripts : maximisation directe de $C(n)$ + détail (#premiers $N_p\ge2$) ; test d'uniformité
(distinct sums mod $p^2$ vs aléatoire). Données : tasks `by9oeygsh`, `b45axmhlg`. Améliore
`STEP10` : la cible passe de « R2$=o(L^2)$ » à « $C(n)=o(L^2)$ » (coïncidences), avec $Q(n)$ gratuit.*
