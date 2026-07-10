# STEP55 — Chantiers I (circularité), E′ (corps de fonctions), J (fine k=2). AUCUNE écriture papier. Tout dans consolidation_notes.md §H.7–H.8, §J.

**Date :** 2026-07-05. Salve de consignation/build. Détails dans `consolidation_notes.md`.

## Chantier I — la voie sup-norme→moments est close par CIRCULARITÉ (pas absence de littérature)
`Σ_ξ|S(ξ)|^{2k}=p²·E_k^{add}` (énergie additive d'ordre k de {2^j}) = exactement la quantité que (TB)
contrôle. BC Cor 4.5 donne le L^∞ ; fermer demande le L^{2k} = l'énergie = **(TB) elle-même**. ⟹ chercher
« la bonne borne » ne peut pas aider, elle EST la conjecture. Et la sup-norme n'allait jamais fermer (tout
ε<1 ⟹ B²=(L+1)^{2−2ε}>1 ; même √-cancellation ε=1/2 ⟹ B²=L+1>1). **(TB) est une vraie estimation ouverte,
pas un énoncé en attente de référence.** + clarification mult (square sieve, quasi-triviaux ~L) vs additif
(BC, L^{1−ε}) ; contre-ex 4.23 (θ=1+p, ordre 1 mod p) ⟹ **scission Type A/B FORCÉE** (Type A=García–Voloch,
Type B=BC).

## Chantier E′ — corps de fonctions : trois-issues = « prouvable-par-structure, mais NE transpose PAS »
- **(a)** Le pipeline de blocage vaut aussi sur F_q[t] : Weil ε=1/2 ⟹ B²=(L+1)>1 ⟹ **bloque identiquement**
  (prédiction Fable confirmée). La circularité (I) est FONDAMENTALE, pas un artefact du petit ε sur ℤ.
- **(b)** MAIS (TB)-F_q[t] est **prouvable-par-structure** : {t^j} sont des MONÔMES, Σt^{a_i}−Σt^{b_i} est
  un polynôme de degré ≤L ; ≡0 mod P² (deg 2degP) ⟹ nul OU deg≥2degP. Donc **deg P>L/2 ⟹ aucune collision
  non triviale ⟹ (TB) TRIVIAL** ; collisions seulement pour deg P≤L/2, comptées par le degré. Pas de Weil,
  pas de sup-norme — juste indépendance linéaire des monômes + comptage (q>2k).
- **(c)** Le mécanisme **NE se transpose PAS en car. 0** : sur ℤ, 2^a+2^b−2^c−2^d peut être divisible par p²
  en étant ≠0 — **aucune borne de degré n'empêche la divisibilité par un carré**. C'est EXACTEMENT
  l'obstruction diviseurs-carrés (STEP47-48). ⟹ le sandbox corps de fonctions ne fournit PAS de méthode
  car.-0 ; il PROUVE que (TB)-ℤ est structurellement plus dur (catégorie square-sieve/Wieferich). Issue
  honnête : « prouvable-par-structure sur F_q[t], mais inéquation décisive (deg P>L/2) sans analogue sur ℤ ».
  **(TB)-ℤ ne tombera pas par transposition.**

## Chantier J — mesure fine k=2 : les doubles sont 100% structurés (Mersenne)
Histogramme #{p∈(L,L²]:p²|N}, N=1+2^β−2^γ−2^δ, L=40,60,80 : massivement compte=1 (210,468,778), queue
compte=2 (2,10,30) et 3 (0,2,5). **Les quadruples à compte≥2 sont TOUS structurés (100%)** : Mersenne-
carrés (N=±(2^14−1)²=3²·43²·127², p=[43,127]) et/ou facteur 2^m±1. Aucun sauvage. Confirme+étend STEP22.
Compte=1 : ~76% « structurés » mais classifieur gonflé par petits facteurs (3=2²−1…). Signal réel = les
doubles/triples 100% structurés ⟹ **cible de classification élémentaire k=2** : « p² divise deux quadruples
⟹ N Mersenne-carré ». [Pour Fable.]

## Statut
- (TB)-ℤ : close par circularité (voie sup-norme), structurellement plus dure que F_q[t] (pas de borne de
  degré). = vraie estimation ouverte, catégorie square-sieve. Ne tombe ni par BC-sup-norme ni par
  transposition F_q[t]. **García–Voloch (TA) reste le seul gain inconditionnel** (STEP52, court L^{2/3}).
- Cible élémentaire résiduelle : classification des doubles k=2 (tous Mersenne, Chantier J).
- Côté Fable : reste à voir s'il existe une borne d'ÉNERGIE (pas sup-norme) qui contourne la circularité —
  mais I montre que ce serait (TB) elle-même. Le corps de fonctions comme piste est CLOS (ne transpose pas).
- **4ᵉ salve sans faux positif écrit** (I/E′/J = consignation honnête, aucune sur-vente). Rien au papier.

Voir [[project_erdos11_fable_leads]], [[project_erdos11_twopow_status]], [[feedback_verify_before_writing]].

---
*I : voie sup-norme close par CIRCULARITÉ (le moment L^{2k} manquant = énergie = (TB)). E′ : F_q[t] bloque
pareil (ε=1/2), (TB)-F_q[t] prouvable par monômes/degré MAIS ne transpose pas (ℤ = pas de borne de degré
sur p²|N) ⟹ (TB)-ℤ structurellement plus dur, sandbox clos. J : doubles k=2 100% structurés (Mersenne) =
cible classification élémentaire. Rien au papier.*
