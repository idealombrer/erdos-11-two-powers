# STEP49 — Lead Fable n°1 (larger sieve de Gallagher) : MORT, par manque de concentration (≠ STEP44).

**Date :** 2026-07-04. Script `larger_sieve_test.py`. Test décisif du lead le plus prometteur de Fable
(« k=2 de (TB) via le larger sieve, peut-être prouvable inconditionnellement »). **Résultat : le larger
sieve ne mord PAS. Les premiers non-Sidon dans (L,L²] sont ÉQUIDISTRIBUÉS mod petits q (ν(q)=q−1), donc
aucune concentration à exploiter. Échec par manque de concentration — mécanisme DIFFÉRENT de STEP44
(là c'était le range exponentiel ; ici range polynomial mais pas de concentration).**

## Données (L=100, 140)

- **B2 = {p∈(L,L²]: M_p≥2}** (non-Sidon) : |B2|=167 (L=100), 276 (L=140). Déjà ≤ π(N) trivialement.
  **ν_B2(q)/(q−1) = 1.00 pour tout q=3..47** — équidistribution parfaite. Borne de Gallagher : dénom≤0
  jusqu'à Q~1000 ; ne passe sous π(N) qu'à Q≈N, et donne alors 181 (>|B2|=167) — inutile, et requiert
  ν(q) empirique pour tout q≤N (circulaire, pas un théorème).
- **B3 = {M_p≥3}** : |B3|=32 (L=100), 53 (L=140). ν_B3(q)/(q−1) descend à 0.50 (q=47) — **ARTEFACT de
  petit échantillon** : |B3|=32<q=47 ⟹ baseline aléatoire = 46(1−e^{−32/46})≈23 = exactement observé.
  Aucune concentration réelle. (Leçon STEP42 : le signal « p mod 16 » était déjà un artefact de moyenne ;
  vérifié avant de m'y faire prendre.)

## Pourquoi c'est structurel

La condition « p²|N pour un quadruplet N=1+2^β−2^γ−2^δ » est une condition mod p², **indépendante de
p mod q** pour q petit. Donc les premiers anomaux sont génériques mod q (équidistribués) — forcé, pas
coïncidence. Le larger sieve, dont TOUTE la force est d'exploiter la concentration (ν(q)≪q), n'a aucune
prise. Contraste avec STEP44 (grand crible générique) : là l'échec était le range exponentiel N=2^L ;
ici les premiers sont en range polynomial (L,L²] — **pas de mur exponentiel — mais pas de concentration**.
Deux modes d'échec distincts ; les deux cribles écartés pour des raisons différentes et précises.

## Statut des leads Fable après STEP49

- **n°1 larger sieve : MORT** (équidistribution, ce STEP). Rejoint la liste des cribles écartés-avec-raison.
- n°2 Stepanov : Fable concède déjà exposants insuffisants (|H|^{2/3} ⟹ L^{8/3}/logL).
- n°3 Cilleruelo–Garaev, n°4 réduction p-adique/Fermat, n°5 corps de fonctions, n°6 digits : non testés.
- Amélioration gratuite (Markov ηL² sur mur B) + moments CRT : non faite, correcte, à écrire.

**Prochaine cible :** soit l'amélioration gratuite (sûre, renforce le théorème inconditionnel), soit
lead n°4 (réduction p-adique de (TB) via quotients de Fermat — le plan le plus structuré, recycle Lemme K),
soit n°5 (sandbox corps de fonctions). Voir [[project_erdos11_fable_leads]].

---
*larger_sieve_test.py. Larger sieve de Gallagher sur non-Sidon primes = INUTILE : équidistribués mod q
(ν(q)=q−1), aucune concentration. Échec ≠ STEP44 : range polynomial (pas exponentiel) mais pas de
concentration. Artefact B3 = petit échantillon (leçon STEP42). Lead n°1 mort. PAPER/Lean non touchés.*
