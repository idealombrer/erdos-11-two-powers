# STEP52 — Chantier D (Fable) : borne de Stepanov VÉRIFIÉE avant écriture (le check a attrapé une subtilité). Dernière passe papier consolidée.

**Date :** 2026-07-05. Script `chantierD_stepanov.py`. Fable a fait les recherches biblio pour #3/Stepanov
et proposé d'écrire une proposition κ_p≪e_p^{2/3}. **Règle appliquée (celle qui a sauvé Chantier A) : vérifier
numériquement AVANT d'écrire. Le check a attrapé une subtilité réelle.**

## Vérification de la borne HB-K : max_n r_p(n) ≤ 4 e_p^{2/3} ?

r_p(n)=#{(u,v)∈G²:u+v≡n mod p}, G=⟨2⟩ mod p, |G|=e_p. Filtre e_p≤p^{2/3} (condition du théorème).

- **AVEC n=0 inclus : FAUX.** 66 violations/152, ratio DÉRIVE vers le haut (2.5→4→6→9.06 à e_p=744).
  Cause : cas dégénéré n=0 (2^l+2^m≡0 ⟺ −1∈⟨2⟩) donne r_p(0)=|G∩−G|=e_p ⟹ ratio e_p^{1/3}→∞.
- **AVEC n≠0 (non-dégénéré) : VRAI.** ratio ≤ ~0.97 (max bucket [400,409]), AUCUNE violation de 4,
  pas de dérive jusqu'à e_p=889. Donc HB-K correcte pour n≢0.

**⟹ La lecture de Fable est correcte MODULO l'exclusion du dégénéré n=0.** Écrire la borne « pour tout n »
aurait été un faux théorème (ratio→∞). Le check l'a évité — 2ᵉ fois que « vérifier avant d'écrire » sauve.

## Transfert à notre problème (le dégénéré est hors-portée pour Type A)

Le dégénéré mod p² (2^l+2^m≡0 mod p²) exige 2^{m−l}≡−1 mod p², i.e. m−l≍ord_{p²}(2)/2. Pour Type A
(e_p≤L mais ord_{p²}(2)=p·e_p≫L), m−l≍p e_p/2 ≫ L : **INATTEIGNABLE dans [0,L]**. Donc le résidu
dégénéré ne se produit pas dans notre plage Type A ⟹ la borne non-dégénérée s'applique à κ_p.

## Écrit au papier (passe UNIQUE et CONSOLIDÉE, puis stop)

1. **§7 refined picture** : nouvelle borne « cinquième toolkit » Stepanov/HB-K : r_p(n)≤4e_p^{2/3} (n≢0,
   condition e_p≤p^{2/3}, vérif numérique ratio<1 à e_p~900, caveat dégénéré hors-portée Type A) ⟹
   κ_p≪e_p^{2/3} (vs trivial κ_p≤e_p) ⟹ **Σ_Type A M_p=O(L^{8/3}/logL)** — réel mais court de o(L²) d'un
   facteur L^{2/3}. Marges non exploitées (max_n pire-cas ; rigidité involution) ⟹ question ouverte :
   descendre l'exposant 2/3→o(1) sur les fibres 1+2^δ. Conditions exactes = source primaire (HB-K ;
   Konyagin–Shparlinski, monographie), cité en texte (non vérifié en source).
2. **§7 « four toolkits »** → « four ENERGY-scale toolkits » + reconnaissance de la 5ᵉ famille (max-scale,
   mord sur Type A, court d'un facteur L).
3. **§7 consolidation (thèse verrou unique)** : Var[C]=Σ_p Σ_r c_r⁴/p² = E_4^tot ; troncature → Σ(c_r choose K)=E_K^tot.
   Donc Chebyshev (gain num. L² vers O(1/(L³logL)), Var/C̄≈2.1–2.9) et tout raffinement de moments sont
   conditionnels au MÊME crible du carré que (M″). Un seul verrou : la distribution de multiplicité de
   {2^l+2^m mod p²}.

Papier : 18pp, compile. **PLUS DE MODIF PAPIER jusqu'au signal de l'user.**

## Bilan salve Fable (complet)

- Corrections rigueur (Lemme K, pont CRT) : faites.
- Amélioration gratuite mur-B (Markov ηL²) : O(1/logL)→O(1/(L logL)) INCONDITIONNEL.
- Lead #1 larger sieve : MORT (Chantier B, objet correct, sum-product sature Z/q).
- Lead #4 réduction p-adique : PARTIELLE (STEP50).
- Chantier A moments : CONDITIONNEL (M_max=o(L)/4ᵉ moment), pas inconditionnel. Fable a concédé.
- Chantier D Stepanov : borne VÉRIFIÉE (n≠0), écrite avec caveats ⟹ κ_p≪e_p^{2/3}, Σ_TypeA M_p=O(L^{8/3}/logL),
  court de L^{2/3}. **1er vrai gain inconditionnel sur (TA)** (empirique → borne).
- Restent : #5 corps de fonctions (build, prochaine inflexion), #6 digits (mini-test s₂(n)), #3 conditions
  exactes HB-K (lecture source = Fable).

Règle gravée : **aucun théorème au papier sans sa preuve écrite / vérif numérique** (a sauvé 2× : Chantier A
et Chantier D-dégénéré). Voir [[project_erdos11_fable_leads]], [[project_erdos11_twopow_status]].

---
*Chantier D : HB-K r_p(n)≤4e_p^{2/3} FAUX pour n=0 (dégénéré, ratio→9), VRAI n≠0 (ratio<1 à e_p~900).
Dégénéré hors-portée Type A. Écrit au papier avec caveats : κ_p≪e_p^{2/3} ⟹ Σ_TypeA M_p=O(L^{8/3}/logL),
court L^{2/3}. + 5ᵉ toolkit + consolidation E_k^tot (verrou unique). Papier 18pp. STOP modif papier.*
