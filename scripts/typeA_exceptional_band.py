# CHANTIER G (Fable) — la bande exceptionnelle García–Voloph existe-t-elle vraiment dans les données ?
# GV: N2(b)<=4|G|^{2/3} pour b≠0 SI |G| < (p-1)/((p-1)^{1/4}+1) ≈ p^{3/4}. Pour Type A (e_p<=L), échoue
# seulement si e_p > p^{3/4}, i.e. p < e_p^{4/3} <= L^{4/3}. Bande p∈(L,L^{4/3}). Contribution triviale
# M_p<=L+1 => O(L^{7/3}/logL), absorbée par O(L^{8/3}/logL) ? Vérif + comptage réel.
from sympy import primerange
import math

def ord2(p):
    x=1
    for k in range(1,p):
        x=(2*x)%p
        if x==1: return k
    return p-1

print("### CHANTIER G — combien de premiers Type A violent la condition de taille GV (e_p > p^{3/4}) ?")
print("### Bande théorique p∈(L,L^{4/3}). Contribution triviale (L+1)·#band vs terme principal L^{8/3}/logL.\n")
print(f"  {'L':>4} {'#TypeA(e_p<=L)':>15} {'#viol(e_p>GVthr)':>17} {'max p viol':>11} {'L^{4/3}':>9} "
      f"{'contrib band':>13} {'main L^{8/3}/logL':>17} {'absorbé?':>9}")
for L in (60,100,140,200,300):
    nTA=0; nviol=0; maxpv=0;
    for p in primerange(L+1, L*L+1):
        e=ord2(p)
        if e>L: continue           # Type B, skip
        nTA+=1
        thr = (p-1)/((p-1)**0.25 + 1)   # condition GV: |G| < thr
        if e >= thr:
            nviol+=1; maxpv=max(maxpv,p)
    band_contrib = nviol*(L+1)                 # M_p<=L+1 sur la bande
    main = L**(8/3)/math.log(L)
    L43 = L**(4/3)
    ok = "OUI" if band_contrib < main else "NON — à revoir"
    print(f"  {L:>4} {nTA:>15} {nviol:>17} {maxpv:>11} {L43:>9.0f} {band_contrib:>13} {main:>17.0f} {ok:>9}")
print("\n[Si #viol petit et max p viol < L^{4/3} et contrib band << main : la proposition tient, bande")
print(" traitée trivialement. Si #viol=0 : encore mieux, condition GV jamais violée sur Type A réel.]")
