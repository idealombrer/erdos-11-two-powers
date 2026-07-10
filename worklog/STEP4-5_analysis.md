> ⚠️ **CE FICHIER CONTIENT UNE ERREUR — voir `STEP4-5_revised.md`.** La réduction « le terme
> grand-premier force $k$ à être un carré de premier » (§ « Grands premiers ») n'est valide
> que pour $p>\sqrt{n/2}$ ; en général $k$ doit seulement être *divisible* par $p^2$. Le
> comptage élémentaire ne ferme PAS ce terme (vérifié : `largeprime.py`/`largeprime2.py`). La
> petitesse réelle vient d'une **équidistribution** (Lemme E), pas d'un comptage de carrés.
> Conservé pour la trace historique du raisonnement.

# Erdős #11, variante deux-puissances : crible élémentaire & verdict (étapes 4-5)

**Date :** 2026-06-22. **Dossier :** `~/erdos-11-powers`. Suite de `STEP1-2_statement.md`.

## 4. Un argument de crible élémentaire pour la variante deux-puissances

**Verdict : OUI, il existe un argument de comptage élémentaire qui ferme la variante,
modulo un seul terme résiduel (sous-dominant) — et c'est exactement ce terme qui, pour la
version *une* puissance, explose et produit le couplage Wieferich.** Voici le squelette.

### Cadre
$n$ impair, grand, $L=\lfloor\log_2 n\rfloor$. Paires candidates : $(l,m)$, $0\le l\le m$,
$2^l+2^m<n$ ; nombre total $P(n)\sim L^2/2$ (ou $\sim L^2$ ordonnées). On veut **une** paire
avec $k=n-2^l-2^m$ squarefree. Remarque : $2^l+2^m$ pair $\Rightarrow k$ **impair**, donc
$p=2$ ne divise jamais $k$ — la somme sur les premiers démarre à $p=3$.

Paire « mauvaise » pour $p$ : $p^2\mid k$, i.e. $2^l+2^m\equiv n\pmod{p^2}$.

### Petits premiers ($p\le z$)
$2^m\bmod p^2$ est périodique de période $d_p=\mathrm{ord}_{p^2}(2)$. Pour chaque $l$
($\le L$ valeurs), $2^m\equiv n-2^l\pmod{p^2}$ fixe $m$ modulo $d_p$ (0 ou 1 solution par
période), soit $\le L/d_p+1$ valeurs de $m$. D'où
$$\#\{\text{mauvaises}_p\}\ \le\ \frac{L^2}{d_p}+L.$$
Somme sur $p\le z$ : $\displaystyle \le L^2\sum_{p\le z}\frac1{d_p} + L\,\pi(z).$

**Le pivot, calculé (`orders.py`) :**
$$\sum_{p\ge3}\frac1{\mathrm{ord}_{p^2}(2)}\ \approx\ \boxed{0{,}3205}\ <\ \tfrac12,$$
dominé par $p=3$ ($d_3=6\Rightarrow0{,}1667$), $p=5$ ($d_5=20\Rightarrow0{,}05$),
$p=7$ ($d_7=21\Rightarrow0{,}0476$) ; queue $\sum_{p\ge5000}\sim2\times10^{-5}$. Donc le
terme principal petit-premier est $\le 0{,}3205\,L^2 + L\pi(z) = 0{,}3205\,L^2+o(L^2)$ pour
$z$ fixe.

### Grands premiers ($p>z$) — le point décisif
Une mauvaise paire pour $p>z$ exige $p^2\mid k$ avec $k<n$ et $p^2>z^2$. Comme $k<n$, cela
force $k$ à être **un multiple de $p^2$ inférieur à $n$**, et pour $p$ proche de $\sqrt n$,
le seul candidat est $k=p^2$ lui-même. Autrement dit :
$$\#\{\text{mauvaises}_{p>z}\}\ \le\ \#\{(l,m):\ n-2^l-2^m=q^2\ \text{pour un premier }q>z\}
\ \le\ \#\{(l,m):\ n-2^l-2^m\ \text{est un carré}\}.$$
C'est une coïncidence **rare** : pour $l$ fixé, $n-2^l-2^m=\square$ est une équation
« puissance de 2 + carré = constante », dont les solutions sont éparses (au plus
$O(L\cdot\log n)$ au total, et heuristiquement $\sum 1/\sqrt{k}=o(L^2)$). **Ce terme est
sous-dominant devant $L^2$.**

### Bilan
$$\#\{\text{bonnes paires}\}\ \ge\ L^2-0{,}3205\,L^2-o(L^2)\ \approx\ 0{,}68\,L^2\ >\ 0.$$
**Une paire squarefree existe pour tout $n$ assez grand** (les petits $n$ se vérifient à la
main / par le calcul jusqu'à $5\times10^7$ : aucune exception). La fraction prédite
$\approx68\%$ colle à la fraction squarefree empirique du **pire cas** observée ($\sim60$–$62\%$,
écart = termes $+L$ et corrections grand-premier). ∎ *(modulo la mise au propre rigoureuse
du terme « rarement un carré ».)*

### Pourquoi le MÊME argument échoue pour une puissance
Candidats $\sim L$ (au lieu de $L^2$). Petits premiers : $\le L\sum1/d_p+\pi(z)\approx
0{,}32\,L+\pi(z)$. **Grands premiers** : le terme $\pi(\sqrt n)\sim\sqrt n/\log\sqrt n$
**dépasse $L$ = le nombre total de candidats**. Le crible ne peut pas le rendre négligeable
relativement à seulement $L$ candidats — et c'est précisément dans ce terme que vit la
rigidité « $2^a\equiv n\pmod{p^2}$ » exploitée par Granville–Soundararajan pour produire la
condition de Wieferich. **La version une-puissance est couplée à Wieferich exactement là où
la version deux-puissances respire.**

## 5. Verdict honnête

**La variante deux-puissances est RÉELLEMENT plus attaquable — ce n'est pas une impression
non vérifiée.** Trois faits concordants l'établissent :

1. **Quantitatif** : passage de $\sim L$ à $\sim L^2/2$ candidats $\Rightarrow$ le terme
   grand-premier (le tueur de la version une-puissance, $\sim\sqrt n$) devient
   **sous-dominant** ($o(L^2)$), car il faut désormais $n-2^l-2^m$ = carré exact, condition
   rare. Le problème se réduit alors à une inégalité de constante **vérifiée** :
   $\sum_p 1/\mathrm{ord}_{p^2}(2)\approx0{,}32<\tfrac12$.
2. **Découplage Wieferich** : l'argument ci-dessus n'invoque **aucun** ingrédient de type
   Wieferich/G–S — il est autonome. La version une-puissance, elle, voit son crible échouer
   exactement à l'endroit du couplage Wieferich. Donc la variante deux-puissances n'hérite
   **pas** du mur professionnel de l'énoncé principal. (Non vérifié formellement contre la
   construction exacte de G–S, mais l'autonomie de la preuve le rend très probable.)
3. **Empirique** : marge du pire cas **quadratique** en $\log n$ ($\ge400$ représentations
   au pire vers $5\times10^7$, $\sim60\%$ de toutes les paires), sans le moindre signe de
   rétrécissement, vs marge **linéaire** et cas tendus persistants ($r_1=2$) pour une
   puissance.

**Statut réel & ce qui reste à faire.** Le fichier Lean la liste `research open` et aucune
preuve publiée n'a été trouvée — « peut-être facile » est resté une *croyance* d'Erdős, pas
un théorème écrit. Le seul vrai travail restant est de **rendre rigoureux le terme
grand-premier** (« $n-2^l-2^m$ est rarement un carré de premier », uniformément en $n$) —
section de crible standard, pas un mur. C'est, **de loin, le candidat le plus attaquable de
toute l'investigation méta** : non pas un mur à 2-3 % comme #478/#11-complet/#23, mais une
cible avec un chemin de preuve identifié et un pivot numérique déjà vérifié.

**Plausibilité d'une preuve élémentaire complète : ~15-25 %** (le terme carré-de-premier
demande un vrai soin, et les « peut-être facile » d'Erdős ont parfois caché des
difficultés ; mais le squelette tient et le pivot $0{,}32<0{,}5$ est solide). **Comme cible
de formalisation Lean** : prématuré tant que la preuve papier du terme résiduel n'est pas
bouclée — d'abord finir l'argument, ensuite formaliser. **Recommandation : c'est ICI qu'il
faut creuser si on veut une vraie tentative de recherche à rendement non négligeable.**

---
*Sources : `compute.py` (crible squarefree numpy jusqu'à $5\times10^7$, 0 exception) ;
`orders.py` (ordres $\mathrm{ord}_{p^2}(2)$ via diviseurs de $p(p-1)$, somme $\approx0{,}3205$) ;
mécanisme Granville–Soundararajan via `11.lean` + `ANALYSIS_11.md`. L'argument de crible
ci-dessus est une reconstruction personnelle (cohérente avec « perhaps easy » d'Erdős), pas
une citation d'une preuve publiée — le terme grand-premier reste à formaliser.*
