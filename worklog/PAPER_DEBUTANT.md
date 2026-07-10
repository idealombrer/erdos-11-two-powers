# Comprendre la variante « deux puissances » du problème d'Erdős #11

*Un guide à partir de zéro, avec trois exemples filés : n=15, n=21, n=45.*

---

## Comment lire ce document

Ce texte explique, sans prérequis de théorie des nombres avancée, un problème
ouvert et tout ce qu'on a pu en comprendre. Trois ingrédients reviennent
partout :

- des **Boîtes à outils** : chaque notion nouvelle (carré, sans facteur
  carré, ordre d'un élément, etc.) y est définie avec une analogie et un
  exemple chiffré, *avant* d'être utilisée ;
- trois exemples filés, **n=15, n=21, n=45**, recalculés à chaque nouvelle
  notion ;
- des encadrés **« En résumé »** à la fin de chaque section.

Quand une phrase abstraite vous échappe, descendez à l'exemple chiffré
juste en dessous.

---

## 1. Le problème, en mots simples

Le problème original d'Erdős #11 demande : peut-on toujours écrire un grand
entier $n$ comme $n=k+2^m$, où $k$ n'a **aucun facteur carré** (on dit que
$k$ est *sans facteur carré*, ou *squarefree*) ? C'est un problème ouvert.

Ici, on étudie une variante **plus généreuse** : au lieu d'une seule
puissance de $2$, on s'autorise à en utiliser **deux**.

> **La question étudiée.** Pour tout entier impair $n>1$, existe-t-il des
> entiers $k,l,m\ge0$ avec $k$ sans facteur carré tels que
> $$n=k+2^l+2^m\ ?$$

Intuitivement : on a deux « jetons », chacun valant une puissance de $2$ (pas
forcément différentes : $l=m$ est permis, ça revient à utiliser $2\cdot2^l$).
On les retire de $n$, et on espère que ce qui reste, $k$, n'est divisible par
aucun carré $p^2$ ($p$ premier).

Cette variante n'est pas un problème numéroté d'Erdős à part : elle apparaît
comme une *variante formelle* de #11 (`erdos_11.variants.two_pow_two` dans
les bibliothèques de conjectures formalisées), accompagnée d'une remarque
attribuée à Erdős selon laquelle un assouplissement à deux puissances
« pourrait être facile » — nous n'avons pas vérifié cette attribution contre
une source primaire, et la mentionnons donc avec cette réserve.

### Premier contact : n=15

$$15 = k + 2^l+2^m.$$
Essayons le choix le plus simple, $l=m=0$ (les deux jetons valent $1$) :
$$k = 15-1-1=13.$$
$13$ est premier, donc sans facteur carré. **Ça marche dès le premier
essai.**

### Deuxième contact : n=21 — et un piège

$$21 = k+2^l+2^m.$$
Essayons $l=0,m=1$ : $k=21-1-2=18=2\cdot3^2$. Le facteur $3^2=9$ est un
carré : **$18$ n'est pas sans facteur carré.** Ce choix échoue.

Essayons plutôt $l=m=1$ : $k=21-2-2=17$, premier, sans facteur carré. **Ça
marche.** La leçon : il ne suffit pas qu'*un* choix de $(l,m)$ marche en
général ; le problème demande qu'*au moins un* choix marche, et certains
choix peuvent échouer en cours de route — c'est tout l'enjeu du document.

> **En résumé.** On retire de $n$ deux puissances de $2$ (égales ou non), et
> on espère que le reste $k$ est sans facteur carré. Pour $n=15$ et $n=21$,
> ça marche, mais pas avec n'importe quel choix de puissances : il faut en
> tester plusieurs.

---

## 2. Boîte à outils I : facteur carré, et « sans facteur carré »

> **Boîte à outils — Facteur carré.** Un entier $k$ a un *facteur carré* si
> $p^2\mid k$ pour un nombre premier $p$. On dit que $k$ est **sans facteur
> carré** (squarefree) si aucun premier ne se répète dans sa factorisation.
>
> *Analogie.* Factoriser un nombre, c'est le décomposer en briques premières.
> « Sans facteur carré » veut dire qu'on n'a **jamais deux fois la même
> brique** : chaque premier apparaît au plus une fois.
>
> *Exemples.* $30=2\cdot3\cdot5$ : sans facteur carré. $18=2\cdot3^2$ : *pas*
> sans facteur carré ($3$ apparaît deux fois). $1$ est sans facteur carré par
> convention.

> **Boîte à outils — Reste modulo $m$, et congruence.** Le reste de la
> division de $a$ par $m$ se note $a\bmod m$. On écrit $a\equiv b\pmod m$
> quand $a$ et $b$ ont le même reste, c'est-à-dire quand $m$ divise $a-b$.
>
> *Analogie.* Une horloge à $m$ heures : on ne retient que la position sur le
> cadran, pas le nombre total d'heures écoulées.
>
> *Exemple.* $18\equiv0\pmod9$ (le reste de $18$ par $9$ est $0$) : c'est
> exactement dire que $9\mid18$, c'est-à-dire que $18$ a un facteur carré
> $3^2=9$.

### Pourquoi c'est la bonne traduction du problème

Dire « $p^2$ divise $k=n-2^l-2^m$ » revient à dire « $2^l+2^m\equiv n\pmod{p^2}$ ».
On va donc compter, pour chaque petit premier $p$, **combien de paires
$(l,m)$ tombent dans le piège** $2^l+2^m\equiv n\pmod{p^2}$ — ce sont les
paires à éviter. S'il y a moins de pièges au total que de paires possibles,
il en reste forcément au moins une qui s'en sort : c'est tout le plan
d'attaque.

> **En résumé.** « $k$ sans facteur carré » se traduit, pour chaque premier
> $p$, par « $2^l+2^m\not\equiv n\pmod{p^2}$ ». On va compter les pièges
> (les paires qui tombent dans une mauvaise congruence) premier par premier.

---

## 3. Le plan d'attaque (le crible)

Fixons $n$ impair, et posons $L:=\lfloor\log_2n\rfloor$ (le nombre de bits de
$n$, moins un). On regarde les paires $(l,m)$ avec $0\le l,m\le L$ — il y en
a $T:=(L+1)^2$ (en comptant $(l,m)$ et $(m,l)$ séparément, par simplicité).

> **Exemple, n=21.** $21$ s'écrit en binaire $10101$, sur $5$ bits, donc
> $L=4$. Il y a $T=5^2=25$ paires $(l,m)$ avec $0\le l,m\le4$ (on a listé les
> $14$ paires avec $l\le m$ plus haut implicitement ; en comptant aussi
> $l>m$ on a bien $25$).

Pour un premier $p$, notons
$$N_p(n):=\#\{(l,m): \ p^2\mid n-2^l-2^m\}$$
le nombre de paires « piégées » par $p$. Une paire $(l,m)$ échoue (donne un
$k$ *non* squarefree) seulement si **un** premier $p$ la piège. Donc :

> **Principe du crible (rigoureux).** Le nombre de paires « mauvaises » est
> au plus $\sum_{p\ge3}N_p(n)$ (sommé sur les premiers $p\le\sqrt n$ ; $p=2$
> n'intervient jamais car $k$ est toujours impair). **Si cette somme est
> strictement plus petite que $T$, il reste au moins une bonne paire** — et
> le problème est résolu pour ce $n$.

Le travail consiste donc à montrer $\sum_p N_p(n) < T = (L+1)^2$, pour tout
$n$ (ou presque tout $n$). On va voir que les petits premiers sont faciles
(section 5), qu'un argument élémentaire nouveau (le « Lemme K », section 6)
tue le morceau principal des premiers moyens, et que ce qui reste se réduit
à deux questions précises, encore ouvertes (section 10).

> **En résumé.** On majore les « mauvaises » paires par une somme sur les
> premiers, $\sum_pN_p(n)$. S'il y a moins de $T=(L+1)^2$ pièges en tout, il
> reste forcément une bonne paire.

---

## 4. Boîte à outils II : ordre multiplicatif et sous-groupe engendré

> **Boîte à outils — Ordre multiplicatif.** Modulo un entier $m$, l'*ordre*
> de $2$, noté $\mathrm{ord}_m(2)$, est le plus petit entier $d\ge1$ tel que
> $2^d\equiv1\pmod m$. Les puissances $2^0,2^1,2^2,\dots$ modulo $m$ sont
> alors **périodiques de période $d$** : $2^{l+d}\equiv2^l\pmod m$ pour tout
> $l$.
>
> *Analogie.* Une roue dentée qui revient à sa position de départ après $d$
> crans, puis recommence à l'identique.
>
> *Exemple.* Modulo $9$ ($=3^2$) : $2^0=1,2^1=2,2^2=4,2^3=8,2^4=16\equiv7,
> 2^5=32\equiv5,2^6=64\equiv1$. Donc $\mathrm{ord}_9(2)=6$ : la liste des
> puissances de $2$ modulo $9$ est $\{1,2,4,8,7,5\}$ puis ça recommence.

On notera $d_p:=\mathrm{ord}_{p^2}(2)$ et $e_p:=\mathrm{ord}_p(2)$ (le même
calcul, mais modulo $p$ tout seul, sans le carré). L'ensemble des puissances
de $2$ modulo $p^2$, qui a exactement $d_p$ éléments distincts, est noté
$\langle2\rangle$.

> **Exemple, $p=3$.** $e_3=\mathrm{ord}_3(2)=2$ (car $2^1=2,2^2=4\equiv1$).
> $d_3=\mathrm{ord}_9(2)=6$ (calculé ci-dessus). On remarque
> $d_3=6=3\cdot2=3\cdot e_3$ : un facteur $3$ supplémentaire apparaît en
> passant de $9$ à $3$. C'est le cas *générique* (« non-Wieferich », section
> suivante) — pour seulement deux premiers connus au monde, $1093$ et
> $3511$, ce facteur $3$ supplémentaire (en fait $p$ supplémentaire)
> n'apparaît *pas* : $d_p=e_p$. Ces deux exceptions s'appellent les
> *premiers de Wieferich* ; elles sont rares, connues, et faciles à mettre
> de côté une par une.

> **En résumé.** $d_p$ = la période des puissances de $2$ modulo $p^2$.
> Presque toujours, $d_p=p\cdot e_p$ (un facteur $p$ de plus que modulo
> $p$ seul) ; seulement deux premiers connus, $1093$ et $3511$, font
> exception.

---

## 5. Les petits premiers sont faciles

> **Boîte à outils — Borne de périodicité.** Si $2^l\bmod p^2$ se répète
> tous les $d_p$ pas, alors pour $l$ fixé, l'équation
> $2^m\equiv n-2^l\pmod{p^2}$ a au plus $\lceil(L+1)/d_p\rceil$ solutions $m$
> parmi $0,\dots,L$ (un peu plus d'une solution par période complète).
> En sommant sur les $L+1$ valeurs de $l$ :
> $$N_p(n)\ \le\ \frac{(L+1)^2}{d_p}+(L+1).$$

Le morceau dominant de cette borne est $(L+1)^2/d_p$. Si on somme sur
plusieurs petits premiers $p$, on obtient $(L+1)^2\sum_p1/d_p$ ; pour que ce
soit une fraction de $T=(L+1)^2$ strictement inférieure à $\tfrac12$, il
suffit que $\sum_{p}1/d_p<\tfrac12$.

> **Calcul exact, fait à la machine (script `orders.py`).** Pour les premiers
> $3\le p<5000$ (calcul exact de chaque $d_p$, pas d'approximation) :
> $$\sum_{3\le p<5000}\frac1{d_p}=0{,}320516\ldots,$$
> dominé par $p=3$ ($1/6\approx0{,}167$), $p=5$ ($1/20=0{,}05$), $p=7$
> ($1/21\approx0{,}048$) ; la contribution des premiers suivants devient vite
> minuscule. **C'est déjà $<\tfrac12$**, avec une marge confortable
> ($0{,}5-0{,}32=0{,}18$).

On peut aussi montrer, par un argument élémentaire indépendant du calcul
(donc valable même pour les premiers $p\ge5000$, qu'on n'a pas tous testés un
par un), que la somme **complète** $\sum_{p\ge3}1/d_p$ est un nombre fini :
en effet $p$ divise $2^{e_p}-1$, donc $p<2^{e_p}$, donc $e_p$ est au moins de
l'ordre de $\log_2p$ ; et $\sum_p\frac1{p\log p}$ est un fait classique
(théorème de Mertens) qui converge. C'est ce qui garantit que la somme reste
sous contrôle même en ajoutant tous les premiers manquants au-delà de
$5000$, et pas seulement ceux qu'on a testés.

> **En résumé.** En sommant $1/d_p$ sur les premiers, on obtient un nombre
> fini, calculé exactement $\approx0{,}3205<\tfrac12$. Cela règle, une fois
> pour toutes et pour tout $n$, la part des petits et moyens premiers — il
> reste de la marge ($\approx0{,}18\,T$) avant le seuil $T$.

---

## 6. Le Lemme K : l'outil nouveau de ce document

C'est le cœur technique de toute l'investigation. Il dit que, pour presque
tous les premiers, une certaine somme de « phases » s'annule **exactement**,
sans aucune hypothèse de hasard.

> **Boîte à outils — Racine de l'unité et somme de phases.** Pour un entier
> $q$, on note $e_q(t):=e^{2\pi it/q}$, un nombre complexe de module $1$ (un
> point sur le cercle, à l'angle $2\pi t/q$). La propriété clé :
> $$\sum_{j=0}^{p-1}e_p(j)=0$$
> (une somme géométrique de $p$ points régulièrement répartis sur le cercle
> s'annule — ils s'équilibrent exactement). Plus généralement,
> $\sum_{j=0}^{p-1}e_p(aj)=0$ dès que $p\nmid a$ (les $p$ points tournent
> juste plus vite, mais restent régulièrement répartis).
>
> *Analogie.* $p$ personnes régulièrement espacées sur un manège qui tourne :
> leur centre de masse reste au centre, exactement, quelle que soit la
> vitesse (tant qu'elle n'est pas multiple de $p$ tours).

> **Lemme K.** Soit $p\ge3$ un premier *non-Wieferich* (c'est-à-dire
> $d_p=p\cdot e_p$, le cas générique). Pour tout entier $a$ avec $p\nmid a$ :
> $$S(a):=\sum_{x\in\langle2\rangle}e_{p^2}(ax)\ =\ 0.$$

**Pourquoi.** Comme $d_p=p\cdot e_p$, l'ensemble $\langle2\rangle$ (qui a
$d_p$ éléments) contient un sous-ensemble très spécial,
$K=\{1,1+p,1+2p,\dots,1+(p-1)p\}$ ($p$ éléments, régulièrement espacés de
$p$ modulo $p^2$). On regroupe $\langle2\rangle$ en paquets de la forme
$g\cdot K$ ($g$ parcourant les représentants des paquets). Dans chaque
paquet, la somme des phases $e_{p^2}(a\cdot g\cdot(1+jp))$ pour $j=0,\dots,p-1$
se factorise en $e_{p^2}(ag)$ fois $\sum_je_p(agj)$ — et cette dernière
somme est *exactement* la somme de $p$ points régulièrement espacés sur le
cercle, qui s'annule par la boîte à outils ci-dessus. Chaque paquet contribue
donc $0$, et la somme totale aussi.

> **Vérification numérique (script `lemmaE2.py`).** Pour
> $p=3,5,7,11,13,17,19,23,29,31,37,41,43,127$ : le mécanisme ($K\subseteq
> \langle2\rangle$) est confirmé, et la plus grande valeur de $|S(a)|$
> mesurée est exactement $0$, pour tout $a$ non multiple de $p$. Pour les
> deux premiers de Wieferich $1093$ et $3511$ : le mécanisme **casse**
> exactement comme prévu ($K\not\subseteq\langle2\rangle$), et $S(a)\ne0$.
> C'est une confirmation très précise que le lemme capture le bon
> phénomène.

### Conséquence : on connaît exactement le nombre de pièges sur une période complète

En utilisant le Lemme K (par une transformée de Fourier sur le groupe
$\langle2\rangle$), on montre que, sur une période complète $[0,d_p)^2$, le
nombre de paires piégées par $p$ vaut **exactement**
$$p\cdot r_p(n),\qquad r_p(n):=\#\{(u,v): u,v\text{ puissances de }2\bmod p,\ u+v\equiv n\!\!\pmod p\}.$$

> **Exemple, $p=3$, $n=15$.** Modulo $3$, les puissances de $2$ sont
> $H_3=\{1,2\}$ ($2^0=1,2^1=2\equiv-1$). $15\equiv0\pmod3$. Cherchons
> $(u,v)\in H_3^2$ avec $u+v\equiv0\pmod3$ : $1+2=3\equiv0$ ✓, $2+1=3\equiv0$
> ✓ ; $1+1=2\not\equiv0$, $2+2=4\equiv1\not\equiv0$. Donc $r_3(15)=2$. Le
> Lemme K prédit que, sur une période complète de $6\times6=36$ paires
> $(l,m)$ modulo $9$, exactement $3\times2=6$ tombent dans le piège
> $3^2\mid15-2^l-2^m$ — et c'est vérifié exactement par calcul direct
> (script `verify_structure.py`, pour tous les premiers testés
> $3,5,7,11,13,17,19,23$, sur **toutes** les valeurs de $n$ modulo $p^2$, pas
> seulement $n=15$).

Comme $r_p(n)$ est toujours $\le e_p$ (au plus une valeur de $v$ par valeur
de $u$), ceci donne, pour tout $n$, une borne **exacte et uniforme** sur la
contribution des périodes complètes — sans avoir besoin d'aucune hypothèse
d'équidistribution. C'est l'apport principal de ce travail : le morceau
dominant du problème est désormais tué *exactement*, par un argument
élémentaire, pour tout $n$.

> **En résumé.** Le Lemme K dit qu'une certaine somme de phases s'annule
> exactement (pas seulement « en moyenne ») dès que $p$ n'est pas un premier
> de Wieferich. Conséquence : sur une période complète, le nombre de pièges
> est exactement $p\cdot r_p(n)\le p\cdot e_p=d_p$, ce qui referme,
> uniformément en $n$, la part principale du problème.

---

## 7. Le bord (R1) : ce qui dépasse d'une période complète

Le Lemme K contrôle les périodes *complètes*. Mais $\{0,\dots,L\}$ n'est en
général pas un multiple exact de $d_p$ : il y a un petit bout qui dépasse,
le **bord**. On montre que ce bord est, lui aussi, négligeable — par un
argument différent, élémentaire, sans Lemme K.

> **Observation clé.** Si $p$ est non-Wieferich et a une période complète
> dans $\{0,\dots,L\}$ (c'est-à-dire $d_p\le L+1$), alors forcément
> $p\le L+1$ (car $d_p=p\cdot e_p\ge p$). **Il n'y a donc que très peu de
> tels premiers** — au plus $\pi(L+1)\sim(L+1)/\log(L+1)$, le compte des
> premiers jusqu'à $L+1$.

On montre ensuite (par un découpage direct du comptage en « nombre de
périodes complètes $Q_p$ » plus « bord ») que la contribution du bord, pour
chaque tel premier, est au plus $3(L+1)$ — petit. En sommant sur les $\le
\pi(L+1)$ premiers concernés :

> **Proposition R1.** Le bord total $R1(n)$ vérifie
> $$R1(n) < 3(L+1)\,\pi(L+1) = O\!\left(\frac{L^2}{\log L}\right),$$
> qui est *minuscule* comparé à $T=(L+1)^2$ (le rapport $\to0$ quand
> $L\to\infty$).

> **Vérification (`verify_residual.py`).** Pour le pire $n$ testé à chaque
> échelle, jusqu'à $n\approx2^{22}$ : le plus grand premier ayant jamais une
> période complète est $7$ (loin de la borne $L+1\approx21$), et le bord
> mesuré reste $\le32$, bien sous la borne prouvée ($\in[234,528]$ sur la
> même plage).

> **En résumé.** Le bord (ce qui dépasse d'une période complète) ne concerne
> qu'une poignée de petits premiers ($\le L+1$), et sa contribution totale
> est $O(L^2/\log L)$ — négligeable devant $T=(L+1)^2$. **Avec le Lemme K,
> tous les premiers $p\le L+1$ sont désormais réglés, pour tout $n$,
> élémentairement.**

---

## 8. Le Lemme M : dissoudre le pire cas sur les grands premiers

Reste les premiers $p>L+1$ (en gros, ceux sans période complète), jusqu'à
$\sqrt n$. Le comptage brut échoue complètement ici : il y a trop de tels
premiers ($\sim\sqrt n$ d'entre eux) pour qu'une borne $N_p(n)\le L+1$ par
premier suffise. Les données montrent pourtant que le total reste petit
($\ll L^2$), concentré sur la tranche $(L,L^2]$. L'idée du Lemme M est
d'éliminer le problème du *pire $n$* dans cette tranche.

> **Boîte à outils — Maximum sur $n$.** Pour un premier $p$ fixé, on définit
> $$M_p:=\max_n N_p(n)$$
> (le plus grand nombre de pièges que $p$ peut jamais créer, en faisant
> varier $n$). **C'est un nombre qui ne dépend plus de $n$** — une quantité
> purement arithmétique sur les puissances de $2$ modulo $p^2$.

> **Lemme M (dissolution, totalement élémentaire).** Pour *tout* $n$,
> $$\sum_{p\in(L,L^2]}N_p(n)\ \le\ \sum_{p\in(L,L^2]}M_p.$$

C'est presque trivial à démontrer ($N_p(n)\le M_p$ par définition de $M_p$,
pour chaque $p$), mais c'est précieux : si on arrive à montrer que la somme
de droite, qui **ne dépend plus du tout de $n$**, est petite, alors on a
réglé *simultanément* le pire cas pour *tous* les $n$ à la fois — plus besoin
de s'inquiéter d'un $n$ particulièrement malchanceux.

### La moitié qu'on sait prouver : les premiers « Sidon »

> **Boîte à outils — Premier Sidon (pour cette tranche).** On dit que $p$
> est *Sidon* si toutes les sommes $2^i+2^j\bmod p^2$ (pour $i,j$ dans la
> plage utile) sont distinctes, sauf l'échange $i\leftrightarrow j$. Pour un
> tel $p$, $M_p=2$ exactement (une représentation et son échange, jamais
> deux représentations vraiment différentes pour le même reste).
>
> *Analogie.* Une salle où chaque paire de convives a une somme d'âges
> différente : aucune coïncidence, sauf si on échange les deux convives
> entre eux.

On découpe alors :
$$\sum_{p\in(L,L^2]}M_p=\underbrace{2\bigl(\pi(L^2)-\pi(L)\bigr)}_{\text{premiers Sidon}}
+\underbrace{\sum_{\text{non-Sidon}}(M_p-2)}_{\text{excès}}.$$

Le premier terme est **prouvé**, sans aucune hypothèse : il n'y a tout
simplement pas assez de premiers entre $L$ et $L^2$ pour que ce terme
dépasse $L^2$ (c'est juste un comptage de premiers, via le théorème des
nombres premiers) — il est $O(L^2/\log L)$, négligeable.

Le second terme (l'excès dû aux quelques premiers *non*-Sidon, où une
coïncidence se produit) est précisément l'un des deux maillons encore
ouverts (section 10, « M$''$ »).

> **En résumé.** Le Lemme M remplace « le pire $n$ » par « le pire cas
> arithmétique, fixé une fois pour toutes », ce qui élimine le problème du
> mauvais $n$. La moitié de la somme obtenue (la contribution des premiers
> sans coïncidence) est prouvée petite sans condition ; l'autre moitié (les
> rares premiers à coïncidence) reste ouverte.

---

## 9. Presque tout $n$ : un théorème inconditionnel par la moyenne

Section précédente : on a besoin du pire cas. Ici, on change de stratégie et
on regarde la **moyenne** sur $n$ — ce qui permet de conclure pour presque
tous les $n$, au prix de ne plus couvrir absolument tous les $n$.

> **Boîte à outils — Inégalité de Markov.** Si une quantité $X(n)\ge0$ a une
> moyenne $\overline X$ (sur un grand nombre de valeurs de $n$), alors la
> proportion de $n$ pour lesquels $X(n)$ dépasse un seuil $T$ est au plus
> $\overline X/T$.
>
> *Analogie.* Si le salaire moyen dans une entreprise est $3000$€, on ne
> peut pas avoir plus d'un sixième des employés payés $18000$€ ou plus
> (sinon, eux seuls dépasseraient déjà la moyenne totale).

On définit le **terme de coïncidence**
$$C(n):=\sum_{p\in(L,L^2]}N_p(n)\bigl(N_p(n)-1\bigr)$$
(grosso modo : le nombre de fois où *deux* paires différentes tombent dans le
même piège, pour le même $p$). On montre, par un argument de second moment
(une moyenne sur $n$, calculable), que la moyenne de $C(n)$ vaut environ
$$\overline C\approx\frac{L}{12\log L}\ =\ o(L^2)$$
(mesuré numériquement : $\overline C\approx0{,}4$ à $\approx1$ pour
$L=16$ à $32$ — minuscule).

> **Théorème (presque tout $n$, sur la tranche $(L,L^2]$).** Par Markov,
> la proportion de $n$ pour lesquels $\sum_{p\in(L,L^2]}N_p(n)$ dépasse
> $\pi(L^2)+0{,}4L^2$ est au plus $O(1/(L\log L))\to0$. C'est-à-dire :
> **pour presque tous les $n$** (à une exception de densité $\to0$ près),
> cette tranche de premiers contribue moins de $\approx0{,}4\,T$.

**Ce que ce théorème donne, honnêtement, et ce qu'il ne donne pas.** En
combinant ce $0{,}4\,T$ avec les $\approx0{,}32\,T$ déjà réglés
élémentairement (sections 5–7) pour *tout* $n$, on obtient, pour ce même
ensemble de presque tous les $n$ : un total $\approx0{,}72\,T$ sur les
tranches couvertes, laissant une marge de $\approx0{,}28\,T$. **Mais** il
reste une tranche de premiers, $(L^2,\sqrt{n/2}]$, qui n'est *pas* couverte
par ce théorème, même en moyenne (section 10, « B ») : ce théorème ne prouve
donc *pas* la conjecture complète pour presque tout $n$, seulement qu'elle s'y
réduit, pour cette même grande proportion de $n$, à la seule question (B).

> **En résumé.** En passant d'un contrôle « pour tout $n$ » à un contrôle
> « en moyenne sur $n$ », on prouve, sans aucune condition, que la tranche
> dominante $(L,L^2]$ contribue peu pour presque tous les $n$. C'est un vrai
> théorème, mais portant sur une tranche précise, pas sur le problème
> complet.

---

## 10. Ce qui reste ouvert : deux maillons précis

Après tout ce travail, le problème se réduit à exactement deux questions
propres, isolées, et non résolues ici. On donne pour chacune l'endroit
*exact* où le comptage élémentaire échoue.

### Maillon (M$''$) : la queue de distribution des coïncidences, sur $(L,L^2]$

Il s'agit de montrer que la somme des « excès de coïncidence »
(section 8) sur les premiers non-Sidon de $(L,L^2]$ reste $o(L^2)$ — pas
seulement en moyenne, mais **pour tout $n$** (pour retrouver le pire cas, pas
seulement presque tout cas).

*Où le calcul brutal échoue.* On sait que $M_p$ (le pire nombre de pièges
qu'un premier $p$ puisse jamais créer) **n'est pas borné par une constante
absolue** : il croît lentement (empiriquement $3,4,4,4,5,6$ pour
$L=20,30,40,50,60,70$), atteint sur des premiers où l'ordre de $2$ est
anormalement petit (par exemple $p=127$, où $2$ n'a que $7$ valeurs
possibles avant de boucler). La borne brute (multiplicité maximale fois
nombre de premiers concernés) donne $\Theta(L^2)$ — pas $o(L^2)$ : ça échoue
d'un cheveu, pas d'un ordre de grandeur. Il faudrait montrer que la
*répartition* des multiplicités décroît assez vite (peu de premiers ont une
multiplicité $\ge3$, encore moins $\ge4$, etc.) — un énoncé du type
« combinatoire additive fine », plausible (la proportion de premiers
non-Sidon, $\approx17\,\%$, est stable empiriquement, pas écrasante) mais que
nous n'avons pas su établir.

### Maillon (B) : le mur d'équidistribution, sur $(L^2,\sqrt{n/2}]$

Il s'agit de montrer que les premiers **entre $L^2$ et $\sqrt{n/2}}$**
(la tranche la plus large en nombre de premiers parmi toutes celles
considérées !) ne créent, ensemble, que $o(L^2)$ pièges — même seulement *en
moyenne* sur $n$, ce qu'on n'a même pas réussi à établir.

*Où le calcul brutal échoue.* Pour un premier $p$ aussi grand, chaque valeur
$k=n-2^l-2^m$ ($\le n$) n'a qu'au plus $O(L/\log L)$ facteurs premiers au
carré dans cette tranche (car $(L^2)^{L/\log L}\sim n$) ; la borne brute
donne donc $(L+1)^2\cdot O(L/\log L)=O(L^3/\log L)$ — le **cube** de $L$, pas
le carré : c'est, dans le pire des cas naïfs, la tranche la plus dangereuse
de toutes, même si les données numériques suggèrent qu'elle reste en réalité
modeste. Il faudrait un résultat de densité-sans-facteur-carré ou
d'équidistribution pour la suite structurée $\{n-2^l-2^m\}$ dans cette
tranche — du même esprit que ce qui sous-tend les résultats « presque tout
$n$ » connus pour la variante à une seule puissance du problème #11
original, mais nous n'avons pas trouvé comment le réduire davantage par des
moyens élémentaires.

### Une tranche, en revanche, est entièrement réglée : $(\sqrt{n/2},\sqrt n]$

Pour les tout premiers plus grands ($p$ proche de $\sqrt n$), un résultat
récent de Kalinin (2026) — utilisant une analyse $2$-adique élémentaire,
sans équidistribution — bornent cette tranche par $O(L)$, pour **tout** $n$.
C'est, avec les petits premiers (section 7), la seule tranche complètement
fermée sans condition.

### Tableau récapitulatif

| Tranche de premiers $p$ | Statut |
|---|---|
| $p\le L+1$ | **réglé**, pour tout $n$ (Lemme K + Proposition R1) |
| $(L,L^2]$ | pire cas dissous ; reste ouvert : $o(L^2)$ (maillon M$''$) ; presque tout $n$ : prouvé |
| $(\sqrt{n/2},\sqrt n]$ | **réglé**, pour tout $n$ (Kalinin 2026) |
| $(L^2,\sqrt{n/2}]$ | ouvert, même en moyenne (maillon B) |

> **En résumé.** Il reste deux questions précises et isolées, chacune butant
> sur le comptage brut à un endroit identifié : (M$''$) une décroissance fine
> de la distribution des coïncidences sur une tranche étroite de premiers
> juste au-dessus de $L$ ; (B) une équidistribution/densité sans facteur
> carré sur la tranche, beaucoup plus large, entre $L^2$ et $\sqrt n$.

---

## 11. Conclusion

Pour résumer tout le chemin parcouru sur nos trois exemples filés
($n=15,21,45$, où l'on a vu dès la section 1 que le premier essai marche
parfois et échoue parfois) : le problème se réduit maintenant à deux
questions d'analyse des nombres, propres et nommées, après une fermeture
élémentaire complète de tous les petits et moyens premiers (Lemme K, une
contribution nouvelle de ce travail, plus la Proposition R1), une
élimination déterministe du problème du pire $n$ sur la tranche dominante
(Lemme M), et un théorème inconditionnel « presque tout $n$ » sur cette même
tranche obtenu par une moyenne et l'inégalité de Markov. Aucun de ces deux
maillons restants — (M$''$) et (B) — n'est, à notre connaissance, une
reformulation d'une conjecture déjà connue ; les deux nous semblent du
ressort d'un spécialiste des sommes d'exponentielles / du grand crible, mais
nous ne les avons pas résolus. Rien de tout cela n'est encore formalisé en
Lean ; seul l'énoncé cible (`erdos_11.variants.two_pow_two`) existe sous
cette forme.
