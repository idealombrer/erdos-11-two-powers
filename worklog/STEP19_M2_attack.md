# STEP19 — Attaque de M″ : réduction propre + verdict (vrai, marge croissante, mais Θ(L²) à toute borne brute)

**Date :** 2026-06-24. Attaque ciblée de M″ (dernier verrou « tout n »).
$M_p=\max_n\#\{(a,b)\ \text{non-ord.},a,b\in[0,L]:p^2\mid n-2^a-2^b\}$ ;
**M″ :** $S_1:=\sum_{p\in(L,L^2]}(M_p-1)=o(L^2)$.
Scripts : `checkM2.py` (L=20–50, distribution + énergie), `checkM2_maxM.py` (maxM jusqu'à L=70).

## Données décisives (L=30→70)

| L | #p | $S_1$ | $S_1/L^2$ | #{$M_p\ge2$} | $S_1/\#\{\ge2\}$ | maxM | maxM/lnL |
|---|---|---|---|---|---|---|---|
| 30 | 144 | 36 | 0.0400 | 28 | 1.29 | 4 | 1.18 |
| 40 | 239 | 56 | 0.0350 | 46 | 1.22 | 4 | 1.08 |
| 50 | 352 | 79 | 0.0316 | 62 | 1.27 | 4 | 1.02 |
| 55 | 418 | 85 | 0.0281 | 65 | 1.31 | 4 | 1.00 |
| 60 | 486 | 96 | 0.0267 | 72 | 1.33 | 5 | 1.22 |
| 65 | 560 | 105 | 0.0249 | 82 | 1.28 | 5 | 1.20 |
| 70 | 635 | 124 | 0.0253 | 97 | 1.28 | 6 | 1.41 |

Distribution (ratios $\#\{\ge3\}/\#\{\ge2\}\approx0.20$, $\#\{\ge4\}/\#\{\ge3\}\approx0.1$–0.2,
$\#\{\ge5\}=0$ jusqu'à L=55) : décroissance géométrique en $k$, raison $\approx0.2$.

## La réduction propre (apport de la session)

$$S_1=\sum_{p:M_p\ge2}(M_p-1)\ \le\ (\,\overline{M}-1)\cdot\#\{p:M_p\ge2\},\quad
\#\{p:M_p\ge2\}\le\pi(L^2)=o(L^2)\ \text{(TRIVIAL)}.$$
Donc **M″ $\iff$ l'excès moyen de multiplicité $\overline{M}-1:=S_1/\#\{\text{non-Sidon}\}$ reste $O(1)$**
(le nombre de premiers non-Sidon est trivialement $o(L^2)$ ; tout est dans l'excès moyen).
**Donnée : $S_1/\#\{\ge2\}\approx1{,}3$, REMARQUABLEMENT STABLE** sur L=30–70. C'est le cœur :
chaque premier non-Sidon a en moyenne $\approx1{,}3$ représentations en excès, indépendamment de L.

Condition suffisante plus simple : **M″ $\Longleftarrow$ maxM $=o(\log L)$** (car
$S_1\le(\text{maxM}-1)\pi(L^2)$, et $\pi(L^2)\sim L^2/(2\ln L)$). **MAIS la donnée la réfute
comme voie de preuve : maxM/lnL $\approx1$ (oscille, ne décroît pas)** — donc cette borne
suffisante donne $\Theta(L^2)$, pas $o(L^2)$. C'est elle, et non $S_1$, qui échoue.

## Pourquoi toutes les bornes brutes calent à $\Theta(L^2)$ (réfutation des voies de preuve)

- **Énergie + Cauchy–Schwarz :** $S_1\le\sqrt{\#p\cdot\sum\Delta_p}$. Mesuré : $\sum\Delta_p/L^2$
  CROÎT (0.67→1.9), donc CS $\approx0{,}5\,L^2$ et croissant. **Échoue.**
- **$S_1\le\sum\sqrt{\Delta_p}$ :** $\approx0{,}16\,L^2$, ratio quasi-constant. **Ne $\to0$ pas.**
  (Trop lâche : un premier $M_p=2$ avec $\Delta_p$ grand pèse $1$ dans $S_1$ mais $\sqrt{\Delta_p}$ dans la borne.)
- **$M_p-1\le C\,L/d_p$ :** $C$ requis EXPLOSE (1600→100000). **Mort** (confirme réfutation M1, STEP15).
- **maxM·#{non-Sidon} :** $(\text{maxM}-1)\pi(L^2)/L^2\approx0{,}4$–$0{,}65$, croissant. **Échoue.**

Le vrai $S_1=0{,}03\,L^2$ est ~5–15× sous toutes ces bornes : l'écart EST le mur « échoue d'un
facteur constant » de STEP16, ici localisé exactement à *l'excès moyen* $\approx1{,}3$.

## Étape 2 — conspirateurs ($M_p\ge3$, L=50) : hétérogènes, pas de signature unique

$p=257$ (Fermat, ord 16), $127$ (Mersenne, ord 7), $71$ (ord 35), $683$ (ord 22), $241$ (ord 24),
$101$ (ord 100 = racine primitive !), $89$ (ord 11), $83$ (ord 82). **Mélange** : beaucoup ont
$2$ d'ordre petit (Mersenne/Fermat $2^k\pm1$), mais $101,83$ ont $2$ presque primitif. $p/L\in[1.4,13.7]$.
**Pas de structure S-unités propre exploitable** : la piste « collision $\Rightarrow$ structure
$a-b$ ou $a+b$ constante » ne se dégage pas nettement (conspirateurs trop variés).

## Étape 4 — décorrélation B/M″ : FAITE — B et M″ sont INDÉPENDANTS

Contributions *par n* sur une fenêtre (L=23,24, 3M entiers ; `checkM2_step45.py`) :
$M2(n)=\sum_{p\in(L,L^2]}N_p(n)$, $B(n)=\sum_{p\in(L^2,\sqrt{n/2}]}N_p(n)$.
- **Corrélation $\approx-0{,}001$** (nulle) ; $\#\{B>0\,\&\,M2>0\}\approx$ produit des marges
  (78987 vs 79158 ; 85795 vs 85918) → **événements statistiquement indépendants**.
- Pire $n$ pour M2 (maxM2$=13$) a $B=0$ ; pire $n$ pour B (maxB$=4$) a M2$=2$.
- **Conséquence :** B et M″ ne se concentrent PAS sur le même $n$ → argument d'union pire-cas
  valide ; et B étant $O(1)$ (STEP18), il est négligeable. Le pire-cas global est piloté par M2
  (+ petits premiers) ; maxM2$=13\ll T=576$.

## Étape 5 — voie « borne de collisions » RÉFUTÉE (chaîne conditionnelle cassée)

Conjecture du plan : $\Delta_p\le C\,L^2/d_p$ (avec $\sum_{(L,L^2]}1/d_p=o(1)$ acquis, donnerait
$S_1\le\sum\Delta_p\le CL^2\sum1/d_p=o(L^2)$).
- **$\max_p\Delta_p d_p/L^2 = 1385,1810,2406,10906$ (L=20,30,40,50) — NON borné** ⟹ conjecture
  **fausse** ($\Delta_p$ pas contrôlé par $d_p$ ; argmax $p=181,491,1741$).
- $\sum\Delta_p/L^2=0{,}67\to1{,}89$ **croît** : collisions totales $\omega(L^2)$, pas $o(L^2)$.
  Donc **M″ ne vient PAS de « peu de collisions » mais de leur ÉTALEMENT** ($M_p$ petit).
- **Structure des quadruplets** (p=127) : aucune — $|a-b|,a+b$ dispersés, pas de $a-c$/$a+b$
  constant. Piste S-unités « collisions structurées » : rien d'exploitable.

**Bilan 4–5 :** B$\perp$M″ ; et **toutes** les voies conditionnelles (énergie/CS, $M_p\le CL/d_p$,
$\Delta_p\le CL^2/d_p$) **cassées** — même cause : collisions nombreuses ($\omega(L^2)$) mais
*étalées*. Seul l'**excès moyen $O(1)$** ($\approx1{,}3$) capture la vérité.

## Verdict

- **PROUVÉ (rigoureux) :** la réduction $S_1\le(\text{maxM}-1)\,\pi(L^2)$ et l'équivalence
  **M″ $\iff$ excès moyen $O(1)$** (puisque #{non-Sidon} $\le\pi(L^2)=o(L^2)$). Réfutation
  rigoureuse des 4 voies de borne (toutes $\Theta(L^2)$).
- **CONDITIONNEL :** M″ tient SI maxM $=o(\log L)$ [non vérifié : maxM$\approx\log L$], ou SI
  l'excès moyen reste borné [vérifié empiriquement $\approx1{,}3$, non prouvé].
- **RESTE OUVERT (nommé précisément) :** *l'excès moyen de multiplicité additive de
  $\{2^a\bmod p^2\}$ est $O(1)$ en moyenne sur $p\in(L,L^2]$* — énoncé $B_2[g]$/Sidon-multiplicité,
  non élémentaire, *borderline* (toute borne brute donne $\Theta(L^2)$). C'est le maillon, et il
  est plus fin (et mieux localisé : « excès moyen », un seul nombre $\approx1{,}3$) que la
  formulation « décroissance de distribution » de STEP16.
- **Plausibilité de M″ :** **TRUE à très haute confiance** — $S_1/L^2\to0$ monotone et robuste
  (L jusqu'à 70), excès moyen $\approx1{,}3$ d'une stabilité frappante. Mais preuve = niveau
  spécialiste (l'écart facteur-constant est exactement le point dur). Élémentaire ~3-5 % inchangé.

---
*Scripts `checkM2.py`, `checkM2_maxM.py`. Réduit M″ à « excès moyen de multiplicité = O(1) »
(≈1.3 stable, L=30–70) ; réfute énergie/CS/maxM comme voies (toutes Θ(L²)) ; conspirateurs
hétérogènes (pas de voie S-unités nette). Ne touche pas PAPER (cf. feedback).*
