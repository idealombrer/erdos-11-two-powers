# STEP17 — Liens #9 / #16, l'approche harmonique de GPT, et un GAIN : « presque tout n » s'étend au mur B

**Date :** 2026-06-24. Lecture intégrale de Chen (arXiv:2312.04120v3 = problème #16),
du PDF harmonique de GPT, et de Pan (arXiv:0905.3809 = #9). Réponse aux PHASES 1 et 2.
**Résultat net :** les outils de #9/#16 ne transfèrent pas (raison structurelle DURE,
pas seulement « plus difficile ») ; MAIS l'analyse révèle que le mur B
n'est un mur que pour le *pire* n — son **premier moment est petit**, ce qui
**étend le théorème « presque tout n » à TOUT le problème** (gain réel, corrige PAPER §6).

## 0. Corrections factuelles au cadrage (et à la tentative précédente)

- **#16 N'EST PAS la variante deux-puissances.** #16 (Chen 2023/24) porte sur **une seule
  puissance** : $U=\{$impairs $\ne p+2^k\}$ ; Conjecture A d'Erdős = « $U$ = une seule
  progression arithmétique + densité nulle » ; **Chen la réfute** (Thm 1.1 : $U$ n'est pas
  union finie d'AP + densité nulle). Le cousin *deux-puissances* $p+2^a+2^b$, c'est **#9**
  (Crocker, Pan).
- **L'outil partagé de #16, #9, Crocker, Pan, Chen est le RECOUVREMENT (covering
  congruences) mod $p$ — degré 1**, PAS un crible. La tentative précédente disait « Pan
  utilise un crible combinatoire type Brun–Titchmarsh » : **FAUX**. Pan (vérifié,
  arXiv:0905.3809) construit un *système de recouvrement mod $p$* forçant
  $p\mid n-2^a-2^b$ pour une famille de premiers couvrant tous les exposants via $r_p=
  \mathrm{ord}_p(2)$. Le seul crible/second-moment chez Chen est Cauchy–Schwarz +
  Romanoff ($\sum r(n)^2\ll x$), utilisé pour la *densité positive de représentables*,
  jamais pour fabriquer une obstruction.
- Le mécanisme exact (Chen §3, repris d'Erdős 1950) : le recouvrement de $\mathbb Z$ par
  $\{0\bmod2,1\bmod4,3\bmod8,1\bmod3,3\bmod12,23\bmod24\}$ tuile les exposants $k$, ce qui
  via $r_p$ envoie $2^k$ dans des classes mod $\{3,5,17,7,13,241\}$ (ordres
  $2,4,8,3,12,24$, tous $2^a3^b$), d'où une AP de module $11184810=2\cdot3\cdot5\cdot7\cdot13
  \cdot17\cdot241$ entièrement non-représentable. La réfutation de Conj. A suit de
  $\gcd(11184810,3292241-992077)=2$. (La tentative précédente avait ce mécanisme **correct**.)
- **Correction bibliographique pour PAPER.tex** : Crocker [8] = « *On the sum of a prime
  and two powers of two* », Pacific J. Math. **36** (1971), 103–107 (titre exact, via la
  bibliographie de Chen ; j'avais mis un titre approximatif « UNCERTAIN »).

## 1. PHASE 1 — Les outils de #16 transfèrent-ils à B ou M″ ? NON (raison dure)

Les outils de #16 sont : (a) systèmes de recouvrement mod $p$ via $r_p$ ; (b) CRT ;
(c) Cauchy–Schwarz/Romanoff pour la densité. Transfert :

- **(a)+(b) recouvrement → degré 1 seulement.** Le recouvrement produit la
  **divisibilité** $p\mid n-2^a-2^b$, qui tue la **primalité** (un nombre $>p$ divisible
  par $p$ n'est pas premier). Notre obstruction est **$p^2\mid k$** (degré 2). Or
  $p\mid k$ est *inoffensif* pour le squarefree (densité $\sim1/p$, et un squarefree peut
  parfaitement être divisible par $p$). Pour menacer le squarefree il faudrait **recouvrir
  avec des $p^2$** — et c'est **IMPOSSIBLE** :
  $$\sum_{p\ge3}\frac1{p^2}=0{,}20225\ldots<1$$
  (calculé, `checkB.py`). Un système de recouvrement exige $\sum1/m_i\ge1$ ; avec des
  modules $p^2$ ($p$ impair) on plafonne à $0{,}20$ (même en incluant *tous* les carrés de
  premiers : $P(2)-1/4\approx0{,}45<1$). **Donc l'outil central de #9/#16/Crocker/Chen ne
  peut pas, même en principe, fabriquer d'exception squarefree.** C'est la version
  quantitative dure du « découplage de Crocker » de PAPER §1.4. *Bonne nouvelle pour la
  conjecture* : la machine qui rend les ensembles exceptionnels de #9/#16 gros est
  indisponible côté squarefree.
- **(c) Cauchy–Schwarz/Romanoff** est le SEUL outil de #16 conceptuellement transférable —
  et c'est **exactement** notre machine « presque tout $n$ » (STEP12 : $\overline C=o(L^2)$
  + Markov). Donc #16 ne nous apporte rien de neuf ici : on l'a déjà.

**Conclusion PHASE 1 :** aucun outil de #16 ne ferme B ou M″. Le recouvrement est
*structurellement degré 1* (impossible à $p^2$, $\sum1/p^2<1$) ; le second-moment est
déjà chez nous (presque-tout). (Confirme la conclusion de la tentative précédente, en
corrigeant : Pan = recouvrement, pas crible ; et en donnant la raison DURE $\sum1/p^2<1$.)

## 2. PHASE 2 — #9 mod $p$ vs notre mur B mod $p^2$ ; synergie Lemme K + harmonique sur B

### 2a. Les techniques de #9 (recouvrement) se généralisent-elles à mod $p^2$ ?
**NON, et pas « à coût élevé » : à coût INFINI** (impossible). Même raison qu'en §1 :
recouvrir $\mathbb Z$ par des congruences mod $p^2$ demande $\sum1/p^2\ge1$, faux
($0{,}20$). Pintz/Pan/Crocker ne donnent que des **minorations de l'ensemble exceptionnel**
(construction de beaucoup de $n$ non-représentables) — toutes par recouvrement, donc
toutes mortes à degré 2. Ils n'offrent aucun outil de *majoration* de la représentabilité
(le sens dont on a besoin). Le seul outil de majoration-par-le-bas de la littérature
Romanoff (Chen–Sun, Elsholtz–Schlage-Puchta, Pintz « Romanoff constant ») est le
second-moment — encore une fois = notre « presque tout $n$ ».

### 2b. Synergie Lemme K + harmonique (GPT §11.2) restreinte à B : change-t-elle la difficulté ?
**NON — sur B c'est strictement plus dur, et le Lemme K y est INERTE.** Le Lemme K exige
une **période complète** : $d_p=\mathrm{ord}_{p^2}(2)\le L+1$, donc (non-Wieferich)
$p\le L+1$. Pour $p\in(L^2,\sqrt{n/2}]$, $d_p$ est typiquement $\sim p\gg L$ : **aucune
période complète**, le Lemme K ne s'applique jamais (régime R2, $Q_p=0$). L'approche
harmonique de GPT y demande exactement $|S_p(t)|=|\sum_{a\le L}e_{p^2}(t2^a)|=o(L)$ pour
une **somme lacunaire INCOMPLÈTE** de longueur $L+1$ modulo $p^2$ avec $p$ énorme — le
régime Bourgain/Garaev/Konyagin, le plus dur. Donc « attaque globale GPT » et « attaque
B-seule » **coïncident sur B** : B *est* le résidu de difficulté précisément parce que le
Lemme K en est absent. Le Lemme K n'a jamais acheté que $p\le L+1$ (déjà fermé). La
synergie est réelle, mais seulement là où elle marchait déjà.

**Le PDF de GPT** (lu) ne fait que reformuler tout ceci en langage harmonique
($T_p(n)=p^{-2}\sum_t e_{p^2}(-tn)S_p(t)^2$, objectif $|S_p(t)|\ll p^{1-\delta}$) et conclut
honnêtement « hors de portée des techniques standards » à cause du manque de cancellation
uniforme dans $S_p(t)$. **Aucune fermeture nouvelle.** Il ne mentionne ni le Lemme K, ni la
dissolution pire-cas (Lemme M), ni le découpage par plages — il attaque $S_p(t)$
globalement, donc bute plein-pot sur la borne lacunaire incomplète. Notre travail est
strictement en avance (Lemme K tue les périodes complètes ; Kalinin tue le très-haut ;
reste B + M″).

## 3. GAIN RÉEL de cette session : « presque tout $n$ » s'étend à B (donc à TOUT le problème)

L'analyse de B sous l'angle « premier moment » (motivée par §2a : pas d'obstruction
possible, donc B doit être petit) donne un **théorème inconditionnel élémentaire** que
PAPER §6 ratait (j'y avais écrit, à tort, « pas même de version en moyenne pour B »).

**Comptage direct (rigoureux, élémentaire).** Pour $n\in[N,2N]$ ($N=2^L$),
$$\#\{n\in[N,2N]:\ \textstyle\sum_{p\in(L^2,\sqrt{n/2}]}N_p(n)\ge1\}
\le\sum_{(l,m)}\sum_{p>L^2}\#\{n\in[N,2N]:\ n\equiv2^l+2^m\!\!\pmod{p^2}\}.$$
Chaque classe mod $p^2$ a $\le N/p^2+1$ éléments dans $[N,2N]$, d'où
$$\le(L+1)^2\Big(N\sum_{p>L^2}\tfrac1{p^2}+\pi(\sqrt{N/2})\Big)
=(L+1)^2\Big(N\cdot O\big(\tfrac1{L^2\log L}\big)+O(\tfrac{\sqrt N}{\log N})\Big)
=N\cdot O\big(\tfrac1{\log L}\big)+o(N).$$
(On a utilisé Mertens : $\sum_{p>y}1/p^2=O(1/(y\log y))$ avec $y=L^2$ ; et
$(L+1)^2\sqrt N=o(N)$ car $N\gg L^4$.) **Donc le mur B contribue $0$ pour tout $n$ sauf une
densité $O(1/\log L)\to0$ : presque tout $n$.**

**Vérification numérique (`checkB.py`).** Fraction de $n$ avec B-contribution $>0$ :
$0\%$ ($L{=}15$, B vide), $3{,}4\%$ ($L{=}18$), $5{,}4\%$ ($L{=}22$) ; moyenne
$\le0{,}056$, max $2$. Petit, cohérent avec la borne $(L+1)^2\sum_{p>L^2}1/p^2\approx0{,}13$
(`checkB.py`) qui décroît lentement.

**Théorème (inconditionnel, presque tout $n$, COMPLET).** En combinant :
- $p\le L+1$ : **déterministe** $\le0{,}3205\,T+o(T)$ pour *tout* $n$ (Lemme K + R1) ;
- $(L,L^2]$ : densité d'exceptions $O(1/(L\log L))$ au-delà de $0{,}4\,T$ (STEP12) ;
- $(L^2,\sqrt{n/2}]$ : densité d'exceptions $O(1/\log L)$ au-delà de $0$ (**ICI, nouveau**) ;
- $(\sqrt{n/2},\sqrt n]$ : **déterministe** $O(L)=o(T)$ pour *tout* $n$ (Kalinin) ;

l'union des ensembles exceptionnels a densité $O(1/\log L)\to0$, et hors d'elle
$\sum_pN_p(n)<0{,}73\,T<T$. **Donc la variante deux-puissances de #11 vaut pour presque
tout $n$ impair, inconditionnellement, sur TOUTES les plages de premiers.** (Avant :
seulement sur $(L,L^2]$, B explicitement non couvert.)

Le taux d'exception passe de $O(1/(L\log L))$ (sous-plage) à $O(1/\log L)$ (problème
complet) — plus lent mais portant sur **tout** le problème. Le maillon dominant en mesure
est désormais B (premier moment $\sim1/\log L$), pas $(L,L^2]$.

## 4. Bilan mis à jour

| Plage de $p$ | Tout $n$ | Presque tout $n$ |
|---|---|---|
| $\le L+1$ | **FAIT** (Lemme K + R1) | idem |
| $(L,L^2]$ | pire-cas dissous ; $o(L^2)$ ⟸ M″ (ouvert) | **FAIT** (STEP12) |
| $(L^2,\sqrt{n/2}]$ | mur B (ouvert) | **FAIT (NOUVEAU, §3)** premier moment |
| $(\sqrt{n/2},\sqrt n]$ | **FAIT** (Kalinin) | idem |

**Pour « tout $n$ » il reste exactement (M″) et (B) en pire-cas** — inchangé. **Pour
« presque tout $n$ », c'est désormais COMPLET et inconditionnel.**

**Plausibilités (inchangées sur le fond) :** tout-$n$ élémentaire ~3-5 % ; spécialiste
~50 % ; **presque-tout-$n$ : ACQUIS et désormais complet.** Le recouvrement (l'arme de
#9/#16) est *prouvé inapplicable* au squarefree ($\sum1/p^2<1$) — argument net en faveur de
la véracité de la conjecture, et explication structurelle de pourquoi la variante squarefree
est plausible là où la variante premier ($p+2^a+2^b$, #9) est fausse.

---
*Sources : Chen arXiv:2312.04120v3 (=#16, lu intégralement) ; Pan arXiv:0905.3809 (=#9,
recouvrement confirmé) ; erdosproblems.com/9 (Crocker $\gg\log\log N$, Pan $\gg_\varepsilon
N^{1-\varepsilon}$) ; PDF GPT (harmonique $S_p(t)$, aucune fermeture). Scripts : `checkB.py`
(premier moment B, $\sum_{p\ge3}1/p^2=0{,}202$). Corrige tentative précédente (Pan =
recouvrement, pas crible) et PAPER §6 (presque-tout couvre maintenant B).*
