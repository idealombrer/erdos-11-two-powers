# L'argument CRT pour $C(n)=o(L^2)$ : faille identifiée + ce qui se sauve rigoureusement

**Date :** 2026-06-23. Objectif : prouver $C(n)=\sum_{p\in(L,3L]}N_p(n)(N_p(n)-1)=o(L^2)$ pour
le **pire** $n$, via l'argument CRT proposé. **Résultat : l'argument CRT tel qu'énoncé est FAUX
(faille précise ci-dessous), mais sa version *en moyenne* est rigoureuse et donne la conjecture
deux-puissances pour PRESQUE TOUT $n$. Le « tout $n$ » reste ouvert au même mur moyenne-vs-pire-cas.**

## 1. La faille de l'argument CRT (étape 2 du plan)

L'argument supposait : « si $N_p(n)\ge2$ alors $n$ est dans une classe mod $p^2$ de densité
$\sim1/p^2$, donc $k$ premiers ⟹ densité $\prod1/p^2\sim L^{-2k}$ ». **Trois erreurs :**

**(a) La densité de $\{n\bmod p^2:N_p(n)\ge2\}$ n'est PAS $1/p^2$ — elle est $\sim\lambda_p^2/2$
(loi de Poisson), $\lambda_p=\binom{L+2}{2}/p^2$.** Vérifié numériquement (décisif) :

| $L=20$, $p$ | 23 | 29 | 31 | 37 | 41 | 53 |
|---|---|---|---|---|---|---|
| $\lambda_p$ | 0.44 | 0.27 | 0.24 | 0.17 | 0.14 | 0.08 |
| densité$(N_p\ge2)$ mesurée | **0.089** | 0.034 | 0.055 | 0.0095 | 0.0030 | 0 |
| $\lambda_p^2/2$ (Poisson) | 0.095 | 0.038 | 0.029 | 0.014 | 0.009 | 0.003 |
| $1/p^2$ (supposé, FAUX) | 0.0019 | 0.0012 | 0.0010 | 0.0007 | 0.0006 | 0.0004 |

Pour $p\sim L$ la densité réelle ($\sim0{,}05$–$0{,}09$) est **50× plus grande** que $1/p^2$.
Raison : les $\sim L^2/2$ paires couvrent presque tout $\mathbb Z/p^2$ (car $p^2\sim L^2$), donc
les collisions (≥2 paires sur le même résidu) sont *fréquentes*, pas rares. La prémisse
« densité $1/p^2$ » est donc fausse d'un facteur $\sim(\lambda_p^2/2)p^2=\Delta_p/2$.

**(b) Confusion densité ↔ valeur de $C(n)$.** $C(n)$ est une quantité *déterministe* pour chaque
$n$ ; une « densité » est une moyenne *sur* $n$. La ligne « $C(n)\le k\cdot L^2\cdot L^{-2k}$ »
mélange les deux : une densité de conditions ne se convertit pas en une borne sur $C(n)$ pour un
$n$ fixé.

**(c) Rare $\ne$ jamais.** Même avec les bonnes densités, « peu de $n$ sont mauvais » (densité
faible) n'implique pas « aucun $n\le2^L$ n'est mauvais ». Un ensemble de densité $2^{-L}$ sur une
période $\gg2^L$ peut très bien avoir tous ses éléments dans $[1,2^L]$. C'est le mur
**moyenne/densité vs pire-cas** — exactement l'obstacle de toutes les sessions.

## 2. Ce qui SE SAUVE rigoureusement : la version *en moyenne* ⟹ presque tout $n$

La bonne version de l'idée CRT donne un vrai théorème. **En moyenne sur $n$** (rigoureux) :
$$\overline{C}:=\frac1{p^2\cdots}\sum_n C(n)=\sum_{p\in(L,3L]}\frac{\Delta_p}{p^2},\qquad
\Delta_p=\#\{(P,P'):P\ne P',\ \mathrm{sum}(P)\equiv\mathrm{sum}(P')\bmod p^2\}.$$
Pour les premiers $p\in(L,3L]$, $\Delta_p\approx(\#\text{paires})^2/p^2=L^4/(4p^2)$ (collisions
quasi-aléatoires, vérifié), d'où $\Delta_p/p^2\approx L^4/(4p^4)$ et
$$\overline{C}\approx\frac{L^4}4\sum_{p>L}\frac1{p^4}\approx\frac{L^4}4\cdot\frac1{3L^3\ln L}
=\frac{L}{12\ln L}.$$
**Mesuré : $\overline C\approx0{,}44,0{,}43,0{,}51,0{,}96,0{,}52$ pour $L=16,20,24,28,32$** —
$O(L/\ln L)$, très lentement croissant, $=o(L^2)$ avec une marge énorme.

**Conséquence rigoureuse (Markov).** Densité de $\{n:C(n)\ge T\}\le\overline C/T$. Avec
$T=0{,}4L^2$ : densité des $n$ exceptionnels $\le\dfrac{L/(12\ln L)}{0{,}4L^2}=O\!\Big(\dfrac1{L\ln L}\Big)\to0.$
Donc $R2\le\pi(L^2)+C(n)<0{,}5L^2$ pour **presque tout $n$** ⟹ il existe une paire $(i,j)$ avec
$n-2^i-2^j$ sans facteur carré pour **presque tout $n$**.

> **Théorème (rigoureux, presque tout $n$).** La variante deux-puissances de #11 vaut pour une
> proportion $1-O(1/(L\ln L))$ des entiers impairs $\le2^{L+1}$ (avec $Q(n)\le\pi(L^2)$
> inconditionnel + $\overline C=o(L^2)$ + Markov). C'est le pendant deux-puissances du « presque
> tout $n$ » d'Erdős pour une puissance.

## 3. Pourquoi « tout $n$ » reste hors d'atteinte (le maillon, nommé)

Le passage moyenne → *tout* $n$ exige de borner $\max_n C(n)$, pas $\overline C$. Le pire $n$
pourrait (a priori) concentrer $N_p$ sur quelques petits $p$. Les bornes déterministes
disponibles ($N_p\le L+1$ par premier, $O(L/\ln L)$ premiers) donnent $C(n)\le O(L^3/\ln L)$ —
le mur $L^3$. L'argument de densité/CRT borne la *fréquence* des mauvais $n$ (→0) mais pas leur
*existence* sous $2^L$. **C'est le même mur moyenne-vs-pire-cas / équidistribution depuis le début.**

**Maillon manquant (précis) :** $\displaystyle\max_{n}\ C(n)=\max_n\!\!\sum_{p\in(L,3L]}\!\!N_p(n)(N_p(n)-1)=o(L^2)$,
i.e. *aucun* $n$ ne concentre les collisions ; équivalent à une équidistribution de
$\{2^i+2^j\bmod p^2\}$ valable uniformément en $n$ (pas seulement en moyenne). Type Heilbronn /
grand crible — non élémentaire.

## 4. Verdict final honnête

**(b/c) PAS de preuve complète ; mais nouveau résultat rigoureux + maillon proprement nommé.**

- **L'argument CRT du plan est faux** (densité $\lambda_p^2/2$, pas $1/p^2$ ; densité≠valeur ;
  rare≠jamais). Je ne l'ai pas « validé » — je l'ai réfuté, test numérique à l'appui.
- **Acquis rigoureux nouveau :** $Q(n)\le\pi(L^2)=o(L^2)$ (inconditionnel) **+** $\overline{C(n)}
  =o(L^2)$ (second moment) **⟹ conjecture deux-puissances pour PRESQUE TOUT $n$** (densité
  d'exceptions $O(1/(L\ln L))$). C'est un vrai théorème, propre, du niveau « presque tout »
  d'Erdős.
- **« Tout $n$ » :** reste ouvert, réduit au maillon $\max_n C(n)=o(L^2)$ (pire-cas, non
  élémentaire), même mur moyenne-vs-pire-cas.

**Plausibilités (inchangées sur le fond) :** « presque tout $n$ » = **acquis** ; « tout $n$ »
élémentaire ~5-10 % ; via spécialiste (équidistribution uniforme mod $p^2$) ~40-50 %.

**Honnêteté :** l'idée CRT était bonne en *esprit* (l'indépendance limite la concentration) mais
ne franchit pas, telle quelle, le mur moyenne→tout. Ce mur est désormais identifié de façon
récurrente et robuste : **toutes** nos réductions (équidistribution mod $p^2$, puis coïncidences
$C(n)$, puis CRT) y reviennent. C'est le cœur analytique irréductible du problème.

---
*Scripts : densité de $\{N_p\ge2\}$ vs $1/p^2$ (réfutation de l'étape 2) ; $\overline C=\sum\Delta_p/p^2$
(presque-tout). Améliore `STEP11` : la moitié $Q(n)$ + la moyenne $\overline C$ donnent un
théorème « presque tout $n$ » rigoureux ; le pire-cas reste le maillon.*
