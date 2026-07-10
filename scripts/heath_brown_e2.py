# STEP35 — Crible du carré sur E_2 : le gain vient-il de l'averaging sur p (pas per-prime) ?
import numpy as np
from collections import Counter
from sympy import primerange, n_order
import math

print("### ÉTAPE 2a : E_2^tot ~ L³/logL ? (scaling vers constante)")
print(f"{'L':>4}{'#p':>6}{'E2^tot':>9}{'L³/logL':>10}{'E2·logL/L³':>12}")
def E2_all(L):
    tot=0; nP=0
    for p in primerange(L+1,L*L+1):
        p2=p*p; c=Counter(((1<<a)+(1<<b))%p2 for a in range(L+1) for b in range(a,L+1))
        tot+=sum(v*(v-1)//2 for v in c.values()); nP+=1
    return tot,nP
for L in (30,40,50,60,70):
    tot,nP=E2_all(L)
    print(f"{L:>4}{nP:>6}{tot:>9}{L**3/math.log(L):>10.0f}{tot*math.log(L)/L**3:>12.3f}")

print("\n### ÉTAPE 2b : Δ_p / aléatoire(P²/2p²) par premier — ~1 en moyenne ? distribution")
print("  (si Δ_p ~ P²/2p² pour la plupart ⟹ Σ_p Δ_p = O(Σ P²/2p²) = O(L³/logL). Gain = averaging.)")
L=60; P=(L+1)*(L+2)//2
ratios=[]
for p in primerange(L+1,L*L+1):
    p2=p*p; c=Counter(((1<<a)+(1<<b))%p2 for a in range(L+1) for b in range(a,L+1))
    D=sum(v*(v-1)//2 for v in c.values())
    rnd=P*P/(2*p2)
    if rnd>0.01: ratios.append(D/rnd)
ratios=np.array(ratios)
print(f"  L={L}: Δ_p/aléatoire — moy={ratios.mean():.2f} médiane={np.median(ratios):.2f} "
      f"max={ratios.max():.1f} %(>2)={100*(ratios>2).mean():.0f}%")
print(f"  ⟹ Σ_p Δ_p / Σ_p aléatoire = {ratios.mean():.2f} (borné ⟹ averaging donne le bon ordre).")

print("\n### ÉTAPE 4 : sommes de caractères Σ_{j≤L} χ(2^j) — O(1), O(√p), ou O(L) ? (piège 1)")
print(f"  {'p':>6}{'ord_p(2)':>9}{'#{χ:χ(2)=1}':>11}{'max|Σχ(2^j)|':>13}{'/√p':>7}{'/L':>6}{'#{|Σ|>√p}':>10}")
for p in [211, 409, 809, 1279]:
    for L in [80]:
        if not (L<p<=L*L): continue
        e=n_order(2,p)
        # ind(2): trouver g racine primitive, ind = log_g(2). On calcule directement χ_k(2)=g_root^k...
        # plus simple : χ(2)=e(k*ind2/(p-1)). On énumère les valeurs χ(2)=zeta^k, k=0..p-2, zeta=e(1/(p-1)).
        # Σ_j χ(2^j) = Σ_j χ(2)^j. χ(2) parcourt les racines (p-1)/e ... en fait {χ(2):χ} = groupe des
        # racines d'ordre e (car χ(2) a ordre divisant e). On énumère w=e(m/e), m=0..e-1 (chaque atteint (p-1)/e fois).
        maxS=0; ntriv=0; nbig=0
        for m in range(e):
            w=np.exp(2j*np.pi*m/e)
            S=abs(sum(w**j for j in range(L+1)))
            if m==0: ntriv=(p-1)//e; continue
            maxS=max(maxS,S)
            if S>math.sqrt(p): nbig+=1
        print(f"  {p:>6}{e:>9}{(p-1)//e:>11}{maxS:>13.1f}{maxS/math.sqrt(p):>7.2f}{maxS/L:>6.2f}{nbig*((p-1)//e):>10}")
print("  (χ(2) a ordre | e_p ; on somme sur m=0..e-1. max|Σ| = ? Si ~L : piège 1 confirmé.)")

print("\n### verdict scaling : E_2^tot·logL/L³ converge ? Δ_p averaging borné ? char sums ?")
