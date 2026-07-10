# STEP33bis — Appliquer la littérature (Dubhashi-Ranjan, Méliot-Nikeghbali-Visentin, Untrau) : les trois sont du côté PROBABILISTE/SOMMES COMPLÈTES ; notre résidu est DÉTERMINISTE/SOMMES INCOMPLÈTES. La chaîne ne ferme pas.

**Date :** 2026-07-02. Lecture + vérification logique (pas de code). **AVERTISSEMENT : pas d'accès web
en session ; je raisonne à partir de la connaissance des domaines (association négative ; mod-φ de
Méliot-Nikeghbali ; équidistribution de sommes de sous-groupes), sans citer d'énoncés exacts non
vérifiables.** Conclusion : les trois références fournissent le CADRE et la CIBLE mais **aucune ne
donne l'input arithmétique manquant** — une borne sur les sommes exponentielles INCOMPLÈTES (courtes)
de la suite lacunaire {2^k mod p²} aux ordres k=2..logL/loglogL. RESTE OUVERT ; maillon précisé.

## Rappel du résidu (STEP33) et de ce qu'il faut

M″=o(L²) ⟸ maxM_B=O(logL/loglogL) ⟸ **E_k^tot ≤ C^k E_k^Poisson** (moments factoriels sous-Poisson),
où E_k^tot = Σ_{p Type B} Σ_r C(N_p(r),k). Deux ingrédients requis :
(NA) l'occupation des fibres est négativement associée ⟹ moments factoriels ≤ Poisson ;
(EQ) les {2^a+2^b mod p²} sont équidistribués (pour que l'arithmétique imite le modèle aléatoire).

## Réf. A — Dubhashi-Ranjan 1998 : NA du modèle ALÉATOIRE, PAS du déterministe

Ce qu'ils établissent (solide, connu) : si m balles sont jetées **indépendamment et uniformément**
dans n urnes, les occupations (B_1,…,B_n) sont **négativement associées** ⟹ E[Πf_i(B_i)] ≤ ΠE[f_i(B_i)]
pour f_i monotones ⟹ moments factoriels et queues ≤ cas indépendant (Poisson). **C'est exactement
(NA) — mais pour le modèle ALÉATOIRE.**

**Le blocage (que le plan anticipe, ÉTAPE 4) :** nos « balles » 2^a+2^b mod p² sont **DÉTERMINISTES**
(nombres fixés, pas de tirage). L'association négative est une propriété d'une LOI JOINTE de variables
aléatoires ; sans espace de probabilité, « NA » est vide/indéfinie pour notre suite. **D-R ne s'applique
PAS.** Il fournit la CIBLE (à quoi ressemble le sous-Poisson attendu) et VALIDE l'heuristique (STEP33 :
E_k^tot ≤ Poisson empiriquement), mais **ne PROUVE rien sur la suite arithmétique**.

Idem Pemantle 2000 (« Towards a theory of negative dependence ») et Borcea-Brändén-Liggett 2009
(mesures fortement Rayleigh / polynômes stables) : tous PROBABILISTES, exigent une mesure aléatoire.
Notre objet est déterministe ⟹ inapplicables tels quels. **Pas de version « déterministe » de la NA
qui s'appliquerait sans passer par l'équidistribution.**

## Réf. C — Untrau 2023 : sommes de sous-groupe COMPLÈTES, pas incomplètes

Ce que cette ligne de travaux établit (équidistribution de sommes exponentielles indexées par un
sous-groupe H⊂(ℤ/qℤ)* de cardinal donné T) : la distribution des sommes **COMPLÈTES**
Σ_{h∈H} e(nh/q) (les T termes), quand n varie, converge vers une loi limite (type Sato-Tate/gaussienne),
normalisée par √T. C'est une équidistribution **statistique**, pas une borne sup uniforme.

**Deux blocages pour nous :**
1. **Somme COMPLÈTE vs INCOMPLÈTE.** Untrau : Σ sur TOUT H (T termes). Nous : S_p(t)=Σ_{k=0}^L e(t·2^k/p²),
   seulement **L+1 ≪ T=ord_{p²}(2)≈p²** termes (Type B). Les sommes **incomplètes/courtes** sont un
   problème DIFFÉRENT et plus dur (régime Bourgain-Garaev, STEP21). L'équidistribution des sommes
   complètes ne borne PAS une somme partielle d'un générateur spécifique.
2. **Équidistribution ≠ borne sup.** Même complète, une loi limite dit « la plupart des sommes ~√T »,
   pas « toutes ≤ C√T·p^{−δ} ». Pour l'extrême Poisson il faut contrôler les MOMENTS (ordre k), i.e.
   Σ_t|S_p(t)|^{2k} sur la part non-triviale — un contrôle des sommes incomplètes à tout ordre.

⟹ **Untrau ne s'applique pas** : il concerne les sommes complètes, notre difficulté est la partie
incomplète courte (STEP31 avait mesuré le sup √L empirique, mais le PROUVER = BG, non fourni ici).

## Réf. B — Méliot-Nikeghbali-Visentin 2022 : mod-Poisson = CADRE, pas l'input

La théorie mod-φ (Méliot-Nikeghbali) : X_n est mod-Poisson convergente si E[e^{izX_n}]e^{−λ_n(e^{iz}−1)}
→ ψ(z). Ça donne des Chen-Stein d'ordre supérieur, TCL locaux, grandes déviations PRÉCIS ⟹ donnerait
l'extrême exact O(logL/loglogL) et les meilleures constantes. **MAIS l'input requis est la convergence
mod-Poisson de notre processus de collisions**, i.e. le contrôle des CUMULANTS/fonction caractéristique
= exactement les moments factoriels E_k = les sommes exponentielles incomplètes. **Le cadre PACKAGE la
difficulté (meilleure erreur une fois l'input acquis), il ne la CONTOURNE pas.**

## La chaîne, maillon par maillon

| Maillon | Statut | Référence qui aiderait | Fournie ? |
|---|---|---|---|
| Type A (Σ⌊L/e⌋+ι_p≤2) | **acquis** (STEP26-lit, 30) | — | — |
| (NA) moments factoriels ≤ Poisson | cible claire | A (D-R) | **NON** (aléatoire≠déterministe) |
| (EQ) k=2 : variance Poisson | **quasi-acquis** (Sidon/ℤ, STEP32) | — | oui (élémentaire) |
| (EQ) k≥3 : équidistribution d'ordre k | **MANQUANT** | C (Untrau) / BG | **NON** (sommes complètes only) |
| extrême O(logL/loglogL) sous (NA)+(EQ) | conditionnel | B (mod-Poisson) | cadre oui, input non |
| M″=o(L²) ⟹ #11 | conditionnel | — | — |

**Le maillon manquant, précisément :** (EQ) aux ordres k≥3 = **une borne sur les sommes exponentielles
INCOMPLÈTES Σ_{k≤L} e(t·2^k/p²) suffisante pour que les moments factoriels E_k des fibres restent
Poisson jusqu'à k~logL/loglogL.** C'est un énoncé sur les sommes courtes d'une suite lacunaire mod p²
— le cœur dur de Bourgain-Garaev (STEP21), NON couvert par ces trois références.

## Verdict (format demandé)

- **Dubhashi-Ranjan applicable ?** **NON.** Donne la NA du modèle ALÉATOIRE (⟹ sous-Poisson), mais nos
  fibres sont DÉTERMINISTES (pas de tirage) ⟹ NA indéfinie. Fournit la cible/heuristique, pas la preuve.
  (Pemantle, Borcea-Brändén-Liggett : idem, probabilistes.)
- **Untrau donne une borne sur sommes incomplètes ?** **NON.** Ses résultats portent sur les sommes de
  sous-groupe COMPLÈTES (T termes) et l'équidistribution statistique ; nous avons des sommes INCOMPLÈTES
  courtes (L+1≪T) et il faut des bornes de MOMENTS, pas une loi limite. Régime BG, non traité.
- **Méliot-Nikeghbali-Visentin ?** Cadre mod-Poisson PERTINENT (donnerait l'extrême exact), mais exige
  la convergence mod-Poisson = les moments/sommes incomplètes en INPUT. Package, ne résout pas.
- **Chaîne complète : M″ prouvé ?** **NON.** k=2 (variance) quasi-acquis (Sidon/ℤ) ; k≥3 (extrême)
  bloqué sur (EQ) d'ordre supérieur.
- **Quel maillon manque exactement ?** **(EQ) aux ordres k≥3 : borne sur sommes exponentielles
  incomplètes de {2^k mod p²} garantissant E_k^tot ≤ C^k E_k^Poisson jusqu'à k~logL/loglogL.** Ni A
  (probabiliste), ni C (sommes complètes), ni B (cadre) ne le fournissent.
- **STATUT : RESTE OUVERT.** Les trois références confirment que le CADRE (sous-Poisson via NA +
  équidistribution ; extrême via mod-Poisson) est le bon et standard, mais **le résidu est un énoncé
  d'analyse (sommes exponentielles courtes lacunaires mod p²) que la littérature citée ne couvre pas**.
  Réf. A = cible/heuristique ; Réf. C = mauvais régime (complet≠incomplet) ; Réf. B = cadre sans input.

## Note honnête

Le clivage est net et récurrent : depuis STEP19, chaque outil est soit un outil de « densité/2ᵉ moment/
loi » (énergie, covering, NA, mod-Poisson) — qui décrit la STRUCTURE et confirme l'attendu — soit il
faudrait un input d'ÉQUIDISTRIBUTION arithmétique (sommes exponentielles incomplètes) — qui reste le
verrou. Les trois références sont du premier type. Le problème #11 (every-n) est CONDITIONNEL à une
borne de sommes exponentielles courtes pour {2^k mod p²}, empiriquement vraie (sup √L, STEP31 ;
sous-Poisson tous ordres, STEP33) mais non prouvée. C'est le mur, et il est analytique (BG), pas
probabiliste — les outils probabilistes le confirment sans le franchir.

---
*Lecture logique (pas d'accès web ; raisonnement de domaine). D-R : NA aléatoire ≠ déterministe.
Untrau : sommes complètes ≠ incomplètes courtes. Méliot : cadre mod-Poisson, input manquant. Maillon
manquant = équidistribution d'ordre k≥3 = sommes exponentielles incomplètes lacunaires mod p² (BG).
RESTE OUVERT, conditionnel à cet input analytique. PAPER intact.*
