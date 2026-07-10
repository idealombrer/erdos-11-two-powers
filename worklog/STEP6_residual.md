# Erdős #11 deux-puissances — R1 fermé élémentairement ; seul R2 reste (analytique)

**Date :** 2026-06-22. **Suite de** `PROOF.md` (Lemme K, §1–§3). Cette étape attaque le terme
résiduel $R=R1+R2$ par les deux pistes demandées.

## Résultat principal de l'étape : **R1 (bord) est élémentairement $o(L^2)$**

Rappel du découpage (PROOF.md §4) : après le Lemme K, le résiduel se scinde en
- **R1** = bords des premiers ayant ≥1 période complète ($d_p\le L+1$) ;
- **R2** = premiers sans période complète ($d_p>L+1$).

### Proposition R1 (rigoureuse, élémentaire)

> Pour $n$ impair, $L=\lfloor\log_2 n\rfloor$,
> $$R1(n):=\!\!\sum_{\substack{p\ \text{non-Wief.}\\ d_p\le L+1}}\!\!\big(N_p(n)-Q_p^2\,p\,r_p(n)\big)
> \ <\ 3(L+1)\,\pi(L+1)\ =\ O\!\Big(\frac{L^2}{\log L}\Big)\ =\ o(L^2).$$

**Preuve.**
*(a) Localisation des premiers concernés.* Pour $p$ non-Wieferich, $d_p=p\cdot\mathrm{ord}_p(2)\ge p$.
Donc $d_p\le L+1\Rightarrow p\le L+1$ : **les premiers porteurs de bord sont tous $\le L+1$**,
au nombre de $\le\pi(L+1)$. *(Vérifié : `verify_residual.py` donne $\max\{p:d_p\le L+1\}\le7$
jusqu'à $n=2^{22}$ — confinement effectif encore plus fort.)*

*(b) Borne par premier.* Écrivons $L+1=Q_p d_p+s_p$, $0\le s_p<d_p$. Posons, sur une période,
$c(x)=\#\{l\le L:2^l\equiv x\}=Q_p+\varepsilon(x)$ avec $\varepsilon(x)\in\{0,1\}$ et
$\#\{x:\varepsilon(x)=1\}=s_p$ (les $s_p$ résidus $2^0,\dots,2^{s_p-1}$). Alors, avec
$P_n=\{x\in\langle2\rangle:n-x\in\langle2\rangle\}$ ($|P_n|=p\,r_p(n)$ par le Lemme K, §3),
$$N_p(n)=\sum_{x\in P_n}c(x)c(n-x)=Q_p^2\,|P_n|+2Q_p\gamma_p(n)+\delta_p(n),$$
où $\gamma_p(n)=\#\{x\in P_n:\varepsilon(x)=1\}\le s_p$ et $0\le\delta_p(n)\le\gamma_p(n)$. D'où
$$\mathrm{bord}_p(n)=N_p(n)-Q_p^2\,p\,r_p(n)=2Q_p\gamma_p(n)+\delta_p(n)\le(2Q_p+1)s_p.$$
Comme $Q_p s_p<Q_p d_p\le L+1$ et $s_p<d_p\le L+1$ :
$(2Q_p+1)s_p=2Q_p s_p+s_p<2(L+1)+(L+1)=3(L+1)$.

*(c) Somme.* $R1(n)=\sum_{d_p\le L+1}\mathrm{bord}_p(n)<3(L+1)\cdot\pi(L+1)$. Par le théorème
des nombres premiers $\pi(L+1)\sim (L+1)/\log(L+1)$, donc $R1=O(L^2/\log L)=o(L^2)$.
Les $\le2$ premiers de Wieferich connus $\le\sqrt n$ ajoutent $O(L)$, négligeable. $\blacksquare$

**Vérification (`verify_residual.py`, pire $n$ par échelle jusqu'à $2^{22}$) :** $R1$ effectif
$\in[0,32]$, toujours $\ll 3(L+1)\pi(L+1)\in[234,528]$ ; $R1/L^2\le0{,}094$ et la *borne*
$3\pi(L+1)/L\to0$. ✓

**C'est l'apport de cette étape :** approche (b) **réussit**. Le bord ne nécessite **aucune**
équidistribution — il est tué par un simple argument de localisation (les premiers à période
sont rares, $\le\pi(L+1)$) + une borne $O(L)$ par premier.

## R2 (grands premiers, $d_p>L+1$) : approche (a) — l'analytique reste nécessaire

$$R2(n)=\!\!\sum_{\substack{p\le\sqrt n\\ d_p>L+1}}\!\!N_p(n),\qquad
N_p(n)=\#\{(l,m)\in[0,L]^2:2^l+2^m\equiv n\,(p^2)\}\ (\le L+1,\ \text{car }2^l\ \text{distincts}).$$

**Pourquoi le comptage élémentaire échoue (confirmé, deux bornes) :**
- *Par premier* : $N_p\le L+1$, et $\#\{p:d_p>L+1,p\le\sqrt n\}\sim\pi(\sqrt n)\sim\sqrt n$,
  d'où $R2\le(L+1)\sqrt n\gg L^2$.
- *Par paire* : $R2=\sum_{(l,m)}\#\{p:d_p>L+1,p^2\mid k_{l,m}\}\le\sum_{(l,m)}\omega_2(k_{l,m})
  \le(L+1)^2\cdot\frac{\log n}{2\log2}=O(L^3)$.

Aucune des deux ne descend sous $L^2$ : R2 exige une **annulation** (le Lemme K ne sert plus,
$Q_p=0$, pas de période).

**Forme analytique exacte (ce qu'il faut établir).** Via
$N_p(n)=p^{-2}\sum_a e_{p^2}(-an)T(a)^2$, $T(a)=\sum_{l=0}^L e_{p^2}(a2^l)$ :
- terme principal $a=0$ : $\sum_{d_p>L+1}(L+1)^2/p^2\le(L+1)^2\sum_{p>z}p^{-2}=o(L^2)$ ✓ ;
- termes $a\ne0$ : exigent $|T(a)|=o(L)$ (somme **lacunaire incomplète** : $d_p>L$ donc
  $<$ une période, le Lemme K ne s'applique pas). C'est précisément une borne de type
  **Bourgain / Garaev–Shparlinski / Konyagin** sur $\sum_{l\le L}e(a2^l/q)$ — non élémentaire.

**Données (`verify_residual.py`, `largeprime2.py`) :** $R2/L^2\in[0{,}035,\,0{,}16]$ pour le
pire $n$, sans signe net de croissance (plutôt décroissant aux grandes échelles), et
contribution **nulle** des $p>L^2$ (déjà observé). Donc $R2$ est *empiriquement* $\ll0{,}68\,L^2$
— largement dans le coussin — mais le *prouver* requiert l'estimation lacunaire.

## Bilan actualisé de la preuve

| Composant | Statut | Méthode |
|---|---|---|
| Réduction $(\star)$ + petits premiers $\le0{,}3205\,(L+1)^2$ | **rigoureux** | élémentaire (§1) |
| Lemme K (annulation $S(a)=0$, $p$ non-Wief., $p\nmid a$) | **rigoureux** | élémentaire (§2) |
| Périodes complètes des grands premiers $=o(L^2)$ unif. en $n$ | **rigoureux** | Lemme K (§3) |
| **R1 (bord), $d_p\le L+1$** | **rigoureux (NOUVEAU)** | localisation $p\le L+1$ + $O(L)$/premier |
| **R2 (grands premiers, $d_p>L+1$)** | **ouvert** | borne lacunaire $\sum_{l\le L}e(a2^l/p^2)$ |

**Il ne reste donc qu'UN seul morceau : R2.** Tout le reste — y compris le terme de bord qui
semblait, en fin de session précédente, du même niveau de difficulté que R2 — est désormais
**élémentaire et rigoureux**. R2 est un énoncé propre, autonome, de sommes d'exponentielles
sur $\{2^l\}$ modulo $p^2$ pour $p$ grand, qui relève d'une littérature existante (Bourgain et
al.) mais non élémentaire.

**Plausibilités (mises à jour) :**
- preuve complète **via une borne lacunaire standard pour R2** + §1–§3 + R1 : **~40-50 %**
  (en hausse : R1 fermé élémentairement, ne reste qu'un lemme analytique *isolé et nommé*).
- preuve **entièrement élémentaire** : **~5-10 %** — il faudrait une annulation élémentaire
  pour R2 (grands premiers, pas de période) ; rien d'évident, mais le Lemme K et la fermeture
  de R1 montrent que des surprises élémentaires existent.
- **Lean** : §1–§3 + Proposition R1 (tout l'élémentaire) formalisables **dès maintenant** —
  ce serait un théorème conditionnel propre « variante deux-puissances ⟸ borne lacunaire R2 »,
  un vrai résultat partiel.

**Prochaine étape :** R2 seul. Soit (i) invoquer/adapter une borne publiée
$|\sum_{l\le L}e(a2^l/p^2)|\ll L^{1-\delta}$ uniformément utilisable et la sommer contre
$p^{-2}$ ; soit (ii) chercher — plus spéculativement — une annulation élémentaire propre aux
grands premiers (analogue « partiel » du Lemme K pour périodes tronquées).

---
*Scripts : `verify_residual.py` (split R1/R2, pire $n$, jusqu'à $2^{22}$). Proposition R1 :
prouvée ci-dessus, vérifiée numériquement. R2 : ouvert, renvoyé aux sommes lacunaires.*
