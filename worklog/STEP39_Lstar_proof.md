# STEP39 — Prouver L* : argument proposé RÉFUTÉ (vacue), L* ≡ E₂^tot (pas plus facile), partiel O(L⁴) conditionnel. RESTE OUVERT.

**Date :** 2026-07-03. Script `lstar.py`. Tentative de preuve de
L* : Σ_{N=2^a+2^b−2^c−2^d≠0, a,b,c,d∈[0,L]} #{p∈(L,L²]:p²|N} = O(L³/log L).
**Résultat : l'argument proposé (p²>|N|, ÉTAPE 3-4) est VACUE pour la plage ; L* est EXACTEMENT
E₂^tot (la variance TB), pas un sous-problème plus facile ; Cauchy-Schwarz donne une borne partielle
O(L⁴) mais conditionnelle à ω₂(N)≤2 (empirique) — sinon le trivial O(L⁵/logL). La cible O(L³/logL)
exige le grand crible à modules carrés (STEP38). RESTE OUVERT.**

## PART 1 — L'argument « p²>|N| ⟹ 0 solution » est VACUE pour (L,L²]

|N|max = 2^{L+1}, donc p²|N (N≠0) impossible seulement si p²>2^{L+1}, i.e. p>2^{(L+1)/2}. Or :

| L | 16 | 20 | 24 | 28 | 32 | 40 |
|---|---|---|---|---|---|---|
| L² | 256 | 400 | 576 | 784 | 1024 | 1600 |
| 2^{(L+1)/2} | 362 | 1448 | 5793 | 23170 | 92682 | 1.5e6 |
| #p∈(L,L²] avec p>2^{(L+1)/2} | **0** | **0** | **0** | **0** | **0** | **0** |

**L² < 2^{(L+1)/2} pour tout L≥16** ⟹ toute la plage (L,L²] est SOUS le seuil ⟹ p²≤L⁴ ≪ 2^{L+1}=|N|max
partout ⟹ l'argument ne tue **AUCUN** premier de la plage. (C'est la faille de STEP37 Maillon 2 : la
même arithmétique. L'argument ne s'applique qu'au-delà de 2^{L/2}, i.e. AU-DESSUS de wall B, hors sujet.)
Vérifié : Δ_p>0 pour p Type B dans la plage (p=211 : Δ=1). « 0 solution non triviale » RÉFUTÉ.

## PART 2 — L* est EXACTEMENT E₂^tot (le prompt le note « circulaire » à l'ÉTAPE 2)

L* = Σ_{quad, N≠0} ω₂^{(L)}(N) = Σ_{p∈(L,L²]} #{quad non triv. : p²|N} = Σ_p Δ_p = **E₂^tot**.
Ce n'est PAS un sous-problème plus accessible : c'est la variance TB elle-même. Toute preuve de L*
EST une preuve de la variance TB. Le per-prime Δ_p ~ L² (typique) ⟹ Σ_p = O(L⁴/logL) (STEP35) ; le
vrai O(L³/logL) exige l'averaging sur p (grand crible), aucun raccourci élémentaire.

## PART 3-4 — Borne partielle Cauchy-Schwarz : O(L⁴), conditionnelle à ω₂≤2

E(S) = énergie additive du sumset S={2^i+2^j} : E(S)/|S|² = 1.94,1.90,1.85,1.82,1.79 (L=16→32),
**borné** ⟹ **E(S)=O(|S|²)=O(L⁴)** (S presque-Sidon, énergie ~1.8× le plancher). Alors
$$L^\ast=\sum_N r(N)\,\omega_2(N)\ \le\ \Bigl(\sum_N r(N)^2\Bigr)^{1/2}\Bigl(\sum_{N\,\mathrm{repr}}\omega_2(N)^2\Bigr)^{1/2}
=\sqrt{E(S)}\cdot\sqrt{\textstyle\sum_{\mathrm{repr}}\omega_2^2}.$$
- Avec **ω₂(N)≤2** (empirique, STEP22 ; les ω₂=2 sont des carrés de Mersenne (2^k−1)²) :
  Σ_repr ω₂² ≤ 4·#{N repr distincts} ≤ 4|S−S| = O(L⁴) ⟹ **L* ≤ √(L⁴)·√(L⁴) = O(L⁴)** [conditionnel].
- Avec la borne **PROUVÉE** ω₂(N) ≤ log|N|/(2logL) = O(L/logL) : Σ_repr ω₂² ≤ (L/logL)²·O(L⁴) ⟹
  L* ≤ √(L⁴)·√(L⁶/log²L) = **O(L⁵/logL)** = TRIVIAL. Le gain O(L⁴) exige ω₂≤2, NON prouvé.

Bilan des bornes (facteurs) : trivial L⁵/logL ; CS+ω₂≤2 : L⁴ ; **cible L³/logL** (facteur L manquant).
Le crible du carré / grand crible à modules carrés (STEP38) est nécessaire pour le dernier facteur L
(= l'averaging sur p, que ni p²>|N| ni Cauchy-Schwarz per-N ne fournissent).

## Pourquoi Cauchy-Schwarz plafonne à L⁴ (structurel)

CS remplace Σ r(N)ω₂(N) par √(Σr²)·√(Σω₂²). Σr²=E(S) est presque optimal (≈2|S|²), mais Σω₂² compte
TOUS les N représentables (≈|S|²=L⁴) sans exploiter que RARE parmi eux a un facteur carré. La perte
est exactement le facteur « densité de diviseurs carrés » ~1/(L logL) que seul un crible (pas CS)
récupère. CS voit r et ω₂ séparément ; le grand crible les corrèle (les N à facteur carré sont peu
nombreux ET ont r modéré). ⟹ CS ne peut PAS atteindre L³/logL. Même clivage moyenne-vs-structure.

## Verdict (format demandé)

- **Borne triviale O(L⁵/logL) ?** OUI confirmée (ÉTAPE 1 du plan correcte).
- **Argument Sidon-ℤ + p>2^{L/2} ⟹ E₂^pow=0 ?** **NON — VACUE** : aucun p∈(L,L²] ne dépasse 2^{(L+1)/2}
  (L²<2^{(L+1)/2}) ; collisions non triviales existent (Δ_p>0). Réfuté.
- **Borne sur Σ E₂^pow/p² = O(L³/logL) ?** **Non prouvée.** CS donne O(L⁴) conditionnel à ω₂≤2 ;
  inconditionnel = trivial O(L⁵/logL). Cible non atteinte.
- **L* prouvé ?** **NON.** L* ≡ E₂^tot (variance TB), pas plus facile. Partiel O(L⁴) [conditionnel ω₂≤2].
- **STATUT : RESTE OUVERT.** L'argument élémentaire proposé échoue (p²>|N| vacue) ; L* n'est pas un
  raccourci ; le vrai contenu est le grand crible à modules carrés (STEP38), inchangé. Deux acquis
  honnêtes : (i) réfutation propre de l'argument p²>|N| (arithmétique : L²<2^{L/2}) ; (ii) borne
  partielle O(L⁴) via CS + E(S)=O(L⁴) + ω₂≤2 (améliore le trivial d'un facteur L·logL, reste à un
  facteur L de la cible).

---
*Script lstar.py. Argument p²>|N| VACUE (plage entière sous 2^{L/2}) ; L*≡E₂^tot ; CS+ω₂≤2 ⟹ O(L⁴)
(vs trivial L⁵/logL, cible L³/logL) ; le facteur L final = grand crible à modules carrés (STEP38),
non fourni par p²>|N| ni CS. RESTE OUVERT. PAPER/Lean non touchés.*
