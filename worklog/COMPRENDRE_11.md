# Comprendre le papier #11 — guide en langage simple

*Document compagnon de « Elementary reductions for the two-powers squarefree
variant of Erdős Problem #11 ». Même but que COMPRENDRE_273.md : savoir ce que
le papier affirme, comment (dans les grandes lignes), ce qui reste ouvert, et
quoi répondre aux questions.*

---

## 1. Le problème, en partant de zéro

### 1.1 « Sans facteur carré », c'est quoi ?

Un entier est **squarefree** (sans facteur carré) si aucun carré parfait > 1 ne
le divise. Autrement dit : dans sa décomposition en facteurs premiers, chaque
premier apparaît au plus une fois.

- 10 = 2 × 5 → squarefree ✓
- 15 = 3 × 5 → squarefree ✓
- 12 = 2² × 3 → PAS squarefree (divisible par 4) ✗
- 45 = 3² × 5 → PAS squarefree (divisible par 9) ✗

C'est une propriété *fréquente* : environ 61 % des entiers sont squarefree
(la proportion exacte est 6/π²). C'est important : on cherche quelque chose de
courant, pas de rare — c'est ce qui rend le problème plausible.

### 1.2 Le problème #11 d'Erdős, et notre variante

**Le problème #11 original** (ouvert) : tout entier assez grand peut-il s'écrire
n = k + 2^m, avec k squarefree et 2^m une puissance de 2 ?

**Notre variante « deux puissances »** : tout entier impair n > 1 peut-il
s'écrire n = k + 2^l + 2^m, avec k squarefree ?

Exemple : n = 23. On essaie 2^1 + 2^2 = 6 → k = 17, premier donc squarefree ✓.
Trouvé du premier coup — et c'est typique : il y a *beaucoup* de choix de paires
(l, m), et il suffit qu'UN SEUL donne un k squarefree.

Donner deux puissances au lieu d'une devrait rendre le problème plus facile
(plus de tentatives autorisées) ; une remarque attribuée à Erdős suggère qu'il
pensait cette relaxation « peut-être facile ». Notre papier montre qu'elle ne
l'est pas — mais qu'on peut la pousser très loin, et localiser exactement où
elle se bloque. La variante est enregistrée sous le nom
`erdos_11.variants.two_pow_two` dans les dépôts de formalisation Lean ; à notre
connaissance, personne ne l'avait étudiée.

### 1.3 Vérifié à la machine jusqu'à 50 millions

Avant toute théorie : la variante a été testée pour tous les n impairs jusqu'à
5 × 10⁷. Aucune exception. Ça ne prouve rien (il y a une infinité d'entiers),
mais ça dit que si un contre-exemple existe, il est grand.

---

## 2. La stratégie : compter les échecs

### 2.1 Le budget d'essais

Pour un n donné, notons L le nombre de bits de n (précisément L = ⌊log₂ n⌋).
Les paires possibles (l, m) avec 2^l + 2^m < n sont environ **T = (L+1)²**.
Pour n autour d'un milliard, L ≈ 30 : environ 960 essais.

**L'idée maîtresse du papier tient en une phrase** : au lieu de chercher une
paire qui MARCHE, on compte les paires qui ÉCHOUENT. Une paire échoue quand
k = n − 2^l − 2^m est divisible par un carré p² (p premier). Si on prouve que
le nombre total d'échecs est **strictement inférieur à T**, alors au moins une
paire réussit — et le problème est résolu pour ce n. Toute la bataille consiste
à majorer les échecs, premier par premier.

### 2.2 La répartition par taille de premier

Chaque premier p peut « saboter » certaines paires (celles où p² divise k).
Combien ? Ça dépend de la taille de p. Le papier découpe les premiers en zones :

| Zone | Statut final |
|---|---|
| Petits premiers (p ≤ L+1) | **FERMÉE** pour tout n — c'est le cœur du papier (Lemme K + Prop. R1) |
| Zone médiane (L < p ≤ L²) | fermée pour *presque tout* n ; pour *tout* n, c'est LE verrou (deux sous-cas, voir §4) |
| Grande zone (L² < p ≤ √(n/2)) | fermée pour presque tout n ; ouverte pour tout n (« mur B ») |
| Très grands (près de √n) | fermée (argument de carrés parfaits) |

### 2.3 Le Lemme K : le terme dominant s'annule EXACTEMENT

Le plus gros danger vient des petits premiers (3, 5, 7 sabotent beaucoup de
paires). Le papier prouve que leur contribution se calcule **exactement** grâce
à une annulation de « sommes de caractères » — une identité algébrique, pas une
estimation. Résultat : les petits premiers sabotent au plus ≈ 32 % des paires
(la constante 0,3205 du papier), pour TOUT n, sans aucune hypothèse.

Une curiosité au passage : cette annulation exige que p ne soit pas un
« premier de Wieferich » (une propriété rarissime : on n'en connaît que deux
dans tout l'univers des nombres, 1093 et 3511). Le papier montre que ces deux
exceptions coûtent une miette négligeable — et, point important, notre argument
ne dépend PAS de la conjecture ouverte sur l'infinité des Wieferich.

---

## 3. Le théorème principal : vrai pour « presque tout » n

### 3.1 Ce qu'il dit

> **Corollaire 6.9 (inconditionnel).** La proportion des n impairs pour lesquels
> la variante pourrait échouer tend vers 0 (à vitesse ≈ 1/(L log L)). Autrement
> dit : pour presque tous les entiers impairs, n = squarefree + 2^l + 2^m, et
> c'est PROUVÉ, sans aucune hypothèse.

« Presque tout » a ici un sens mathématique précis : l'ensemble des exceptions
possibles a une densité qui s'écrase vers zéro. Ce n'est pas « tout n » (voir
§4), mais c'est un vrai théorème, complet, autonome (aucun résultat extérieur
non vérifié n'est utilisé), et c'est le résultat central du papier.

### 3.2 L'idée de la preuve (l'image du casino)

Pour la zone médiane et la grande zone, on ne sait pas contrôler le PIRE n —
mais on sait contrôler le n MOYEN. L'argument est probabiliste : on calcule la
moyenne du nombre d'échecs sur tous les n d'une plage, on montre qu'elle est
petite, et l'inégalité de Markov (un principe élémentaire : si la moyenne des
dépenses est petite, peu de gens dépensent beaucoup) borne la proportion de n
« malchanceux ». Les malchanceux existent peut-être, mais ils sont rares, et de
plus en plus rares quand n grandit.

---

## 4. Ce qui bloque pour « TOUT n » — les verrous, expliqués

Pour passer de « presque tout n » à « tout n », il faudrait contrôler le pire
cas de la zone médiane (L < p ≤ L²) et de la grande zone. Le papier montre que
tout se ramène à UNE question : dans la zone médiane, combien de paires
différentes peuvent donner le même reste modulo p² ? (La « multiplicité ».)
Cette question se coupe en deux selon le comportement du nombre 2 modulo p :

### 4.1 Type A — un résultat partiel réel, avec un écart mesuré

Pour les premiers où les puissances de 2 « tournent vite » modulo p, on a
trouvé dans la littérature un théorème taillé sur mesure (García–Voloch, 1988,
via la méthode de Stepanov) qui borne directement la multiplicité. Résultat
inconditionnel du papier : la contribution Type A est au plus ≈ L^{8/3},
alors qu'il faudrait L². **Il manque exactement un facteur L^{2/3}** — l'écart
est mesuré au décimal près, et la question ouverte est formulée proprement
(peut-on exploiter une symétrie spéciale de nos sommes, « l'involution », pour
combler l'écart ?).

### 4.2 Type B — fermé « par circularité » (le résultat le plus subtil)

Pour les autres premiers, la borne dont on aurait besoin s'appelle (TB). Le
papier prouve deux choses surprenantes :

1. Un théorème puissant de Bourgain–Chang (2006) s'applique à nos sommes et
   donne une vraie annulation — on l'a vérifié sur les textes sources ET
   numériquement. Bonne nouvelle apparente.
2. MAIS : convertir cette annulation en la borne (TB) exige une autre borne…
   qui est mathématiquement ÉGALE à (TB) elle-même. Le serpent se mord la
   queue : l'ingrédient manquant EST la conclusion visée.

C'est ce qu'on appelle la **fermeture par circularité** : (TB) n'est pas « un
résultat qui attend sa référence dans la littérature », c'est une vraie
estimation ouverte, au front de la recherche. Le documenter précisément épargne
des mois à quiconque réessaiera.

### 4.3 Le diagnostic final : le coupable, ce sont les RETENUES

Le papier teste toute l'architecture dans un monde parallèle : les polynômes
(remplacer le nombre 2 par la variable t). Là-bas, l'analogue de (TB) se
démontre en trois lignes. Pourquoi ? Parce que les monômes ne « portent »
jamais : t^a + t^a = 2·t^a, toujours de degré a. Alors que chez les entiers,
2^a + 2^a = 2^{a+1} : l'addition binaire PROPAGE DES RETENUES, exactement comme
quand tu poses une addition à l'école. Ce phénomène de retenue est précisément
ce qui empêche de borner les coïncidences modulo p². Conclusion du papier : la
difficulté de #11-variante n'est pas un manque d'annulation (elle existe, on
l'a prouvé), c'est un phénomène « archimédien » — les retenues de l'écriture
binaire. Localiser un mur à ce niveau de précision est une contribution en soi.

### 4.4 Deux pièges classiques évités (à connaître pour la FAQ)

- **Wieferich** : notre preuve n'a PAS besoin de la conjecture ouverte sur les
  premiers de Wieferich — seulement d'écarter les deux connus (coût négligeable).
- **Crocker** : le problème cousin avec un PREMIER au lieu d'un squarefree
  (n = p + 2^a + 2^b) est FAUX (réfuté en 1971 par une astuce de congruences).
  Le papier explique pourquoi cette astuce ne peut pas s'appliquer chez nous :
  « composite » se force par congruence, « non-squarefree » non (les squarefree
  sont trop fréquents dans toute progression). Notre variante reste plausible
  là où sa cousine est fausse.

---

## 5. La vérification machine (Lean)

Cinq lemmes élémentaires qui portent les résultats inconditionnels ont été
formalisés et vérifiés dans l'assistant de preuve Lean 4 (fichier
`Erdos11_verified.lean`, zéro `sorry` — c'est-à-dire zéro trou de preuve).
Les parties analytiques et conditionnelles ne sont volontairement PAS
formalisées : leur statut de conjecture est ainsi visible dans la structure
même du dépôt. Personne n'a à nous croire sur les briques de base : la machine
les a vérifiées.

---

## 6. FAQ — si on te pose la question

**« Vous avez résolu la variante ? »** — Non. Prouvé pour presque tout n
(inconditionnellement) ; pour tout n, c'est conditionnel à (TB) + deux entrées
plus douces, et le papier localise exactement pourquoi (TB) est hors de portée
actuelle.

**« Et le problème #11 original ? »** — Pas touché. On étudie une relaxation ;
nos techniques ne remontent pas au problème à une puissance. D'ailleurs le
papier montre que le verrou (TB), regardé de près, est lui-même un cousin de
#11 — la difficulté ne se contourne pas par relaxation, elle se concentre.

**« Pourquoi croire les calculs ? »** — Chaque affirmation numérique pointe vers
un script nommé ; les cinq lemmes de base sont vérifiés en Lean ; les théorèmes
externes (García–Voloch, Bourgain–Chang, Heath-Brown) sont cités avec leurs
conditions exactes, collationnées sur les sources — et le papier signale
lui-même le seul endroit où une dépendance externe non re-vérifiée subsiste
(le preprint de Kalinin, utilisé uniquement dans la partie conditionnelle ;
le théorème principal n'en dépend plus).

**« Quelle est la contribution si rien n'est résolu ? »** — Un théorème
inconditionnel (presque tout n), un résultat partiel avec écart mesuré (Type A),
une fermeture par circularité documentée (Type B), un diagnostic structurel
(les retenues), et deux questions ouvertes formulées au millimètre. C'est la
transformation d'un problème flou en problème précis — le matériau exact dont
le prochain chercheur a besoin.

---

## 7. Petit lexique (complément de celui du #273)

- **Squarefree** : aucun carré > 1 ne le divise (≈ 61 % des entiers).
- **L** : le nombre de bits de n ; **T = (L+1)²** : le nombre de paires d'essai.
- **N_p(n)** : le nombre de paires sabotées par le premier p (celles où p²
  divise n − 2^l − 2^m).
- **Somme de caractères** : somme d'exponentielles complexes dont l'annulation
  traduit une répartition parfaitement équilibrée ; le Lemme K en prouve une
  annulation EXACTE.
- **Wieferich** : premier p tel que p² divise 2^{p−1} − 1 ; deux connus (1093,
  3511), infinité ouverte — notre preuve n'en dépend pas.
- **Type A / Type B** : premiers de la zone médiane selon que l'ordre de 2
  modulo p est petit (≤ L) ou grand (> L).
- **(TA), (TB), (B)** : les trois énoncés ouverts nommés ; (TB) est le verrou
  central, clos par circularité.
- **Circularité** : situation où l'ingrédient manquant pour prouver X est
  logiquement équivalent à X — signe qu'on est au front, pas en retard de
  bibliographie.
- **Presque tout n** : tous sauf un ensemble d'exceptions de densité tendant
  vers 0 (sens mathématique précis, pas une façon de parler).
- **Corps de fonctions / F_q[t]** : le « monde parallèle » des polynômes où
  l'on teste l'architecture ; les monômes n'ont pas de retenues.
- **Archimédien** : relatif à la taille réelle des nombres (ici : le phénomène
  de retenue binaire), par opposition aux propriétés de divisibilité.
