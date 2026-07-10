# CHANTIER H tâche 4 (Fable) — vérif numérique de la sup-norme Bourgain-Chang sur Type B.
# Claim: pour p Type B (e_p>L, p∈(L,L²]), max_{p∤ξ} |S(ξ)|/(L+1) < 1, décroissant (le (L+1)^{-ε}),
# où S(ξ)=Σ_{j≤L} e_{p²}(ξ 2^j). AVANT toute conversion moments : la borne s'observe-t-elle ?
import numpy as np
from sympy import primerange

def ord2(p):
    x=1
    for k in range(1,p):
        x=(2*x)%p
        if x==1: return k
    return p-1

def supnorm_ratio(p, L):
    """max_{p∤ξ, ξ≠0} |S(ξ)|/(L+1), S(ξ)=Σ_{j=0}^L e_{p²}(ξ 2^j)."""
    p2=p*p
    a=np.array([pow(2,j,p2) for j in range(L+1)], dtype=np.float64)
    # ξ parcourt 1..p²-1 avec p∤ξ ; vectorisé par blocs pour la mémoire
    best=0.0
    xis=np.arange(1,p2)
    xis=xis[xis % p != 0]           # p∤ξ
    B=200000
    for s in range(0,len(xis),B):
        blk=xis[s:s+B][:,None]      # (b,1)
        ph=2*np.pi*(blk*a % p2)/p2  # (b,L+1)
        S=np.abs(np.cos(ph).sum(1)+1j*np.sin(ph).sum(1))
        m=S.max()
        if m>best: best=m
    return best/(L+1)

print("### CHANTIER H tâche4 — sup-norme |S(ξ)|/(L+1) sur premiers Type B (attendu <1, décroissant).")
print(f"  {'L':>4} {'p':>7} {'e_p':>6} {'max|S(ξ)|/(L+1) (p∤ξ)':>24}")
for L in (40,80,120):
    # quelques premiers Type B : les premiers p>L avec e_p>L, p pas trop grand (coût p²)
    cnt=0
    for p in primerange(L+1, 3*L):
        e=ord2(p)
        if e<=L: continue           # Type A
        r=supnorm_ratio(p,L)
        print(f"  {L:>4} {p:>7} {e:>6} {r:>24.4f}")
        cnt+=1
        if cnt>=4: break
print("\n[Si ratio <1 partout et tendance décroissante avec L : Bourgain-Chang confirmé sur nos données.")
print(" (Type A exclu : e_p<=L, contre-ex 4.23 = 1+p, ordre 1 mod p, pas de cancellation.)]")
