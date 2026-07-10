# STEP53 — Salve García–Voloch : Chantiers G (consolidation), E (dictionnaire corps de fonctions), F (digits). AUCUNE écriture papier (consigne user). Tout dans consolidation_notes.md.

**Date :** 2026-07-05. Fable a lu la source primaire (notes Konyagin). Livrables dans `consolidation_notes.md`.

## Chantier G — consolidation García–Voloch (attribution + bande + p|n)
- **Attribution corrigée :** la borne N₂(b)≤4|G|^{2/3} est de **García–Voloch** (Thm 2.1), PAS Heath-Brown–
  Konyagin. HB = preuve Stepanov ; HB-K = énergie T₂≪|G|^{5/2}. Réf : Konyagin–Shparlinski (CUP).
- **Cas dégénéré = exclusion b≠0 du théorème source.** Notre découverte numérique STEP52 (borne fausse
  n=0) coïncide EXACTEMENT avec la condition b∈Z_p^* de GV. Source ↔ numérique en accord total.
- **Condition de taille p^{3/4}** (mieux que p^{2/3} annoncé de mémoire). Bande exceptionnelle p∈(L,L^{4/3}).
  **CONFIRMÉ numériquement (chantierG_band.py) :** #viol=8,15,16,23,43 (L=60..300) ; max p viol < L^{4/3}
  partout (157<235,...,2003<2008) ; contribution triviale (488→12943) ≪ terme principal L^{8/3}/logL
  (13476→707121). ⟹ **Prop Σ_TypeA M_p=O(L^{8/3}/logL) TIENT**, bande absorbée par M_p≤L+1.
- **p|n** (n≡0 mod p) : O(L/logL) premiers/n, contribution O(L²/logL) < O(L^{8/3}/logL), absorbée.
- **Bonus source (Fable exploitera) :** (i) T_k(G)≪|G|^{2k−2+2^{1−k}} (|G|≤p^{1/2}) = énergies d'ordre
  supérieur mod p. (ii) **Bourgain Thm 3.15** : max_{a≠0}|Σ_{j<T}e(a g^j/p)|≪Tp^{−ε} pour T>p^δ, g^j
  distincts — **vérifie notre Type B** (e_p>L, T=L+1>p^δ car p≤L²). ⟹ **cancellation sup-norme des sommes
  géom. incomplètes existe DÉJÀ mod p, inconditionnelle**. Manque pour (TB) = passage mod p² (p∤t).
  Cible : Bourgain(–Chang) sous-groupes de Z_{p²}^*. **Fable localise/lit ; NE RIEN écrire avant.**

## Chantier E — dictionnaire F_q[t] (le build). Aucune preuve à ce stade.
Architecture entière transposée : ℤ↦F_q[t], 2↦t, sans-carré↦sans-carré (densité 1−1/q), premiers p↦
irréductibles P, ord_p(2)↦ord_P(t), noyau K=1+pℤ/p²↦K_P=1+P(F_q[t]/P²), Lemme K et involution se
traduisent directement, Σ1/|P|²<1 (q=2:≈0.60) ⟹ couverture impossible (même obstruction). **Le gain :
(TB) analogue = moyenne quadratique de sommes géom. incomplètes mod P², bornées par WEIL (inconditionnel)
— l'estimation conjecturale sur ℤ (niveau Bourgain) est un THÉORÈME sur F_q[t].** Prédiction : every-n
analogue prouvable inconditionnellement ; la borne de Weil exacte utilisée = la cible à chercher en car. 0.
**Ne se traduit PAS proprement :** Wieferich (densité + Frobenius/inséparabilité en car. p), la condition
« n impair », Kalinin (pas de 2-adique en car. p). Détails E.1–E.6 dans consolidation_notes.md.

## Chantier F — mini-test digits (table brute, sans verdict)
R(n)=#{(l,m):n−2^l−2^m sans facteur carré}. **minR croît 44→145 (L=11..20), toujours ≫0 : aucun contre-
exemple, marge large.** s₂ moy des 5% pires n = ~1 sous le global (5.49 vs 7.00,...,10.50 vs 11.50) =
**effet faible (~0.4σ)** : pires n penchent poids binaire faible, mais pas de dichotomie nette. Signal
« poids léger » faible, aucun « poids lourd ». Table complète dans consolidation_notes.md.

## Statut
- Chantier G : proposition Stepanov/GV **solidifiée** (attribution, condition p^{3/4}, bande confirmée
  absorbée). Prête à écrire au papier (sur signal) avec García–Voloch cité.
- Chantier E : dictionnaire F_q[t] fait ; prochaine inflexion = rédiger la section (sur signal), voir si
  (TB)-F_q[t] tombe par Weil.
- Chantier F : pas de signal digits fort ; scission par s₂ faiblement justifiée côté léger.
- **Côté Fable :** lire Bourgain(–Chang) sous-groupes Z_{p²}^*, q composé (le maillon qui peut basculer (TB)).

**AUCUNE écriture papier cette salve** (consigne user maintenue). Tout dans consolidation_notes.md.
Voir [[project_erdos11_fable_leads]], [[feedback_verify_before_writing]].

---
*García–Voloch (pas HB-K) : N₂(b)≤4|G|^{2/3}, b≠0, |G|<p^{3/4}. Bande p∈(L,L^{4/3}) confirmée absorbée
(chantierG_band.py). Bonus Bourgain Thm3.15 : sup-norme mod p déjà inconditionnelle en Type B. Dictionnaire
F_q[t] fait (Weil clôt (TB) analogue). Digits : minR≫0 (pas de contre-ex), s₂ pires ~1 sous moyenne (faible).
Rien au papier. Fable lit Bourgain composé.*
