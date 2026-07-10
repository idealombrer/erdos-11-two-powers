# STEP36 — Théorème conditionnel (every-n) + mise à jour PAPER.tex

**Date :** 2026-07-03. Assemblage de STEP19-35 en un théorème conditionnel propre + additions ciblées
au papier. **Politique d'honnêteté conservée : tout ce qui est conditionnel/ouvert est explicitement
signalé.**

## Le théorème conditionnel (nouveau résultat principal, every-n)

Notations : n impair, L=⌊log₂n⌋, P=(L+1)(L+2)/2, N_p(n)=#{(l,m)∈[0,L]²:2^l+2^m≡n mod p²},
M_p=max_n N_p(n), e_p=ord_p(2). Découpage de (L,L²] : **Type A** = {e_p≤L}, **Type B** = {e_p>L}.

**THÉORÈME (conditionnel, every-n).** Supposons :
- **(TB)** [analytique, grand crible] il existe C absolu tel que, pour tout L grand et tout
  k ≤ k* := ⌊3 log L/log log L⌋,
  $$E_k^{tot} := \sum_{\substack{p\in(L,L^2]\\ e_p>L}}\sum_r \binom{N_p(r)}{k}
    \ \le\ C^k\, E_k^{null},\qquad E_k^{null}:=\sum_{\substack{p\in(L,L^2]\\ e_p>L}}\frac{\binom{P}{k}}{(p^2)^{k-1}};$$
- **(TA)** [rigidité] il existe κ absolu tel que, pour tout premier non-Wieferich p∈(L,L²] avec
  e_p≤L, toute fibre maximale est portée par au plus κ classes de résidus δ mod e_p ;
- **(WB)** [gamme large, worst-case] Σ_{p∈(L²,√(n/2)]} N_p(n) = o(L²) uniformément en n.

Alors tout entier impair n>1 (n≥n₀) s'écrit n = m + 2^l + 2^m avec m sans facteur carré.

**Statut des hypothèses :** (TB) empiriquement vraie (ratios E_k^tot/E_k^null ∈ [0.34,0.96],
k=2,3,4, L=40-160), = borne de grand crible / crible du carré de Heath-Brown, terme d'erreur =
moyenne quadratique des sommes de caractères (régime BG incomplet, STEP35). (TA) empiriquement vraie
avec κ=2 (orbites d'involution, STEP30). (WB) vraie *en moyenne* (Thm Bavg, densité O(1/log L)),
worst-case ouvert (déjà dans le papier §7.3).

## Parties INCONDITIONNELLES (preuves)

### (U1) Somme d'ordres : Σ_{p∈(L,L²]} ⌊L/e_p⌋ = O(L²/log L) = o(L²). [NOUVEAU, élémentaire]
Preuve : ⌊L/d⌋ = #{j∈[1,L]:d|j}, et e_p|j ⟺ p|2^j−1. Donc
Σ_p⌊L/e_p⌋ = Σ_{j≤L} #{p∈(L,L²]:p|2^j−1}. Les premiers p>L divisant 2^j−1 ont un produit ≤2^j−1<2^j,
donc si m d'entre eux, L^m<2^j, m<j log2/log L. Ainsi Σ_{j≤L} j log2/log L = (log2/log L)L(L+1)/2
= O(L²/log L). ∎ (Corrige le Θ(L²) naïf : le facteur log L vient de p>L.)

### (U2) Identité d'involution. [NOUVEAU] Pour tout δ : 1+2^{e_p−δ} ≡ 2^{−δ}(1+2^δ) mod p.
Preuve : 2^{−δ}(1+2^δ) = 2^{−δ}+1 = 2^{e_p−δ}+1 (car 2^{e_p}≡1). ∎ ⟹ δ et e_p−δ dans la même
classe de ⟨2⟩ mod p ⟹ les fibres se décomposent en progressions arithmétiques de pas e_p.

### (U3) Borne per-classe. [semi-élémentaire, non-Wieferich p>L]
Pour p non-Wieferich >L, d_p=p·e_p>L ⟹ pour chaque l≤L, ≤1 solution m∈[0,L] de 2^m≡n−2^l mod p².
En groupant les reps d'une fibre par (l mod e_p, δ=|l−m| mod e_p), chaque classe forme une
progression arithmétique de raison multiple de e_p, tronquée par la boîte {l,m≤L} à ≤⌊L/e_p⌋+1
termes. D'où **M_p ≤ κ_p·(⌊L/e_p⌋+1)**, κ_p = nb de classes actives. (Empirique : κ_p≤2, involution.)

### (U4) Markov factoriel. [élémentaire]
#{p:M_p≥k} ≤ Σ_p #{r:N_p(r)≥k} ≤ Σ_p Σ_r C(N_p(r),k) = E_k^tot (chaque r à N_p(r)≥k contribue
C(N_p(r),k)≥1). Donc maxM_B = max{k:E_k^tot≥1}, sans aucune indépendance.

### (U5) Seuil du null. [élémentaire]
E_k^null ~ (P^k/k!)·Σ_{p>L}p^{−(2k−2)} ~ L³/(2^k k!(2k−3)log L), qui croise 1 à k*~3log L/loglog L.
Sous (TB), E_{k}^tot ≤ C^k E_k^null < 1 pour k un peu au-delà de k* ⟹ maxM_B = O(log L/loglog L).

## Assemblage (preuve du théorème)

Par Prop★ (borne d'union), il suffit de Σ_{3≤p≤√n} N_p(n) < T=(L+1)². Découpage :
1. **p≤L+1** : Lemme K + R1 ⟹ (0.3205+o(1))T. [inconditionnel, déjà dans le papier]
2. **(L,L²] Type A** (e_p≤L) : par (U3) M_p≤κ_p(⌊L/e_p⌋+1) et (TA) κ_p≤κ, donc Σ_A M_p ≤
   κ(Σ⌊L/e_p⌋ + #A) = κ·o(L²) = o(L²) par (U1) et #A≤π(L²)=o(L²). [conditionnel à (TA)]
3. **(L,L²] Type B** (e_p>L) : Σ_B(M_p−1) = Σ_{k≥2}#{B:M_p≥k} ≤ Σ_{k≥2}min(E_k^tot,π(L²)). Sous
   (TB) et (U4,U5) : ≤ k*·π(L²) + Σ_{k>k*}C^k E_k^null = O(L²/loglog L) + o(1) = o(L²). Par Lemme M,
   ce range contribue ≤ Σ_{(L,L²]}M_p = o(L²) à tout n. [conditionnel à (TB)]
4. **(L²,√(n/2)]** : Σ N_p(n) = o(L²) par (WB). [conditionnel à (WB) ; inconditionnel en moyenne]
5. **(√(n/2),√n]** : O(L) par Kalinin. [inconditionnel]
Somme : (0.3205+o(1))T + o(L²)·4 < T pour n grand. Prop★ conclut. ∎

## COROLLAIRE INCONDITIONNEL (déjà dans le papier, réaffirmé)
La densité des n impairs non représentables est O(1/log L) → 0 (almost-all-n, inconditionnel,
Cor. cor:almostall). Les hypothèses (TA),(TB),(WB) ne sont requises que pour le passage à *tout* n.

## Modifications apportées à PAPER.tex (additions ciblées, pas de réécriture)

1. §5 (Lemma M) : nouvelle Prop. (U1) « order sum unconditionally o(L²) » après prop:sidonterm.
2. §5 : nouvelle sous-section « Classification Type A/Type B ; involution ; per-class bound »
   (U2, U3, définition κ_p, Type A conditionnel à κ_p=O(1)).
3. §5 : nouvelle sous-section « The Type B residual as a factorial-moment (grand-sieve) condition »
   (U4, U5, E_k^tot/E_k^null, le THÉORÈME conditionnel, réduction Heath-Brown, obstruction STEP35).
4. §6/§7 : table empirique des ratios E_k^tot/E_k^null (k=2,3,4 ; L=80,120,160).
5. §7.2 : mise à jour de la discussion (M″) — cross-ref au raffinement Type A/B + E_k (garder
   « where brute force fails » ; ajouter que (M″) se scinde et que le Type B = grand crible).
6. Références : Heath-Brown (1984, square sieve) ; Rudin (1960, Λ(p) sets).
7. Abstract/intro/conclusion : ajouts minimaux (almost-all PROUVÉ/complet ; every-n réduit à
   grand crible + rigidité + wall B ; théorème conditionnel = nouveau).

Tout marqué PROUVÉ / CONDITIONNEL / OUVERT. PAPER compile avec tectonic.
