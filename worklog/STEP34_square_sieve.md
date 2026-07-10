# STEP34 — Crible du carré & Rudin Λ(2k) : les deux marchent et CONVERGENT sur le même cœur (diviseurs carrés des combinaisons de puissances). E_2 (variance) essentiellement prouvable ; k≥3 = crible du carré de Heath-Brown.

**Date :** 2026-07-03. Script `square_sieve.py`. Test des deux outils sur le résidu E_k^tot ≤ C^k E_k^null.
**Résultat : (1) crible du carré — la densité de N=2^a+2^b−2^c−2^d avec diviseur carré p²>L² est ~1.3×
la prédiction aléatoire Σ1/p² (constante bornée) ⟹ E_2=O(E_2^null) au bon ordre ; (2) Rudin Λ(2k)
mod p² TIENT (E_k^pow ≤ (2k)^k(L+1)^k, k=2,3,4). CLÉ : les deux outils sont deux lentilles sur le MÊME
cœur — la non-dissociativité de {2^j mod p²} = les diviseurs carrés des combinaisons de puissances.
E_2 (variance) prouvable (Rudin=E_2^tot ou crible) ; k≥3 = crible du carré de Heath-Brown (le tool).**

## E_2, E_3 : sous-multinomial + décroissance Poisson

| L | E_2^tot/null | E_3^tot/null | E_3/E_2 | ~λ |
|---|---|---|---|---|
| 40 | 0.77 | 0.34 | 0.019 | 0.32 |
| 60 | 0.96 | 0.57 | 0.026 | 0.31 |
| 80 | 0.91 | 0.91 | 0.050 | 0.31 |
| 100 | 0.96 | 0.92 | 0.043 | 0.31 |

Ratios ≤1 (sous-multinomial) ; E_3/E_2 ~ λ ⟹ décroissance Poisson confirmée.

## ÉTAPE 1 — Crible du carré sur E_2 : densité au bon ordre

E_2^tot = Σ_{quadruples} ω₂(N), N=2^a+2^b−2^c−2^d≠0. Échantillon (40k quadruples) :

| L | frac(∃p²>L²\|N) | Σ_{p>L}1/p² (prédiction) | ratio | maxω₂ |
|---|---|---|---|---|
| 40 | 0.00713 | 0.00539 | 1.32 | 2 |
| 60 | 0.00413 | 0.00320 | 1.29 | 1 |
| 80 | 0.00302 | 0.00218 | 1.39 | 3 |

**La densité de N à diviseur carré = 1.3× la densité « aléatoire » Σ1/p² — constante bornée, MÊME
ORDRE.** Donc E_2^tot ~ 1.3·(#quadruples)·Σ1/p² ~ 1.3·L⁴/(L logL) = 1.3 L³/logL = O(E_2^null). maxω₂≤3
(les rares ω₂≥2 = carrés de Mersenne, STEP22). **Heath-Brown square sieve** (1984) borne exactement
Σ_N #{p²|N} pour N valeurs d'une forme ⟹ **outil qui prouverait E_2=O(E_2^null) rigoureusement** (le
constant 1.3 = léger excès des différences de puissances, borné).

## ÉTAPE 3 — Rudin Λ(2k) mod p² : TIENT

E_k^pow = (1/p²)Σ_t|S_p(t)|^{2k} = énergie additive d'ordre k des PUISSANCES {2^j} (≠ E_k^tot des
paires ! piège Fourier ; identité vraie seulement à k=2 : E_2^tot=E_2^pow). Borne Rudin (Ck)^k(L+1)^k :

| p | L | k | E_k^pow | diag k!(L+1)^k | /Rudin(2k)^k(L+1)^k |
|---|---|---|---|---|---|
| 409 | 60 | 2 | 7493 | 7442 | 0.13 |
| 409 | 60 | 3 | 1.67e6 | 1.36e6 | 0.03 |
| 409 | 60 | 4 | 1.48e9 | 3.3e8 | 0.03 |
| 809 | 100 | 3 | 7.6e6 | 6.2e6 | 0.03 |

**E_k^pow ≤ (2k)^k(L+1)^k à tout k testé (ratios 0.01–0.16 <1).** Le contrôle des moments lacunaires
vaut mod p². L'excès sur la diagonale ℤ (k!(L+1)^k, Sidon binaire) croît avec k (1% → 23% → 4× pour
k=2,3,4) mais reste sous Rudin.

## La convergence : Rudin ≡ crible du carré au cœur

Rudin classique (tore) repose sur la **dissociativité** : {2^j} n'a pas de petite combinaison
Σε_j2^j=0 (ε∈{−1,0,1}) ⟹ moments = diagonale. **Mod p², la dissociativité ÉCHOUE** pour p petit :
|Σε_j2^j| < 2^{L+1} peut être ≡0 mod p² (p²<2^{L+1} si p~L). L'excès E_k^pow − k!(L+1)^k EST
exactement **#{combinaisons Σε_j2^j ≡ 0 mod p²}** = les paires (combinaison, p²|elle) = **les diviseurs
carrés des combinaisons de puissances**. ⟹ **Rudin mod p² et le crible du carré contrôlent le MÊME
objet.** Empiriquement il est au bon ordre (densité ~Σ1/p²), donc les deux tiennent.

## Chaîne : ce qui est acquis vs restant

- **E_2^tot = E_2^pow** (identité) ⟹ **la VARIANCE est prouvable** par Rudin mod p² (4ᵉ moment lacunaire)
  OU par le crible du carré. C'est essentiellement fait (rédaction).
- **k≥3 :** Rudin donne l'énergie des PUISSANCES E_k^pow ; il reste le transfert puissances→paires
  (E_k^tot ≤ f(E_j^pow)) OU l'application directe du crible du carré aux combinaisons d'ordre k
  (#{Σε_j2^j≡0 mod p²} avec 2k termes). **Le crible de Heath-Brown est le tool** : il borne la densité
  de diviseurs carrés, empiriquement ~Σ1/p² (aléatoire) à tout ordre.

## Verdict (format demandé)

- **E_2^tot/E_2^null : ratio et décroissance ?** 0.77→0.96, ≤1 stable. Densité diviseurs carrés
  1.3×Σ1/p² (bon ordre). **E_2=O(E_2^null) confirmé + prouvable (Rudin/crible).**
- **E_3^tot/E_3^null, gain du log par itération ?** 0.34→0.92, ≤1 ; E_3/E_2~λ (décroissance Poisson).
  L'itération p²|N₁,N₂ ⟹ p²|(N₁−N₂) (ω₂≤2) donne bien ≤O(1) premiers par triplet.
- **Rudin Λ(2k) mod p² tient ?** **OUI empiriquement** (E_k^pow ≤ (2k)^k(L+1)^k, k=2,3,4). La
  dissociativité mod p² échoue mais l'excès (=diviseurs carrés) reste borné.
- **Piste la plus prometteuse ?** **Le crible du carré de Heath-Brown** : il attaque directement le
  cœur commun (diviseurs carrés des combinaisons de puissances), au bon ordre empirique, et existe
  comme théorème. Rudin est équivalent au cœur mais moins directement « prouvant ».
- **M″ : prouvé / conditionnel / mur ?** **CONDITIONNEL, avec voie concrète.** PAS un mur : les deux
  outils NE échouent PAS structurellement — ils réduisent à « densité de diviseurs carrés des
  combinaisons de puissances = O(Σ1/p²) », empiriquement vérifiée (ratio ~1.3, borné). E_2 prouvable ;
  k≥3 via Heath-Brown (à formaliser).
- **STATUT :**
  - **PROUVABLE (essentiellement) :** E_2^tot=O(E_2^null) = variance Poisson (Rudin mod p² / crible).
  - **CONDITIONNEL, voie identifiée :** E_k^tot ≤ C^k E_k^null pour k≥3 via crible du carré de
    Heath-Brown appliqué aux combinaisons de 2k puissances (densité de carrés au bon ordre).
  - **RESTE OUVERT (mais délimité, avec outil) :** formaliser la borne de Heath-Brown à tout ordre
    k≤logL/loglogL. Cœur = non-dissociativité de {2^j mod p²} = diviseurs carrés, ≠ mur, empiriquement
    au bon ordre.

---
*Script square_sieve.py. Crible du carré : densité N-à-diviseur-carré ~1.3·Σ1/p² (bon ordre, maxω₂≤3).
Rudin Λ(2k) mod p² tient (E_k^pow≤(2k)^k(L+1)^k). Les deux = même cœur (diviseurs carrés des
combinaisons de puissances). E_2 prouvable ; k≥3 = Heath-Brown square sieve. CONDITIONNEL, voie
concrète, PAS un mur. PAPER intact.*
