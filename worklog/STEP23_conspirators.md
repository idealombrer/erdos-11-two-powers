# STEP23 — Caractérisation des conspirateurs : haut M_p ⟺ petit ordre. Pas de nouvelle voie.

**Date :** 2026-06-24. Dernière piste : structure multiplicative (degré 1) de $N$ pour les
premiers à $M_p$ élevé. **Résultat : haut $M_p$ ⟺ petit $\mathrm{ord}_p(2)$ (corr$(M_p,1/e_p)=+0{,}71$),
mais la « structure $2^k-1$ » des $N$ n'est que $p\mid N$ redit ; et des premiers à GRAND ordre
sont aussi conspirateurs ⟹ pas de réduction nouvelle. Conforme à l'estimation 5-10 % : jolie
caractérisation, pas de fermeture.** Script `check_conspirators.py`. PAPER : mis à jour cette session.

## Donnée (L=60)
- **corr$(M_p, 1/e_p)=+0{,}710$** (fort), corr$(M_p,e_p)=-0{,}32$ : **haut $M_p$ ↔ petit ordre $e_p$.**
- Top conspirateurs : 127($e{=}7$,M=5), 257($e{=}16$), 73($e{=}9$), 71($e{=}35$), **61($e{=}60$=racine
  primitive, M=4)**. Donc petit ordre ⟹ haut M_p (suffisant), **mais pas nécessaire** (61 à grand
  ordre est conspirateur).
- Tous les petits-ordre $e_p\le12$ (73,89,127) ont $M_p\ge3$ : suffisant confirmé.
- $N$-structure (p=127=$2^7-1$) : tous les $N$ divisibles par $2^7-1=127$ — **trivial** (=$p\mid N$,
  p Mersenne). Pas de facteur $2^k-1$ supplémentaire universel.

## Pourquoi ça ne ferme pas
La caractérisation isole les EXTRÊMES (plus haut M_p = petit ordre), mais (a) le gros de
$S_1=\sum(M_p-1)$ vient des ~18 % de premiers non-Sidon, **la plupart à $M_p=2$ et ordre variable**
(pas petit) ; (b) la « structure $N$ » se réduit à $p\mid N$, aucune prise multiplicative nouvelle.
Même mur max-vs-énergie. #{premiers petit-ordre $e_p\le E$ dans $(L,L^2]$} $=O(E^2)$ (diviseurs de
$\prod_{e\le E}(2^e-1)$) — peu nombreux, mais insuffisant pour restructurer $S_1$.

## Verdict
- **PROUVÉ :** haut $M_p$ corrèle fortement à petit $\mathrm{ord}_p(2)$ (0,71) ; petit ordre $\Rightarrow$
  $M_p$ élevé (suffisant non nécessaire).
- **RESTE OUVERT :** inchangé. La caractérisation n'ouvre pas de voie (structure $N$ = $p\mid N$ ;
  conspirateurs pas tous petit-ordre ; bulk de $S_1$ ailleurs). 5ᵉ angle, même mur.
- **Plausibilité M″ :** inchangée, élevée.

---
*Script `check_conspirators.py`. Caractérisation conspirateurs = petit ordre (corr 0,71), mais
pas de nouvelle prise. Clôt l'exploration de M″ : 5 angles testés (Cauchy-Schwarz, Plünnecke,
Bourgain-Garaev, double-comptage, structure multiplicative), tous butent sur max-vs-énergie.*
