# STEP41 — Tests ChatGPT (loi des outliers, régression, excès absolu) : CORRIGE STEP40 sur trois points. Vraie variable = congruence p mod 8/16, PAS l'index. Décomposition diag+struct+err motivée.

**Date :** 2026-07-04. Scripts `regression.py`, vtest. Tests proposés par ChatGPT sur les outliers de
STEP40. **Résultat : STEP40 était FAUX sur trois points, corrigés ici honnêtement. (1) Les outliers ne
sont pas ~20 mais une FRACTION POSITIVE (~1.5% des Type B ~ L²/logL). (2) Ils contribuent ~10% à E₂^tot,
pas <1%. (3) La vraie variable n'est PAS le petit index (corr≈0) mais une CONGRUENCE p mod 8/16
(p≡1 mod 16 : ρ2=4.2, 4× la moyenne). ChatGPT avait raison de pousser ; sa régression a trouvé le vrai
signal. Le grand crible n'est PAS l'unique voie (concédé) ; la décomposition E_k=diag+struct+err devient
concrète (struct ≈ congruence explicite).**

## CORRECTION 1 — Loi du nombre d'outliers : fraction positive ~L²/logL (pas ~20)

| L | #Type B | #(Δ>0) | #(ρ>3) | #(ρ>10) | #(ρ>30) | #(ρ>10)/#TB |
|---|---|---|---|---|---|---|
| 60 | 450 | 47 | 13 | 6 | 3 | 1.3% |
| 100 | 1143 | 38→118* | 38 | 17 | 5 | 1.5% |
| 140 | 2113 | 214 | 66 | 34 | 15 | 1.6% |

**#(ρ>10) ~ 1.5% de #Type B ~ L²/logL** : fraction CONSTANTE, croît, PAS O(1). Mon « une vingtaine »
(STEP40) sous-comptait. #(Δ>0) (non-Sidon) = 47,118,214 ~ L^{1.8}, croît. Les outliers ne sont pas
« rarissimes extractibles » : ils sont trop nombreux pour être O(1) exceptions.

## CORRECTION 2 — Contribution ~10% (pas <1%) ; ratio partiellement artefact (ChatGPT raison)

| L | max Δ_p | Δ au max-ρ | null au max-ρ | max(Δ−null) | ΣΔ_outliers/E₂^tot |
|---|---|---|---|---|---|
| 60 | 459 | 12 | 0.36 | 175 | **6.8%** |
| 100 | 1417 | 84 | 0.19 | 424 | **9.6%** |
| 140 | 2139 | 244 | 0.72 | 931 | **9.7%** |

- **ΣΔ_outliers (ρ>10) / E₂^tot ≈ 10%**, pas <1% (STEP40 faux). Non négligeable.
- **ChatGPT a raison sur l'artefact** : le premier à max-ρ a Δ modeste (12-244) avec null minuscule
  (0.2-0.7) ⟹ ratio gonflé. L'excès ABSOLU (Δ−null) est plus modéré. MAIS séparément max Δ_p = 459→2139
  (genuinement gros ~0.1·L²) — deux populations : (a) grand-ratio-Δ-modeste (artefact, p grand),
  (b) grand-Δ-réel (p petit, structure).

## CORRECTION 3 — La vraie variable : CONGRUENCE p mod 8/16, PAS le petit index

Régression ρ2 vs candidats (L=100, 1143 Type B) :

| variable | corr(ρ2, ·) |
|---|---|
| 1/e_p | −0.014 |
| **index = (p−1)/e_p** | **−0.011 (≈0 !)** |
| log(index) | +0.000 |
| p | +0.008 |
| q_p (quotient de Fermat) | +0.042 |

**corr(ρ2, index) ≈ 0 ⟹ mon « outliers = petit index » (STEP40) est RÉFUTÉ.** Le vrai signal :
- **ρ2 moyen par p mod 8** : 1→**2.2**, 3→1.0, 5→0.6, 7→0.5.
- **ρ2 moyen par p mod 16** : 1→**4.2**, 11→1.7, autres <1.
⟹ **p≡1 mod 16 a ρ2 = 4× la moyenne.** C'est une condition de CONGRUENCE (liée à 2 comme résidu de
puissance de 2), EXPLICITE, pas l'index. (Mécanisme exact non-monotone : ρ2 par v₂(p−1) pique à
v₂=4 (8.1) mais rebaisse à v₂≥5 — structuré mais pas un simple « 2 est résidu 2^k-ième ».)

## Concession logique (ChatGPT a raison) : le grand crible n'est PAS l'unique voie

STEP40 concluait « per-prime échoue ⟹ grand crible incontournable ». **Saut logique.** « Pas de borne
uniforme per-prime » (vrai) ⇏ « seul le grand crible marche ». Autres voies classiques : dispersion,
moyennes pondérées, et surtout la **décomposition E_k = diag + struct + err** (philosophie de ChatGPT).

## Le gain stratégique : décomposition diag + struct + err devient CONCRÈTE

La régression rend la décomposition de ChatGPT exploitable :
- **E₂^diag** (terme principal, ~90%) : la masse des premiers Sidon/génériques, = |S|²Σ1/p²~L³/logL.
- **E₂^struct** (~10%) : les premiers à ρ2 élevé, gouvernés par des CONGRUENCES EXPLICITES (p mod 8/16,
  et raffinements mod 2^k). Une famille explicite ⟹ potentiellement SOMMABLE en forme fermée (somme
  sur classes de congruence pondérée par la structure de résidu de puissance).
- **E₂^err** (le reste générique − diagonale) : petit en moyenne, = l'input d'équidistribution, mais
  ALLÉGÉ (la partie structurée retirée).
C'est plus prometteur qu'attaquer le grand crible frontalement : on isole d'abord le structuré explicite.

## Verdict (format demandé)

- **Loi des outliers ?** **~1.5% des Type B ~ L²/logL** (fraction positive, croît). Pas O(1).
- **Δ_p − E[Δ_p] : artefact de normalisation ?** PARTIELLEMENT (les max-ρ ont Δ modeste, null minuscule) ;
  mais excès absolu réel (max Δ~0.1L²) et contribution ~10%. Deux populations.
- **Petit index = vraie variable ?** **NON (corr≈0).** Vraie variable = **congruence p mod 8/16**
  (p≡1 mod 16 : ρ2 4× la moyenne). Découverte de la régression ChatGPT.
- **Grand crible incontournable ?** **NON — concédé.** Décomposition diag+struct+err est une voie
  alternative motivée, désormais concrète (struct = congruence explicite).
- **STATUT : RESTE OUVERT, recadré.** STEP40 corrigé (outliers ~L²/logL, ~10%, congruence pas index).
  Le comportement générique est proche du hasard (ChatGPT), le difficile est localisé mais sur des
  CONGRUENCES explicites (extractibles ?), pas sur l'index. Prochaine piste : sommer E₂^struct en forme
  fermée sur p mod 2^k, réduire E₂ à E₂^err (équidistribution allégée).

---
*Scripts regression.py, vtest. CORRIGE STEP40 : outliers ~1.5% de #TypeB~L²/logL (pas ~20), ~10% de
E₂ (pas <1%), vraie variable = p mod 8/16 (corr index≈0, RÉFUTE petit index). Grand crible pas unique
voie (concédé). Décomposition diag+struct+err concrète (struct=congruence explicite). PAPER/Lean non touchés.*
