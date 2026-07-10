# STEP49 — Lead Fable n°1 : le larger sieve de Gallagher mord-il sur (M'') ?
# Gallagher: pour A ⊆ [1,N] occupant ν(q) classes mod q, |A| <= (Σ log q − log N)/(Σ log q/ν(q) − log N).
# Puissant SEULEMENT si A concentré (ν(q) << q). Nos premiers non-Sidon sont dans (L,L²] : RANGE
# POLYNOMIAL (pas de mur exponentiel comme STEP44). Question décisive : concentration ou équidistribution ?
from collections import Counter
from sympy import primerange, primepi
import math

def multiplicities(L):
    """M_p pour tout p in (L, L²] ; renvoie B2={p:M_p>=2}, B3={p:M_p>=3}."""
    B2=[]; B3=[]
    for p in primerange(L+1, L*L+1):
        p2=p*p; pw=[1]*(L+1)
        for k in range(1,L+1): pw[k]=(pw[k-1]<<1)%p2
        c=Counter()
        for a in range(L+1):
            pa=pw[a]
            for b in range(a,L+1): c[(pa+pw[b])%p2]+=1
        Mp=max(c.values())
        if Mp>=2: B2.append(p)
        if Mp>=3: B3.append(p)
    return B2,B3

def nu(A,q):
    """#classes distinctes mod q occupées par A."""
    return len(set(a%q for a in A))

def gallagher_bound(A, N, qs):
    """Borne du larger sieve avec premiers cribleurs qs. None si dénominateur<=0."""
    S = sum(math.log(q) for q in qs)
    Sdiv = sum(math.log(q)/nu(A,q) for q in qs)
    num = S - math.log(N); den = Sdiv - math.log(N)
    if den <= 0: return None, num, den
    return num/den, num, den

for L in (100,140):
    N = L*L
    B2,B3 = multiplicities(L)
    piN = int(primepi(N))
    print(f"\n===== L={L}  (N=L²={N}, π(N)={piN}) =====")
    print(f"  |B2| (#non-Sidon, M_p>=2) = {len(B2)}   [déjà <= π(N)={piN} trivialement]")
    print(f"  |B3| (M_p>=3)             = {len(B3)}")
    # concentration ? ν(q) vs q-1 (équidistribution parfaite parmi premiers = q-1)
    print(f"\n  Concentration mod petits q :  ν_B2(q) / (q-1)   [~1.0 = équidistribué = larger sieve INUTILE]")
    smallq=[3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    for q in smallq:
        r2=nu(B2,q)/(q-1); r3=(nu(B3,q)/(q-1)) if B3 else 0
        print(f"    q={q:>3}: ν_B2={nu(B2,q):>3}/{q-1:<3} ={r2:5.2f}   ν_B3={nu(B3,q):>3}/{q-1:<3} ={r3:5.2f}")
    # borne de Gallagher explicite, cribleurs = tous premiers jusqu'à Q
    print(f"\n  Borne de Gallagher (cribleurs q<=Q) sur B2, à comparer à π(N)={piN} et |B2|={len(B2)} :")
    for Q in (50, 200, 1000, N):
        qs=list(primerange(2,Q+1))
        b,num,den = gallagher_bound(B2, N, qs)
        bs = f"{b:12.0f}" if b is not None else f"  dénom<=0 (den={den:.2f})"
        print(f"    Q={Q:>6}: borne |B2| <= {bs}   {'(> π(N): INUTILE)' if (b is None or b>=piN) else '(< π(N): MORD !)'}")
print("\n  ⟹ Verdict : si ν(q)/(q-1)≈1 (équidistribution) la borne dépasse π(N) => larger sieve INUTILE,")
print("     et l'échec est par MANQUE DE CONCENTRATION (STEP42), pas par range exponentiel (STEP44).")
