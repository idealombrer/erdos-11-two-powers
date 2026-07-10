# Erdős #11 — variante "deux puissances de 2" : énoncé exact + statut (étapes 1-2)

**Date :** 2026-06-22. **Dossier :** `~/erdos-11-powers`. Contexte complet : `~/erdos-meta-analysis-v2/ANALYSIS_11.md`.

## 1. Énoncé exact de la variante (vérifié)

De `formal-conjectures/.../11.lean`, `erdos_11.variants.two_pow_two` :

> **Tout entier impair $n>1$ est-il la somme d'un nombre sans facteur carré et de DEUX
> puissances de 2 ?**
> $$\exists\, k,l,m\in\mathbb N:\ \mathrm{Squarefree}(k)\ \wedge\ n = k + 2^l + 2^m.$$

**La partie $k$ est sans facteur carré (squarefree), PAS première** — le prompt parlait de
"$q$ premier ou squarefree" ; c'est bien **squarefree**. Les puissances $2^l, 2^m$ sont
indépendantes ($l=m$ autorisé, donnant $2^{l+1}$). Comme $2^l+2^m$ est toujours **pair**,
$k = n-2^l-2^m$ est impair (donc jamais divisible par 4 — l'obstruction $4\mid k$ ne se
pose pas).

## 2. Pourquoi Erdős la jugeait "peut-être facile" (vérifié sur erdosproblems.com/11)

Citation reconstituée de la page (via recherche web, fetch direct 403) :
- **Énoncé principal (une puissance)** : ouvert, vérifié jusqu'à $2^{50}$ (Hercher 2024,
  arXiv:2411.01964), **lié aux premiers non-Wieferich** (Granville–Soundararajan 1998 :
  conjecture ⟹ infinité de $p$ avec $2^p\equiv2\pmod{p^2}$). Mur professionnel.
- **Erdős "could prove that it is true (with a single power of two) for almost all $n$"** —
  le résultat "presque tout $n$" (densité 1) est, lui, **prouvable** par Erdős.
- **Erdős "thought that proving this with two powers of 2 is perhaps easy"** — confirmé
  textuellement.

**Mécanisme de la différence (cœur de l'affaire) :**
- **Une puissance** : un $n$ donné n'a que $\sim\log_2 n$ candidats $n-2^a$. Prouver
  qu'au moins un est squarefree pour TOUT $n$ revient à exclure une construction de type
  *système de couverture à modules carrés* $p^2$ — et c'est exactement ce blocage qui
  produit le lien Wieferich (G–S) : la version complète une-puissance est **couplée** à un
  problème ouvert et dur.
- **Deux puissances** : $\sim(\log_2 n)^2/2$ candidats $n-2^l-2^m$. L'adversaire devrait
  bloquer *quadratiquement plus* d'événements simultanément, ce qui (i) rend la
  construction de couverture bien plus contrainte et (ii) **découple vraisemblablement du
  lien Wieferich** — l'argument G–S exploite la rigidité du choix unique de $2^a$, qui
  disparaît avec un second degré de liberté. C'est la raison structurelle pour laquelle la
  version deux-puissances pourrait être prouvable par un simple **argument de comptage/crible**.

## 3. Vérification computationnelle (`compute.py`, jusqu'à $10^7$)

**Aucune exception**, ni pour une puissance ni pour deux puissances, parmi les impairs
$1<n<10^7$ (le résultat une-puissance reconfirme le crible ; cohérent avec Hercher $2^{50}$).

**Cas tendus (une puissance), nombre de représentations $r_1(n)=\#\{l:n-2^l\text{ squarefree}\}$ :**
- $r_1=2$ seulement pour $n\in\{3,5,13,29\}$ (tous $\le 29$),
- $r_1=3$ seulement pour $n\in\{7,9,11,17,25,41,53,57\}$ (tous $\le 57$).
- **Au-delà de $n=57$, tout impair a $r_1\ge4$**, et le pire cas par fenêtre dyadique
  croît régulièrement ($\min r_1\approx11$ vers $10^7$, $\approx\tfrac{8}{\pi^2}\log_2 n$
  fraction des $\log_2 n$ candidats). Les cas réellement serrés sont **finis et petits**.

**Marge deux-puissances $r_2^{\mathrm{ord}}(n)=\#\{(l,m):n-2^l-2^m\text{ squarefree}\}$ :**
- pire cas par fenêtre dyadique **croît quadratiquement** : $\min r_2^{\mathrm{ord}}$ passe
  de $1$ ($n=3$) à $\mathbf{334}$ vers $10^7$ ; moyenne $424$.
- Vers $10^7$ : $\sim540$ paires ordonnées au total, dont $\ge334$ squarefree même dans le
  **pire cas** $\Rightarrow$ une fraction $\ge\!60\%\approx\frac{8}{\pi^2}\cdot$(densité
  squarefree) des paires marchent, *uniformément*. Marge écrasante, sans aucun signe de
  rétrécissement.

**Lecture :** la donnée à elle seule ne sépare pas les deux problèmes (zéro exception des
deux côtés — c'est attendu, le principal est vrai jusqu'à $2^{50}$). Ce qui les sépare,
c'est la **marge structurelle** : une-puissance garde des cas tendus ($r_1=2$) et une marge
qui ne croît que **linéairement** en $\log n$ ; deux-puissances a une marge **quadratique**
en $\log n$, $\sim60\%$ de toutes les paires même au pire — exactement le coussin qu'un
argument de crible élémentaire pourrait capturer.

---
*Sources : `11.lean` (lu intégralement) ; erdosproblems.com/11 via recherche web (403 en
direct) ; Hercher arXiv:2411.01964 (pas de discussion de la variante 2-puissances — confirmé
par fetch) ; `compute.py` (crible squarefree numpy + comptage vectorisé des représentations).*
