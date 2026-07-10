# STEP30 — κ_p cache-t-il une structure plus simple ? La décomposition TOUCHE LE FOND : deux noyaux (ι_p≤2 rigide / Poisson irréductible).

**Date :** 2026-07-02. Script `kappa_structure.py`. Question (GPT) : κ_p est-il, comme M_p et COSET
avant lui, le symptôme d'un invariant plus petit ? **Réponse : OUI pour le Type A (κ_p → ι_p≤2,
orbites d'involution), NON pour le Type B (κ_p=M_p=extrême de Poisson, irréductible). La chaîne de
décompositions M_p→COSET→κ_p→ι_p S'ARRÊTE ICI — et on voit POURQUOI (le noyau Type B est aléatoire).**

## Le candidat testé : ι_p = nombre d'ORBITES D'INVOLUTION {δ₀, e−δ₀}

STEP26 : δ↔e−δ forcé (1+2^{e−δ}=2^{−δ}(1+2^δ)). Les δ-classes actives se regroupent en orbites
{δ₀,e−δ₀}. ι_p = # d'orbites (≤ κ_p). Données L=160 (M_p≥4) :

| régime | exemples | e_p | M_p | κ_p | **ι_p** | δ-classes / orbites |
|---|---|---|---|---|---|---|
| **A (structuré)** | 257 | 16 | **11** | 3 | **2** | {0},{7,9} |
| | 683 | 22 | 8 | 3 | **2** | {0},{10,12} |
| | 8191 | 13 | 7 | 2 | **1** | {1,12} (1 paire) |
| | 241 | 24 | 7 | 1 | **1** | {12} |
| **B (générique)** | 163 | 162 | 4 | 4 | **4** | {7},{20},{21},{85} (4 singletons) |
| | 173,179,193… | ~e≈p | 4 | 4 | 4 | 4 singletons, AUCUN appariement |

**Type A : ι_p ∈ {1,2} même quand M_p=11.** Le vrai nombre de degrés de liberté est ≤2 ; M_p est
gonflé par la LONGUEUR des PA (⌊L/e_p⌋), qui est bénigne (Σ⌊L/e⌋=o(L²), STEP26-lit). ι_p RÉDUIT κ_p.

**Type B : ι_p = κ_p = M_p (Poisson).** Aucune orbite d'involution : le partenaire e−δ≈p≫L est **HORS
DE LA BOÎTE** (a+δ≤L). La boîte exclut les partenaires ⟹ pas de structure à retirer ⟹ ι_p ne réduit
rien. Les 4 coïncidences sont indépendantes (extrême de Poisson, STEP24/28).

## Pourquoi la décomposition S'ARRÊTE (réponse à « κ cache-t-il plus simple ? »)

- **M_p → COSET → κ_p → ι_p** : chaque étape a retiré une redondance (STEP25-26). ι_p est la fin de
  cette chaîne **pour le Type A** : ι_p≤2, ~3 patrons canoniques seulement (classe seule / paire
  d'involution / {0}+paire — EXP 2). C'est un noyau RIGIDE et minuscule. La perturbation (EXP 3) le
  casse : retirer un δ d'une PA brise l'alignement p-adique (la fibre s'effondre) — rigidité forte.
- **Type B : rien à décomposer.** ι_p=κ_p=M_p=extrême de Poisson (≈4, ~log L/loglogL). C'est
  l'aléa pur : les M_p coïncidences sont indépendantes (STEP24 : queue super-Poisson ; STEP28 :
  box-aveugle). **Il n'y a PAS de structure plus simple cachée — le désordre EST l'objet.**

Donc κ_p n'est PAS un « symptôme uniforme » d'un invariant plus petit : il se SCINDE en deux noyaux
de nature opposée :
1. **Noyau A (rigide) : ι_p ≤ 2.** Structure algébrique (involution + ≤1 orbite extra). Compris.
2. **Noyau B (aléatoire) : Poisson extreme.** Irréductible par nature (grande déviation).

## EXP 4 — incompatibilités / coexistence

- ι_p=1 : e_p moy 32 ; ι_p≥2 : e_p moy 82. La multi-orbite corrèle avec e_p PLUS GRAND (plus de
  place pour une 2ᵉ coïncidence), mais reste ≤2 pour les gros-M_p (Type A pur).
- La classe δ≡0 (paires b≡a mod e, i.e. diagonale 2^{a+1}) est le « point fixe » récurrent
  (233,257,281,673,683,1613,2731,4051) — l'orbite {0} du patron « 0+paire ».
- **Règle empirique :** un gros M_p (≥7) ⟹ Type A ⟹ ι_p≤2 (rigide) ; un κ_p qui « grandit » (4→6)
  ⟹ Type B ⟹ Poisson. Les deux ne se mélangent pas.

## Croissance : ι_p ne bat pas κ_p dans le PIRE cas

max κ_p = 4,4,4,6 ; max ι_p = 4,4,4,5 (L=80,120,160,200). Quasi identiques : le pire cas est **Type
B** (Poisson), où ι=κ. Donc ι_p **n'améliore pas la borne worst-case** (toujours Poisson) — il
EXPLIQUE la structure (Type A rigide) sans réduire le noyau irréductible (Type B).

## Verdict (questions du plan)

- **κ_p grand par beaucoup de PA, ou peu de PA compatibles ?** Type A : PEU (ι_p≤2, PA longues) ;
  Type B : « beaucoup » de singletons indépendants (Poisson), pas de compatibilité — juste de l'aléa.
- **Combien de patrons (EXP 2) ?** Type A : ~3 canoniques (classe/paire/0+paire). Type B : aucun
  (k singletons). Classification finie POUR LE STRUCTURÉ.
- **Rigidité (EXP 3) ?** Type A : forte (PA p-adiques, perturbation → effondrement). Type B : les
  points sont déjà « indépendants » (aléa).
- **Base minimale (EXP 5) ?** Type A : ι_p≤2 relations génératrices (involution + ≤1). Type B : pas
  de base plus petite (κ_p=M_p irréductible).
- **κ_p est-il le bon invariant / cache-t-il plus simple ?**
  - **Type A : NON — ι_p≤2 est le vrai invariant** (κ_p et M_p gonflés par ⌊L/e⌋, bénin).
  - **Type B : OUI, κ_p=M_p EST fondamental** = extrême de Poisson, irréductible (max-vs-énergie).
- **STATUT : la décomposition TOUCHE LE FOND.** Contrairement à M_p et COSET (qui cachaient une
  structure), κ_p ne cache PAS un invariant uniformément plus petit : il se scinde en {ι_p≤2 rigide
  (compris)} ⊕ {Poisson (irréductible)}. Le « mur » qui changeait de visage a atteint sa forme
  finale : **le noyau irréductible est le régime générique (Poisson), et on peut prouver qu'il ne
  cache rien** (l'involution qui structure le Type A est box-exclue en Type B).

## Portée pour #11

Les deux noyaux mappent EXACTEMENT les deux termes de la réduction M″ (STEP27) :
- Type A (ι_p≤2, M_p≈⌊L/e⌋) → terme Σ⌊L/e_p⌋ = o(L²) **acquis** (STEP26-lit).
- Type B (Poisson, M_p=o(log L)) → terme excès·#{M_p≥2} = o(L²) **si** l'extrême de Poisson est
  o(log L) — le seul point non prouvé, désormais identifié comme **irréductiblement probabiliste**.

Donc κ n'était pas « le dernier verrou » monolithique : la moitié structurée (Type A) est comprise
et bénigne ; le vrai verrou est l'extrême de Poisson générique (Type B), qui ne se décompose plus.

---
*Script kappa_structure.py. κ_p se scinde : Type A → ι_p≤2 (orbites d'involution, rigide, ~3 patrons,
compris) ; Type B → κ_p=M_p=Poisson (irréductible, involution box-exclue). La chaîne de décompositions
s'arrête ; le noyau final est probabiliste (générique), non structurel. PAPER intact.*
