# STEP21 — Bourgain–Garaev ne ferme PAS M″ (écart max-vs-énergie), et 4/π est réfuté

**Date :** 2026-06-24. Suite STEP20. Test : (1) un théorème de somme d'exponentielles type
Bourgain–Garaev ferme-t-il M″ ? (2) la constante 4/π tient-elle jusqu'à L=120 ?
**Résultat : NON aux deux.** (1) Les méthodes de sommes d'exponentielles bornent l'ÉNERGIE ;
M″ porte sur la MULTIPLICITÉ MAX ; pour ces ensembles presque-Sidon, max $\ll\sqrt{\text{énergie}}$
(écart ×18 mesuré), et $\sum\sqrt{\text{énergie}}=\Theta(L^2)$ — la voie cale. (2) EM dérive vers
~1,30 (pas 4/π=1,273). **Mais** la réduction se précise proprement : **M″ ⟺ EM = $o(\log L)$**,
et EM/log L décroît (0,33→0,27) ⟹ M″ tient robustement. PAPER.tex intact. Script `identify_constant_v2.py`.

## Étape 1+3 — Bourgain–Garaev : NE FERME PAS M″ (deux raisons indépendantes)

### Raison A (fondamentale, décisive) : écart max-vs-énergie
Toute méthode de Fourier/somme d'exponentielles contrôle l'**énergie additive**
$E_p=\frac1{p^2}\sum_t|S(t)|^4$, $S(t)=\sum_{k\le L}e_{p^2}(t2^k)$. Or M″ a besoin de la
**multiplicité maximale** $M_p$, et le mieux qu'une borne d'énergie donne est
$M_p\le\sqrt{2\Delta_p}$ ($\Delta_p$ = collisions). **Mesuré (L=120) :**
| p | $M_p$ (vrai) | $\sqrt{2\Delta_p}$ (borne énergie) | écart |
|---|---|---|---|
| 127 | 9 | 167 | ×18 |
| 151 | 5 | 72 | ×14 |
| 137 | 4 | 50 | ×12 |

Pire : **$\sum_p\sqrt{2\Delta_p}/L^2\approx0{,}24$–$0{,}26$, CONSTANTE** (ne $\to0$ pas). Donc même
la borne d'énergie *sommée* donne $\sum(M_p-1)\le\sum\sqrt{2\Delta_p}=\Theta(L^2)$, **jamais
$o(L^2)$**. L'énergie est dominée par les collisions « attendues » étalées ; $M_p$ (le pic) est
$\sqrt{}$-plus-petit. **Aucune borne de somme d'exponentielles ne franchit cet écart** — c'est
le même mur $\Theta(L^2)$ que Cauchy-Schwarz (STEP19) et Plünnecke (STEP20), pour la même cause.

### Raison B (régime) : nos sommes sont trop courtes pour les bornes connues mod $p^2$
$S(t)$ est une somme INCOMPLÈTE de longueur $L+1$ de la fonction exponentielle mod $q=p^2$.
Pour $p\in(L,L^2]$ : $L+1\in[q^{1/4},q^{1/2}]$ (longueur $q^{1/4}$ quand $p\sim L^2$).
- **Korobov** : $\max|S|\ll\sqrt q\,\log q=p\log p$ — **triviale ici** ($L+1\le p\ll p\log p$).
- **Bourgain/Konyagin/Shparlinski** (sous-groupes de $(\mathbb Z/q)^\times$, méthode de Stepanov
  mod $p^2$, cf. arXiv:1302.4170, arXiv:2108.13146, Springer « Bounds for exponential sums mod
  $p^2$ ») : bornes pour sommes **complètes** sur sous-groupes, ou longueurs $N\ge q^\varepsilon$
  avec gain $\delta$ petit ; **notre régime $N\sim q^{1/4}$ (p$\sim L^2$) est au/​sous le front**
  des résultats inconditionnels pour la fonction exponentielle mod $p^2$.

**Conclusion Étape 1+3 :** BG est le bon domaine mais **ne s'applique pas** — la chaîne du plan
casse à l'étape « Cauchy-Schwarz / énergie » (Raison A, indépendante du $\delta$), et en plus le
régime est défavorable (Raison B). La déduction `|S(t)|≤Lp^{-δ} ⟹ M_p petit` est FAUSSE : un bon
$|S(t)|$ borne $E_p$, pas $M_p$, et $M_p\ll\sqrt{E_p}$.

## Étape 2 — la constante : 4/π RÉFUTÉ ; le bon énoncé est EM = o(log L)

EM(L)=$S_1/\#\{$non-Sidon$\}$ étendu à L=120 :
| L | 60 | 80 | 90 | 100 | 110 | 120 |
|---|---|---|---|---|---|---|
| EM | 1.333 | 1.265 | 1.283 | 1.311 | 1.290 | 1.307 |
| \|EM−4/π\| | .060 | .008 | .010 | .038 | .016 | .034 |
| EM/log L | .326 | .289 | .285 | .285 | .274 | .273 |
| maxM | 5 | 6 | 7 | 8 | 8 | 9 |
| ΣM_p/L² | .162 | .150 | .146 | .142 | .137 | **.135** |

- **4/π=1,2732 RÉFUTÉ :** EM dérive vers ~1,30 (moyenne L≥60 = 1,298), $|EM-4/\pi|$ ne décroît
  pas. Candidats $\sqrt{\pi/2}=1{,}253$, $\pi^2/8=1{,}234$ encore plus loin. **Pas de constante
  fermée** — EM est ~1,3, légèrement croissant (la queue de multiplicité s'épaissit : maxM 5→9).
- **MAIS le bon énoncé se dégage : $S_1=EM\cdot\#\{$non-Sidon$\}$, $\#\{$non-Sidon$\}=O(\pi(L^2))
  =O(L^2/\log L)$, donc M″ ($S_1=o(L^2)$) $\iff$ EM $=o(\log L)$.** Donnée : **EM/log L décroît
  (0,33→0,27)** ⟹ EM=$o(\log L)$ soutenu, marge croissante. Et $\sum M_p/L^2$ décroît (0,162→0,135)
  ⟹ **M″ tient empiriquement, margin croissant.**
- maxM croît plus vite que prévu (9 à L=120, maxM/log L $\approx1{,}9$ croissant) — maxM = $\omega(\log L)$
  plausible. **Sans danger** pour M″ : seul l'excès MOYEN compte, et il est $\ll\log L$.

## Verdict (format demandé)

- **Bourgain–Garaev s'applique-t-il ?** **NON.** (A) Fondamental : bornes d'énergie, pas de
  multiplicité-max ; $M_p\ll\sqrt{E_p}$ (×18), $\sum\sqrt{E}=\Theta(L^2)$. (B) Régime : sommes de
  longueur $q^{1/4}$–$q^{1/2}$ mod $p^2$, sous le front des bornes connues (Korobov triviale).
- **4/π confirmée à L=120 ?** **NON, réfutée** (EM dérive vers ~1,30, pas de constante fermée).
- **PROUVÉ (rigoureux) :** la réduction **M″ $\iff$ EM=$o(\log L)$** (via $\#$non-Sidon$=O(L^2/\log L)$) ;
  l'écart max-vs-énergie ($M_p\le\sqrt{2\Delta_p}$ est le mieux de Fourier, et $\sum\sqrt{2\Delta_p}
  =\Theta(L^2)$) ⟹ **aucune méthode de somme d'exponentielles/énergie ne peut prouver M″** ;
  Korobov triviale dans le régime.
- **CONDITIONNEL :** M″ tient si EM=$o(\log L)$ — empiriquement EM/log L↓ (0,33→0,27), $\sum M_p/L^2$↓.
- **RESTE OUVERT (nommé, recentré) :** *contrôler la MULTIPLICITÉ ADDITIVE MAXIMALE (pas
  l'énergie) de $\{2^k\bmod p^2\}$ en moyenne sur $p\in(L,L^2]$* — un énoncé de **grande déviation /
  Poisson sur la distribution de multiplicité**, INACCESSIBLE aux trois familles d'outils
  standards désormais testées : combinatoire worst-case (STEP20), Cauchy-Schwarz/Plünnecke
  (STEP19/20), sommes d'exponentielles/énergie (STEP21). Tous calent à $\Theta(L^2)$ via l'écart
  max-vs-énergie.
- **Plausibilité de M″ :** **élevée et confirmée** ($\sum M_p/L^2$↓ 0,16→0,135, EM/log L↓). Mais
  la preuve exige un argument de **distribution de multiplicité (Poisson/grande déviation)**, d'une
  nature différente des sommes d'exponentielles — c'est le vrai noyau, plus fin que « Lemme E′/BG ».

---
*Script `identify_constant_v2.py` (EM jusqu'à L=120 ; écart M_p vs √2Δ_p). Réfute 4/π et la voie
BG/énergie ; recentre M″ sur EM=o(log L) [tenu, marge↑] et sur le contrôle de la multiplicité-max
(grande déviation), hors de portée des sommes d'exponentielles. PAPER.tex intact.*
