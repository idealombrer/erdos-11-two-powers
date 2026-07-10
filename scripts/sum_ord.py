# STEP26-lit — Σ_{p∈(L,L²]} 1/ord_p(2) et (⋆)=Σ⌊L/ord_p(2)⌋ : croissance + borne élémentaire.
#
# CLAIM (élémentaire, INCONDITIONNEL) : les premiers p>L divisant 2^k-1 ont un produit < 2^k,
#   donc #{p>L : p|2^k-1} < k·log2/log L.  D'où :
#   (⋆) = Σ_{p∈(L,L²]} ⌊L/ord_p(2)⌋ = Σ_{k<=L} #{p∈(L,L²]: p|2^k-1} < Σ_{k<=L} k·log2/logL
#        = (log2/logL)·L(L+1)/2 = O(L²/log L) = o(L²).   [pas de GRH]
#   et Σ 1/ord_p(2) = [ord<=L] + [ord>L] :
#       [ord>L] < π(L²)/L = O(L/log L) ;  [ord<=L] < Σ_{k<=L}(1/k)·k·log2/logL = O(L/log L).
#   ⟹ Σ 1/ord_p(2) = O(L/log L) = o(L).  M" = o(L²) SI M_p<=⌊L/ord_p⌋+O(1) (STEP26, empirique).

from sympy import primerange, n_order
import math

MAXP = 100*100
print("Précalcul des ordres ord_p(2) pour p <= 10^4 ...")
ordm = {}
for p in primerange(3, MAXP+1):
    ordm[p] = n_order(2, p)
print(f"  {len(ordm)} premiers.\n")

print("### ÉTAPE 2 — croissance de S(L)=Σ_{p∈(L,L²]} 1/ord_p(2) et (⋆)=Σ⌊L/ord_p⌋")
print(f"{'L':>4} {'#p':>6} {'S=Σ1/ord':>9} {'S/L':>8} {'S/logL':>8} {'(⋆)=Σ⌊L/ord⌋':>13} "
      f"{'(⋆)/L²':>8} {'(⋆)/(L²/logL)':>13} {'#ord<=L':>8}")
rows=[]
for L in (20,30,40,50,60,70,80,90,100):
    ps=[p for p in ordm if L < p <= L*L]
    S=sum(1.0/ordm[p] for p in ps)
    star=sum(L//ordm[p] for p in ps)
    nsmall=sum(1 for p in ps if ordm[p]<=L)
    rows.append((L,len(ps),S,star,nsmall))
    print(f"{L:>4} {len(ps):>6} {S:>9.3f} {S/L:>8.4f} {S/math.log(L):>8.3f} {star:>13} "
          f"{star/L**2:>8.4f} {star/(L**2/math.log(L)):>13.3f} {nsmall:>8}")

print("\n### comparaison des ordres de grandeur (repères Mertens)")
for L in (40,70,100):
    ps=[p for p in ordm if L<p<=L*L]
    s_inv_p=sum(1.0/p for p in ps)                  # ~ log2 = 0.693 (Mertens sur (L,L²])
    s_inv_sqrtp=sum(1.0/math.sqrt(p) for p in ps)   # ~ L/logL
    S=sum(1.0/ordm[p] for p in ps)
    print(f"  L={L}: Σ1/ord={S:.3f}  |  Σ1/p={s_inv_p:.3f} (~log2=0.69)  |  Σ1/√p={s_inv_sqrtp:.1f} (~L/logL={L/math.log(L):.1f})")
print("  ⟹ Σ1/ord est de l'ordre de Σ1/p (BORNÉE ~O(1)), PAS de Σ1/√p. Bien plus petite que ma borne O(L/logL).")

print("\n### ÉTAPE 3 — vérif borne élémentaire : #{p>L : p|2^k-1} < k·log2/log L ?")
for L in (50,100):
    print(f"  L={L} :")
    worst=0.0
    for k in range(1, L+1):
        M=2**k-1
        cnt=0
        for p in primerange(L+1, min(M, L*L)+1):
            if M % p == 0: cnt+=1
        bound=k*math.log(2)/math.log(L)
        if cnt> worst*1: pass
        ratio = cnt/bound if bound>0 else 0
        worst=max(worst,ratio)
        if k in (int(math.log2(L))+1, L//2, L, L-1):
            print(f"     k={k:>3}: #{{p∈(L,L²]:p|2^k-1}}={cnt:>2}  borne k·log2/logL={bound:>5.1f}  ok={cnt<=bound}")
    print(f"     max ratio cnt/borne sur k<=L : {worst:.3f}  ⟹ borne {'VALIDE' if worst<=1.001 else 'VIOLÉE'}")

print("\n### ÉTAPE 4 — décomposition Type A (ord<=L) / Type B (ord>L) de S(L)")
print(f"{'L':>4} {'S_typeA(ord<=L)':>14} {'S_typeB(ord>L)':>14} {'S_B/L':>8}")
for L in (40,60,80,100):
    ps=[p for p in ordm if L<p<=L*L]
    SA=sum(1.0/ordm[p] for p in ps if ordm[p]<=L)
    SB=sum(1.0/ordm[p] for p in ps if ordm[p]>L)
    print(f"{L:>4} {SA:>14.3f} {SB:>14.3f} {SB/L:>8.4f}")
print("  (Type B = ord>L : chaque terme <1/L, Σ<π(L²)/L=O(L/logL) — trivialement o(L).)")
