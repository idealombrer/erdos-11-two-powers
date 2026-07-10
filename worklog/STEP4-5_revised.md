# Erdős #11 deux-puissances : le terme grand-premier, rigoureusement (révision)

**Date :** 2026-06-22. **Dossier :** `~/erdos-11-powers`. **Révise et CORRIGE** `STEP4-5_analysis.md`.

> **TL;DR.** En creusant le maillon « grands premiers », on trouve que l'argument de crible
> de la session précédente était **incomplet et contenait une erreur de réduction** (« $k$
> doit être un carré de premier » n'est vrai que pour $p>\sqrt{n/2}$). Le comptage
> **élémentaire ne ferme pas** ce terme : les deux bornes naturelles (union sur les premiers,
> $O(L\sqrt n)$ ; diviseurs par paire, $O(L^3/\log L)$) dépassent toutes deux le budget
> $L^2$. La donnée montre pourtant que le terme est *vraiment* petit ($\max_p M(p)\le3$,
> contribution nulle des $p>L^2$, décroissance en $Z$). La vérité requiert de la
> **compensation / équidistribution** de $2^l+2^m \bmod p^2$, pas du comptage pire-cas — un
> ingrédient d'analyse standard (somme d'exponentielles / grand crible), le **même** que
> celui derrière le résultat « presque tout $n$ » d'Erdős pour une puissance. La variante
> deux-puissances reste **plus facile que l'énoncé complet une-puissance** (découplée de
> Wieferich, et — point nouveau — **immunisée contre l'attaque par congruences couvrantes de
> Crocker** qui tue la variante *première*), mais elle n'est **pas élémentaire**. Plausibilité
> d'une preuve révisée ci-dessous.

---

## 1. Cadre et ce qui est solidement établi

$n$ impair grand, $L=\lfloor\log_2 n\rfloor$, paires $(l,m)$ avec $0\le l\le m$,
$2^l+2^m<n$, $k=n-2^l-2^m$ (impair, $\ge1$). Total $P(n)=\binom{L+1}{2}+\dots\sim L^2/2$.
Paire « mauvaise pour $p$ » : $p^2\mid k$, i.e. $2^l+2^m\equiv n\pmod{p^2}$.

**Faits rigoureux (inchangés, corrects) :**
- $k$ impair $\Rightarrow$ $p=2$ jamais en jeu ; somme sur $p\ge3$.
- **Petits premiers**, borne de périodicité : pour $p$ fixé, $\#\{\text{mauvaises}_p\}\le
  L^2/d_p+L$ où $d_p=\mathrm{ord}_{p^2}(2)$.
- **Constante pivot vérifiée** (`orders.py`) : $\displaystyle\sum_{p\ge3}\frac1{d_p}\approx
  0{,}3205<\tfrac12$ (dominée par $p=3,5,7$).

**Faits empiriques robustes (`largeprime.py`, pire $n$ par échelle, jusqu'à $2^{22}$) :**
- $\#\{\text{bonnes paires}\}/P(n)\approx \mathbf{0{,}65}$, **constante** sur toutes les
  échelles $\Rightarrow$ marge uniforme — c'est *ce qui permet « tout $n$ » et non
  seulement « presque tout »*.
- fraction non-squarefree totale $\approx0{,}33$–$0{,}37\approx\sum_p1/d_p$ : **le terme
  principal colle exactement**.

## 2. L'erreur de la session précédente

Affirmation fausse : « une mauvaise paire pour $p>z$ force $k=n-2^l-2^m$ à être un carré de
premier ». **Faux en général** : $p^2\mid k$ avec $k<n$ signifie $k\in\{p^2,2p^2,\dots,
\lfloor n/p^2\rfloor p^2\}$. Pour $z<p\le\sqrt{n/2}$ il y a **plusieurs** multiples de $p^2$
sous $n$ ; $k$ n'a aucune raison d'être $=p^2$. La réduction « carré » n'est valide que dans
le **haut** du spectre $p>\sqrt{n/2}$ (où $2p^2>n$, donc seul $k=p^2$ tient). Le vrai terme
grand-premier est donc
$$B_{>z}:=\#\{(l,m):\ \exists\,p>z,\ p^2\mid n-2^l-2^m\},$$
qui n'est **pas** réductible à un comptage de carrés.

## 3. Le comptage élémentaire échoue — deux bornes, deux échecs

**(i) Union sur les premiers.**
$B_{>z}\le\sum_{z<p\le\sqrt n}(L^2/d_p+L)=\underbrace{L^2\!\!\sum_{p>z}\tfrac1{d_p}}_{\to0\ (z\to\infty)}
+\;L\,(\pi(\sqrt n)-\pi(z)).$
Le second terme $\sim L\,\pi(\sqrt n)\sim L\sqrt n/\log\sqrt n\approx\sqrt n\cdot\frac{2}{\ln2}$
**dépasse massivement $L^2$** ($\sqrt n\gg(\log n)^2$). Le « $+L$ » par premier, sommé sur
$\sim\sqrt n$ premiers, tue la borne.

**(ii) Diviseurs carrés par paire.** Pour $k<n$, $\#\{p>z:p^2\mid k\}\le\frac{\ln n}{2\ln z}$,
d'où $B_{>z}\le\frac{L^2}{2}\cdot\frac{\ln n}{2\ln z}=O\!\big(L^3/\ln z\big)$ — **pire que
$L^2$** (et $\ln z<\ln\sqrt n\sim L$ donne au mieux $O(L^2)$ sans marge, jamais $o(L^2)$).

**Donc : aucune des deux bornes pire-cas élémentaires ne descend sous $L^2$.** Ce n'est pas
un défaut d'astuce ponctuel : les deux échouent parce qu'elles ignorent toute compensation.

## 4. La donnée montre que la vérité, elle, est $o(L^2)$ — mais par compensation

`largeprime2.py` (pire $n$ par échelle) :
- **$\max_p M(p)\le 3$** pour tout grand premier, à toutes les échelles ($M(p)=\#$paires avec
  $p^2\mid k$). La borne d'union autorisait $\sim L\approx21$ : elle est **fausse d'un facteur
  $L$**. La vraie valeur par premier est $O(1)$.
- **$p>L^2$ : contribution exactement nulle** (aucune paire), à toutes les échelles. Toute
  l'action non-squarefree vit dans $p\le L^2$, en pratique $p\le127$.
- $B_{>z}$ **décroît avec $z$** : $z=31\Rightarrow B\le0{,}011\,L^2$ ; $z=127\Rightarrow
  B\le0{,}004\,L^2$.

Lecture : $B_{>z}=o(L^2)$ pour $z=z(n)\to\infty$ lentement, mais cette petitesse vient de ce
que les $\sim L^2/2$ valeurs $2^l+2^m \bmod p^2$ **ne se concentrent pas** sur le résidu $n$.
C'est une **annulation**, invisible à toute borne pire-cas.

## 5. Le seul ingrédient manquant, énoncé précisément (et il suffit)

> **Lemme E (équidistribution).** Il existe $z(n)\to\infty$ (par ex. $z=\log n$) tel que,
> uniformément en $n$ impair,
> $$\sum_{z<p\le\sqrt n}\#\{(l,m):\ 2^l+2^m\equiv n\!\!\pmod{p^2}\}\ =\ o(L^2).$$

**Réduction (élémentaire) : Lemme E $\Rightarrow$ variante deux-puissances pour $n$ grand.**
Avec $z\to\infty$ : petits premiers $\le L^2\sum_{p\le z}1/d_p+L\,\pi(z)\le0{,}3205\,L^2+o(L^2)$ ;
grands premiers $=o(L^2)$ par E. Donc
$$\#\{\text{bonnes}\}\ \ge\ P(n)-0{,}3205\,L^2-o(L^2)\ \ge\ (0{,}5-0{,}3205)\,\tfrac{L^2}{1}-o(L^2)\ >\ 0$$
(en paires ordonnées $P\sim L^2$ ; le coussin $0{,}5-0{,}32=0{,}18>0$ est la marge uniforme).
Une paire squarefree existe $\Rightarrow n=k+2^l+2^m$. Les $n$ petits : vérifiés sans
exception jusqu'à $5\times10^7$ (`compute.py`). $\qquad\blacksquare$ *(conditionnel à E)*

**Le Lemme E n'est pas élémentaire mais est standard.** C'est une estimation de type **grand
crible / somme d'exponentielles** : écrire l'indicatrice de congruence via caractères additifs
mod $p^2$ et borner $\sum_{l\le L}e\!\big(a\,2^l/p^2\big)$. La suite $2^l\bmod p^2$ étant à
croissance lacunaire, ces sommes admettent des bornes non triviales (à la Erdős–Turán /
crible carré de Heath-Brown). **C'est exactement la machinerie derrière le « presque tout
$n$ » d'Erdős pour une puissance** : le Lemme E en est l'analogue 2-D. Le « bonus » de la
deuxième puissance n'est pas de rendre E *plus facile*, mais de fournir la **marge uniforme
$0{,}18\,L^2$** qui transforme « presque tout » en « tout ».

## 6. Pourquoi la variante squarefree est vraiment plus facile que ses voisines

Deux découplages, tous deux structurels :

1. **vs énoncé complet une-puissance (mur Wieferich).** Une-puissance : $\sim L$ candidats,
   terme grand-premier $\sim\sqrt n\gg L$ — pas de marge, un $n$ adverse peut voir *tous* ses
   candidats tués ; c'est là que Granville–Soundararajan greffent la condition
   $2^p\equiv2\pmod{p^2}$ (Wieferich). Deux-puissances : marge $0{,}18L^2>0$ uniforme, le
   Lemme E (sans Wieferich) suffit.
2. **vs variante PREMIÈRE deux-puissances (théorème NÉGATIF de Crocker).** Crocker (1971,
   *Pacific J. Math.* 36) prouve qu'il existe **une infinité** d'impairs **non** de la forme
   $p+2^a+2^b$, via un **système de congruences couvrantes** exploitant $2^a+2^b\equiv0
   \pmod{2^{2^s}+1}$ (nombres de Fermat) pour forcer $n-2^a-2^b$ dans une classe sans
   premier. **Cette attaque ne touche PAS la version squarefree** : être dans une classe
   fixée modulo un nombre de Fermat $F_s=2^{2^s}+1$ n'impose aucune non-squarefreeness (au
   contraire, $F_s$ est squarefree pour tous les $s$ connus, et la squarefreeness est une
   condition de densité $\approx0{,}6$, pas une condition de primalité éparse). **C'est la
   raison de fond pour laquelle la variante squarefree est conjecturée VRAIE pour tout $n$
   alors que la variante première est FAUSSE pour une infinité de $n$** — et pourquoi Erdős
   pouvait raisonnablement la croire « peut-être facile ».

## 7. Bibliographie (partie 5) — rien de publié sur la cible exacte

- **Hercher 2024** (arXiv:2411.01964) : version une-puissance, vérif. $2^{50}$, heuristique
  $6/\pi^2$. **Ne traite pas** la variante deux-puissances (confirmé par fetch).
- **Granville–Soundararajan 1998** : une-puissance ⟹ infinité de non-Wieferich. Lien de
  dureté, pas un outil ; **ne concerne pas** la variante deux-puissances.
- **Crocker 1971** (*Pacific J. Math.* 36, 103-107) ; **arXiv:0905.3809**, **arXiv:1610.01672**
  (« two squares + ≤2 powers of 2 ») : tous sur la variante **première** $p+2^a+2^b$, résultats
  **négatifs/positifs sur les premiers**, pas sur squarefree.
- **arXiv:2010.15580** (« every integer = square + squarefree ») : décomposition squarefree
  voisine en esprit, modulo différent.
- **Aucune trace** d'une preuve (ni d'un énoncé publié) de « tout impair $=$ squarefree $+2^l+2^m$ ».
  La croyance « perhaps easy » d'Erdős est restée non rédigée ; `11.lean` la tague
  `research open`. **Cible authentiquement ouverte et non revendiquée.**

## 8. Verdict révisé (honnête)

- **Le squelette de preuve est CORRECT et se réduit à un unique lemme analytique clairement
  énoncé (E)** ; la réduction E ⟹ résultat est élémentaire et la marge uniforme $0{,}18L^2$
  est solide (terme principal $\sum1/d_p\approx0{,}32<0{,}5$ vérifié).
- **MAIS ce n'est pas élémentaire** : le Lemme E exige une estimation d'équidistribution
  (somme d'exponentielles sur $2^l\bmod p^2$ / grand crible). La session précédente
  surestimait (« comptage élémentaire ferme le terme, section de crible standard ») — **erreur
  corrigée**.
- **Reste cependant le meilleur candidat de l'investigation**, et nettement : chemin de preuve
  identifié, lemme manquant *nommé et standard*, deux découplages structurels prouvés
  (Wieferich ; Crocker), pivot numérique vérifié, marge uniforme mesurée.

**Plausibilités révisées :**
- preuve **complète via analyse standard** (établir E par sommes d'exp. / grand crible, puis
  la réduction) : **~30-40 %** — vraisemblablement à la portée d'un analyste des nombres ;
  c'est, je pense, ce qu'Erdős appelait « peut-être facile » (facile *pour un expert outillé*).
- preuve **entièrement élémentaire** (sans équidistribution) : **~5 %** — l'annulation paraît
  réellement nécessaire ; aucune des bornes pire-cas ne descend sous $L^2$.
- **formalisation Lean** : prématurée — d'abord établir E sur papier (c'est là tout le
  travail), la réduction se formalisera ensuite sans peine.

**Prochaine étape concrète recommandée** : attaquer le **Lemme E** directement — borner
$\sum_{l\le L}e(a\,2^l/p^2)$ uniformément, puis sommer sur $p$. C'est un problème d'analyse
des nombres bien posé, autonome, et c'est *tout* ce qui manque.

---
*Sources : `compute.py`, `orders.py`, `largeprime.py`, `largeprime2.py` (tous dans ce dossier,
résultats `results_*.txt`) ; Crocker 1971 (Pacific J. Math. 36, via recherche web) ;
Hercher arXiv:2411.01964 ; Granville–Soundararajan 1998 ; recherche web (aucune preuve publiée
de la variante squarefree deux-puissances). Le squelette et le Lemme E sont une reconstruction
personnelle, à faire relire ; la réduction E ⟹ résultat est vérifiée à la main ci-dessus.*
