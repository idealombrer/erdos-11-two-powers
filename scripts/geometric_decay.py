# STEP47 — Le verrou EM=O(1) se reformule-t-il en décroissance géométrique de #{M_p>=k} ?
# Si #{M_p>=k+1}/#{M_p>=k} <= rho < 1 stable => EM <= 1/(1-rho) = O(1) => M"_B = o(L^2) => every-n.
from collections import Counter
from sympy import primerange
import math

def counts_Mge(L, kmax=8):
    """#{Type B primes : M_p >= k} pour k=2..kmax, + M''_B = sum(M_p-1)."""
    Nk=[0]*(kmax+1)  # Nk[k] = #{M_p>=k}
    Mpp=0            # sum (M_p - 1)
    nTB=0
    for p in primerange(L+1, L*L+1):
        x=1; tA=False
        for k in range(1,L+1):
            x=(x<<1)%p
            if x==1: tA=True; break
        if tA: continue
        nTB+=1; p2=p*p; pw=[1]*(L+1)
        for k in range(1,L+1): pw[k]=(pw[k-1]<<1)%p2
        c=Counter()
        for a in range(L+1):
            pa=pw[a]
            for b in range(a,L+1): c[(pa+pw[b])%p2]+=1
        Mp=max(c.values())
        Mpp += Mp-1
        for k in range(2,kmax+1):
            if Mp>=k: Nk[k]+=1
    return Nk, Mpp, nTB

print("### Décroissance géométrique de #{M_p>=k} (Type B) ⟹ EM=O(1) ⟹ M\"_B=o(L²) ?")
for L in (60,100,140,180):
    Nk,Mpp,nTB = counts_Mge(L)
    P=(L+1)*(L+2)//2
    EM = Mpp/Nk[2] if Nk[2] else 0
    print(f"\n--- L={L}  (#TypeB={nTB}, M\"_B={Mpp}, #{{M_p>=2}}={Nk[2]}, EM={EM:.2f}) ---")
    print(f"  {'k':>3}{'#(M_p>=k)':>11}{'ratio k+1/k':>13}")
    for k in range(2,8):
        ratio = Nk[k+1]/Nk[k] if Nk[k] and k+1<=8 else 0
        print(f"  {k:>3}{Nk[k]:>11}{ratio:>13.3f}")
    # borne EM via geometric: si max ratio = rho, EM <= 1/(1-rho) (approx, si Nk[2] domine)
    ratios=[Nk[k+1]/Nk[k] for k in range(2,7) if Nk[k]>0]
    rho=max(ratios) if ratios else 0
    print(f"  max ratio (k=2..6) = rho = {rho:.3f} ; borne géométrique EM <= 1/(1-rho) = {1/(1-rho) if rho<1 else float('inf'):.2f}")
    print(f"  M\"_B / (L²/logL) = {Mpp/(L**2/math.log(L)):.3f}  [o(L²) si borné et /L²->0]")
    print(f"  M\"_B / L² = {Mpp/L**2:.4f}  [doit ->0]")
print("\n  ⟹ si rho stable < 1 et EM borné : le verrou = 'décroissance géométrique de la queue',")
print("     reformulation plus attaquable (chaque rep en plus = un diviseur carré p²|N indépendant).")
