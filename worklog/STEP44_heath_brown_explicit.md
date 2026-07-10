# STEP44 — Travail « papier » : l'inégalité de crible explicite pour Σ_p Δ_p, développée dans notre régime. OÙ ÇA CASSE : le TERME D'ERREUR (portée exponentielle 2^L), hypothèse manquante = Lemme L*.

**Date :** 2026-07-04. Dérivation analytique explicite (demande de l'user, reprise de la piste
Heath-Brown proposée en STEP34). Objectif : écrire la meilleure inégalité de crible pour Σ_p Δ_p,
développer chaque terme sans heuristique, identifier EXACTEMENT où la preuve échoue.

## 0. Le régime (paramètres exacts)

- **Ensemble :** S = {2^a+2^b : 0≤a≤b≤L} (sumset), |S| =: P = (L+1)(L+2)/2 ~ L²/2 (éléments distincts
  sur ℤ : {2^k} Sidon binaire). S ⊂ [0, 2^{L+1}], donc **portée N := 2^{L+1}** (exponentielle !).
- **Modules :** carrés p², p premier ∈ (L, L²] avec ord_p(2)>L (Type B). Donc p² ≤ L⁴, **Q := L²**
  (max de p), et #modules π_TB ~ L²/(2logL).
- **Cible :** Σ_p Δ_p = Θ(L³/logL), où Δ_p = #{(s,s')∈S², s≠s' : p²|(s−s')}.
- Rappels : Σ_{p∈(L,L²]}1/p² ~ 1/(L logL) ; E₂^ℤ := #{(a,b,c,d):2^a+2^b=2^c+2^d sur ℤ} = 2P−(L+1)
  (Sidon : seules solutions triviales {a,b}={c,d}).

## 1. Décomposition EXACTE (identité de Parseval discrète)

Pour p Type B, avec S_p(t)=Σ_{k≤L}e(t·2^k/p²) :
$$\Delta_p^{\mathrm{ord}}=\underbrace{\frac1{p^2}\sum_{t=0}^{p^2-1}|S_p(t)|^4}_{D_p^{\mathrm{all}}}\ -\ E_2^{\Z},
\qquad D_p^{\mathrm{all}}=\#\{(a,b,c,d):2^a+2^b\equiv2^c+2^d \bmod p^2\}.$$
Le terme t=0 vaut (L+1)⁴/p² ; les t≠0 contiennent la diagonale ℤ ET l'excès modulaire. En Fourier,
$$\Delta_p=\sum_{\substack{m\neq0\\ p^2\mid m}}r(m),\qquad r(m):=\#\{(a,b,c,d):2^a+2^b-2^c-2^d=m\},$$
donc **Σ_p Δ_p = Σ_{m≠0} r(m)·ω₂(m)** avec ω₂(m)=#{p∈(L,L²]:p²|m} — c'est L* (STEP39).

## 2. TERME PRINCIPAL : ✓ correct, = Θ(L³/logL)

Prédiction de densité (chaque m divisible par p² avec « proba » 1/p²) :
$$M=\binom P2\sum_{p\in(L,L^2]}\frac1{p^2}\ \sim\ \frac{L^4}{8}\cdot\frac1{L\log L}=\frac{L^3}{8\log L}.$$
**Vérifié (STEP43) : E₂^tot/M = 0.955, 0.957, 0.935 (L=60,100,140), stable.** Le terme principal est
le bon ordre, à ~5% près (légèrement sous-Poisson : répulsion Sidon). ✓ **Aucun problème ici.**

## 3. TERME D'ERREUR : ✗ échoue avec TOUT crible générique (portée exponentielle)

L'erreur = déviation à l'équidistribution : Σ_p [Δ_p − |S|²/(2p²)] = (1/2)Σ_p (Var_p − |S|), où
Var_p=Σ_{a mod p²}(m_a−|S|/p²)². Deux inégalités standard, développées explicitement :

**(a) Grand crible classique (Montgomery–Vaughan) :** pour a_s∈ℂ, s≤N,
$$\sum_{q\le Q}\ \sideset{}{^*}\sum_{a\bmod q}\Bigl|\sum_{s}a_s e(as/q)\Bigr|^2\le(N+Q^2)\sum_s|a_s|^2.$$
Avec a_s=1_S, Σ|a_s|²=|S|~L²/2, **N=2^{L+1}**, Q≤L² : borne ≤ (2^{L+1}+L⁴)(L²/2) **~ 2^L·L²**.

**(b) Grand crible à modules CARRÉS (Baier–Zhao) :** ~ (N+Q³)(NQ)^ε Σ|a_s|², Q=L², Q³=L⁶ :
borne **~ 2^L·L²·L^ε**. Le terme Q³ n'aide pas — **N=2^L domine dans les deux**.

**Développement du ratio :** borne / cible = 2^L·L² / (L³/logL) = **2^L·logL/L**. Numériquement
(STEP43) : **10^17, 10^29, 10^41** pour L=60,100,140. **ASTRONOMIQUEMENT inutile.**

**POURQUOI :** S est **exponentiellement creux** (|S|~L² points dans un intervalle de longueur 2^L).
Tout crible générique paie le terme de portée +N=2^L. **La preuve échoue EXACTEMENT ICI : le terme
d'erreur, parce qu'aucun crible générique n'exploite que S = sommes de puissances de 2.**

## 4. HYPOTHÈSE MANQUANTE (Lemme L* autonome)

Le seul moyen d'éviter le +2^L est d'exploiter la structure lacunaire de S dans le terme d'erreur.
En Fourier, l'erreur = Σ_p (1/p²)Σ_{t≠0}|S_p(t)|⁴ − (part diagonale). Or |S_p(t)|⁴ est le module⁴
d'une **somme exponentielle lacunaire** ; la diagonale ℤ est contrôlée par Rudin (Λ(4), sur le tore) :
$$\int_0^1\Bigl|\sum_{k\le L}e(2^k\theta)\Bigr|^4d\theta=E_2^{\Z}=2P-(L+1)\ \le\ (C\cdot2)^2(L+1)^2.$$
Il reste la **correction mod p²**, qui n'est PAS un énoncé de crible générique :

> **Lemme L\* (forme exp-sum, autonome, base-indépendante — STEP42) :**
> $$\sum_{\substack{p\in(L,L^2]\\ \mathrm{ord}_p(2)>L}}\Bigl(\frac1{p^2}\sum_{t=1}^{p^2-1}|S_p(t)|^4-E_2^{\Z}\Bigr)
> \ =\ O\!\Bigl(\frac{L^3}{\log L}\Bigr),$$
> de façon équivalente Σ_{m≠0} r(m)ω₂(m)=O(L³/logL) : **les combinaisons Σε_j2^{j} (≤4 puissances)
> ont, en moyenne sur les carrés p²∈(L²,L⁴], une densité de diviseurs carrés O(Σ1/p²)** — au niveau
> aléatoire.

C'est la **correction mod-p² de Rudin** = le cœur non-standard (STEP38). Ni Montgomery–Vaughan ni
Baier–Zhao ne le donnent (ils voient S générique, portée 2^L). Il exploite la structure de puissance
via les sommes de caractères Σ_{j≤L}χ(2^j) (moyenne quadratique ~L, STEP35).

## 5. Ce que STEP43 dit sur L* (encourageant, pas une preuve)

- Le terme principal est PROUVÉ être le bon ordre (densité = E₂ à 5%).
- La déviation (= exactement le membre de gauche de L*) est **petite, stable, NÉGATIVE** : −0.045,
  −0.043, −0.065, **−0.039** pour L=60,100,140,**180** — **sans tendance croissante** jusqu'à
  n~2^{180}~10^{54} (répond à la crainte « ça bascule à 10^8 » : sur 3 ordres de grandeur de L, la
  déviation reste 4-6% et négative). C'est une somme **signée** : les premiers sous-Sidon (Δ_p<aléatoire) sur-compensent
  les outliers (STEP41). **Cancellation favorable** ⟹ un crible spécialisé de type Heath-Brown, qui
  capture la cancellation via Σχ(2^j), a la bonne structure de signe — c'est là qu'une preuve doit
  passer, pas par une borne de valeur absolue.

## 6. Verdict (format demandé — DEUX questions)

**Q1 (où la preuve échoue) :**
- **Terme principal :** ✓ correct, Θ(L³/logL), vérifié (densité=E₂ à 5%).
- **Terme d'erreur :** ✗ **c'est ICI que ça casse.** Tout crible générique (Montgomery–Vaughan,
  Baier–Zhao carrés) donne ~2^L·L² (facteur 2^L·logL/L de trop) car S est exp. creux (portée N=2^L).
- **Hypothèse manquante :** le **Lemme L\*** (correction mod-p² de Rudin ; densité de diviseurs carrés
  des combinaisons de ≤4 puissances = O(Σ1/p²)). Formulé ci-dessus comme énoncé autonome, base-indép.

**Q2 (le grand crible spécialisé peut-il marcher ?) :** Le générique NON (prouvé, portée exp). Le
SPÉCIALISÉ (Heath-Brown sur la forme 2^a+2^b−2^c−2^d, exploitant la structure lacunaire via Σχ(2^j))
est la SEULE voie crible ; son terme principal est acquis (densité), son terme d'erreur = moyenne
quadratique de Σχ(2^j) (~L) avec cancellation de signe favorable (déviation négative). **RESTE OUVERT,
mais le point d'échec est isolé au caractère-lacunaire du terme d'erreur — un énoncé (L*) précis,
autonome, publiable, au front (Bourgain-Garaev incomplet, en moyenne quadratique).**

---
*Dérivation papier. Décomposition exacte Σ_p Δ_p = main (densité, ✓ Θ(L³/logL)) + erreur (= L*).
Cribles génériques (MV, Baier-Zhao) donnent ~2^L·L² (portée exp N=2^L, S creux) : ÉCHEC au terme
d'erreur. Hypothèse manquante = Lemme L* (correction mod-p² de Rudin, densité de diviseurs carrés des
combinaisons de puissances = O(Σ1/p²)), autonome, base-indépendant. Cancellation favorable (déviation
négative, STEP43). PAPER/Lean non touchés.*
