# STEP33b — Test empirique des conditions NA : la NA STRICTE échoue (covariances >0), MAIS elle n'est PAS nécessaire. L'extrême est un premier-moment (Markov) ; le résidu est une borne d'énergie additive d'ordre k (déterministe), pas de la NA.

**Date :** 2026-07-02. Script `empirical_NA.py`. Les 3 PDF (Dubhashi-Ranjan, Méliot-Nikeghbali-
Visentin, Untrau) LUS — confirment STEP33bis (probabiliste / sommes complètes / cardinalité fixe).
**Test des conditions NA sur nos fibres DÉTERMINISTES. Résultat : (1) moments factoriels
sous-multinomiaux à TOUS les ordres (TEST 1 ✓) ; (2) mais NA STRICTE ÉCHOUE (covariances >0 à des
décalages arithmétiques, TEST 2). Clarification : la NA n'est PAS nécessaire — l'extrême est un pur
PREMIER MOMENT (Markov), et le résidu est E_k^tot ≤ C^k E_k^null, une énergie additive d'ordre k
DÉTERMINISTE. Le détour probabiliste (NA, mod-Poisson) est superflu.**

## Confirmation des 3 PDF (lus)

- **Untrau 2023** : sous-groupe de cardinalité **FIXE** d (notre ⟨2⟩ : ordre ~p² CROISSANT), sommes
  **COMPLÈTES** (les d éléments), résultat DISTRIBUTIONNEL (régions à hypocycloïdes). Note explicite :
  « our problem will be quite different [de Heilbronn] since ... subgroup of fixed cardinality ». ⟹
  **inapplicable** (mauvais régime + sommes complètes + pas de borne sup).
- **Dubhashi-Ranjan 1998** : « throw m balls into n bins **independently at random** » ⟹ NA des
  occupations, propriété d'une LOI JOINTE aléatoire. Nos fibres déterministes ⟹ **NA indéfinie**.
- **Méliot-Nikeghbali-Visentin 2022** : Chen-Stein d'ordre sup via mod-Poisson, pour variables
  aléatoires (dépendantes) ; exige la convergence mod-Poisson (fct caractéristique) en INPUT ⟹ cadre,
  pas l'input arithmétique.

## TEST 1 — moments factoriels E_k^tot / E_k^null : ≤ 1 à TOUS les ordres

E_k^null = Σ_{p Type B} C(P,k)/(p²)^{k−1} = k-ième moment factoriel EXACT de la multinomiale (modèle
NA de D-R). E_k^tot = Σ_p Σ_r C(N_p(r),k).

| L | k=2 | k=3 | k=4 | k=5 | k=6 |
|---|---|---|---|---|---|
| 80 | 0.91 | 0.91 | 0.40 | 0.00 | 0.00 |
| 120 | 0.95 | 0.70 | 0.35 | 0.00 | 0.00 |
| 160 | 0.95 | 0.86 | 0.67 | 0.00 | 0.00 |

**Tous ≤ 1** : la distribution MARGINALE des tailles de fibres est **sous-multinomiale à tout ordre**.
E_k tombe à 0 dès k=5 (multinomiale prédit encore >0). C'est la condition qui contrôle l'extrême.

## TEST 2 — NA STRICTE ÉCHOUE (covariances positives à des décalages arithmétiques)

Autocovariance c(h) = ⟨N(r)N(r+h)⟩_r − λ² (via FFT), p Type B, L=120 :

| p | λ | Var=c(0) | ⟨c(h≠0)⟩ | max c(h≠0) |
|---|---|---|---|---|
| 211 | 0.166 | 0.165 | −3.7e−6 | **+1.05e−2** |
| 409 | 0.044 | 0.045 | −2.7e−7 | **+2.05e−3** |
| 809 | 0.011 | 0.011 | −1.7e−8 | **+3.6e−4** |

- **Moyenne c(h≠0) < 0** (forcé : Σ_h c(h)=0, c(0)=Var>0). NA-like en agrégat.
- **MAIS max c(h≠0) > 0** (jusqu'à 6 % de Var) : à certains décalages h=2^b−2^c, les fibres r, r+h
  sont POSITIVEMENT corrélées (structure involution/coset, STEP26). ⟹ **les fibres ne sont PAS
  négativement associées au sens strict.** D-R ne s'applique donc PAS, même heuristiquement.

## TEST 3 — sommes exp Poisson-contrôlées

⟨|S_p(t)|²⟩ = L+1 EXACT (Parseval, puissances distinctes) ; ⟨|S_p(t)|⁴⟩ ≈ 2(L+1)² (ratio 0.99–1.16).
Le 4ᵉ moment (= énergie additive des puissances) match le prédit aléatoire à ~10 % ⟹ équidistribution
2ᵉ ordre. (Léger excès pour p~L, quasi-exact pour p grand.)

## La CLARIFICATION : la NA n'est PAS nécessaire

En écrivant la chaîne, l'extrême ne demande **AUCUNE** NA/indépendance — c'est un pur PREMIER MOMENT
(Markov) :
$$\#\{p:M_p\ge k\}\ \le\ \sum_p \#\{r:N_p(r)\ge k\}\ \le\ \sum_p\sum_r C(N_p(r),k)\ =\ E_k^{tot}.$$
(Chaque r avec N_r≥k contribue C(N_r,k)≥1.) Donc **maxM_B = max{k : E_k^tot ≥ 1}**, sans NA.

Et E_k^null décroît PROUVABLEMENT : E_k^null ~ (P^k/k!)Σ_p p^{−(2k−2)} ~ L³/(2^k k!(2k−3)logL),
croise 1 à **k* ~ 3logL/loglogL**. Donc si E_k^tot ≤ C^k E_k^null (TEST 1 ✓, ratios ≤1), alors
E_{k*}^tot < 1 ⟹ **maxM_B < k* = O(logL/loglogL)** ⟹ M″=o(L²) ⟹ #11.

**Le détour probabiliste (NA D-R, mod-Poisson) est SUPERFLU** : Markov suffit pour l'extrême, et le
résidu est un énoncé DÉTERMINISTE d'énergie additive d'ordre k, pas une propriété de dépendance.

## Verdict (format demandé)

- **Ratios E_k^tot/E_k^Poisson (multinomiale), k=2..6 : tous ≤ 1 ?** **OUI** (0.35–0.95), à tout L.
  Marginale sous-multinomiale à tous les ordres.
- **Covariances négatives ou positives ?** **Moyenne <0, mais MAX >0** (décalages arithmétiques
  h=2^b−2^c). **NA STRICTE RÉFUTÉE.** Les fibres ne sont pas négativement associées (structure coset).
- **Sommes exp : moments d'ordre k contrôlés ?** OUI : ⟨|S|²⟩=L+1 exact, ⟨|S|⁴⟩≈2(L+1)² (ratio~1).
- **Conditions NA satisfaites à tous les ordres nécessaires ?** **NON pour la NA stricte** (cov >0) ;
  **OUI pour la seule condition qui compte** (moments factoriels marginaux ≤ multinomiale).
- **CONCLUSION / STATUT :**
  - **CLARIFICATION :** la NA (D-R) n'est PAS nécessaire ni satisfaite (stricte réfutée). L'extrême
    est un PREMIER MOMENT (Markov) : maxM_B=max{k:E_k^tot≥1}.
  - **CONFIRMÉ empiriquement (fort) :** E_k^tot ≤ E_k^null à tout k (2..6), maxM_B<k*~logL/loglogL.
  - **CONDITIONNEL :** M″=o(L²) sous **E_k^tot ≤ C^k E_k^null** (énergie additive d'ordre k
    DÉTERMINISTE, bornée par la multinomiale), pour k jusqu'à ~logL/loglogL.
  - **RESTE OUVERT (résidu, plus propre) :** prouver E_k^tot ≤ C^k E_k^null = les k-énergies additives
    de {2^a+2^b mod p²} ne dépassent pas le hasard. C'est un énoncé d'ÉQUIDISTRIBUTION d'ordre k
    (sommes exp incomplètes lacunaires), NON fourni par les 3 refs (probabilistes/complètes),
    empiriquement dépassé avec marge. **Ni NA ni mod-Poisson requis : Markov + borne d'énergie.**

---
*Script empirical_NA.py. 3 PDF lus : confirment STEP33bis. NA stricte RÉFUTÉE (cov >0 aux décalages
arithmétiques) MAIS non nécessaire : l'extrême est Markov (maxM_B=max{k:E_k^tot≥1}), moments
factoriels sous-multinomiaux à tout ordre (TEST 1). Résidu = E_k^tot ≤ C^k E_k^null (énergie additive
d'ordre k déterministe), = équidistribution d'ordre k, PAS de la NA. PAPER intact.*
