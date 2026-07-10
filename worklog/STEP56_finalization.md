# STEP56 — Passe de finalisation pré-circulation (checklist Fable). Papier 22pp, self-contained, prêt à relire.

**Date :** 2026-07-05. Commits f69ae3c (rédaction), 3bb96b6 (Lean 5ᵉ lemme), 02955ff (finalisation).

## Items faits (1–6)
1. **§1.2 Contributions réécrite** : « This is new » retiré de Lemme K (aligné §3/abstract) ; ajout des
   contributions distinctives — García–Voloch (Type A), Bourgain–Chang+circularité (Type B), modèle
   corps de fonctions (§8), vérification Lean (5 lemmes).
2. **Dépendance Kalinin RETIRÉE du résultat inconditionnel.** Au lieu de reprouver sa borne sharp ≤2
   (fragile, règle « ne pas écrire ce qu'on ne peut vérifier »), **Prop sqrange** : premier moment trivial
   ⟹ densité O((L+1)²·2^{−L/2})→0 pour la gamme (√(n/2),√n]. **Cor almostall n'utilise plus AUCUN input
   externe** (vraiment self-contained). Kalinin gardé pour l'every-n pire-cas (déjà conditionnel).
3. **Table §7.4** : split Type A (O(L^{8/3}/logL) García–Voloch) / Type B (clos par circularité) ;
   ligne a.a.-n self-contained.
4. **Réf García–Voloch** : source secondaire vérifiée (Konyagin notes Thm 2.1 / Konyagin–Shparlinski CUP)
   comme origine de la formulation exacte ; García–Voloch primaire ; prop:gv cite les deux.
5. **Uniformisation** : titre §7 anglais ; abstract lissé ; injection κ_p→reps mod p clarifiée (réduction
   des fibres, pas involution).
6. **Paquet arXiv** : README.md (build + table 5 lemmes Lean + map claim-numérique→script + note
   méthodo) ; LICENSE (MIT code / CC-BY papier) ; section Acknowledgements (méthodo IA exécuteur/validateur,
   règle no-theorem-without-proof). PAPER.tex autonome (bib inline). Compile 22pp, 0 réf/citation non définie.

## Item 7 (optionnel) — classification Mersenne : TENTÉE, PAS prouvée, PAS écrite
Cible : p²q²|N=1+2^β−2^γ−2^δ ⟹ N de (2^k−1)². Empiriquement 100% (Chantier J). Départ 2-adique consigné
(consolidation_notes §K) mais **direction dure (réciproque) non prouvée** — territoire Pillai/abc (squarefull
dans suite lacunaire). Reste sous-cible ouverte, non écrite au papier (règle respectée).

## État final du papier
- **Inconditionnel, self-contained** : almost-all-n (densité 1−O(1/(L logL)), aucun input externe).
- **(TA)** : borne García–Voloch O(L^{8/3}/logL), à L^{2/3} de o(L²) ; ouvert = pousser 2/3→o(1).
- **(TB)** : clos par circularité (le moment L^{2k} manquant = l'énergie = (TB)) ; diagnostic archimédien
  via corps de fonctions ; = vraie estimation ouverte square-sieve, cousin de #11.
- **(B)** : moyenne réglée, pire-cas calibre #11.
- **Lean** : 5 lemmes, 0 sorry.

Prochaine étape : relecture finale par Fable, puis circulation (mail Bloom, wiki, arXiv math.NT). Éventuel
nouveau problème = salve de triage (critères : verrou constructif, vérifiabilité machine, pas d'entrée wiki
récente). Voir [[project_erdos11_twopow_status]], [[project_erdos11_fable_leads]], [[feedback_verify_before_writing]].

---
*Finalisation faite : §1.2 réécrite, Kalinin retiré de l'inconditionnel (Prop sqrange, 1er moment),
table+réfs+langue+acks, README+LICENSE. 22pp self-contained, 5 lemmes Lean. Classification Mersenne tentée
non prouvée (non écrite). Prêt à circuler après relecture Fable.*
