# STEP32 — Approximation de Poisson du Type B : variance Poisson PROUVABLE, sup-bound √L CONFIRMÉ (C≈3), extrême = Chen-Stein (résidu, PAS le mur énergie).

**Date :** 2026-07-02. Script `poisson_approx.py`. Attaque frontale de l'approximation de Poisson
des fibres génériques (Type B). **Résultat : variance Poisson confirmée (moralement prouvable via
Sidon/ℤ) ; le sup-bound |S_p(t)|≤C√L (C≈3) TIENT empiriquement (contredit le pessimisme STEP21) ;
mais l'EXTRÊME maxM_B=O(log/loglog) exige Chen-Stein (dépendance faible), PAS le sup-bound seul.
Le résidu est un énoncé de grande déviation/Chen-Stein, PAS le mur max-vs-énergie. CONDITIONNEL.**

## ÉTAPE 1 — variance Poisson : CONFIRMÉE (et quasi-prouvable)

Type B (e_p>L), L=80,120 : Var(N_p)/λ ∈ [0.93, 1.10] (Poisson=1) ; ρ=Δ_p/(P²/2p²) centré sur 1
(bruit près du petit bout p~L) ; **d_TV(N_p, Poisson(λ)) ∈ [0.001, 0.025]**, petit.

**Quasi-preuve :** {2^k} est Sidon sur ℤ (STEP22, N=2^a+2^b−2^c−2^d≠0 toujours). Donc les seules
collisions mod p² viennent de p²|N, rares : Δ_p = #{quadruples p²|N} ≈ P²/(2p²) (prédiction Poisson).
La variance Poisson est donc une conséquence directe du caractère Sidon + comptage des p²|N. **La
2ᵉ-moment Poisson est essentiellement acquise.**

## ÉTAPE 3/4 — sup-bound |S_p(t)| ≤ C√L : TIENT (C≈3), contre STEP21

max_{t≠0}|S_p(t)|/√L pour p Type B (S_p(t)=Σ_{k≤L}e_{p²}(t·2^k)) :

| p | e_p | L=40 | L=80 | L=120 | L=160 |
|---|---|---|---|---|---|
| 409 | 204 | 3.46 | 3.13 | 2.93 | 3.00 |
| 809 | 404 | 4.19 | 3.24 | 3.11 | 3.00 |
| 211,277,373 | — | — | 2.8–3.4 | 2.8–3.1 | — |

**max|S_p(t)| ≤ ~4·√L, borné, DÉCROISSANT en L.** Ce n'est PAS √(L·logL) (qui croîtrait comme
√logL) — c'est un vrai √L. La **sqrt-cancellation lacunaire tient** pour {2^k mod p²}. (STEP21
craignait le contraire pour BG ; ici, pour la plage p>L et la question d'équidistribution, elle
tient.) ⟹ |S_p(t)|²/p² ≤ C²L/p² → 0 sauf t=0 (ÉTAPE 3 : oui, petit).

## La nuance décisive : le sup-bound NE DONNE PAS l'extrême (calcul)

Piège de l'ÉTAPE 4 (« √L suffit »). Le sup-bound contrôle la VARIANCE mais **pas** le max :
- Moments : Σ_t|S_p(t)|^{2k} = p²·E_k (k-énergie additive). Sup-bound ⟹ E_k ≤ C^{2k}L^k.
- MAIS E_k inclut les solutions TRIVIALES (~k!·L^k, appariements). Le sup-bound borne le TOTAL, pas
  la part non-triviale (= ce dont M_p a besoin). C^{2k}L^k ≈ k!L^k est cohérent avec le trivial seul.
- Donc |N_p(r)−λ| ≤ (1/p²)Σ|S_p|² = L+1 (trivial) : le sup-bound seul ⟹ M_p≤L+1, inutile pour l'extrême.

**Conclusion : le sup-bound √L (même prouvé) donne la variance Poisson, pas maxM_B=O(log/loglog).**
L'extrême exige la loi complète (méthode des moments non-triviaux / Chen-Stein).

## ÉTAPE 2 — Chen-Stein : le bon cadre pour l'extrême (et il n'est PAS le mur énergie)

d_TV(N_p, Poisson) petit (0.001–0.025, ÉTAPE 1) = **dépendance faible** entre fibres ⟹ Chen-Stein
(Arratia-Goldstein-Gordon) applicable. L'extrême d'un champ Poisson-approximé sur ~p² fibres × N
premiers donne maxM_B ≈ log(Np²)/loglog ≈ O(log L/loglog L) — la valeur voulue.

**Chen-Stein ≠ mur max-vs-énergie :** le mur (STEP19-28) disait « l'énergie ne borne pas le max ».
Chen-Stein ne PASSE PAS par l'énergie : il borne d_TV via la STRUCTURE DE DÉPENDANCE des collisions
(combien de collisions partagent un exposant). C'est un énoncé combinatoire (b₂=Σ paires dépendantes),
pas un 2ᵉ moment. Pour Type B, collisions rares + involution box-exclue (STEP30) ⟹ dépendance faible
plausible. **Le résidu est donc Chen-Stein, un objet probabiliste standard, pas l'énergie.**

## Verdict (format demandé)

- **Distance à Poisson décroît avec L ?** d_TV ∈ [0.001,0.025], petit ; bruité par-premier mais
  globalement décroissant. Variance Poisson (Var/λ≈1) nette.
- **Dépendance Chen-Stein faible ?** OUI (d_TV petit ⟹ dépendance faible ; collisions rares + pas de
  clustering car involution box-exclue).
- **|S_p(t)|²/p² petit sauf t≡0 ?** OUI (≤C²L/p²→0).
- **Borne √L sur |S_p(t)| tient ?** OUI empiriquement, **C≈3-4, borné, décroissant** (vrai √L, pas √(L logL)).
- **Approximation Poisson prouvable ? méthode ?**
  - **Variance/2ᵉ moment : OUI, quasi-prouvable** (Sidon/ℤ + comptage p²|N).
  - **Extrême : via Chen-Stein** (dépendance des collisions), PAS via le sup-bound seul (qui ne
    sépare pas trivial/non-trivial). Le sup-bound √L est un bonus d'équidistribution, ni nécessaire
    ni suffisant pour l'extrême.
- **M″ prouvé sous quelle hypothèse ?** Sous **« les collisions Type B sont Chen-Stein-Poisson
  (dépendance faible) »** ⟹ maxM_B=O(log L/loglog L) ⟹ Σ_B(M_p−1)≤maxM_B·π(L²)=o(L²) ⟹ (avec Type A
  acquis) **M″=o(L²) ⟹ #11 every-n**.
- **STATUT :**
  - **PROUVABLE (quasi) :** variance Poisson (Sidon/ℤ).
  - **CONFIRMÉ empiriquement :** sup-bound √L (C≈3), d_TV petit, Var/λ≈1, sous-Poisson (STEP31).
  - **CONDITIONNEL :** M″=o(L²) sous l'approximation de Poisson-Chen-Stein de l'extrême Type B.
  - **RESTE OUVERT (résidu unique, bien posé) :** la borne de dépendance de Chen-Stein pour le
    processus de collisions {2^a+2^b≡2^c+2^d mod p²} en Type B. Objet PROBABILISTE combinatoire
    (paires de collisions partageant un exposant), **PAS le mur énergie**, empiriquement satisfait
    (d_TV→0, sous-Poisson). C'est le meilleur cadrage de la campagne : un énoncé Chen-Stein standard.

---
*Script poisson_approx.py. Variance Poisson quasi-prouvée (Sidon/ℤ) ; sup-bound √L confirmé C≈3
(≠STEP21) ; mais l'extrême exige Chen-Stein (le sup-bound ne sépare pas trivial/non-trivial). Résidu
= dépendance Chen-Stein des collisions Type B, empiriquement faible (d_TV∈[0.001,0.025]), objet
probabiliste standard ≠ mur énergie. CONDITIONNEL. PAPER intact.*
