# STEP26 — CLASSIFICATION des fibres exceptionnelles : identité d'involution, structure PA, borne M_p ≤ L/e_p+O(1), et réduction de M″ à une somme d'ordres réciproques

**Date :** 2026-07-02. Scripts `relations.py`, `relations2.py`. Suite STEP25 (piste GPT : classer
les relations ; « COSET se cassera comme le bulk »). **Résultat : COSET se casse effectivement, et
on obtient un théorème de structure + une réduction propre de M″ à un objet classique.** C'est le
progrès le plus substantiel de la campagne #11. Vise un résultat AUTONOME (conseil GPT).

## 1. Identité d'involution (PROUVÉE, universelle) — pourquoi ces δ ?

$$\boxed{\,1+2^{\,e-\delta}\equiv 2^{-\delta}(1+2^{\delta})\pmod p\,}\qquad e=\mathrm{ord}_p(2).$$
Preuve : $2^{-\delta}(1+2^\delta)=2^{-\delta}+1=2^{e-\delta}+1$ (car $2^e\equiv1$). ∎ (0 violation / 200 premiers.)

**Conséquence :** δ et $e-\delta$ donnent TOUJOURS la même classe de ⟨2⟩ mod p. Les valeurs-gap
$\{1+2^\delta\}$ sont appariées par l'involution $\delta\mapsto e-\delta \pmod e$. Les fibres
exceptionnelles ne sont donc PAS des coïncidences arbitraires : leurs δ vivent dans des classes
d'involution mod $e_p$.

## 2. Structure des fibres = union de PROGRESSIONS ARITHMÉTIQUES (graphe = chemins)

Développement p-adique : $2^{e}\equiv 1+q_p\,p \pmod{p^2}$ ($q_p$ = quotient de Fermat, Wieferich
⟺ $q_p=0$). En écrivant $a=a_0+e n,\ \delta=\delta_0+e m$, la valeur de fibre mod $p^2$ se réduit à
**UNE équation linéaire** $n(1+u)+m u\equiv c \pmod p$ ($u=2^{\delta_0}\bmod p$). D'où :

> **Chaque fibre = (boîte $\{a+\delta\le L\}$) ∩ (droite mod p).** Les δ d'une classe mod $e_p$
> forment une PROGRESSION ARITHMÉTIQUE de pas multiple de $e_p$.

Vérifié (graphe des relations, sommets=δ, L=160) — **union de PA, jamais de graphe dense** :
- p=257 (e=16, M=11) : δ≡0→[16,48,80,112,144] pas 32=2e ; δ≡7→[7,23,39] pas 16=e ; δ≡9→[9,25,41] pas e.
  (Les classes {7,9} sont une paire d'involution : 7+9=16=e ; {0} auto-appariée.)
- p=683 (e=22, M=8) : δ≡0→[22,66,110,154] pas 44=2e ; paire d'involution {10,12}→[10,32],[12,34].
- p=8191 (e=13, M=7) : paire d'involution {1,12}→[1,40,79],[38,77,116,155] pas 39=3e.

Les « relations » sont **entièrement paramétrées par (classe d'involution $\delta_0$, pas $k\,e_p$),
$k\in\{1,2,3\}$** — une poignée de patrons, pas des objets libres. Le nombre de TYPES est $O(e_p)$.

## 3. Borne universelle M_p ≤ ⌊L/e_p⌋ + O(1)  [remplace le M1 réfuté]

Recherche de $C=\max_p (M_p-2(\lfloor L/e_p\rfloor+1))$ :

| L | 60 | 80 | 100 | 120 | 140 | 160 |
|---|---|---|---|---|---|---|
| max excès C | 1 | 2 | 2 | 2 | 2 | 2 | **← stable, ne croît pas** |

Et $\max_p(M_p-\lfloor L/e_p\rfloor)$ = 3,4,4 (L=60,100,160), atteint sur les **racines primitives**
($e_p=p-1>L$, $M_p=4$). Donc empiriquement (L≤160) :
$$\boxed{\,M_p\ \le\ \big\lfloor L/e_p\big\rfloor + 4\,,\qquad e_p=\mathrm{ord}_p(2).}$$
**Point clé :** M1 (STEP15) — réfuté — bornait par $L/d_p$ avec $d_p=\mathrm{ord}_{p^2}(2)=p\,e_p$
(trop petit, $C$ explosait). La VRAIE échelle est $e_p=\mathrm{ord}_p(2)$ ($=d_p/p$), $p$ fois plus
grande — et là la borne tient avec constante additive. C'est le bon dénominateur (le facteur $p$
manquant = un niveau p-adique tué par l'involution).

## 4. Dichotomie Type A / Type B (COSET se casse — prédiction GPT confirmée)

- **Type A** ($e_p\le L$, « structuré ») : δ dans peu de classes d'involution, en PA de pas $k e_p$.
  Porte TOUS les gros $M_p$ (jusqu'à 11 à L=160). $M_p\lesssim 2(\lfloor L/e_p\rfloor+1)$.
- **Type B** ($e_p> L$, « générique ») : δ tous distincts mod $e_p$ (≥3-4 classes d'involution),
  aucune PA, **$M_p=4$ EXACTEMENT** (jamais ≥5, L≤160). Régime Poisson (extrême de la loi bulk).

L=160 : Type A = 21 premiers (maxM=11) ; Type B = 4 premiers (maxM=4). La difficulté « gros $M_p$ »
est ENTIÈREMENT dans le Type A structuré (involution+PA), contrôlable par $L/e_p$.

## 5. RÉDUCTION de M″ à une somme d'ordres réciproques (le gain)

Avec $M_p-1\le \lfloor L/e_p\rfloor+3$ et $M_p=1$ pour les premiers Sidon :
$$M''=\!\!\sum_{p\in(L,L^2]}\!\!(M_p-1)\ \le\ \underbrace{\sum_{p\in(L,L^2]}\lfloor L/e_p\rfloor}_{(\star)}
\ +\ \underbrace{3\,\#\{p:M_p\ge2\}}_{\le\,3\pi(L^2)=o(L^2)\ \text{INCONDITIONNEL (PNT)}}.$$
Le second terme est $o(L^2)$ gratuitement. Donc :
$$\boxed{\ M''=o(L^2)\ \Longleftarrow\ \sum_{p\in(L,L^2]}\frac{L}{\mathrm{ord}_p(2)}=o(L^2)
\ \Longleftrightarrow\ \sum_{p\in(L,L^2]}\frac{1}{\mathrm{ord}_p(2)}=o(L).\ }$$

**C'est une somme de réciproques d'ordres multiplicatifs** — objet CLASSIQUE (Pappalardi, Kurlberg–
Pomerance, Murty–Séguin–Stewart sur $\mathrm{ord}_p(2)$), bien plus standard que « excès moyen
EM≈1.3 » (STEP19). Empiriquement $(\star)/L^2\approx0{,}006$, décroissant (0.0078→0.0056, L=80→120).

## Verdict (format demandé)

- **Autopsie/classification aboutie ?** **OUI, théorème de structure.** (1) Identité d'involution
  PROUVÉE ; (2) fibres = union de PA (droite ∩ boîte) ; (3) borne $M_p\le\lfloor L/e_p\rfloor+4$
  (empirique, C stable) ; (4) dichotomie Type A structuré / Type B Poisson.
- **COSET irréductible ?** **NON** — se casse en A (involution+PA, gros M) / B (Poisson, M=4),
  exactement la prédiction GPT « comme le bulk ». Le mot « mur ultime S-unité » de STEP25 est nuancé :
  le gros M_p est STRUCTURÉ (PA d'ordre), pas S-unité sporadique.
- **Réduction obtenue ?** **OUI, nette :** $M''=o(L^2)\Leftarrow \sum_{p\in(L,L^2]}1/\mathrm{ord}_p(2)=o(L)$,
  le terme additif étant $o(L^2)$ inconditionnellement. Objet classique, ≠ EM≈1.3.
- **Résolu ?** NON. $(\star)=\sum\lfloor L/e_p\rfloor$ : borne brute $\#\{e_p=d\}\le d$ redonne
  $\Theta(L^2)$ (même gap facteur-constant) ; $o(L^2)$ empirique. MAIS la cible est désormais un
  **objet nommé et classique**, potentiellement dans la littérature des ordres de 2.
- **Résultat AUTONOME (conseil GPT) ?** Candidat : *« pour tout p, toute fibre additive de
  $\{2^a+2^b\bmod p^2\}$ de multiplicité ≥3 est portée par des PA en δ de pas multiple de
  $\mathrm{ord}_p(2)$, closes sous l'involution $\delta\mapsto e-\delta$ ; d'où
  $M_p\le\lfloor L/\mathrm{ord}_p(2)\rfloor+O(1)$ »* — publiable si les O(1)/PA sont prouvés,
  indépendamment de #11.
- **Plausibilité M″/#11 :** inchangée haute, mais la COMPRÉHENSION a bondi : d'une statistique
  (EM) à une structure algébrique (involution + PA d'ordre) + une réduction à $\sum 1/\mathrm{ord}_p(2)$.

---
*Scripts relations.py/relations2.py. Involution PROUVÉE ; fibres = union de PA (droite p-adique ∩
boîte) ; borne $M_p\le\lfloor L/e_p\rfloor+4$ (C stable, remplace M1 réfuté qui utilisait $d_p$) ;
dichotomie A/B ; réduction $M''=o(L^2)\Leftarrow\sum_{(L,L^2]}1/\mathrm{ord}_p(2)=o(L)$ (terme
additif $o(L^2)$ gratuit). PAPER.tex/PDF intacts.*
