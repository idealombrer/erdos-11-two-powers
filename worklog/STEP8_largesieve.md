# R2 et le grand crible : pourquoi il ne s'applique PAS directement (analyse honnête)

**Date :** 2026-06-22. Réponses aux questions 1–6. **Corrige l'optimisme de `STEP7`** (« ~45-55 %,
assembler une machinerie standard ») : après examen, le grand crible standard **ne ferme pas R2**,
et la littérature disponible est *modulo $p$*, pas $p^2$. R2 est un vrai sous-problème analytique.

## Q1 — Le grand crible standard (Montgomery–Vaughan / Bombieri) s'applique-t-il ? **NON, directement.**

On veut borner $R2=\sum_{p:\,d_p>L+1,\ p\le\sqrt n}N_p(n)$,
$N_p(n)=\#\{(l,m)\in[0,L]^2:2^l+2^m\equiv n\,(p^2)\}$.

**Tentative grand crible sur la suite des valeurs.** Posons $u_v=\#\{(l,m):k_{l,m}=v\}\le2$,
supportée sur $[1,n]$, $\|u\|_2^2\le2(L+1)^2$. Alors $N_p(n)=\sum_{v\equiv0(p^2)}u_v$, et
$$N_p(n)-\frac{(L+1)^2}{p^2}=\frac1{p^2}\sum_{b=1}^{p^2-1}U(b/p^2),\quad U(\alpha)=\sum_v u_v e(v\alpha).$$
Cauchy–Schwarz + grand crible $\sum_{q\le R}\sum_{(a,q)=1}|U(a/q)|^2\le(N+R^2)\|u\|_2^2$ donne,
avec $N=n$ et modules $q=p^2\le n$ (donc $R=\sqrt n$, $R^2=n$) :
$$\text{erreur}\ \lesssim\Big(\sum_p p^{-2}\Big)^{1/2}\big((N+R^2)\|u\|_2^2\big)^{1/2}
\lesssim z^{-1/2}\cdot\sqrt{n\cdot(L+1)^2}=\frac{\sqrt n\,(L+1)}{\sqrt z}.$$
**$\sqrt n\,L\gg L^2$ : catastrophique.** Cause : la suite $u_v$ est *ultra-parcimonieuse*
($(L+1)^2$ points dans $[1,n]$), donc $\|u\|_2^2\sim L^2$ est noyé par le facteur $N=n$ du grand
crible. **Le grand crible est conçu pour des suites denses dans $[1,N]$ ; la nôtre ne l'est pas.**

**Même en confinant les modules.** On a établi (calcul ci-dessous, Q-structure) que *tout R2 vient
des premiers $p\in(L,L^2]$* (les $p>L^2$ contribuent **zéro** empiriquement), donc modules
$p^2\le L^4=(\log n)^4$, minuscules. Mais alors le grand crible donne
$\sum_{p\le L^2}\sum_a|T_p(a)|^2\le(n+L^4)(L+1)\approx n(L+1)$, **plus faible que la borne triviale
de Parseval** $\sum_p p^2(L+1)\sim L^7\ll n$. Le grand crible est *trivial* (battu par Parseval) car
modules petits + suite étalée. **Conclusion Q1 : ni Montgomery–Vaughan ni Bombieri ne mordent.**

## Structure de R2 (calcul, `STEP8` inline) : R2 vit sur $p\in(L,L^2]$

Pire $n$ par échelle (jusqu'à $2^{22}$), split de $R2=\sum_{d_p>L+1}N_p(n)$ :

| échelle | $L$ | $L^2$ | $R2$ | $p\in(L,L^2]$ | $p>L^2$ |
|---|---|---|---|---|---|
| $2^{16}$ | 16 | 256 | 33 | **33** | **0** |
| $2^{19}$ | 19 | 361 | 20 | 20 | 0 |
| $2^{22}$ | 21 | 441 | 20 | 20 | 0 |

**$p>L^2$ : contribution nulle** (les $\sim(L+1)^2<L^4<p^2$ paires ne percutent jamais le résidu
$n$ pour des modules aussi grands). Donc R2 est porté par $\pi(L^2)-\pi(L)\sim L^2/\log L$ premiers
*moyens* $p\in(L,L^2]$.

## Q2/Q3 — Faut-il adapter ? **Oui, et ce n'est PAS quelques lignes.**

Sur la plage $p\in(L,L^2]$ : terme principal $\sum_p(L+1)^2/p^2\le\sum_{p>L}(L+1)^2/p^2=O((L+1)^2/L)=
o(L^2)$ ✓. Le **terme d'erreur** est le problème : par premier, Parseval ne donne que
$N_p(n)\le L+1$ (trivial), et sommé sur $\sim L^2/\log L$ premiers $\Rightarrow R2\le L^3/\log L$,
**facteur $L/\log L$ de trop**. Il faut donc montrer que l'erreur **moyenne** $N_p(n)-(L+1)^2/p^2$
est $\ll\log L$ (au lieu de $\le L$) sur ces premiers, *uniformément en $n$* — c'est-à-dire une
**annulation dans les sommes courtes** $T_p(a)=\sum_{l\le L}e_{p^2}(a2^l)$, en moyenne sur
$p\in(L,L^2]$. Ce n'est :
- **pas** le grand crible (trivial ici, cf. Q1) ;
- **pas** un résultat publié directement applicable (cf. Q5 : tout est modulo $p$, pas $p^2$, et nos
  sommes sont dans le régime « très court » $L\sim\log p^2$) ;
- **pas** réductible à une borne ponctuelle $|T_p(a)|\ll\sqrt L$ : même avec la racine-carrée
  (mesurée), $|\sum_{a\ne0}e(an)\overline{T(a)}^2|$ se borne par Parseval $=p^2L$, et la
  compensation ponctuelle est noyée par les $p^2$ valeurs de $a$ ; le gain doit venir du twist
  $e(an)$ sommé sur $a$, qui *est* $p^2N_p(n)-(L+1)^2$ — circulaire.

**C'est donc une adaptation non triviale, voire un problème ouvert** : borner les sommes
d'exponentielles **très courtes** sur $\{2^l\}$ **modulo $p^2$**, en moyenne sur $p\in(L,L^2]$,
uniformément en $n$.

## Q5 — Bibliographie : Garaev / Bourgain / Konyagin sur $2^l\bmod p$

- **Garaev, « The large sieve for $2^{[\dots]}$ modulo primes »** (arXiv:math/0505396) : grand crible
  pour $\lambda^{s_n}\bmod p$, **modulo $p$ seulement**, exige une suite d'exposants pas trop
  parcimonieuse ($|S_N|>N^{14/15}$) — *satisfait* chez nous ($s_n=n$) — mais c'est une moyenne
  $\sum_{p\le X}\frac1{\tau(p-1)}\max_a|\dots|^2$ sur les premiers, **mod $p$, pas $p^2$**.
- **« Incomplete exponential sums over exponential functions »** (arXiv:1302.4170) : sommes
  incomplètes $\sum_{n\le N}e_p(ag^n)$, $g$ d'ordre $t$, bornes $\le p^{1/8}N^{71/96+o(1)}$ etc. —
  **modulo $p$ uniquement**, et le régime utile est $N\le t$ non « très court ».
- **Bourgain–Garaev–Konyagin** (sommes sur sous-groupes / puissances mod $p$) : tout est **mod $p$**.

**Aucun résultat trouvé pour $2^l\bmod p^2$ avec des sommes très courtes ($L\sim\log p^2$ termes)
sommées sur les premiers moyens.** C'est précisément ce qu'il faudrait, et c'est au mieux une
extension non publiée, au pire ouvert. Le passage $p\to p^2$ n'est pas cosmétique (les bornes de
Weil/Bourgain se comportent différemment modulo $p^2$ ; *mais* le Lemme K montre que la structure
mod $p^2$ a aussi des annulations exactes — piste, pas preuve).

## Q6 — Applicabilité au problème général (une puissance) et lien avec #317

**(a) Problème général une-puissance ($n=s+2^l$) : NON, nos méthodes ne s'y appliquent pas.**
Tout repose sur la **marge uniforme quadratique** $0{,}68\,L^2$ (issue des $(L+1)^2/2$ paires). Pour
une puissance il n'y a que $L+1$ candidats : le terme principal petits-premiers est $0{,}32(L+1)$,
laissant une marge **linéaire** $0{,}68(L+1)$, tandis que l'obstruction grand-premier vaut
$\sim\pi(\sqrt n)\sim\sqrt n\gg(L+1)$. Même le **Lemme K** (qui vaut toujours, il porte sur le
module, pas le nombre de puissances) ne sauve pas : son terme de périodes complètes pour une
puissance est $\le(L+1)\sum1/d_p=0{,}32(L+1)$, mais le bord/grands premiers reste $\sim\sqrt n$, sans
marge pour l'absorber. **La marge quadratique est essentielle et absente** — cohérent avec le mur
Wieferich de l'énoncé complet. Nos outils sont spécifiques à deux puissances.

**(b) Lien avec #317 : AUCUN transfert.** #317 (sommes signées de fractions unitaires,
anti-concentration / Littlewood–Offord inverse, machinerie $P^*$-projection/Wilson/CRT, lien #320)
relève d'un **tout autre arsenal**. Notre cœur dur (sommes d'exponentielles sur $\{2^l\}$ mod $p^2$,
ordre multiplicatif, annulation de noyau) n'a **rien** à voir avec l'anti-concentration inverse. Le
seul point commun superficiel — « ça parle de grands premiers » — est trompeur : ce sont des grands
premiers comme **modules de congruence** ici, vs. des premiers comme **dénominateurs/projections**
dans #317. Même schéma de non-transfert que pour #1/#307/#1056/#478 (cf. [[erdos-meta-v2-status]]).
La littérature pertinente pour R2 est Bourgain–Garaev–Konyagin (sommes lacunaires), disjointe de
celle de #317.

## Verdict honnête révisé

- **Acquis solides (inchangés) :** réduction + petits premiers $0{,}3205$ ; **Lemme K** ; périodes
  complètes $=o(L^2)$ ; **R1 (bord) $=o(L^2)$, élémentaire** ; localisation de R2 sur $p\in(L,L^2]$.
- **R2 : plus dur que je ne l'avais dit dans STEP7.** Le grand crible n'aide pas (Q1), la
  littérature est mod $p$ (Q5), et il faut une annulation des sommes **très courtes** $T_p(a)$ mod
  $p^2$ en moyenne sur les premiers moyens — un vrai problème analytique, **non réductible à une
  citation**.
- **Plausibilités corrigées (à la baisse pour la preuve complète) :**
  - preuve complète : **~20-30 %** (R2 est de la recherche analytique réelle, peut nécessiter une
    idée nouvelle ou une extension non publiée à $p^2$ ; *pas* un simple assemblage) ;
  - entièrement élémentaire : **~5 %** ;
  - **résultat partiel conditionnel** (tout sauf R2) **rigoureux et Lean-formalisable maintenant** :
    « variante 2-puissances vraie pour $n$ grand SI $\sum_{L<p\le L^2}N_p(n)=o(L^2)$ » — solide, mais
    l'hypothèse est proche d'une reformulation, pas d'un lemme connu.

**Ce qui reste vrai et important :** c'est toujours **de loin** le meilleur candidat de
l'investigation — un chemin à ~80 % rigoureux, un Lemme K élémentaire inattendu, R1 fermé, et un
unique cœur dur **précisément localisé** (sommes courtes de $2^l$ mod $p^2$, $p\in(L,L^2]$). Mais
honnêtement, ce cœur est un problème d'analyse des nombres à part entière, pas une formalité.

---
*Scripts : tous dans le dossier. Structure de R2 (split $p\le L^2$ / $p>L^2$) : calcul inline,
pire $n$ jusqu'à $2^{22}$. Bibliographie : Garaev math/0505396, arXiv:1302.4170 (lus via ar5iv,
les deux mod $p$). Corrige `STEP7_R2_cancellation.md` (le grand crible n'est pas applicable
directement).*
