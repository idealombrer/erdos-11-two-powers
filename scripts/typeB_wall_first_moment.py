# Test: average-case behaviour of the "wall B" range p in (L^2, sqrt(n/2)].
# Claim to verify: for almost all n, the B-range contributes 0 (no pair killed by
# a square prime factor p^2 with p in (L^2, sqrt(n/2)]). I.e. its first moment ->0.
from sympy import primerange
import math

def Bstats(lo, hi):
    n_total=0; n_bad=0; total_contrib=0; maxc=0
    for n in range(lo|1, hi, 2):
        L = n.bit_length()-1
        loB = L*L
        hiB = int((n/2)**0.5)
        if hiB <= loB:
            n_total+=1; continue
        # collect pairs values k=n-2^l-2^m >=1
        ks=[]
        for l in range(L+1):
            for m in range(l,L+1):
                k=n-(1<<l)-(1<<m)
                if k>=1: ks.append(k)
        contrib=0
        for p in primerange(loB+1, hiB+1):
            p2=p*p
            c=sum(1 for k in ks if k% p2==0)
            contrib+=c
        total_contrib+=contrib
        maxc=max(maxc,contrib)
        n_total+=1
        if contrib>0: n_bad+=1
    return n_total, n_bad, total_contrib/n_total, maxc

for (lo,hi) in [(50000,60000),(500000,510000),(5000000,5010000)]:
    nt,nb,avg,mx=Bstats(lo,hi)
    L=(lo).bit_length()-1
    print(f"n in [{lo},{hi}) L~{L}: frac with B-contrib>0 = {nb}/{nt} = {nb/nt:.4f}, "
          f"avg B-contrib = {avg:.5f}, max = {mx}, 1/(2lnL)~{1/(2*math.log(L)):.4f}")
