# STEP45 — Clarification (4e auto-correction) : E₂/L* N'EST PAS le verrou. Le vrai verrou est maxM_B = o(log L) (l'extrême, moments d'ordre élevé). E₂^tot = Θ(L³/logL) = ω(L²).

**Date :** 2026-07-04. Analyse (déclenchée par le prompt LaTeX « borner L* pour E₂=o(L²) »).
**Résultat : le cadrage de STEP38-44 (et du prompt) est imprécis. (1) E₂^tot n'est PAS o(L²) — c'est
Θ(L³/logL)=ω(L²). (2) E₂ (=L*) n'est PAS la quantité contraignante : #{M_p≥2}≤π(L²) borne le terme
k=2 GRATUITEMENT. Le vrai verrou est maxM_B = o(log L) (l'EXTRÊME), contrôlé par les moments d'ordre
k~logL/loglogL, pas par E₂. E₂ est le cas k=2 : le plus facile, témoin du mécanisme, mais ni suffisant
ni contraignant.**

## 1. E₂^tot = Θ(L³/logL) = ω(L²), pas o(L²)

Mesuré (STEP43-44) : main/(L³/logL) ≈ 0.06 stable ⟹ E₂^tot ≈ 0.06·L³/logL. À L=140 : E₂^tot=31162,
L²=19600, L³/logL=555000. Donc **E₂^tot ≈ 1.6·L² et croît comme L³/logL = ω(L²)**. La cible « E₂=o(L²) »
(prompt) est IMPOSSIBLE. E₂^tot est censé être Θ(L³/logL) — c'est le bon comportement, pas o(L²).

## 2. La réduction ne passe PAS par E₂ (le compte exact)

M″_B = Σ_{p∈(L,L²], e_p>L}(M_p−1) doit être o(L²). Or :
$$M''_B=\sum_{k\ge2}\#\{p:M_p\ge k\},\qquad \#\{p:M_p\ge k\}\le\pi(L^2)\ \text{(pas plus de premiers)}.$$
- **Terme k=2 :** #{M_p≥2} ≤ π(L²) = L²/(2logL) = o(L²). **GRATUIT — E₂ (nombre de PAIRES en collision)
  n'intervient pas.** Ce qui compte est #{PREMIERS avec collision}, borné par π(L²).
- **Somme :** M″_B ≤ Σ_{k=2}^{maxM_B}π(L²) = (maxM_B−1)·π(L²). Donc
$$\boxed{M''_B=o(L^2)\ \Longleftarrow\ \max_B M_p=o(\log L).}$$

**Le verrou est maxM_B = o(log L)** — l'EXTRÊME. E₂^tot (=Σ_pΔ_p, le total des collisions, ~L³/logL)
peut être aussi grand qu'il veut : ça ne borne PAS maxM_B (un premier peut avoir beaucoup de collisions
étalées, M_p petit ; ou peu, concentrées, M_p grand — c'est le mur max-vs-énergie de STEP19 !).

## 3. Donc E₂/L* était le mauvais focus (STEP38-44)

E₂ (=L*) est la **k=2 énergie**. Elle borne #{M_p≥2}, mais #{M_p≥2}≤π(L²) est gratuit. **Prouver
E₂=O(L³/logL) ne ferme RIEN** : ni o(L²) (c'est ω(L²)), ni maxM_B (énergie ≠ max). Le mur max-vs-énergie
(STEP19-28) disait exactement ça : l'énergie (E₂) ne contrôle pas le max. J'ai oublié ma propre leçon
en STEP38-44 en focalisant sur E₂.

**Ce qui reste vrai et utile de STEP38-44 :** (a) le MÉCANISME (E₂=densité=Sidon/ℤ, STEP43) est le bon
et s'étend à tout k ; (b) le grand crible générique échoue (portée exp) pour tout k ; (c) L* est un
énoncé autonome intéressant. Mais L* n'est pas la clé de #11.

## 4. Le vrai verrou, précisément : l'extrême via les moments d'ordre élevé

maxM_B = max{k : E_k^tot ≥ 1} (STEP33). E_k^null ~ L³/(2^k k! logL) croise 1 à k*~3logL/loglogL.
Donc maxM_B ≤ k* = O(logL/loglogL) = o(logL) SI E_k^tot ≤ C^k E_k^null pour k jusqu'à k*. **Le cas
CONTRAIGNANT est k~k*~logL/loglogL (l'extrême), PAS k=2.** C'est un énoncé de GRANDE DÉVIATION (la
multiplicité max), pas de variance. Le crible du carré spécialisé doit être appliqué à l'ORDRE k*,
pas seulement k=2.

## 5. Réponse à la question finale du prompt (reformulée honnêtement)

- **« Borne L* meilleure que O(L⁴) suffisante pour E₂=o(L²) ? »** Question mal posée : E₂ est ω(L²)
  (pas o(L²)), et E₂ n'est pas requis (k=2 gratuit via π(L²)).
- **La vraie question :** peut-on prouver maxM_B = o(logL) ? ⟸ E_k^tot ≤ C^k E_k^null pour k~logL/loglogL.
- **Quel outil ?** PAS une borne d'énergie E₂ (mur max-vs-énergie). Il faut contrôler l'EXTRÊME
  (multiplicité max), i.e. les moments factoriels d'ordre k*~logL/loglogL — une **grande déviation**
  sur la distribution de multiplicité de {2^a+2^b mod p²}. Le crible du carré spécialisé (Heath-Brown)
  s'applique à l'ordre k* (2k*-uplets de puissances), pas k=2. Le mécanisme (Sidon/ℤ ⟹ densité) le
  soutient à tout ordre (STEP43, base-indép STEP42), mais la PREUVE à l'ordre k* est le cœur dur.

## Verdict

- **E₂^tot = o(L²) ?** NON — c'est Θ(L³/logL)=ω(L²). Cible du prompt impossible.
- **E₂ (L*) est-il le verrou ?** NON — #{M_p≥2}≤π(L²) gratuit ; E₂ (énergie) ≠ maxM_B (extrême).
- **Le vrai verrou ?** maxM_B = o(logL) ⟸ E_k^tot ≤ C^k E_k^null à l'ordre k*~logL/loglogL (grande
  déviation, pas variance). Le crible/Rudin à l'ordre k*, pas k=2.
- **STATUT : RESTE OUVERT, recentré (4e auto-correction).** STEP38-44 étudiaient E₂ = le cas facile /
  témoin du mécanisme, mais PAS le verrou. Le verrou est l'extrême (moments d'ordre logL/loglogL).
  Le mur max-vs-énergie (STEP19) s'applique : E₂ ne suffit jamais, il faut le max.

---
*Analyse. E₂^tot=Θ(L³/logL)=ω(L²) (pas o(L²)). E₂ pas le verrou : #{M_p≥2}≤π(L²) gratuit. Vrai verrou
= maxM_B=o(logL) ⟸ E_k^tot≤C^k E_k^null à l'ordre k*~logL/loglogL (extrême/grande déviation, pas
variance). STEP38-44 focalisaient sur le cas facile k=2 (témoin du mécanisme) mais pas contraignant.
Format LaTeX du prompt fige une imprécision (2e moment vs énergie). PAPER/Lean non touchés.*
