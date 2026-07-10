# STEP42 — Universalité : le phénomène (outliers E2, signal congruence) est-il spécifique à g=2 ?
# + robustification : TAUX d'outliers par classe de congruence (pas moyenne, pour ecarter artefact).
from collections import Counter
from sympy import primerange
import numpy as np, math

def profile_base(g, L):
    """Pour base g : sur les Type B (ord_p(g)>L), rho2=Delta_p/aleatoire."""
    P=(L+1)*(L+2)//2; rows=[]
    for p in primerange(L+1, L*L+1):
        if p==g or g%p==0: continue
        # Type B ? ord_p(g)>L <=> g^k mod p != 1 pour k=1..L
        x=1%p; typeA=False
        for k in range(1,L+1):
            x=(x*g)%p
            if x==1: typeA=True; break
        if typeA: continue
        p2=p*p
        pw=[1]*(L+1)
        for k in range(1,L+1): pw[k]=(pw[k-1]*g)%p2
        c=Counter()
        for a in range(L+1):
            pa=pw[a]
            for b in range(a,L+1): c[(pa+pw[b])%p2]+=1
        D=sum(v*(v-1)//2 for v in c.values()); null=P*(P-1)/2/p2
        rows.append((p,D,D/null if null>0 else 0))
    return rows

print("### UNIVERSALITÉ : outliers E2 pour g=2,3,5,6,7,10 (L=100). Base 2 spéciale ?")
print(f"{'g':>4}{'#TB':>6}{'#(ρ>3)':>8}{'#(ρ>10)':>9}{'#(ρ>30)':>9}{'max ρ2':>9}{'moy ρ2':>8}{'ΣΔout/E2':>10}")
allrows={}
for g in (2,3,5,6,7,10):
    rows=profile_base(g,100)
    allrows[g]=rows
    rr=[r[2] for r in rows]
    E2=sum(r[1] for r in rows)
    out=sum(r[1] for r in rows if r[2]>10)
    print(f"{g:>4}{len(rows):>6}{sum(1 for x in rr if x>3):>8}{sum(1 for x in rr if x>10):>9}"
          f"{sum(1 for x in rr if x>30):>9}{max(rr):>9.0f}{np.mean(rr):>8.2f}{out/E2 if E2 else 0:>10.3f}")
print("  ⟹ si g=3,5,7 ont AUSSI des outliers ~= : phénomène UNIVERSEL (sumset de PG, pas spécifique à 2).")
print("     si seul g=2 explose : base 2 réellement spéciale (info énorme).")

print("\n### ROBUSTIFICATION signal congruence : TAUX d'outliers (ρ>10) par p mod 16, pour g=2")
print("     (le mean ρ peut être tiré par qq extrêmes ; le TAUX est robuste)")
rows=allrows[2]
by=Counter(); tot=Counter()
for (p,D,r) in rows:
    tot[p%16]+=1
    if r>10: by[p%16]+=1
print(f"  {'p mod16':>8}{'#prem':>7}{'#outl':>7}{'taux%':>7}")
for m in range(1,16,2):
    print(f"  {m:>8}{tot[m]:>7}{by[m]:>7}{100*by[m]/tot[m] if tot[m] else 0:>7.1f}")
print("  ⟹ si taux(p≡1 mod16) >> autres : signal congruence ROBUSTE (pas artefact de moyenne).")

print("\n### même robustification pour g=3 : le signal est-il sur p mod (structure de 3) ?")
rows3=allrows[3]
for M in (16,): # pour 3, tester p mod ... ; commençons mod 16 aussi
    by=Counter(); tot=Counter()
    for (p,D,r) in rows3:
        tot[p%M]+=1
        if r>10: by[p%M]+=1
    print(f"  g=3, taux outliers par p mod {M} :", end=" ")
    for m in range(1,M,2):
        if tot[m]: print(f"{m}:{100*by[m]/tot[m]:.0f}%", end=" ")
    print()
