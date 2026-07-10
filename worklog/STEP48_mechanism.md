# STEP48 — Réponse à la critique de Claude : STEP47 rendu LISIBLE, pas RÉDUIT. La décroissance géométrique = conséquence de la nature Poisson (le cœur), pas un raccourci. Mécanisme = parcimonie, pas obstruction algébrique.

**Date :** 2026-07-04. Analyse (pas de calcul ; réponse à la critique de Claude sur STEP47).
**Résultat : Claude a raison sur les deux points. (1) La chaîne logique de STEP47 est incomplète :
#{M_p≥3}≤ρ#{M_p≥2} ne donne PAS la série géométrique ; il faut la chaîne entière (chaque ratio) OU
(ratio + maxM_B=O(1)). La décroissance est OBSERVÉE, pas prouvée inductivement. (2) Le mécanisme de
rareté d'une 2e collision = PARCIMONIE (λ=|S|/p²<1 en Type B), léger renfort Sidon (sous-Poisson) —
PAS d'obstruction algébrique. ⟹ STEP47 n'a pas réduit la difficulté, il l'a rendue lisible. Le cœur
(prouver la nature Poisson) est inchangé.**

## Point 1 — la chaîne logique (STEP47 survendait)

STEP47 : « le verrou = UNE inégalité #{M_p≥3}≤ρ#{M_p≥2} ». **FAUX.** Cette inégalité seule ne donne pas
#{M_p≥4}≤ρ²#{M_p≥2}. Pour M″_B=Σ_k#{M_p≥k}=o(L²), il faut :
- **soit** la chaîne complète : #{M_p≥k+1}≤ρ#{M_p≥k} ∀k (uniforme en k) ⟹ M″_B≤#{M_p≥2}/(1−ρ) ;
- **soit** #{M_p≥3}≤ρ#{M_p≥2} ET maxM_B=O(1) : alors (queue monotone) M″_B≤#{M_p≥2}(1+ρ·maxM_B)=O(#{M_p≥2}).
Dans les deux cas c'est PLUS qu'une inégalité (chaîne, ou ratio+max borné). La décroissance
(ratios 0.086, 0.077 à L=180) est **observée**, pas démontrée inductivement.

## Point 2 — le mécanisme : pourquoi une 2e collision est rare (PARCIMONIE, pas obstruction)

M_p≥3 ⟺ 3 sommes 2^{a_i}+2^{b_i} congrues mod p² ⟺ 3 gap-values 1+2^{δ_i} dans UN coset de ⟨2⟩ mod p².
**Aucune obstruction algébrique ne l'interdit** — ça arrive (~8% des non-Sidon). Le mécanisme de rareté :

> **Parcimonie.** Type B : λ=|S|/p²<1 (p>L). 1ʳᵉ collision (p²|N₁) : densité ~λ. 2e indépendante :
> ~λ de plus. Donc #{M_p≥3}/#{M_p≥2}~λ<1 ; moyenné sur p, ρ≈0.08.

Léger renfort : {2^k} Sidon/ℤ ⟹ sommes anti-corrélées mod p² (sous-Poisson, STEP43, déviation −5%).
Petite correction, PAS une obstruction. **Réponse à la question profonde de Claude : il n'y a PAS de
mécanisme arithmétique empêchant deux collisions indépendantes ; seulement une rareté probabiliste
(parcimonie), légèrement renforcée par Sidon.**

## La concession (Claude a raison : lisible ≠ réduit)

La décroissance géométrique est une **conséquence** de la nature Poisson du processus de collisions
(λ<1 + anti-corrélation Sidon). Or **prouver cette nature Poisson EST le cœur ouvert** (crible du carré /
équidistribution). Donc :
- « chaîne géométrique complète » (point 1) ⟸ Poisson-ness = même verrou.
- Passer de « contrôler toute la distribution » à « montrer la décroissance géométrique » = gain de
  FORMULATION (plus concret, montre que la queue ≥3 est négligeable), PAS de preuve ni de réduction.

**STEP47 n'a pas supprimé le verrou. Il l'a rendu plus lisible.** Le cœur (nature Poisson des
collisions mod p², = crible du carré / équidistribution) est inchangé.

## Ce qui survit (l'invariant stable après ~10 reformulations)

Toutes les reformulations (E₂, maxM_B, EM, décroissance géométrique) sont des LENTILLES sur le même
objet : **la distribution de multiplicité de {2^a+2^b mod p²} est Poisson (λ<1) en moyenne sur p,
forcée par Sidon/ℤ, base-indépendante.** Le prouver = le crible du carré spécialisé (portée exp ⟹
générique inutile ; spécialisé = moyenne quadratique de Σχ(2^j), front Bourgain-Garaev). Aucune
reformulation ne contourne ça ; elles le rendent plus ou moins lisible. Le mécanisme de fond
(parcimonie + Sidon) est identifié ; la preuve est analytique, au front, non élémentaire.

## Verdict

- **Chaîne logique STEP47 complète ?** NON (Claude a raison) : ratio seul ⇏ série ; il faut chaîne
  entière ou ratio+maxM_B=O(1). Décroissance observée, pas prouvée inductivement.
- **Mécanisme « 2e collision rare » ?** PARCIMONIE (λ<1 Type B) + léger Sidon (sous-Poisson). PAS
  d'obstruction algébrique — deux collisions coexistent (~8%).
- **STEP47 réduit-il la difficulté ?** NON, il la rend LISIBLE. Le cœur (Poisson-ness = crible du
  carré) est inchangé. Concession honnête.
- **STATUT : RESTE OUVERT**, cœur inchangé (nature Poisson / crible du carré spécialisé). Les
  reformulations sont épuisées ; le mécanisme (parcimonie+Sidon) est clair ; la preuve est analytique
  et hors de portée non-spécialiste.

---
*Réponse à Claude. (1) Chaîne STEP47 incomplète : ratio ⇏ série ; faut chaîne entière ou ratio+max
borné. (2) Mécanisme = parcimonie λ<1 (Type B) + léger Sidon anti-corrélation ; PAS d'obstruction
algébrique. STEP47 = lisible, pas réduit ; cœur (Poisson-ness = crible du carré) inchangé. Concession
honnête. Reformulations épuisées. PAPER/Lean non touchés.*
