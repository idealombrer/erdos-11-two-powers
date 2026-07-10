# CHANTIER J (Fable) — mesure fine k=2 : histogramme de #{p∈(L,L²]: p²|N}, N=1+2^β−2^γ−2^δ.
# Inventaire des quadruples avec compte>=1 ; classifier structurés (N=(2^k−1)², ou facteur 2^m±1) vs
# sauvages. TABLE BRUTE, pas de verdict.
from sympy import primerange
from collections import Counter, defaultdict
import math

def is_pow2(x):
    return x>0 and (x & (x-1))==0

def is_mersenne_square(N):
    a=abs(N)
    r=math.isqrt(a)
    if r*r!=a: return False
    return is_pow2(r+1)          # r=2^k−1 ⟺ r+1 puiss. de 2

def has_2pm1_factor(N, mmax=64):
    a=abs(N)
    if a<=1: return False
    for m in range(2, mmax+1):
        for pm in (( 1<<m)-1, (1<<m)+1):
            if pm>1 and a % pm==0: return True
    return False

for L in (40,60,80):
    N2p = defaultdict(set)   # N (entier) -> ensemble de p tq p²|N
    for p in primerange(L+1, L*L+1):
        p2=p*p
        pw=[pow(2,j,p2) for j in range(L+1)]
        sums=defaultdict(list)
        for g in range(L+1):
            for d in range(g,L+1):
                sums[(pw[g]+pw[d])%p2].append((g,d))
        for b in range(L+1):
            t=(1+pw[b])%p2
            if t in sums:
                for (g,d) in sums[t]:
                    N=1+(1<<b)-(1<<g)-(1<<d)
                    if N!=0:
                        N2p[N].add(p)
    # histogramme du compte
    hist=Counter(len(ps) for ps in N2p.values())
    nN=len(N2p)
    # classification
    struct=0; mers_sq=0; wild=0
    multi=[]   # N avec compte>=2
    for N,ps in N2p.items():
        s = is_mersenne_square(N) or has_2pm1_factor(N)
        if is_mersenne_square(N): mers_sq+=1
        if s: struct+=1
        else: wild+=1
        if len(ps)>=2: multi.append((N,sorted(ps)))
    print(f"\n===== L={L} =====  (#N distincts avec p²|N : {nN})")
    print(f"  histogramme #{{p: p²|N}} : {dict(sorted(hist.items()))}")
    print(f"  classification : structurés={struct} (dont (2^k−1)²={mers_sq}) | sauvages={wild}"
          f"  [structuré = (2^k−1)² OU facteur 2^m±1]")
    print(f"  quadruples 'doubles' (compte>=2) : {len(multi)}")
    for N,ps in multi[:12]:
        tag=[]
        if is_mersenne_square(N): tag.append("(2^k−1)²")
        if has_2pm1_factor(N): tag.append("fact 2^m±1")
        print(f"    N={N}  p={ps}  {'|'.join(tag) if tag else 'SAUVAGE'}")
print("\n[Table brute. Si tous les 'doubles' sont structurés => cible de classification élémentaire k=2.]")
