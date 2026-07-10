# STEP54 — Chantier H (Bourgain–Chang → moments). Sup-norme CONFIRMÉE, conversion naïve BLOQUE (super-poly). Verdict honnête.

**Date :** 2026-07-05. LE calcul de la salve (Fable : meilleur rapport gain/effort). Scripts
`chantierH_supnorm.py`. Notes détaillées dans `consolidation_notes.md` §H. **AUCUNE écriture papier.**

## Ce qui est CONFIRMÉ
Bourgain–Chang GAFA 16 (2006) Cor 4.5 : `max_{p∤ξ}|S(ξ)|<(L+1)^{1−ε}`, S(ξ)=Σ_{j≤L}e_{p²}(ξ2^j), pour
Type B (e_p>L, p∈(L,L²]), ε absolu. **Vérifié numériquement** (chantierH_supnorm.py) : ratio 0.37→0.24
(L=40,80,120), <1, décroissant (ε_eff≈0.4). Conditions vérifiées par Fable (δ=1/5). Contre-ex 4.23 du
papier = 1+p (ordre 1 mod p) = exactement pourquoi Type A exclu. Tout cohérent.

## Ce qui BLOQUE (contre l'espoir de Fable — 3ᵉ fois que la vérif tranche)
Conversion sup-norme → moment factoriel E_k^tot via l'identité d'orthogonalité
`M_k=(1/p²)^{k−1}Σ_{Σξ=0}Π S(ξ_i)²`. Le terme « toutes fréquences ≠0 » borné par sup-norme :
`E_k^{tot,≠0} ≲ (L+1)^{2k−2−2(k−2)ε₀}·L²/(2^k k! logL)`, qui à **k~k*=3logL/loglogL** vaut
**exp(6(1−ε₀)log²L/loglogL)/(L logL) = SUPER-POLYNOMIAL ≫ L²**.
**Raison exacte :** chaque fréquence ≠0 de plus multiplie par `B²=(L+1)^{2−2ε₀}>1` (somme p² sur la
fréquence libre × sup-norme B² × 1/p² du préfacteur). La sup-norme sauve (L+1)^{−2ε₀}/fréq mais la somme
libre apporte (L+1)^{+2} : gain insuffisant, accumulation explose à k~k*.
**⟹ Cor 4.5 (sup-norme SEULE) ne ferme PAS (TB).**

## Ce qu'il faudrait
Exploiter la cancellation dans Σξ_i=0 (convolution k-fois) = bornes **L⁴/corrélation d'ordre supérieur**
sur S, pas juste sup-norme. Question source pour Fable : Bourgain–Chang a-t-il de telles bornes de moment
(pas seulement Cor 4.5 sup-norme) ? Si oui (TB) peut passer ; sinon la voie sup-norme est close.

## Bonus : bug d'énoncé Thm 5.8 (à corriger)
(TB) énoncée « pour k≤k* » mais utilisée pour k>k* (la queue). Corriger : (TB) pour tout k≥2, ou traiter
la queue séparément. (k*·π(L²)=o(L²) déjà inconditionnel pour k≤k* ; le vrai besoin = queue k>k*.)

## Verdict
- Sup-norme BC : VRAIE, confirmée. (TB) via sup-norme naïve : BLOQUE super-poly (exposant exact en H.3).
- Pas de fermeture de (TB) cette salve. **Progrès réel de cadrage** : on sait EXACTEMENT où ça bloque
  (terme toutes-fréq-≠0, B²>1/fréq) et ce qu'il faut (moments L⁴+ de S, pas sup-norme). Le Type B reste
  ouvert ; García–Voloch (TA, STEP52) reste le seul vrai gain inconditionnel de la campagne Fable.
- Règle « vérifier avant d'écrire » a de nouveau évité un faux « Type B clos » (3ᵉ save après Chantier A
  et le dégénéré Stepanov). Voir [[feedback_verify_before_writing]].

**Statut leads Fable :** #1 mort, #4 partiel, Chantier A conditionnel, García–Voloch (TA) écrit+consolidé
(gain réel, court L^{2/3}), Bourgain–Chang (TB) sup-norme confirmée mais conversion bloque, corps de
fonctions (E) dictionnaire fait. Voir [[project_erdos11_fable_leads]], [[project_erdos11_twopow_status]].

---
*Chantier H : Bourgain–Chang Cor 4.5 sup-norme CONFIRMÉE num. (ratio 0.37→0.24). Conversion → E_k^tot
BLOQUE super-poly à k~k* (chaque fréq ≠0 : facteur B²=(L+1)^{2−2ε}>1). Sup-norme seule insuffisante ;
faut bornes L⁴/corrélation. (TB) PAS fermé. Bug Thm 5.8 (TB énoncé k≤k*, utilisé k>k*). Rien au papier.*
