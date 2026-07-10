# STEP50 — Lead Fable n°4 (réduction p-adique via Lemme K / quotients de Fermat) : PARTIELLE, n'atteint pas le Type B ouvert. + note §7 honnête.

**Date :** 2026-07-04. Évaluation analytique (pas empirique) du plan le plus structuré de Fable pour (TB).
**Résultat : la réduction Lemme-K du moment fonctionne pour les caractères p|t (⟹ sommes mod p) et pour
les périodes complètes (Type A, déjà clos), mais NE réduit PAS les caractères p∤t (sommes incomplètes
mod p²) = précisément le Type B ouvert. Comme lead #1, ne casse pas (TB), mais pour une raison précise
et différente (incomplétude, pas équidistribution). Gain réel : identifie que la frontière est le
sum-product (Bourgain), pas Korobov — la §7 sous-vendait. Note ajoutée.**

## L'identité de réduction (correcte)

Moment/énergie mod p² via S(t)=Σ_{k≤L} e_{p²}(t·2^k). Scinder selon p|t :
- **p|t, t=pb :** S(pb)=Σ_{k≤L} e_{p²}(pb·2^k) = Σ_{k≤L} e_p(b·2^k) = **somme géométrique mod p**, longueur
  L+1. Si e_p≤L (Type A) : somme COMPLÈTE sur ⟨2⟩ mod p (Lemme K la traite ; déjà inconditionnel, Prop
  ordersum). Si e_p>L (Type B) : géométrique INCOMPLÈTE mod p, longueur L < e_p.
- **p∤t :** S(t)=Σ_{k≤L} e_{p²}(t·2^k) = somme incomplète mod p², longueur L. **Lemme K ne la réduit PAS**
  (Lemme K annule la somme COMPLÈTE sur ⟨2⟩ ; ici incomplète). C'est le gros des p²−p caractères.

## Verdict honnête

- **Ce que ça donne :** les p|t (fraction 1/p) et le Type A (déjà clos). Recycle Lemme K là où on a déjà
  réussi.
- **Ce que ça NE donne PAS :** le Type B ouvert = caractères p∤t, sommes incomplètes mod p², longueur L
  ∈[q^{1/4},q^{1/2}], q=p². Lemme K muet. La réduction p-adique n'atteint pas l'obstacle.
- **Comme lead #1 (larger sieve), lead #4 ne casse pas (TB)** — mais pour une raison précise différente :
  #1 = équidistribution (pas de concentration) ; #4 = incomplétude (Lemme K ne réduit que le complet).

## Gain réel (§7 corrigée)

Fable a raison sur un point : la §7 écartait via Korobov (√q log q trivial à longueur <q^{1/2}), mais
la vraie frontière est le **sum-product** (Bourgain–Glibichuk–Konyagin : sommes géométriques incomplètes
de longueur L mod p ou p², valide pour ordre e_p≥p^δ) — qui peut battre Korobov pour une progression
GÉOMÉTRIQUE spécifiquement. Note ajoutée en §7 (toolkit-4) : la réduction p-adique isole le p∤t
incomplet-mod-p² comme le vrai (TB) ouvert, et le sum-product (pas Korobov) est l'input pertinent —
énoncé HONNÊTEMENT (non vérifié qu'il atteint la longueur L en moyenne quadratique ; caveat Fable). Pas
d'over-claim.

## Bilan de la session « test des leads Fable »

- **Corrections papier (a7d8d57) :** Lemme K sur-vendu → reformulé ; pont CRT → ajouté. Justes.
- **Amélioration gratuite (c764250) :** Markov ηL² mur (B) ⟹ densité exceptionnelle O(1/logL)→**O(1/(L logL))**
  (goulot déplacé vers (L,L²]) + remarque moments-CRT vers O(L^{−A}). Réel, implémenté.
- **Lead #1 larger sieve (STEP49, 7eab0e2) :** MORT (équidistribution).
- **Lead #4 réduction p-adique (ce STEP) :** PARTIELLE (incomplétude Type B). Note §7 honnête.
- **Non testés :** #3 Cilleruelo (concentration r_p(n)), #5 corps de fonctions (sandbox), #6 digits.

**Le noyau reste inchangé :** (TB) = sommes géométriques incomplètes mod p², longueur L, en moyenne
quadratique — sum-product/Bourgain, au front, non élémentaire. Deux cribles écartés pour deux raisons
précises. Voir [[project_erdos11_fable_leads]], [[project_erdos11_twopow_status]].

---
*Lead #4 : réduction Lemme-K partielle (p|t → mod p ; Type A clos ; p∤t Type B non réduit = incomplétude).
Ne casse pas (TB). Gain : §7 corrigée, frontière = sum-product (Bourgain) pas Korobov. Amélioration
gratuite + 2 fixes rigueur implémentés. Restent #3,#5,#6.*
