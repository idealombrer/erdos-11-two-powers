# STEP47 — Attaque spécialiste : le verrou se REFORMULE proprement en une seule inégalité (EM=O(1) via décroissance géométrique de #{M_p≥k}). Cible plus concrète, pas encore prouvée.

**Date :** 2026-07-04. Script `geometric_decay.py`. Tentative d'attaque (demande de l'user). **Résultat :
pas de preuve, MAIS une vraie simplification du verrou. La distribution #{M_p≥k} (Type B) décroît
GÉOMÉTRIQUEMENT (ratio ρ≈0.08, stable) ⟹ EM=1.09=O(1) ⟹ M″_B=o(L²). Le verrou se réduit à UNE
inégalité : #{M_p≥3} ≤ ρ·#{M_p≥2}, ρ<1 (double-vs-triple coïncidence de diviseurs carrés). C'est plus
concret que la tour E_k ou l'extrême maxM_B, mais la preuve touche encore le cœur diviseurs-carrés.**

## Données (Type B, L=60→180, n jusqu'à ~10^54)

| L | #{M_p≥2} | #{M_p≥3} | #{M_p≥4} | #{M_p≥5} | ratio ≥3/≥2 | **EM** | M″_B/L² |
|---|---|---|---|---|---|---|---|
| 60 | 47 | 4 | 0 | 0 | 0.085 | 1.09 | 0.0142 |
| 100 | 118 | 9 | 1 | 0 | 0.076 | 1.08 | 0.0128 |
| 140 | 214 | 18 | 2 | 0 | 0.084 | 1.09 | 0.0119 |
| 180 | 304 | 26 | 2 | 0 | 0.086 | 1.09 | 0.0102 |

- **ρ = #{M_p≥3}/#{M_p≥2} ≈ 0.08**, stable. #{M_p≥5}=0 partout. Décroissance géométrique franche.
- **EM = 1.08–1.09, remarquablement stable.** Borne géométrique 1/(1−ρ) prédit EM à 0.01 près.
- M″_B/L² décroît (0.0142→0.0102) → 0 ; M″_B/(L²/logL) ≈ 0.055 constant ⟹ **M″_B = Θ(L²/logL) = o(L²)**.

## La reformulation du verrou (le gain)

$$M''_B=\sum_{k\ge2}\#\{M_p\ge k\},\quad \#\{M_p\ge2\}\le\pi(L^2)=o(L^2).$$
Si **#{M_p≥k+1} ≤ ρ·#{M_p≥k}** avec ρ<1 (décroissance géométrique), alors
$$M''_B\le\frac{\#\{M_p\ge2\}}{1-\rho}\le\frac{\pi(L^2)}{1-\rho}=o(L^2)\ \Rightarrow\ \text{every-n Type B}.$$
⟹ **Le verrou entier se réduit à : #{M_p≥3} ≤ ρ·#{M_p≥2}, ρ<1** (empiriquement ρ≈0.08). C'est UNE
inégalité, pas la tour infinie E_k ni l'extrême maxM_B. (Et #{M_p≥4},#{M_p≥5} minuscules/nuls : la
queue au-delà de 3 est négligeable en pratique.)

## Interprétation arithmétique de la cible

- **#{M_p≥2}** = #{p∈(L,L²]: p²|N pour un quadruplet N=2^a+2^b−2^c−2^d≠0} = premiers à UNE coïncidence.
- **#{M_p≥3}** = #{p: p²|N₂ ET p²|N₃} (N₂,N₃ deux quadruplet-différences partageant une paire) =
  premiers à DEUX coïncidences ⟹ p²|gcd(N₂,N₃) ⟹ p² diviseur carré de DEUX combinaisons.
- Cible **#{M_p≥3} ≤ ρ·#{M_p≥2}** = « avoir deux diviseurs-carrés-coïncidents est ≤ ρ fois avoir un ».
  Moralement : la 2ᵉ coïncidence est ~λ fois plus rare (λ=densité), λ<1 en Type B. Mais λ varie sur p ;
  la moyenne pondérée donne ρ≈0.08.

## Honnêteté : prouvable ?

**Pas par moi, pas élémentairement.** La cible #{M_p≥3} ≤ ρ·#{M_p≥2} est un énoncé de coïncidence de
diviseurs carrés (combien de p² divisent DEUX quadruplet-combinaisons vs UNE), qui touche le même cœur
que L*/le crible du carré — mais à un niveau plus concret et fini (un ratio, pas une tour). Une preuve
demanderait de contrôler #{p²|gcd(N₂,N₃)} sommé sur les configs — un comptage de type crible du carré /
grand crible, hors de portée élémentaire. **Ce n'est donc pas une percée**, mais c'est la
**reformulation la plus concrète du verrou** obtenue : d'« EM=o(log L) » (abstrait) à « une inégalité
géométrique #{M_p≥3}≤ρ#{M_p≥2} » (spécifique, checkable).

## Ce que la tentative a apporté (bilan de l'attaque spécialiste)

- **Positif :** le verrou n'est PAS la tour E_k ni l'extrême maxM_B (mes cadrages STEP38-45) mais UNE
  inégalité géométrique EM=O(1), et la queue #{M_p≥k} est négligeable dès k=4 (empiriquement). Cible
  la plus nette de la campagne. EM=1.09 d'une stabilité frappante (n~10^54).
- **Négatif honnête :** la preuve de #{M_p≥3}≤ρ#{M_p≥2} touche encore le cœur diviseurs-carrés
  (comptage de coïncidences p²|gcd), non élémentaire. Pas de percée.
- **Verdict :** attaque spécialiste = pas de preuve, mais reformulation concrète maximale. Le verrou
  est UNE inégalité de coïncidence de diviseurs carrés, empiriquement écrasante (ρ≈0.08, EM≈1.09
  stables), au front analytique.

## Verdict (statut)

- **EM = O(1) ?** OUI empiriquement (1.09, stable n~10^54), via décroissance géométrique ρ≈0.08.
- **⟹ M″_B = o(L²) ⟹ every-n Type B ?** OUI si #{M_p≥3}≤ρ#{M_p≥2} prouvé.
- **Prouvé ?** NON. Cible = coïncidence de diviseurs carrés (crible du carré), plus concrète mais même
  cœur. RESTE OUVERT, cible affinée à UNE inégalité.

---
*Script geometric_decay.py. #{M_p≥k} (Type B) décroît géométriquement (ρ≈0.08 stable), EM=1.09=O(1),
M″_B=Θ(L²/logL)=o(L²). Verrou reformulé en UNE inégalité #{M_p≥3}≤ρ#{M_p≥2} (double-vs-triple diviseur
carré) — la plus concrète de la campagne, mais preuve = crible du carré, non élémentaire. PAPER/Lean
non touchés.*
