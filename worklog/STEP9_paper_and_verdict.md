# Erdős #11 deux-puissances — papier Kalinin, biblio ciblée mod $p^2$, et verdict sur R2

**Date :** 2026-06-23. Répond à : (0) le PDF `erdos11.pdf` aide-t-il ? (1) biblio mod $p^2$,
(2) test empirique R2, (3) tentative élémentaire, (4) verdict honnête.

## 0. Le papier `erdos11.pdf` (Kalinin, « A multiplicity bound for a fixed squarefree kernel », 29 mars 2026)

**Ce qu'il prouve.** Pour $m$ squarefree fixé, $T_m(n)=\{k\ge1: n-2^k=mu^2,\ u\in\mathbb Z_{\ge0}\}$
(exposants $k$ où le décalage dyadique $n-2^k$ vaut $m\times$carré). Résultats, **tous élémentaires
(2-adiques, type Ramanujan–Nagell)** : $|T_m(n)|\le2$ pour $m\ge3$ squarefree impair ; $|T_1(n)|\le3$
(net, atteint par $17\cdot4^t=u^2+2^k$). Corollaire 6 : parmi $k\le K$, au moins $\lceil(K-1)/2\rceil$
**noyaux squarefree distincts** apparaissent.

**Est-ce que ça aide ? Réponse honnête : marginalement, et pas sur le point dur (R2).** Analyse :
- **C'est un quantité DIFFÉRENTE.** Le papier borne la *multiplicité* des représentations
  Ramanujan–Nagell $n-2^k=m u^2$ (une puissance, équation **exacte** sur $\mathbb Z$). Notre R2
  est un *comptage de congruences* $p^2\mid n-2^i-2^j$ (deux puissances, mod $p^2$). La rigidité du
  papier vient de l'unicité binaire **dans $\mathbb Z$** ; elle disparaît mod $p^2$. La technique
  ne transfère donc pas au comptage mod $p^2$.
- **Le papier NE prouve PAS la conjecture** (ni une ni deux puissances) : il borne des
  multiplicités locales, pas l'existence d'une représentation squarefree.
- **Ce qu'il donne réellement pour nous : il borne rigoureusement la contribution des
  carrés-parfaits / TRÈS grands premiers à R2.** Pour $p>\sqrt{n/2}$, $p^2\mid n-2^i-2^j$ force
  $n-2^i-2^j=p^2$ = carré parfait. Or $\#\{(i,j): n-2^i-2^j=\square\}=\sum_j|T_1(n-2^j)|\le3(L+1)=O(L)$
  par son Théorème 4. **Donc la contribution des premiers $p>\sqrt{n/2}$ à R2 est $O(L)=o(L^2)$** —
  rigoureux, élémentaire, et **confirme** notre observation empirique « $p>L^2$ contribue $\approx0$ ».
  Mais c'est la partie *déjà inactive* ; la **plage active $(L,L^2]$** (où $n/p^2\gg1$, donc
  $n-2^i-2^j$ n'a pas à être un carré) **n'est PAS touchée**.
- **Il confirme notre bibliographie** : cite exactement Granville–Soundararajan, Hercher, Crocker,
  Platt–Trudgian — rien de neuf à consulter. (Et son intro confirme « peut-être facile » d'Erdős et
  le lien Wieferich.)

**Bilan PDF : bon à citer (seul papier récent sur la structure locale de #11, et il ferme
proprement la queue carré-parfait de R2), mais il n'attaque pas la difficulté de fond.** Je
l'avais identifié dans l'esprit (Ramanujan–Nagell) mais pas ce papier précis ; il valide notre
cadre et notre biblio.

## 1. Biblio ciblée : sommes courtes mod $p^2$ = territoire de Heilbronn (très dur)

L'objet canonique « somme à structure multiplicative mod $p^2$ » est la **somme de Heilbronn**
$H_p(a)=\sum_{n=1}^{p}e_{p^2}(a n^p)$ (longueur $p=q^{1/2}$, $q=p^2$). Historique :
- montrer simplement $H_p(a)=o(p)$ fut **ouvert des années** ; **Heath-Brown 1996** (méthode de
  Stepanov) : $H_p\ll p^{11/12}$ ; puis $p^{7/8}$ (Heath-Brown–Konyagin) ; puis $p^{5/6}\log^{1/6}p$.
- Littérature dédiée « sommes sur sous-groupes de $\mathbb Z_{p^2}^*$ » (Bourgain–Garaev, Shkredov,
  …) : active, technique, gains modestes.

**Notre $T_p(a)=\sum_{l\le L}e_{p^2}(a2^l)$ est PIRE que Heilbronn :** pour $p\in(L,L^2]$,
$L\ge\sqrt p=(p^2)^{1/4}$, donc longueur $\approx q^{1/4}$ — **encore plus courte** que la longueur
$q^{1/2}$ de Heilbronn (les sommes plus courtes sont plus dures). Aucune borne publiée ne couvre ce
régime (tout est mod $p$, ou longueur $\ge q^{1/2}$ mod $p^2$). **Passage $p\to p^2$ + sommes très
courtes = frontière de la recherche.**

## 2. Test empirique : R2 n'est PAS proprement structuré

Pire $n$ à l'échelle $2^{22}$ ($n=4193775$, $L=21$) : les premiers $p\in(L,L^2]$ qui contribuent à
R2 sont $23,29,37$ avec ordres $e_p=11,28,36$ (modérés, **pas** petits) et $N_p=3,2,2$. **R2 n'est
pas concentré sur les premiers à petit ordre** ($p\mid2^d-1$, $d$ petit) — il est étalé sur des
premiers génériques. Donc **pas de réduction élémentaire « petits ordres seulement »** (qui aurait
été sommable car ces premiers sont rares). La structure exploitable espérée est absente.

## 3. Tentative élémentaire : télescopage + moyenne d'orbite (vrais, mais insuffisants)

Deux faits **élémentaires exacts** (vérifiés numériquement) :
1. **Télescopage :** $T_p(a)-T_p(2a)=e_{p^2}(a)-e_{p^2}(a2^{L+1})$, donc $|T_p(a)-T_p(2a)|\le2$
   (mesuré : $=2$). Le doublage $a\mapsto2a$ ne change $T$ que de $O(1)$.
2. **Moyenne d'orbite nulle :** $\frac1{d_p}\sum_{j=0}^{d_p-1}T_p(2^j a)=0$ (conséquence directe du
   Lemme K : on échange les sommes et chaque période complète s'annule). Vérifié ($\sim10^{-15}$).

**Mais ça ne donne pas la compensation.** L'orbite $\{T_p(2^ja)\}$ a moyenne $0$ et pas de $\le2$,
donc ses valeurs vivent dans un intervalle de taille $\le d_p$ : l'élémentaire ne prouve que
$|T_p(a)|\le d_p$ (dérive triviale). Or le **vrai** max d'orbite mesuré est $\approx2{,}8\sqrt L$
($\approx12$–$18$ pour $d_p\sim10^4$) — la compensation racine-carrée est **réelle** mais
**invisible** à l'algèbre de groupe (un écart de $\sqrt L$ vs $d_p$). La complétion (Polya–Vinogradov)
ramène la somme incomplète à des sommes complètes *twistées* $\sum_l e_{p^2}(a2^l)e_{d_p}(tl)$ qui ne
sont **pas** nulles (objets de type Gauss sur sous-groupe, durs). **Aucune annulation partielle
élémentaire sur période incomplète.**

## 4. Verdict honnête sur R2 : **(b) — vrai problème ouvert, niveau spécialiste**

Après les trois angles, R2 n'est **pas** (a) « accessible en 1-2 sessions ». C'est (b) :

- **Nature exacte :** borner (en moyenne sur $p\in(L,L^2]$, uniformément en $n$) une somme
  d'exponentielles **très courte** ($\approx q^{1/4}$ termes) sur $\{2^l\}$ **modulo $q=p^2$**.
- **Comparaison de dureté :** strictement plus dur que la somme de Heilbronn (même modulus $p^2$,
  structure multiplicative, mais Heilbronn est *plus longue*, $q^{1/2}$, et a déjà demandé Stepanov
  + 20 ans pour des gains modestes $p^{5/6}$). Les sommes mod $p^2$ courtes sur $\{2^l\}$ ne sont
  pas couvertes par la littérature existante (Garaev/Bourgain/Konyagin : mod $p$ ; Heilbronn :
  longueur $q^{1/2}$).
- **Pas de raccourci :** le grand crible ne mord pas (STEP8), la structure de petit-ordre est
  absente (§2), l'algèbre de groupe élémentaire plafonne à la dérive triviale (§3), et le seul
  papier récent (Kalinin, §0) ne touche que la queue carré-parfait (inactive).

**Ce qui RESTE acquis et solide** (inchangé) : Lemme K, R1 fermé, périodes complètes $o(L^2)$,
localisation de R2 sur $(L,L^2]$, queue $p>\sqrt{n/2}$ fermée (via Kalinin Thm 4). Soit ~80-85 %
d'une preuve, **conditionnelle à une estimation de somme d'exponentielle mod $p^2$ de niveau
recherche**.

**Plausibilités (finales, honnêtes) :**
- preuve complète **par nous, outils accessibles, 1-2 sessions** : **~3-5 %** (R2 = territoire
  Heilbronn ; il faudrait un miracle élémentaire ou réimporter Stepanov mod $p^2$ courte) ;
- preuve complète **par un spécialiste des sommes d'exponentielles mod $p^k$** (Heath-Brown,
  Konyagin, Shkredov, Shparlinski…) : **plausible, ~30-40 %** — c'est *leur* type de problème, et
  la cible (gagner un facteur $\log$) est modeste ; mais le régime court mod $p^2$ peut résister ;
- **résultat partiel conditionnel rigoureux + Lean-formalisable maintenant** : solide (tout sauf R2).

**Recommandation :** présenter le travail comme **« réduction élémentaire de la variante
deux-puissances de #11 à une estimation de somme d'exponentielle courte mod $p^2$ »** — un énoncé
propre qui isole exactement le cœur analytique. C'est un résultat partiel réel et publiable, et la
bonne personne à qui le soumettre est un spécialiste des sommes mod $p^k$ (pas une tentative
élémentaire de plus de notre part).

---
*Sources : `erdos11.pdf` (Kalinin, lu intégralement) ; Heath-Brown (Heilbronn $p^{11/12}$),
Heath-Brown–Konyagin ($p^{7/8}$), bornes ultérieures $p^{5/6}\log^{1/6}p$ (recherche web) ;
test empirique + télescopage : scripts inline. Confirme et clôt l'analyse de `STEP8`.*
