# STEP37 — Trois maillons : deux cibles réfutées (κ≤2, B=O(1)), (TA) relâché à o(log L), consolidation en UN cœur analytique.

**Date :** 2026-07-03. Script `three_links.py`. Attaque des trois hypothèses (TA),(WB),(TB) du théorème
conditionnel STEP36. **Résultat : aucun ne se ferme, mais (1) « κ_p≤2 » (TA) et « max B(n)=O(1) » (WB)
sont RÉFUTÉS comme trop forts ; (2) (TA) se relâche proprement à κ_p=o(log L) [suffisant, robuste] ;
(3) les trois maillons se CONSOLIDENT en un seul cœur : la distribution de multiplicité de
{2^l+2^m mod p²} (moments factoriels / grand crible), à trois échelles de premiers.**

## MAILLON 1 (TA) — « κ_p≤2 » RÉFUTÉ ; (TA) se relâche à κ_p = o(log L)

max κ_p sur Type A (e_p≤L) : **4, 4, 4, 6** pour L=60,100,160,200 — CROÎT, pas ≤2. Premiers Type A à
κ_p≥3 : p=61 (e=60, κ=4), 101 (e=100, κ=4), 233 (e=29, κ=5), etc. Ce sont surtout les premiers
**frontière** (e_p≈L, quasi racine primitive) : ils sont Poisson-like, κ_p = extrême de Poisson.

**Mais « ≤2 » n'est PAS nécessaire.** Il suffit que Σ_A M_p = o(L²), et
$$\sum_{\substack{p\in(L,L^2]\\ e_p\le L}}M_p \le (\max_A\kappa_p)\Bigl(\sum_p\lfloor L/e_p\rfloor+\pi(L^2)\Bigr)
\le (\max_A\kappa_p)\cdot O\!\Bigl(\tfrac{L^2}{\log L}\Bigr).$$
Comme Σ⌊L/e⌋=O(L²/logL) a déjà le gain 1/logL, il suffit de **max_A κ_p = o(log L)** ⟹ Σ_A M_p =
o(logL)·O(L²/logL) = o(L²). Empiriquement κ_p ~ logL/loglogL = o(logL) (extrême de Poisson). **Donc
(TA) se relâche de « κ_p≤κ borné » à « κ_p = o(log L) »** — plus faible, correct, empiriquement robuste.
(κ_p≤2 ne vaut que pour l'ordre GÉNUINEMENT petit e_p≪L, ex. p=8191 e=13 ; la frontière e_p≈L est Poisson.)

## MAILLON 2 (WB) — « max B(n)=O(1) » RÉFUTÉ ; c'est ~L/logL, mais o(L²) tient

L'argument du plan « p>2^{L/2} ⟹ p²>|N| ⟹ 1 paire/fibre » est **FAUX** : la plage est
(L², √(n/2)] = (L², ~2^{L/2}], donc p²≤2^L, alors que |N|max=4·2^L > 2^L. **p²<|N| est possible partout**.

max B(n) (échantillon 1500) : 0, 4, 2, 4 (L=16,18,20,22) ; moyenne →0 (E[B]~1/(8logL)). Cohérent avec
l'**extrême de Poisson 0.69 L/logL ~ 4-5** (pas O(1)). Donc **max B(n) ~ L/logL, pas O(1)** — mais
L/logL = o(L²), donc **(WB) tient** (avec marge). C'est une instance **TB-type** (moment factoriel /
grand crible) pour p>L² : les premiers y sont plus GRANDS ⟹ collisions plus rares ⟹ extrême plus petit
⟹ instance plus FAIBLE que (TB). Trivial bound O(L³/logL) toujours trop grand ⟹ preuve = même averaging.

## MAILLON 3 (TB) — Cauchy-Schwarz per-prime insuffisant (facteur L)

CS : E₂ ≤ √((L+1)·E₃^pow) par premier. Mesuré (E₃^pow=Σ|S|⁶/p²) : CS/(L+1)² = 2.5–3.5 ⟹ E₂ ≤ ~3(L+1)²
par premier. Or E₂^pow réel ~ 2(L+1)² (inclut la diagonale triviale). Sommé sur π(L²) premiers :
~(L+1)²·L²/logL = **O(L⁴/logL)**, facteur L trop grand (besoin L³/logL). **Le per-prime NE gagne PAS
l'averaging sur p** (même mur STEP35). De plus CS borne E₂^pow (avec diagonale), pas le Δ_p non-trivial.
⟹ Maillon 3 ne ferme pas (TB).

## CONSOLIDATION : les trois maillons = UN cœur analytique

| Maillon | échelle premiers | ce qu'il demande | nature |
|---|---|---|---|
| (TA) e_p petit | p∈(L,L²], e_p≪L | κ_p=o(logL) [reste : rigidité involution] | multiplicité (classes) |
| (TA) frontière + (TB) | p∈(L,L²], e_p≳L | E_k^tot ≤ C^k E_k^null | moments factoriels / grand crible |
| (WB) | p∈(L²,√(n/2)] | E_k grand crible (p>L², plus faible) | moments factoriels / grand crible |

**Les trois sont la MÊME question** — la distribution de multiplicité de {2^l+2^m mod p²} (moments
factoriels ≤ Poisson / grand crible sur les sommes exponentielles incomplètes lacunaires), à trois
échelles de p. (TB) est l'instance centrale (dominante) ; (WB) est plus faible (p plus grand) ; (TA)
frontière s'y rattache ; seul (TA) à ordre génuinement petit est distinct (rigidité, κ_p≤2, prouvable
via involution — mais rare et contrôlé par Σ⌊L/e⌋). **Il n'y a donc pas 3 murs mais 1**, plus une
rigidité mineure.

## Verdict par maillon (format demandé)

- **(TA) κ_p≤2 :** **RÉFUTÉ** (κ_p atteint 6, croît). Mais **(TA) relâché à κ_p=o(log L) : tient**
  empiriquement (extrême Poisson) et **suffit** (Σ_A M_p=o(L²)). Reste à prouver κ_p=o(logL) = énoncé
  de multiplicité, plus faible que (TB).
- **(WB) max B(n)=O(1) :** **RÉFUTÉ** (~L/logL, extrême Poisson ; argument p²>|N| faux). Mais o(L²)
  (ce dont on a besoin) **tient** avec marge ; = instance grand-crible plus faible que (TB).
- **(TB) Cauchy-Schwarz :** **N'aide PAS** (per-prime O(L⁴/logL), facteur L ; averaging essentiel).
  (TB) inchangé = grand crible / crible du carré (STEP34-35).
- **STATUT GLOBAL : CONDITIONNEL, consolidé.** Aucun maillon ne se ferme, mais les trois se ramènent
  à UN cœur (moments factoriels / grand crible sur {2^l+2^m mod p²}) + une rigidité mineure (involution).
  Deux cibles trop optimistes réfutées (κ≤2, B=O(1)) ; (TA) corrigé en o(logL). PAS trois murs, un seul.

## Correction à porter à PAPER.tex

- **(TA)** : remplacer « il existe κ absolu avec κ_p≤κ » par « κ_p = o(log L) » (hypothèse correcte).
  Ajuster la preuve : Σ_A M_p ≤ (max κ_p)(Σ⌊L/e⌋+π(L²)) = o(logL)·O(L²/logL) = o(L²).
- Remarque : κ_p≤2 seulement pour e_p≪L ; la frontière e_p≈L est Poisson (κ_p ~ extrême).
- Remarque de consolidation : (WB) est une instance grand-crible plus faible que (TB) (p>L²) ; les
  hypothèses analytiques (TB) et (WB) sont de même nature.
