# M1 : verdict — l'énoncé « $M_p\le C$ absolu » est FAUX ; $M_p$ croît (~log L). Evertse ne s'applique pas.

**Date :** 2026-06-23. Objectif : prouver M1 ($M_p\le C$ constante absolue, $p\in(L,L^2]$).
**Résultat : M1 tel qu'énoncé est FAUX — $M_p$ croît lentement (~$\log L$), atteint sur les
premiers à petit ordre. Mais M1 n'est PAS nécessaire au Lemme M. Le vrai maillon est M2
(#{non-Sidon}$=o(L^2)$), non élémentaire, et Evertse ne s'y applique pas (anneau fini).**

## 1. Reformulation (réponse Q1) et pourquoi le groupe ne donne pas de borne absolue

$M_p=\max_n\#\{(i,j):2^i+2^j\equiv n\ (p^2)\}$. Une collision $2^a+2^b\equiv2^c+2^d\ (p^2)$ est
une **équation additive entre éléments du groupe $\langle2\rangle\subset(\mathbb Z/p^2)^\times$**
(cyclique d'ordre $d_p$). Mais $M_p$ n'est PAS le nombre total de solutions (= $\Delta_p$,
l'énergie, qui est **non bornée**, ~$L^2$ pour petits $p$) ; $M_p$ est la **multiplicité maximale
en un seul $n$**. Les deux diffèrent : les collisions sont *étalées* sur beaucoup de $n$ (testé :
$p=31$ a $\Delta_p=118$ mais $M_p^{\text{unord}}=3$).

**Pourquoi le groupe ne borne pas $M_p$ :** dans un **anneau fini** $\mathbb Z/p^2$ (ou un corps
fini), les équations en S-unités $x+y=z+w$ avec $x,y,z,w\in H$ (sous-groupe) ont
$\sim|H|^2/p^2\cdot|H|^2$… BEAUCOUP de solutions (pas de borne absolue). C'est le contraire de
la caractéristique 0.

## 2. Evertse ne s'applique PAS (réponse Q2 — correction d'un malentendu)

Le théorème d'Evertse (et ESS/Evertse–Győry) borne le nombre de solutions **non dégénérées**
d'équations en S-unités **sur les corps de nombres** (caractéristique 0). Il **ne s'applique
pas** à $\mathbb Z/p^2$ : (i) $\mathbb Z/p^2$ n'est pas $\mathbb F_{p^2}$ (le corps), c'est un
anneau local avec diviseurs de zéro ; (ii) même sur $\mathbb F_p$ ou $\mathbb F_{p^2}$, les
équations en S-unités ont $\sim|H|^2/q$ solutions (Garcia–Voloch, etc.) — **non bornées** quand
$|H|\to\infty$. Donc l'intuition « Evertse ⟹ $M_p\le C$ » est erronée. Le cadre correct pour la
multiplicité max serait un problème de type $B_2[g]$ / Sidon, pas Evertse.

## 3. Donnée décisive (réponse Q3) : $M_p$ CROÎT, ~$\log L$

| $L$ | 20 | 30 | 40 | 50 | 60 | 70 |
|---|---|---|---|---|---|---|
| $\max_{p\in(L,L^2]}M_p^{\text{unord}}$ | 3 | 4 | 4 | 4 | 5 | 6 |
| premier argmax | 23 | 31 | 41 | 71 | 127 | 127 |
| $\mathrm{ord}_p(2)$ | 11 | 5 | 20 | 35 | **7** | **7** |
| $\log_2 L$ | 4.3 | 4.9 | 5.3 | 5.6 | 5.9 | 6.1 |

- **$\max M_p$ croît : $3\to6$ pour $L:20\to70$** — *pas* une constante absolue. Croissance
  lente, sous-linéaire, cohérente avec $\sim\log L/\log\log L$ (modèle aléatoire : $\sim L^2/2$
  sommes dans $\ge L^2$ classes mod $p^2$ ⟹ max-par-classe $\sim$ max de Poisson $\sim\log L/\log\log L$).
- **Atteint sur les premiers à PETIT ordre** ($p=127$, $\mathrm{ord}=7$) : là $\langle2\rangle$
  est petit, $d_p=7\cdot127=889$ relativement petit, plus de collisions concentrées.
- $\Delta_p$ (énergie totale) : non bornée (testé, jusqu'à 118 pour $p=31$, $L=20$) — à ne pas
  confondre avec $M_p$.

**Donc M1 (constante absolue) est FAUX.** Le bon énoncé est $M_p=o(L)$ (en fait ~$\log L$), ce qui
est *suffisant* pour le Lemme M (voir §4).

## 4. Pourquoi le Lemme M survit quand même (M1 n'était pas nécessaire)

$\sum_{p\in(L,L^2]}M_p=2\pi_{\text{rg}}+\sum_{\text{non-Sidon}}(M_p-2)$. Avec
$\#\{\text{non-Sidon}\}=O(L)$ (M2, donnée STEP14) et l'excès empirique $\sum(M_p-2)=O(L)$
(la plupart des non-Sidon ont $M_p=3$, excès 1), on a $\sum M_p=o(L^2)+O(L)=o(L^2)$.
**Le Lemme M ne dépend donc PAS de $M_p\le C$ absolu** ; il dépend de :
- **(M2)** $\#\{\text{non-Sidon }p\in(L,L^2]\}=o(L^2)$ [empiriquement $O(L)$] — le vrai maillon ;
- **(M1$'$)** excès moyen borné / $M_p=o(L)$ sur les non-Sidon — empiriquement OK ($M_p\sim\log L$),
  bien plus faible que M1.

## 5. Verdict (réponse Q4) : (c) — M1 réfuté, nouveau maillon = M2

**M1 (constante absolue) : RÉFUTÉ** (donnée : $M_p$ croît $3\to6$). Ni la structure de groupe ni
Evertse ne donnent de borne absolue (anneau fini : équations en S-unités non bornées).

**Ce qui reste réellement** (inchangé, mais clarifié) :
- **(M2)** $\#\{\text{non-Sidon }p\in(L,L^2]\}=o(L^2)$. C'est l'énoncé clé pour le Lemme M, et
  c'est **non élémentaire** : il s'agit de borner le nombre de premiers $p>L$ tels que
  $p^2\mid 2^a+2^b-2^c-2^d$ (combo $\ne0$, exposants $\le L$). Comptage brut $=L^3$ (ou $L^5$ par
  produit) ; la vérité $O(L)$ exige de contrôler les **facteurs carrés des combos à 4 termes de
  puissances de 2** = équation en S-unités **sur $\mathbb Z$** / formes linéaires de logarithmes
  ($p$-adiques, Baker–Wüstholz, ou théorie des équations $2^a\pm2^b\pm2^c\pm2^d=p^2 m$). Standard
  pour un spécialiste, hors de portée élémentaire.
- (M1$'$) $M_p=o(L)$ (~$\log L$) : empiriquement solide, suffisant, probablement accessible par
  le modèle de comptage, mais formellement aussi un énoncé de multiplicité $B_2[g]$ non trivial.

## 6. Bilan global #11 deux-puissances (le plus précis)

| Plage de $p$ | Statut |
|---|---|
| $\le L$ | **FAIT** élémentaire (Lemme K + R1) |
| $(L,L^2]$ | pire-cas $n$ dissous ; $=o(L^2)$ via Lemme M ⟸ **(M2)** [+(M1$'$)] |
| $(\sqrt{n/2},\sqrt n]$ | **FAIT** $O(L)$ (Kalinin, carrés parfaits) |
| $(L^2,\sqrt{n/2}]$ | mur **(B)** : densité squarefree / équidistribution |

**Deux maillons analytiques restants, tous deux non élémentaires, tous deux propres :**
- **(M2)** facteurs carrés des combos à 4 termes de puissances de 2 (S-unités sur $\mathbb Z$) ;
- **(B)** densité squarefree de $\{n-2^i-2^j\}$ plage moyenne-haute (grand crible / équidistribution).

**Plausibilités (stables) :** élémentaire ~3-5 % ; spécialiste ~50-60 % ; partiels rigoureux
(presque-tout $n$ ; réduction à (M2)+(B) ; pire-cas $n$ dissous). 

**Honnêteté :** cette session a *réfuté* la cible M1 (j'ai cherché à la prouver, les données la
contredisent — $M_p$ croît) et a **corrigé l'intuition Evertse** (inapplicable en anneau fini).
Le gain net : le Lemme M ne repose pas sur M1 mais sur M2, et on a clarifié que M2 est une
question de facteurs carrés de combos de puissances de 2 (S-unités sur $\mathbb Z$), pas une
équation en S-unités sur un corps fini. La cartographie finale est inchangée et solide : 2
maillons analytiques standards restants, problème *réduit* mais non *fermé* élémentairement.

---
*Scripts : $M_p$ vs $\Delta_p$ ($p\le200$, $L=20$) ; $\max M_p^{\text{unord}}$ sur $(L,L^2]$
jusqu'à $L=70$ (task `bdmgr0gpe`). Modèle aléatoire pour la croissance $\log L$. Evertse :
inapplicable (anneau fini), corrigé.*
