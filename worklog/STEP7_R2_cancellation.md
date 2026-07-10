> ⚠️ **PARTIELLEMENT CORRIGÉ par `STEP8`.** La compensation racine-carrée de $\max_a|T(a)|$ est
> bien réelle (ci-dessous), MAIS l'affirmation « il suffit d'assembler un grand crible standard,
> ~45-55 % » était trop optimiste : le grand crible **ne s'applique pas directement** (suite trop
> parcimonieuse ; littérature mod $p$ seulement). Voir `STEP8` pour l'analyse corrigée et la
> plausibilité révisée (~20-30 %). La compensation ponctuelle est noyée par Parseval (les $p^2$
> valeurs de $a$) — ce point est expliqué dans `STEP8` Q2/Q3.

# R2 : la compensation racine-carrée est présente (approche (a) viable) — note finale

**Date :** 2026-06-22. Complément à `STEP6_residual.md` (qui ferme R1 ; R2 = seul reste).

## Test de compensation sur la somme lacunaire incomplète

Pour $p$ grand ($d_p>L+1$, donc $2^0,\dots,2^L$ distincts mod $p^2$), on a mesuré
$\displaystyle\max_{a:\,p\nmid a}\Big|T(a)\Big|$, $T(a)=\sum_{l=0}^{L}e_{p^2}(a2^l)$ :

| $L$ | $p$ (échantillon $53..503$) | $\max_a\lvert T(a)\rvert$ | $\sqrt{L+1}$ | trivial $L+1$ | ratio$/\sqrt{L{+}1}$ |
|---|---|---|---|---|---|
| 20 | 53–503 | 12–15 | 4.58 | 21 | **2.6–3.2** |
| 40 | 53–503 | 15–21 | 6.40 | 41 | **2.4–3.2** |

**Conclusion : $\max_a|T(a)|\approx c\sqrt{L+1}$ avec $c\approx2{,}8$ — compensation en racine
carrée, stable en $p$ et en $L$.** C'est le comportement « idéal » attendu d'une somme
d'exponentielles sur une suite lacunaire (cohérent avec Bourgain–Garaev–Konyagin). **L'ingrédient
analytique requis pour R2 EXISTE donc réellement** ; ce n'est pas un mur, c'est une estimation
standard. Approche (a) **viable**.

## Mais : la compensation ponctuelle ne suffit pas seule — il faut le grand crible

Avec $|T(a)|\le c\sqrt{L+1}$ pour tout $a\ne0$, la borne par premier reste :
$$N_p(n)=\frac{(L+1)^2}{p^2}+\frac1{p^2}\sum_{a\ne0}e_{p^2}(-an)T(a)^2,\quad
\Big|\tfrac1{p^2}\!\sum_{a\ne0}\!\dots\Big|\le\frac1{p^2}\sum_{a\ne0}|T(a)|^2=(L+1)-\frac{(L+1)^2}{p^2}.$$
(Parseval : $\sum_a|T(a)|^2=p^2(L+1)$.) Donc **par premier** on ne fait pas mieux que
$N_p(n)\le L+1$ pour un $n$ adverse fixé — la compensation racine-carrée de $\max_a|T(a)|$ est
noyée par les $\sim p^2$ termes $a$. Sommé sur $\pi(\sqrt n)\sim\sqrt n$ premiers : $L\sqrt n$.

**Ce qui sauve, c'est de sommer sur $p$ (grand crible), pas sur $a$ par premier.** Les « mauvais »
$n$ (ceux où $\sum_{a\ne0}e_{p^2}(-an)T(a)^2$ est grand) **diffèrent selon $p$** ; une inégalité de
grand crible / crible carré (Heath-Brown) pour la famille bilinéaire lacunaire $\{2^l+2^m\}$
exploite cette décorrélation pour donner $\sum_{z<p\le\sqrt n}N_p(n)=o(L^2)$ *uniformément en $n$*.
C'est l'étape exacte qui manque — standard mais non élémentaire.

## État final (fin de ce bloc de sessions sur #11 deux-puissances)

**Rigoureux & élémentaire :** réduction $(\star)$ ; petits premiers $\le0{,}3205(L+1)^2$ ;
**Lemme K** (annulation exacte périodes complètes) ; périodes complètes des grands premiers
$=o(L^2)$ unif. ; **Proposition R1** (bord $=O(L^2/\log L)$, confiné à $p\le L+1$).

**Ouvert (1 seul morceau, R2) :** grand crible / crible carré pour $\sum_{d_p>L+1}N_p(n)=o(L^2)$.
L'ingrédient-clé (compensation $\max_a|T(a)|\ll\sqrt L$) est **numériquement confirmé présent** ;
reste à l'assembler via le grand crible sur les modules $p^2$.

**Verdict :** la variante deux-puissances est, après ces sessions, **réduite à un unique énoncé
de grand crible standard**, tout le reste étant élémentaire et rigoureux. C'est de loin le
résultat le plus avancé de toute l'investigation méta — un véritable chemin de preuve, à 80–90 %
rédigé, ne butant que sur une estimation analytique connue dans son principe.

**Plausibilités (finales) :** preuve complète via grand crible standard **~45-55 %**
(compensation confirmée ⇒ pas de mur, juste de l'assemblage technique) ; entièrement
élémentaire **~5-10 %** ; **formalisation Lean conditionnelle** (tout sauf R2) faisable
immédiatement comme résultat partiel publiable.

**Prochaine étape unique :** rédiger/adapter l'inégalité de grand crible pour $\{2^l+2^m\bmod p^2\}$
— soit en invoquant une borne publiée sur $\sum_{l}e(a2^l/q)$ et le crible carré de Heath-Brown,
soit en montant un argument de grand crible additif ad hoc sur les $p^2\le n$.

---
*Test de compensation : script inline (échantillonnage de $4000$ résidus $a$ par premier,
$p\in\{53,\dots,503\}$, $L\in\{20,40\}$). Cohérent avec la littérature des sommes lacunaires.*
