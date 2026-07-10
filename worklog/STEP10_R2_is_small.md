# R2 est minuscule (O(L)) — coussin énorme, mais l'obstacle reste l'équidistribution

**Date :** 2026-06-23. Reprend l'attaque de R2 après la question « les 3-5 %, c'est sûr ? ».
**Nouvelle découverte importante : R2 réel est $O(L)$, pas $\Theta(L^2)$** — donc ce n'est PAS un
mur, le coussin est gigantesque. Mais chaque route élémentaire bute toujours sur la même
équidistribution. Verdict nuancé révisé.

## 1. Le vrai pire-cas de R2 (recherche directe, pas via les petits premiers)

En maximisant **R2 lui-même** sur des fenêtres de $n$ (jusqu'à $2^{23}$) :

| $L$ | 13 | 15 | 17 | 19 | 21 | 22 |
|---|---|---|---|---|---|---|
| max $R2$ | 7 | 9 | 9 | 9 | 11 | 10 |
| # premiers contributeurs | 5 | 7 | 6 | 8 | 8 | 5 |
| $\max_p N_p$ | 2 | 2 | 2 | 2 | 3 | 3 |
| $R2/L$ | 0.54 | 0.60 | 0.53 | 0.47 | 0.52 | 0.45 |

**$R2\approx L/2$, clairement $O(L)$** (et $R2/L^2\to0$). C'est exactement la prédiction
heuristique « aléatoire » : $R2\approx\#\text{paires}\times\Pr[\text{facteur carré moyen}]
\approx\tfrac{L^2}{2}\sum_{p>L}\tfrac1{p^2}\approx\tfrac{L^2}{2}\cdot\tfrac1L=\tfrac L2.$
**La conjecture deux-puissances a un coussin de facteur $\sim L$** (on a besoin de
$R2<0{,}68L^2$, la vérité est $\sim L/2$).

## 2. Structure fine (nouveau) : injectivité mod $p^2$ pour la majorité des premiers

Énergie additive $E_p=\#\{(i,j,i',j'):2^i+2^j\equiv2^{i'}+2^{j'}\ (p^2)\}$ :
- pour $p$ dans la **partie haute** de $(L,L^2]$ : $E_p=$ **diagonale** $=2(L+1)^2-(L+1)$
  exactement ⟹ les sommes $2^i+2^j$ sont **distinctes mod $p^2$** ⟹ **$N_p(n)\le1$** pour tout $n$ ;
- seuls les $p$ proches de $L$ (ex. $23,37$ pour $L=20$) ont des collisions ($E_p$ jusqu'à $1.4\times$),
  d'où $N_p$ pouvant monter (borne d'énergie $N_p\le\sqrt{E_p}\approx\sqrt2\,L$ pour $p\sim L$).

**Conséquence :** R2 est essentiellement $\#\{p\in(L,L^2]:\ p^2\mid n-2^i-2^j\text{ pour une paire}\}$,
chaque premier (haut) comptant pour $\le1$. C'est un **comptage de premiers** $p$ dont le carré
divise l'un des $\sim L^2/2$ entiers structurés $\{n-2^i-2^j\}$.

## 3. Pourquoi c'est petit mais dur à prouver : le coussin n'aide pas les bornes élémentaires

On a besoin de $R2<0{,}68L^2$ ; la vérité est $\sim L/2$ : **coussin de facteur $\sim L$**. Mais
toutes les bornes pire-cas élémentaires perdent *plus* que ce coussin :
- union sur premiers : $\sum_{p\in(L,L^2]}(L+1)/d_p\cdots$ + le « $+1$ par premier » $\times\pi(L^2)
  \Rightarrow O(L^3/\log L)$ ;
- par paire : $\sum_{(i,j)}\#\{p>L:p^2\mid k_{i,j}\}\le\frac{L^2}2\cdot\frac{L}{2\log L}=O(L^3/\log L)$ ;
- Cauchy–Schwarz / 2ᵉ moment $\big(\sum N_p\big)^2\le\pi(L^2)\sum N_p^2$ : perd encore (énergie
  des quadruples $\sim L^5$) $\Rightarrow O(L^{3.5})$ ;
- Möbius $\sum_d\mu(d)N_d$ : même queue grands-$d$.

**Toutes bottent à $\gtrsim L^3/\log L$, soit un facteur $\sim L^2/\log L$ au-dessus de la
vérité $L/2$** (et $\gtrsim L/\log L$ au-dessus de la cible $0{,}68L^2$). Le coussin $\sim L$ ne
suffit donc pas à sauver une borne pire-cas qui, elle, est lâche de $\sim L^2$. Il faut une
**équidistribution** (même faible) des $\{n-2^i-2^j\bmod p^2\}$ : montrer qu'ils ne se
concentrent pas anormalement sur les multiples de $p^2$ — exactement ce que le comptage pire-cas
ne voit pas.

## 4. Verdict honnête révisé (nuancé)

**Ce n'est pas un mur complet.** R2 est $O(L)$, la conjecture a un coussin énorme, et la
structure (injectivité mod $p^2$ pour la plupart des $p$) est propre. **Mais** après *six*
approches élémentaires distinctes (grand crible STEP8 ; télescopage + moyenne d'orbite STEP9 ;
concentration petits-ordres ; énergie/injectivité ; par-paire ; 2ᵉ moment), **toutes butent sur
le même besoin : une estimation d'équidistribution de $\{2^i+2^j\bmod p^2\}$** que le comptage
élémentaire ne fournit pas. J'ai épuisé mes idées élémentaires.

**Point positif vs `STEP9` :** l'input requis est **FAIBLE** (gagner un facteur $L/\log L$, pas
la compensation optimale $\sqrt L$ de Heilbronn). On est donc **loin sous la frontière de
Heilbronn** : une borne d'équidistribution *grossière* suffirait. C'est nettement plus accessible
qu'une borne de somme d'exponentielle optimale.

**Classification : (c), entre accessible et spécialiste**, penchant vers « accessible à un
analyste » :
- preuve **élémentaire par nous** : **~8-12 %** (coussin énorme + structure propre ; il faudrait
  un substitut élémentaire d'équidistribution — pas trouvé en 6 essais, mais pas exclu) ;
- preuve via une **équidistribution faible** (grand crible adapté au régime « peu de modules
  $p^2\in(L^2,L^4]$ », ou un 2ᵉ moment plus fin) : **~40-50 %** — cible faible, accessible à un
  analyste des nombres, possiblement à nous avec un vrai effort technique ciblé ;
- **résultat partiel conditionnel** (tout sauf R2) : **rigoureux, Lean-formalisable, publiable.**

## 5. Recommandation honnête

Le travail est en excellent état comme **résultat conditionnel** : « variante deux-puissances de
#11 vraie pour $n$ grand, dès que $\#\{(i,j):p^2\mid n-2^i-2^j,\ p\in(L,L^2]\}=o(L^2)$ »
— avec $R1$, Lemme K, périodes complètes, queue carré-parfait (via Kalinin) tous fermés
élémentairement, et l'énoncé résiduel réduit à une équidistribution FAIBLE et explicite. La
vérité ($R2\sim L/2$) confirme que l'hypothèse est largement vraie.

**Deux options réelles, honnêtes :**
1. **S'arrêter ici** côté preuve complète : on a un résultat partiel solide et bien isolé ; le
   pas restant est une équidistribution faible mais non élémentaire — je n'ai plus d'idée
   élémentaire neuve après six tentatives.
2. **Tenter un dernier angle technique précis** : un grand crible / 2ᵉ moment **adapté au régime
   spécifique** (modules $p^2$ confinés à $(L^2,L^4]$, suite très courte) — ce n'est pas
   « standard » (STEP8 l'a montré pour le grand crible naïf) mais le confinement des modules +
   le coussin faible pourraient permettre une variante ad hoc. C'est un projet technique borné
   (1-2 sessions), à tenter seulement si on accepte un risque d'échec élevé.

Ce n'est pas un mur ; c'est un **dernier maillon faible mais non élémentaire**, proprement isolé.

---
*Scripts : recherche directe du pire-cas R2 + détail (#premiers, $\max N_p$) jusqu'à $2^{23}$ ;
énergie additive $E_p$. Données : `bgein7kqm`, `bjaw95ee7` (tasks). Met à jour `STEP9` (verdict
adouci de (b) vers (c) grâce au coussin $O(L)$ et à l'injectivité, non vus en STEP9).*
