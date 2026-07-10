# M2 : verdict — le maillon était MAL IDENTIFIÉ. #{non-Sidon} est trivial ; le vrai maillon est $\sum M_p$.

**Date :** 2026-06-23. Attaque de M2. **Résultat : la question a révélé que le maillon de STEP14/15
était MAL POSÉ. « #{non-Sidon}$=o(L^2)$ » est TRIVIAL ($\le\pi(L^2)$). Le vrai contenu du Lemme M
est $\sum_{p\in(L,L^2]}M_p=o(L^2)$, qui TIENT (empirique : $\sim1.15\,\pi(L^2)$), mais dont la
preuve est *borderline* et non élémentaire. Ceci confirme l'avertissement méta : il y avait un
sous-maillon caché.**

## 0. Réponse à la question méta (validée a posteriori)

J'avais estimé ~40-50 % de risque que M2 révèle un sous-maillon. **C'est arrivé** : en creusant,
le « maillon M2 » de STEP14/15 (#{non-Sidon}$=o(L^2)$) s'avère **trivial**, et le vrai maillon est
ailleurs (la *somme* des multiplicités). Le risque méta était justifié.

## 1. Correction factuelle : #{non-Sidon} $=\Theta(L^2/\ln L)$, pas $O(L)$

STEP14 (jusqu'à $L=36$) suggérait #{non-Sidon}$=O(L)$. **C'était un artefact des petits $L$.**
Recalcul jusqu'à $L=48$ :

| $L$ | 32 | 36 | 40 | 44 | 48 |
|---|---|---|---|---|---|
| #{non-Sidon $p$} | 28 | 35 | 46 | 51 | 56 |
| $/\pi(L^2)$ | 0.16 | 0.17 | 0.18 | 0.17 | 0.165 |

**#{non-Sidon}$\approx0.17\,\pi(L^2)=\Theta(L^2/\ln L)$** : une **fraction constante ($\sim17\%$)**
des premiers de la plage sont non-Sidon ! (Pas une poignée.) La « loi linéaire $\sim L$ » de
STEP14 était fausse.

## 2. Conséquence : « #{non-Sidon}$=o(L^2)$ » est TRIVIAL — ce n'était pas le maillon

$\#\{\text{non-Sidon }p\in(L,L^2]\}\le\pi(L^2)-\pi(L)\sim L^2/(2\ln L)=o(L^2)$ **automatiquement**,
juste par le théorème des nombres premiers. Donc l'énoncé que STEP14/15 appelait « le maillon M2 »
est **trivialement vrai** et **ne nécessite ni Baker ni S-unités**. *J'avais mal identifié le maillon.*
(L'argument heuristique « presque tous non-Sidon » échoue aussi : seulement 17 %, pas 100 % —
structure réelle.)

## 3. Le VRAI maillon : $\sum_p M_p=o(L^2)$, et il est *borderline*

Le Lemme M est $\sum_{p\in(L,L^2]}M_p=o(L^2)$ (pour avoir $R2|_{(L,L^2]}\le\sum M_p=o(L^2)$).
$M_p^{\text{unord}}=1$ pour Sidon, donc
$$\sum_p M_p^{\text{unord}}=\pi(L^2)+\underbrace{\sum_{\text{non-Sidon}}(M_p-1)}_{\text{défaut total}}.$$
Données (jusqu'à $L=48$) : $\sum M_p\approx1.15\,\pi(L^2)$, donc défaut $\approx0.15\,\pi(L^2)=o(L^2)$.
$\sum M_p/L^2$ décroît (0.20→0.17, $\sim$const$/\ln L\to0$). **Lemme M TIENT.**

**Pourquoi (distribution) :** #{M=2}$=18,20,37,42$ (domine), #{M=3}$=2,8,8,11$, #{M≥4}$=0,0,1,3$
(rare). La multiplicité moyenne des non-Sidon est $O(1)$ ($\sim1.3$), distribution à décroissance
rapide en $k$.

**Pourquoi c'est *borderline* à prouver :** la borne brute
$\sum_{\text{non-Sidon}}(M_p-1)\le M_{\max}\cdot\#\{\text{non-Sidon}\}\sim(\log L)\cdot(L^2/\ln L)=\Theta(L^2)$
— **échoue d'un cheveu** (donne $\Theta(L^2)$, pas $o(L^2)$). Le $o(L^2)$ exige la **décroissance
de la distribution** : $\sum_{k\ge2}\#\{p:M_p\ge k\}=o(L^2)$ avec #{$M_p\ge k$} décroissant
géométriquement en $k$ (empirique : ratios $0.17,0.05,0.01$). C'est un énoncé de type
**$B_2[g]$ / multiplicité de Sidon** : combien de premiers ont une multiplicité additive élevée.

## 4. Verdict M2 (réponse Q4) : (c) — sous-maillon révélé, re-identifié plus proprement

- L'ancien « M2 » (#{non-Sidon}$=o(L^2)$) : **trivial** (pas un maillon).
- Le vrai maillon : $\sum_{p\in(L,L^2]}M_p=o(L^2)$ $\iff$ **décroissance de la distribution de
  multiplicité** $\sum_{k\ge2}\#\{p\in(L,L^2]:M_p^{\text{unord}}\ge k\}=o(L^2)$.
- **Statut :** TRUE (empirique robuste, $\sum M_p\sim1.15\pi(L^2)$), mais *borderline* :
  la borne triviale donne $\Theta(L^2)$ ; le $o(L^2)$ exige le contrôle fin de la queue de
  distribution des multiplicités, **non élémentaire** (combien de premiers ont $p^2\mid$ plusieurs
  combos à 4 termes simultanément ⟹ multiplicité $\ge k$ ; type énergie additive d'ordre supérieur).

**Pas (a) ni (b) proprement** : ce n'est pas un comptage de facteurs carrés élémentaire (a faux),
ni une seule citation Baker (b incomplet) — c'est (c) un énoncé distributionnel sur les
multiplicités additives de $\{2^l\bmod p^2\}$, propre mais non trivial.

## 5. Bilan global #11 deux-puissances (corrigé)

| Plage de $p$ | Statut |
|---|---|
| $\le L$ | **FAIT** élémentaire (Lemme K + R1) |
| $(L,L^2]$ | pire-cas $n$ dissous ; $=o(L^2)$ via Lemme M ⟸ **décroissance distribution multiplicité** (borderline, non élém.) |
| $(\sqrt{n/2},\sqrt n]$ | **FAIT** $O(L)$ (Kalinin) |
| $(L^2,\sqrt{n/2}]$ | mur **(B)** : densité squarefree / équidistribution |

**Deux maillons restants :** (M$''$) décroissance de la distribution de multiplicité sur $(L,L^2]$
[borderline $o(L^2)$, non élém.] ; **(B)** densité squarefree plage moyenne-haute [équidistribution].

## 6. Évaluation honnête de la profondeur restante (mise à jour)

Cette session **confirme** qu'il y avait de la profondeur cachée : le maillon a dû être
re-identifié (de « #non-Sidon », trivial, vers « somme de multiplicités », borderline). Le motif
récurrent persiste : **chaque fois qu'on précise un maillon, soit il se trivialise, soit il révèle
un énoncé distributionnel/analytique plus fin.** Profondeur restante honnête : **2 maillons
analytiques (M$''$, B), tous deux $o(L^2)$ empiriquement vrais, tous deux non élémentaires
(distribution de multiplicité / équidistribution), et tous deux *borderline* aux bornes brutes
(qui donnent $\Theta(L^2)$ ou $L^3$).** Le problème reste **entièrement réduit et cartographié**,
le pire-cas $n$ dissous, mais la fermeture demande deux estimations analytiques fines —
décidément du ressort d'un spécialiste, pas de l'élémentaire.

**Plausibilités (stables, légèrement précisées) :** élémentaire ~3-5 % (les bornes brutes butent
toutes à $\Theta(L^2)$/$L^3$) ; spécialiste ~50 % (deux estimations fines mais standards) ;
partiels rigoureux : presque-tout $n$ (STEP12), pire-cas dissous (STEP13), réduction à 2 énoncés
distributionnels nommés (ici).

---
*Scripts : #{non-Sidon} jusqu'à $L=48$ (Θ(L²/lnL), ~17%) ; $\sum M_p\approx1.15\pi(L^2)$ +
distribution de multiplicité (#M=2 domine) ; valeurs de collision avec facteur carré (abondantes).
Corrige STEP14/15 (maillon mal posé : #non-Sidon est trivial, le vrai est $\sum M_p$).*
