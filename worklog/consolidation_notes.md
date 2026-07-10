# Notes de consolidation (Erdős #11 deux-puissances) — salve García–Voloch + corps de fonctions + digits.
# PAS d'écriture dans PAPER.tex cette salve (consigne user). Tout ici, à intégrer plus tard sur signal.

---
## CHANTIER G — consolidation García–Voloch (attribution + conditions + bande + p|n)

### G.1 Attribution corrigée (source lue par Fable, notes de Konyagin)
La borne de **multiplicité maximale** N₂(b) ≤ 4|G|^{2/3} n'est **PAS** de Heath-Brown–Konyagin mais de
**García–Voloch** (Theorem 2.1) :

> **Théorème (García–Voloch).** Si `|G| < (p−1)/((p−1)^{1/4}+1)` (≈ p^{3/4}), alors pour tout
> **b ∈ Z_p^*** (b≠0) : `N₂(b) = #{(u,v)∈G²: u+v≡b} ≤ 4|G|^{2/3}`.

- Heath-Brown a redonné une preuve par la **méthode de Stepanov**.
- Heath-Brown–Konyagin ont l'**énergie** T₂(G) ≪ |G|^{5/2} (pour |G| ≤ p^{2/3}).
- Konyagin–Shparlinski, *Character sums with exponential functions* (CUP) = monographie de référence.

⟹ Dans le papier (plus tard) : citer **García–Voloch** pour la borne de multiplicité, HB / HB-K pour la
technique/énergie. NE PAS attribuer la borne à HB-K.

### G.2 Le cas dégénéré = exactement l'exclusion b≠0 du théorème source
Notre découverte numérique (STEP52 : borne fausse pour n=0, r_p(0)=e_p quand −1∈⟨2⟩) **coïncide
parfaitement** avec la condition `b ∈ Z_p^*` de García–Voloch. La borne à écrire est « pour n≢0 mod p »,
exactement ce qui a été vérifié. Source ↔ numérique en accord total.

### G.3 Condition de taille : p^{3/4} (mieux que le p^{2/3} annoncé de mémoire)
Condition `|G| < (p−1)/((p−1)^{1/4}+1) ≈ p^{3/4}`. Pour Type A (e_p≤L, p>L) : échoue seulement si
e_p > p^{3/4}, i.e. **p < e_p^{4/3} ≤ L^{4/3}**. Bande exceptionnelle **p ∈ (L, L^{4/3})**.

**CONFIRMÉ numériquement (chantierG_band.py, ce jour) :**
| L | #TypeA | #viol(e_p>p^{3/4}) | max p viol | L^{4/3} | contrib bande (L+1)·#viol | main L^{8/3}/logL | absorbé |
|---|---|---|---|---|---|---|---|
| 60 | 36 | 8 | 157 | 235 | 488 | 13476 | OUI |
| 100 | 61 | 15 | 353 | 464 | 1515 | 46783 | OUI |
| 140 | 76 | 16 | 727 | 727 | 2256 | 106939 | OUI |
| 200 | 114 | 23 | 971 | 1170 | 4623 | 258192 | OUI |
| 300 | 182 | 43 | 2003 | 2008 | 12943 | 707121 | OUI |

`max p viol < L^{4/3}` partout (bande exactement où prédite), et contribution triviale ≪ terme principal
(rapport ~1/30 à ~1/55). ⟹ **La proposition Σ_{Type A} M_p = O(L^{8/3}/logL) tient**, bande traitée par
le trivial M_p≤L+1. À écrire : « hors la bande p∈(L,L^{4/3}) [O(L^{4/3}/logL) premiers, contribution
O(L^{7/3}/logL) absorbée], García–Voloch donne κ_p≪e_p^{2/3}. »

### G.4 Traitement des p|n (résidu cible ≡ 0 mod p)
n≡0 mod p ⟺ p|n : #{p∈(L,L²]: p|n} ≤ log n/log L = O(L/log L) premiers par n, chacun M_p≤L+1 ⟹
contribution **O(L²/log L)**, strictement sous le terme principal O(L^{8/3}/log L) (car L² < L^{8/3}) ⟹
**absorbée** ✓. Note : le résidu dégénéré mod p² (2^l+2^m≡0 mod p²) reste INATTEIGNABLE en
range Type A (STEP52 : m−l≍ord_{p²}(2)/2≫L), donc c'est bien le cas n≡0 mod p (pas mod p²) qui compte,
géré trivialement.

### G.5 Bonus dans la source (à exploiter plus tard, PAS écrire avant lecture Fable)
- **T_k(G) ≪_k |G|^{2k−2+2^{1−k}}** pour |G|≤p^{1/2} (Thm 2.8, Stepanov–HB itéré) : bornes d'énergie
  d'ordre supérieur mod p — utiles pour les moments factoriels Type A (E_k^tot Type A).
- **Thm 3.15 (Bourgain)** : pour T>p^δ et g^j (j<T) distincts, `max_{a≠0} |Σ_{j<T} e(a g^j/p)| ≪_δ T p^{−ε}`.
  **Vérifie NOTRE régime Type B** : e_p>L ⟹ 2^j (j≤L) distincts mod p ; T=L+1>p^δ car p≤L² (tout δ<1/2).
  ⟹ **la cancellation sup-norme des sommes géométriques incomplètes existe DÉJÀ mod p, inconditionnelle,
  dans exactement notre plage.** Ce qui manque pour (TB) = passage mod p² (caractères p∤t). Cible :
  Bourgain(–Chang) sur sous-groupes de Z_q^*, q composé (q=p²). **Fable localise/lit ; ne rien écrire
  avant.** Si ça couvre les sommes INCOMPLÈTES (segments de ⟨2⟩), (TB) passe « hypothèse → théorème sous
  condition de lecture ».

---
## CHANTIER E — dictionnaire corps de fonctions F_q[t] (le build, priorité). Aucune preuve à ce stade.

**Objectif (Fable) :** faire tourner l'architecture entière (Lemme K → R1 → Lemme M → moments) sur F_q[t]
où (TB) devrait tomber par Weil, et identifier la paire (énoncé (TB), borne de Weil) à transposer en
caractéristique 0.

### E.1 La variante analogue
- **ℤ ↦ F_q[t]** (anneau principal, q fixé, PGCD/factorisation uniques).
- **base 2 ↦ la variable t** (ou un polynôme fixe g(t) ; prendre g=t est le plus propre : ⟨t⟩ lacunaire).
- **n impair ↦ n(t)∈F_q[t]** de degré D (l'analogue de log₂ n = D ; L ~ D).
- **sans facteur carré ↦ sans facteur carré dans F_q[t]** (non divisible par P² pour P irréductible ;
  densité 1−1/q, analogue de 6/π²).
- **Énoncé :** *tout n(t) de degré assez grand (condition de parité/normalisation TBD) s'écrit
  n(t)=k(t)+t^l+t^m avec k(t) sans facteur carré, 0≤l≤m.*

### E.2 Le crible
- **premiers p ↦ irréductibles P(t)** ; **|p| ↦ |P|=q^{deg P}** ; **p≤√n ↦ deg P ≤ D/2**.
- **N_P(n)=#{(l,m): P²|n−t^l−t^m}** ; seuil T ~ (#puissances)² = (L+1)².
- **Σ_p 1/p² ↦ Σ_P 1/|P|²** = Σ_d (#irr deg d)/q^{2d} ~ Σ_d 1/(d q^d) < 1 (q=2 : ≈0.60). ⟹ **couverture
  par congruences mod P² IMPOSSIBLE** (même obstruction structurelle qu'en ℤ, Σ1/|P|²<1). Le découplage
  Crocker se traduit tel quel.

### E.3 ord et Lemme K
- **ord_p(2) ↦ ord_P(t)** = ordre de t dans (F_q[t]/P)^* (groupe cyclique d'ordre |P|−1=q^{deg P}−1).
- **Type A/B :** ord_P(t) ≤ L vs > L.
- **noyau K=1+pℤ/p² ↦ K_P = 1+P·(F_q[t]/P²)** = noyau de (F_q[t]/P²)^* → (F_q[t]/P)^*, d'ordre |P|.
- **Lemme K analogue :** pour P **non-Wieferich** (t^{ord_P(t)} ≢ 1 mod P²), ⟨t⟩ mod P² contient K_P, et
  `Σ_{x∈⟨t⟩} ψ(a x)=0` pour ψ caractère additif non trivial de F_q[t]/P² (annulation sur K_P-classes,
  même preuve : somme géométrique de raison ψ(a·)≠1). **Se traduit directement.**
- **Involution :** `1+t^{e−δ} ≡ t^{−δ}(1+t^δ) mod P` — algébrique, se traduit tel quel.

### E.4 Le rôle de (TB) et la borne de Weil (le cœur du gain)
- **(TB) analogue :** borne de moment/énergie sur la multiplicité de {t^l+t^m mod P²}, = moyenne
  quadratique des sommes géométriques incomplètes `S(a)=Σ_{j≤L} ψ(a t^j)` mod P².
- **La différence décisive :** sur F_q[t], ces sommes sont des **sommes de caractères additifs le long
  d'une progression géométrique dans un corps/anneau fini**, bornées par **Weil (RH pour courbes sur
  corps finis)** — square-root cancellation INCONDITIONNELLE. L'estimation qui est conjecturale sur ℤ
  (niveau Bourgain, cf. G.5) est un **THÉORÈME** sur F_q[t].
  - Mod P (P irréductible, F_q[t]/P = F_{q^{deg P}} corps) : `Σ_{j} ψ(a t^j)` = somme additive sur
    (segment de) ⟨t⟩ ⊂ F_{q^{deg P}}^* ; bornée par Weil/Katz (sommes de caractères sur sous-groupes
    multiplicatifs). **C'est l'analogue EXACT du bonus Bourgain Thm 3.15 (G.5), mais prouvé par Weil.**
  - Mod P² (anneau, pas corps) : analogue du « module composé » de Bourgain. Sur F_q[t] il y a des
    bornes de sommes exponentielles sur anneaux F_q[t]/P² (Weil/Deligne pour sommes sur schémas) OU
    réduction via K_P (Lemme K) au cas mod P. **C'est LE point à établir précisément** — mais il devrait
    tomber, car tout est Weil.
- **⟹ Prédiction :** sur F_q[t], (TB) est un **théorème** (Weil), donc l'every-n analogue devrait être
  **prouvable inconditionnellement** (modulo la rédaction de tous les maillons). Ce serait la validation
  de l'architecture, et la borne de Weil exacte utilisée = la CIBLE à chercher en caractéristique 0
  (quel grand crible / quelle estimation de somme exponentielle joue son rôle).

### E.5 Ce qui NE se traduit PAS proprement (à signaler)
- **Wieferich :** en ℤ, premiers Wieferich (2^{p−1}≡1 mod p²) rares/conjecturalement finis. Sur F_q[t],
  « P Wieferich » (t^{ord}≡1 mod P²) — densité et rôle à CLARIFIER ; en caractéristique p il y a en plus
  la subtilité Frobenius/inséparabilité (t^q, dérivée). Point de vigilance : la classe Wieferich pourrait
  être plus grosse ou se comporter autrement (l'exclusion du Lemme K).
- **Le « impair » / la normalisation :** l'analogue de « n impair » (condition 2∤n) est flou — quelle
  condition sur n(t) ? (deg, coeff dominant, n(0)≠0 ?). À fixer.
- **La constante pivot 0.3205 :** dépend de la densité des premiers (Σ 1/(p log p)) ; l'analogue F_q[t]
  a Σ 1/(|P| deg P) — valeur numérique différente, structure identique.
- **Kalinin (range (√(n/2),√n]) :** l'analogue « t^l=t^m ⟹ carré parfait » et l'analyse 2-adique/mod 8
  n'ont pas d'analogue évident en caractéristique p (pas de 2-adique) — à repenser.

### E.6 Livrable de la salve
Ce dictionnaire. Prochaine étape (sur signal) : rédiger une **section « analogue en corps de fonctions »**
du papier avec (a) l'énoncé de la variante F_q[t], (b) Lemme K analogue, (c) l'énoncé (TB) analogue et
la borne de Weil qui le clôt (à préciser mod P²), (d) la table de traduction E.5 des points non triviaux.
Bénéfice : soit (TB)-F_q[t] tombe (⟹ on sait quelle estimation chercher en car. 0), soit un point résiste
(⟹ on apprend où est la vraie difficulté, même dans le monde « facile »).

---
## CHANTIER H — conversion Bourgain–Chang → moments. Sup-norme CONFIRMÉE, mais la conversion naïve BLOQUE.

### H.1 Sup-norme Bourgain–Chang (Cor 4.5) : CONFIRMÉE numériquement (chantierH_supnorm.py)
`max_{p∤ξ} |S(ξ)|/(L+1)`, S(ξ)=Σ_{j≤L} e_{p²}(ξ2^j), sur premiers Type B :
| L | ratios observés | 
|---|---|
| 40 | 0.37, 0.37, 0.40, 0.46 |
| 80 | 0.33, 0.29, 0.34, 0.29 |
| 120 | 0.25, 0.24, 0.24, 0.25 |
Ratio <1 partout, **décroît nettement avec L** (ε_eff≈0.4). Bourgain–Chang vérifié sur nos données. ✓

### H.2 Identité d'orthogonalité (propre)
N_p(r)=#{(l,m)∈[0,L]²:2^l+2^m≡r mod p²} (ordonné). S(ξ)²=Σ_r N_p(r)e_{p²}(ξr). Moment ordinaire :
`M_k := Σ_r N_p(r)^k = (1/p²)^{k−1} Σ_{ξ_1+…+ξ_k≡0 mod p²} Π_i S(ξ_i)²`.
3 classes : ξ=0 (|S|=L+1) ; p∤ξ (|S|<(L+1)^{1−ε}, BC) ; ξ=pη≠0 (|S|<(L+1)^{1−ε'}, mod p, ordre e_p>√p).
Soit B := max_{ξ≠0}|S(ξ)| < (L+1)^{1−ε₀}, ε₀=min(ε,ε')>0.

### H.3 Le calcul — et l'inéquation qui BLOQUE
Terme « toutes fréquences ≠0 » (k fréquences non nulles, Σ=0) : borner k−2 facteurs par B², garder 2 pour
Parseval (Σ_ξ|S(ξ)|²=p²(L+1)), sommer les k−3 libres restants (facteur (p²)^{k−3}) :
`W_k^{≠0} ≤ (1/p²)^{k−1}·B^{2(k−2)}·(L+1)²·p^{2(k−1)} = B^{2(k−2)}(L+1)² = (L+1)^{2k−2−2(k−2)ε₀}` (par premier).
Sommé sur Type B (Σ_p 1 ~ L²/logL) et divisé par 2^k k! (moment factoriel E_k^tot) :
`E_k^{tot,≠0} ≲ (L+1)^{2k−2−2(k−2)ε₀}·L²/(2^k k! logL)`.
**À k ~ k*=3logL/loglogL** (où E_k^null≈1, k*!~L³) : le terme vaut
`≈ exp(6(1−ε₀)·log²L/loglogL) / (L logL)` = **SUPER-POLYNOMIAL ≫ L²**.

**Raison exacte du blocage :** chaque fréquence non nulle supplémentaire multiplie la borne par
`B² = (L+1)^{2−2ε₀} > 1` (la somme p² sur la fréquence libre × le sup-norme B² × le 1/p² du préfacteur
= B²). La sup-norme sauve un facteur (L+1)^{−2ε₀} par fréquence, MAIS la somme sur la fréquence libre
apporte (L+1)^{+2} : le gain ne compense pas. À k~k*, l'accumulation `(L+1)^{(2−2ε₀)k}` explose
super-polynomialement. **⟹ Cor 4.5 (sup-norme SEULE) ne ferme PAS (TB) par cette conversion.**

### H.4 Ce qu'il faudrait (au-delà de Cor 4.5)
Fermer exigerait d'exploiter la **cancellation dans la contrainte Σξ_i=0** (la convolution k-fois), i.e.
une borne de type **L⁴ / corrélation d'ordre supérieur** sur S, PAS seulement le sup-norme. La sup-norme
donne B<L+1 mais B²>1, insuffisant. Question source (Fable) : Bourgain–Chang a-t-il, ailleurs que 4.5,
des bornes de moment/L^{2k} sur Σ_j e_q(ξ g^j) (pas juste sup-norme) ? Si oui, (TB) pourrait passer ;
sinon la voie sup-norme est close. **Ne PAS écrire « (TB) fermé » — la conversion naïve échoue.**

### H.5 Bug d'énoncé du Théorème 5.8 (à corriger en consolidation)
Le Thm 5.8 énonce (TB) « E_k^tot≤C^k E_k^null pour k≤k* » mais sa preuve utilise (TB) pour **k>k***
(la queue Σ_{k>k*}). L'hypothèse ne couvre pas son usage. Correction : énoncer (TB) **pour tout k≥2**,
OU traiter la queue k>k* séparément (ce que BC ferait — mais H.3 montre que sup-norme seule n'y suffit
pas). À consigner. [Note : E_k^null≈1 franchi à k*, donc k*·π(L²)=O(L²/loglogL)=o(L²) est déjà
inconditionnel pour k≤k* ; le vrai besoin de (TB) est bien la queue k>k*, non couverte par l'énoncé actuel.]

### H.7 CHANTIER I — la voie sup-norme est close par CIRCULARITÉ (pas par absence de littérature)
**Point clé (Fable, vérifié) :** la borne de moment qui manquerait pour fermer la conversion EST (TB).
En effet `Σ_ξ |S(ξ)|^{2k} = p²·E_k^{add}(p)` où `E_k^{add}=#{(j_1..j_k,j'_1..j'_k): Σ2^{j_i}≡Σ2^{j'_i} mod p²}`
= l'énergie additive d'ordre k de {2^j} = exactement la quantité que (TB) contrôle (E_k^tot en est le
moment factoriel). Donc :
- Bourgain–Chang Cor 4.5 donne le **L^∞** (sup-norme). 
- Fermer la conversion demande le **L^{2k}** (moment) de S = l'énergie E_k^{add} = **(TB) elle-même**.
⟹ **La voie sup-norme→moments est close par CIRCULARITÉ** : le chaînon manquant est logiquement
équivalent à la conjecture. Chercher « la bonne borne dans la littérature » ne peut PAS aider — la borne
requise EST (TB). (TB) est donc une vraie estimation ouverte, pas un énoncé en attente de référence.
De plus : la sup-norme n'allait JAMAIS fermer, car tout ε<1 donne B²=(L+1)^{2−2ε}>1 (même la √-cancellation
optimale ε=1/2 donne B²=L+1>1). Le gain réel est dans le moment L^{2k}, = l'énergie, = TB.

**Clarification mult. vs additif (dissout la confusion §5.4) :** le square sieve utilise les caractères
MULTIPLICATIFS χ de Z_{p²}^* ; `Σ_j χ(2^j)` est géométrique en j et vaut ~L pour χ quasi-trivial sur ⟨2⟩
(pas de cancellation — c'est la « taille L » du §5.4). BC borne les caractères ADDITIFS e_{p²}(ξ2^j),
où il n'y a PAS de quasi-trivial (le contre-ex 4.23 = θ=1+p vit dans 1+pℤ, exclu par la condition
d'ordre). Objets différents ; la porte multiplicative (square sieve) était la mauvaise. **Le contre-ex
4.23 prouve que la scission Type A/B est FORCÉE** : Type A = petit ordre mod p = additif sans cancellation
= voie García–Voloch ; Type B = grand ordre = BC. Pas une commodité, une nécessité structurelle.

### H.8 CHANTIER E′ — corps de fonctions : le pipeline bloque AUSSI (ε=1/2), MAIS (TB)-F_q[t] est prouvable par une AUTRE structure qui NE se transpose PAS.
**(a) Le pipeline de blocage vaut aussi sur F_q[t].** Weil donne la √-cancellation ε=1/2. Le blocage
H.3 tient dès que B²=(L+1)^{2−2ε}>1, i.e. ε<1 ; avec ε=1/2, B²=(L+1)>1. ⟹ **prédiction de Fable
confirmée : la conversion sup-norme→moments bloque IDENTIQUEMENT sur F_q[t]**. La circularité H.7 est donc
FONDAMENTALE (pas un artefact du petit ε sur ℤ) : même Weil ne ferme pas par la sup-norme.

**(b) MAIS (TB)-F_q[t] est prouvable — par une structure absente sur ℤ.** Sur F_q[t], {t^j} sont des
MONÔMES : Σt^{a_i}−Σt^{b_i} est un polynôme de degré ≤L, à coefficients entiers réduits mod q. Il est
≡0 mod P² (P irréductible, deg P² =2 deg P) **ssi** il est nul OU deg ≥ 2 deg P. Donc pour **deg P > L/2**,
seul le polynôme nul marche ⟹ **aucune collision non triviale ⟹ N_P Sidon exact ⟹ (TB) TRIVIAL**. Les
collisions n'existent que pour deg P ≤ L/2 (peu de P, |P|≤q^{L/2}), comptées par le DEGRÉ — pas
d'estimation de somme exponentielle requise. (TB)-F_q[t] est donc **prouvable-par-structure** (indépendance
linéaire des monômes + comptage de degré, pour q>2k), **PAS par Weil ni par sup-norme.**

**(c) Le mécanisme NE se transpose PAS en caractéristique 0.** Sur ℤ, 2^a+2^b−2^c−2^d peut être divisible
par p² tout en étant ≠0 : **aucune borne de « degré » n'empêche la divisibilité par un carré**. C'est
EXACTEMENT l'obstruction diviseurs-carrés qu'on a identifiée (STEP47-48). Le monde F_q[t] révèle donc que
la difficulté de (TB)-ℤ est l'**absence de borne de degré sur p²|N** — un obstacle sans analogue sur F_q[t].

**Issue (des trois demandées) : « prouvable-par-structure » sur F_q[t], mais l'inéquation décisive
(deg P>L/2 ⟹ pas de collision) N'A PAS D'ANALOGUE sur ℤ.** ⟹ le sandbox corps de fonctions ne fournit PAS
de méthode caractéristique-0 ; il PROUVE au contraire que (TB)-ℤ est structurellement plus dur (obstruction
diviseurs-carrés, catégorie Wieferich/square-sieve). C'est une clarification honnête, pas une percée :
(TB)-ℤ ne tombera pas par transposition de F_q[t].

### H.6 Verdict honnête
- Sup-norme BC (Cor 4.5) : **VRAIE et confirmée** (H.1, + conditions vérifiées par Fable, δ=1/5).
- Conversion sup-norme → moment factoriel : **BLOQUE** super-polynomialement à k~k* (H.3). Cor 4.5 seule
  insuffisante ; faut des bornes L⁴+/corrélation (H.4).
- Donc (TB) n'est PAS fermé par cette salve. Gain réel malgré tout : on sait EXACTEMENT où ça bloque
  (le terme toutes-fréquences-≠0, facteur B²>1 par fréquence) et ce qu'il faut chercher (moments de S,
  pas sup-norme). C'est un progrès de cadrage, pas une fermeture.

---
## CHANTIER F — mini-test digits (s₂ des pires n). TABLE BRUTE, sans verdict.

`R(n)=#{(l,m), l≤m : n−2^l−2^m>0 sans facteur carré}` ; pire n = min R(n) ; s₂(n)=poids binaire.
Script `chantierF_digits.py`.

| L | #n testés | minR | s₂ des ~10 pires n | s₂ moy 5% pires | s₂ moy global |
|---|---|---|---|---|---|
| 11 | 1024 | 44 | 4,2,6,4,4,6,4,4,5,6 | 5.49 | 7.00 |
| 12 | 2048 | 54 | 3,6,6,8,5,5,5,7,8,8 | 6.18 | 7.50 |
| 13 | 4096 | 60 | 2,8,4,4,4,8,4,5,6,6 | 6.72 | 8.00 |
| 14 | 8192 | 73 | 8,3,5,6,7,3,4,4,5,5 | 7.42 | 8.50 |
| 15 | 16384 | 82 | 4,2,8,4,4,6,6,8,9,5 | 7.79 | 9.00 |
| 16 | 32768 | 94 | 3,5,5,7,7,3,5,5,6,8 | 8.31 | 9.50 |
| 17 | 65536 | 102 | 8,4,7,2,6,7,8,8,10,4 | 8.91 | 10.00 |
| 18 | 131072 | 118 | 6,7,6,7,8,5,7,7,8,8 | 9.49 | 10.50 |
| 19 | 262144 | 131 | 2,4,5,10,4,8,8,9,4,5 | 9.96 | 11.00 |
| 20 | 524288 | 145 | 4,5,5,9,6,7,7,8,9,5 | 10.50 | 11.50 |

Observations brutes (pas de verdict) : (a) **minR croît (44→145), toujours ≫0** — aucun contre-exemple,
marge large à cette échelle. (b) s₂ moy des 5% pires est **systématiquement ~1 sous le global** (écart
constant ≈1.0–1.5, soit ~0.4–0.5 σ car σ(s₂)≈√(L/4)) — les pires n penchent vers un **poids binaire plus
faible**, mais l'effet est modéré, pas une dichotomie nette. La scission par s₂ (poids léger = forme
spéciale) a une justification faible côté « léger », pas de signal « poids lourd ». [Pour Fable.]

---
## CHANTIER J — mesure fine k=2 : #{p∈(L,L²]: p²|N}, N=1+2^β−2^γ−2^δ. TABLE BRUTE, sans verdict.
Script `chantierJ_k2.py`.

| L | #N distincts (p²\|N) | histogramme #{p:p²\|N} | quadruples doubles (≥2) | doubles structurés |
|---|---|---|---|---|
| 40 | 212 | {1:210, 2:2} | 2 | 2 (100%) |
| 60 | 480 | {1:468, 2:10, 3:2} | 12 | 12 (100%) |
| 80 | 813 | {1:778, 2:30, 3:5} | 35 | 35 (100%) |

- **Les quadruples à compte ≥2 sont TOUS structurés** (Mersenne-carrés et/ou facteur 2^m±1). Exemples :
  N=±(2^14−1)²=3²·43²·127² (p=[43,127]) ; N à p=[233,1103,2089] (triple). Aucun « sauvage » parmi les
  doubles/triples, à L=40,60,80. Confirme + étend STEP22 (ω₂(N)=2 ⟹ (2^k−1)²).
- Compte=1 : ~76–79% « structurés », ~21–24% « sauvages » — MAIS classifieur gonflé (petits facteurs
  2^m±1 : 3=2²−1, 5=2²+1, 7=2³−1 attrapent ~beaucoup de N par hasard). Signal réel = **les doubles/triples
  (gros facteurs Mersenne), 100% structurés** ⟹ cible de classification élémentaire pour la partie k≥2 de
  (M″) sur k=2 : « un même p² divise deux quadruples ⟹ N a un gros facteur 2^m±1 (Mersenne-carré) ». [Pour Fable.]

### CHANTIER K (optionnel, Fable) — classification Mersenne : TENTÉE, PAS prouvée. Non écrite au papier.
**Cible :** si N=1+2^β−2^γ−2^δ (en range, ≠0) a deux facteurs premiers-carrés distincts p²,q² (p,q>L),
alors N provient de (2^k−1)². Empiriquement 100% (Chantier J, STEP22).
**Départ 2-adique :** N impair (1+pair−pair−pair selon parités ; normaliser). p²q²|N avec N<2^{L+1}
⟹ (pq)²≤2^{L+1} ⟹ pq≤2^{(L+1)/2}. La famille (2^k−1)² fournit p²|N pour tout p|2^k−1 quand N est un carré
parfait ; c'est la source « évidente » (2^k−1 a beaucoup de facteurs). **La direction DURE = la réciproque
(seulement ceux-là).** 
**Pourquoi c'est dur (honnête) :** c'est un énoncé sur les facteurs carrés de combinaisons binaires à 4
termes — territoire Pillai / abc (les entiers squarefull dans une suite lacunaire). Pas de preuve 2-adique
courte visible ; les cas « sauvages » à compte=1 montrent que la structure n'est PAS forcée dès un seul p².
Il faudrait exploiter que DEUX carrés distincts co-divisent, ce qui sur-contraint — mais je n'ai pas
d'argument complet. **STATUT : sous-cible élémentaire ouverte, consignée, PAS prouvée, PAS écrite au papier**
(règle « seulement si preuve complète »). Reste comme cible de classification pour k=2 si quelqu'un la finit.
