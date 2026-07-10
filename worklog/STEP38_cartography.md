# STEP38 — Cartographie du verrou TB : à quel théorème connu ressemble-t-il ?

**Date :** 2026-07-03. Analyse/bibliographie (pas de calcul ; pas d'accès web — raisonnement de
domaine, sans énoncés/constantes non vérifiables). **Ne touche pas PAPER/Lean.**

## L'objet, isolé de #11

Pour p premier avec ord_p(2)>L (Type B), soit **G = {2^0,…,2^L mod p²}** = segment initial de longueur
L+1 de l'orbite lacunaire de 2 dans (ℤ/p²)* (les L+1 éléments sont distincts car ord_{p²}(2)=p·ord_p(2)>L).
Soit S=G+G (sumset), N_p(r)=#{(a,b):2^a+2^b≡r}. **Verrou TB :**
$$E_k^{tot}=\!\!\sum_{\substack{p\in(L,L^2]\\ \mathrm{ord}_p(2)>L}}\sum_r\binom{N_p(r)}{k}\ \le\ C^kE_k^{null}
\quad(k\le k^\ast\sim\tfrac{3\log L}{\log\log L}).$$
Forme équivalente (Fourier) : avec S_p(t)=Σ_{k≤L}e_{p²}(t·2^k), la 2k-énergie additive de G est
E_k(G)=(1/p²)Σ_t|S_p(t)|^{2k}, et le verrou dit qu'**en moyenne sur les modules carrés p² (p∈(L,L²]),
les énergies additives d'ordre k du segment lacunaire G sont au niveau aléatoire (diagonal), à C^k près.**
Régime : longueur L+1 ∈ (q^{1/4}, q^{1/2}], q=p². Trois ingrédients : lacunarité × sommes incomplètes
mod p² × moyenne sur modules carrés.

## Balayage des domaines : théorème proche + gap précis

### A. Suites lacunaires (Rudin Λ(p), Bourgain découplage) — **le plus proche pour la FORME**
- **Proche :** Rudin (1960) : {2^k} est Λ(p) pour tout p ⟹ sur le tore, ‖Σ_{k≤L}a_ke(2^kθ)‖_{2k} ≪
  √k‖a‖₂, i.e. **E_k(G)_ℤ ≤ (Ck)^k(L+1)^k** — exactement la forme voulue, et PROUVÉE (sur ℤ/tore).
- **Insuffisant :** c'est sur le TORE (ℤ), pas mod p². Le transfert exige la **dissociativité** de
  {2^k} mod p² (aucune petite combinaison Σε_k2^k≡0 mod p²), qui ÉCHOUE pour p petit (p²<2^L) —
  ce sont précisément les collisions arithmétiques. Rudin donne la DIAGONALE (terme principal),
  pas l'excès modulaire. (STEP34 : E_k^pow ≈ diagonale + excès mod p² ; Rudin borne la diagonale.)
- **Hypothèse manquante :** #{Σε_k2^k≡0 mod p²} = O(diagonale·C^k) en moyenne sur p = comptage de
  diviseurs carrés. **Réaliste (c)** : vrai empiriquement (au bon ordre), mais c'est le contenu
  arithmétique, non fourni par Rudin.

### B. Sommes exponentielles incomplètes mod p² (Korobov, Bourgain-Garaev-Konyagin-Shparlinski)
- **Proche :** bornes pour Σ_{k≤N}e_q(a·g^k). Complètes (N=ord) : Weil/Konyagin. Incomplètes N≥q^ε :
  BGKS donnent |Σ|≤N·q^{-δ} sous conditions.
- **Insuffisant :** notre longueur L+1∈(q^{1/4},q^{1/2}], modulo p² (pas p). Korobov (√q log q=p log p)
  est TRIVIAL (≤p termes). Les bornes sup incomplètes pour la fonction exponentielle mod p² dans ce
  régime court sont **au/​sous le front** des résultats inconditionnels (déjà noté PAPER §7 / STEP21).
- **Hypothèse manquante :** annulation √L du sup (empirique STEP31-32), = problème BG incomplet.
  **Ouverte en général (b)** pour le sup ; mais on n'a besoin QUE de la moyenne quadratique (voir E,
  et ÉTAPE 2), plus faible.

### C. Higher additive energies / Vinogradov mean value (Wooley, Bourgain-Demeter-Guth) — **NE s'applique PAS**
- **Proche :** VMVT/découplage bornent J_{s,k}(N)=#solutions du SYSTÈME Σx_i^j=Σy_i^j (j≤k) — énergies
  de la **courbe des moments** {(n,n²,…,n^k)}, suite **POLYNOMIALE**.
- **Insuffisant :** {2^k} est **GÉOMÉTRIQUE**, pas polynomiale. Découplage/efficient congruencing
  exploitent la COURBURE polynomiale ; une progression géométrique n'en a pas — elle est lacunaire.
  L'énergie d'une PG est gouvernée par la lacunarité (Rudin, domaine A), pas par le découplage.
- **Verdict : domaine INADAPTÉ.** La machinerie moderne (Wooley/BDG) ne touche pas le géométrique.
  (Négatif important : ne pas espérer VMVT ici.)

### D. Hypergraph containers (Balogh-Morris-Samotij, Saxton-Thomason) — **NE s'applique PAS**
- **Proche :** containers comptent COMBIEN d'ensembles ont peu de solutions à une équation (sum-free,
  sans k-AP…).
- **Insuffisant :** on a UN ensemble spécifique déterministe G={2^k mod p²} et on veut SON énergie ;
  les containers énumèrent des familles d'ensembles, ils ne bornent pas l'énergie d'un ensemble donné.
- **Verdict : mauvaise question.** Containers = énumération, pas analyse d'un ensemble fixe.

### E. Cumulants / dépendance négative (Méliot-Nikeghbali mod-Poisson, Dubhashi-Ranjan NA)
- **Proche :** balles-urnes est négativement associé ⟹ moments factoriels ≤ Poisson (D-R) ; mod-Poisson
  (M-N-V) donne Chen-Stein d'ordre sup ⟹ la FORME cible E_k≤C^kE_k^Poisson.
- **Insuffisant (STEP33bis, STEP33b) :** PROBABILISTE (modèle aléatoire requis). G est DÉTERMINISTE ;
  et empiriquement les N_p(r) ne sont PAS strictement NA (covariances >0 aux décalages arithmétiques).
- **Hypothèse manquante :** une pseudo-aléatoire déterministe donnant des cumulants bornés = l'input
  d'équidistribution (domaine B). **Se ramène à B.** (STEP33b : la NA n'est même pas nécessaire —
  Markov 1er moment suffit ; il ne reste que la borne de moment E_k = borne exp-sum.)

### F. Décorrélation lacunaire (Kahane, Salem-Zygmund)
- **Proche :** Salem-Zygmund/Kahane : Σa_ke(2^kθ) est asymptotiquement gaussienne ; {2^kθ mod 1} pour
  θ réel aléatoire sont ~indépendants — la « raison morale » du sous-Poisson.
- **Insuffisant :** vit sur le tore CONTINU (θ∈ℝ/ℤ, aléatoire). Mod p², « θ »=t/p² est un ensemble
  DISCRET arithmétique d'entiers t, pas un θ aléatoire. La décorrélation continue ne se transfère PAS
  aux racines p²-ièmes (structure arithmétique = les collisions).
- **Hypothèse manquante :** transfert continu→arithmétique = équidistribution mod p² = **domaine B**.
  Salem-Zygmund est la justification MORALE, pas une preuve mod p².

### G. Combinatoire probabiliste / graphes de dépendance (LLL, Janson)
- **Proche :** Janson/graphe de dépendance des événements 1[N_p(r)≥2].
- **Insuffisant (STEP33) :** voisinages ÉNORMES (ensemble de différences |D|~L²) ⟹ termes d'erreur
  grands (couplage ~1 par densité). Et probabiliste. Le 1er moment (Markov) CONTOURNE le graphe
  (STEP33) ⟹ cadre inutile.
- **Verdict : mauvais cadre** (graphe trop dense ; Markov le rend superflu).

## ÉTAPE 2 — Le domaine où l'écart est minimal : A × B

Les deux plus proches sont **A (Rudin/lacunaire)** et **B (grand crible mod p²)**, deux faces d'une
même pièce : **A donne la FORME** (E_k≤(Ck)^k(L+1)^k, prouvée sur le tore) ; **B est où vit
l'ARITHMÉTIQUE** (l'excès modulaire = comptage de diviseurs carrés). Formulation précise :

> **Le verrou TB ressemble à l'inégalité de Rudin Λ(2k) pour la suite lacunaire {2^k} (domaine A),
> à ceci près qu'elle doit valoir mod p² et non sur le tore ; l'écart exact entre les deux est le
> nombre de petites combinaisons Σε_k2^k ≡ 0 mod p² — un comptage de diviseurs carrés / de
> dissociativité (domaine B), en moyenne sur les modules carrés p², p∈(L,L²].**

Une identification plus précise côté B : la moyenne sur les **modules carrés p²** est exactement le
cadre du **grand crible à modules carrés** (Baier–Zhao ; Heath-Brown, square sieve) — un outil NOMMÉ.
Le grand crible standard donne le 2ᵉ moment (Parseval, trivial ici) ; il faut le 4ᵉ et les moments
supérieurs (énergies), i.e. **le combiner avec la lacunarité (Rudin) et contrôler la moyenne
quadratique des sommes de caractères incomplètes Σ_{j≤L}χ(2^j)** (terme d'erreur STEP35, ~L pas O(1)).

L'hypothèse manquante Z (l'excès modulaire au bon ordre) est de type **(c) : probablement vraie ici,
non un théorème citable en général.** Vraie empiriquement (E_k^tot/E_k^null≤1 à tout k) ; du ressort
du grand crible à modules carrés + Rudin ; le point non standard est la moyenne quadratique des sommes
de caractères courtes lacunaires (front BG en sup, plausible en moyenne quadratique).

## ÉTAPE 3 — Lemme intermédiaire naturel L*

Aucun théorème ne s'applique directement (A sur le tore ; B sans le 4ᵉ moment lacunaire). Le lemme qui
fait disparaître EXACTEMENT la partie arithmétique, laissant la partie Rudin (prouvée) :

> **L* (correction mod-p² de Rudin = grand crible du carré, cas k=2).**
> $$\sum_{N=2^a+2^b-2^c-2^d\neq0}\#\{p\in(L,L^2]:p^2\mid N\}\ =\ O\!\left(\frac{L^3}{\log L}\right).$$

- **Indépendant de #11 et intéressant en soi :** c'est un énoncé de **densité de diviseurs carrés de
  la forme quaternaire 2^a+2^b−2^c−2^d** (généralise STEP22 : ω₂(N)≤2, cas d'un seul N). C'est
  précisément la cible du crible du carré de Heath-Brown.
- **Ce qu'il ferait disparaître :** TOUT l'excès modulaire pour E_2. Avec L* et Rudin (diagonale),
  E_2^tot ≤ (diagonale ℤ) + (excès L*) = O(L³/logL) = O(E_2^null) ⟹ variance TB fermée.
- **Plus accessible que TB direct :** k=2 seulement, forme quaternaire explicite, outil dédié (HB).
  Les k≥3 suivent par l'itération STEP34-37 (p²|N₁,N₂ ⟹ p²|(N₁−N₂)), modulo la croissance de C^k.
- **Propriété suffisante de G :** « dissociativité en moyenne » — au plus O(Σ1/p²) des N=combinaison
  de 4 puissances ont un facteur carré p²>L² — plus faible que l'équidistribution forte, = grand crible.

## ÉTAPE 4 — Le verrou a-t-il déjà un nom ?

À ma connaissance (sans accès web), **non, pas sous un nom unique.** Les objets voisins nommés :
- **Énergie additive de sous-groupes multiplicatifs** (Heath-Brown–Konyagin, Shkredov) — mais pour le
  sous-groupe COMPLET H, énergie E_2 de H (pas de H+H), pas le segment initial incomplet {2^k,k≤L}.
- **Sum-product / Bourgain-Glibichuk-Konyagin** — |A+A||A·A|, pas les énergies d'ordre k d'un segment
  géométrique fixe.
- **Grand crible à modules carrés** (Baier-Zhao ; Heath-Brown square sieve) — le bon cadre pour la
  MOYENNE sur p², mais donne le 2ᵉ moment, pas les énergies lacunaires d'ordre supérieur.
- **Ensembles B_h[g] / Sidon mod q** — G est presque-Sidon ; l'excès est le défaut B_2[g].

⟹ Le verrou est un **HYBRIDE** à l'intersection de trois domaines bien étudiés — (lacunarité/Λ(p)) ×
(sommes exponentielles incomplètes mod p²) × (grand crible à modules carrés) — mais l'énoncé exact
(énergies additives d'ordre k d'un segment initial d'orbite lacunaire mod p², en moyenne sur p) n'a,
à ma connaissance, pas de nom standard. Le cœur non-standard est **la correction mod-p² de Rudin**.

## Verdict (format demandé)

- **A-G :** A (Rudin) = forme, sur le tore ; B (BGKS/grand crible p²) = arithmétique ; C (VMVT),
  D (containers), G (dépendance) INADAPTÉS ; E (cumulants), F (Salem-Zygmund) = justification morale,
  se ramènent à B.
- **Écart minimal :** **A × B** — Rudin Λ(2k) + grand crible à modules carrés (Baier-Zhao/Heath-Brown).
- **« Ressemble à X à ceci près que Z » :** ressemble à l'inégalité de **Rudin Λ(2k)** pour {2^k}, à
  ceci près qu'elle doit valoir **mod p² en moyenne sur les carrés** ; Z = borne de grand crible du
  carré sur les combinaisons de puissances (moyenne quadratique des sommes de caractères Σχ(2^j)).
- **Statut de Z :** **(c)** probablement vraie ici / pas un théorème citable ; empiriquement vraie ;
  du ressort du grand crible à modules carrés.
- **Lemme L* :** Σ_{N=2^a+2^b−2^c−2^d≠0}#{p∈(L,L²]:p²|N}=O(L³/logL) (crible du carré, k=2) —
  indépendant de #11, dédié à Heath-Brown, base de l'itération.
- **Nom existant ?** Non sous un nom unique ; hybride Λ(p)×exp-sums-mod-p²×grand-crible-carrés. Cœur
  non-standard = correction mod-p² de Rudin.
- **STATUT : RESTE OUVERT, mais localisé** — pas une nouvelle approche, une réduction de plus : TB =
  Rudin (acquis, tore) + L* (grand crible à modules carrés, cible nommée, ouverte ici mais réaliste).

---
*Analyse/bibliographie (pas de calcul, pas d'accès web). TB = hybride Rudin Λ(2k) × grand crible à
modules carrés (Baier-Zhao/Heath-Brown). Écart = correction mod-p² de Rudin = L* (densité de diviseurs
carrés de 2^a+2^b−2^c−2^d). C (VMVT/découplage), D (containers), G (dépendance) inadaptés ;
E (cumulants), F (Salem-Zygmund) = moral, ⟶ B. Pas de nom unique. PAPER/Lean non touchés.*
