# STEP30 — κ_p cache-t-il une structure plus simple ? (EXP 2/4/5 : patrons, incompatibilités, minimalité)
#
# Candidat : ι_p = nb d'ORBITES D'INVOLUTION {δ₀, e−δ₀} dans l'ensemble des δ-classes actives.
#   (STEP26 : δ↔e−δ forcé par 1+2^{e−δ}=2^{−δ}(1+2^δ). Les δ-sets observés = orbites d'involution.)
# Question : ι_p ≪ κ_p et borné/O(1) ? La coexistence de plusieurs orbites suit-elle une règle ?

from collections import Counter, defaultdict
from sympy import primerange, n_order

def max_fiber_deltas(p, L):
    p2=p*p; reps=defaultdict(list)
    for a in range(L+1):
        for b in range(a,L+1): reps[((1<<a)+(1<<b))%p2].append((a,b))
    r=max(reps,key=lambda k:len(reps[k])); ab=reps[r]
    e=n_order(2,p)
    dset=sorted(set((b-a)%e for (a,b) in ab))
    return len(ab), e, dset

def involution_orbits(dset, e):
    seen=set(); orbits=[]
    for d in dset:
        if d in seen: continue
        pair={d,(e-d)%e}
        orbits.append(sorted(pair & set(dset)))
        seen|=pair
    return orbits

def is_AP_mod(dset, e):
    if len(dset)<=2: return True
    ds=sorted(dset); steps=set((ds[i+1]-ds[i]) for i in range(len(ds)-1))
    return len(steps)==1

print("### EXP 2/5 : δ-classes actives, orbites d'involution ι_p, patrons (L=160, M_p≥4)")
L=160
print(f"{'p':>6}{'e_p':>5}{'M_p':>4}{'κ_p':>4}{'ι_p':>4}  {'δ-classes mod e':>22}  {'orbites involution':>26}")
rows=[]
for p in primerange(L+1, L*L+1):
    Mp,e,dset=max_fiber_deltas(p,L)
    if Mp<4: continue
    orbs=involution_orbits(dset,e)
    iota=len(orbs)
    rows.append((p,e,Mp,len(dset),iota,dset,orbs))
    print(f"{p:>6}{e:>5}{Mp:>4}{len(dset):>4}{iota:>4}  {str(dset):>22}  {str(orbs):>26}")

# distribution de ι_p et κ_p
kap=[r[3] for r in rows]; iot=[r[4] for r in rows]
print(f"\n  κ_p : min={min(kap)} max={max(kap)} moy={sum(kap)/len(kap):.2f}  |  "
      f"ι_p : min={min(iot)} max={max(iot)} moy={sum(iot)/len(iot):.2f}")
print(f"  #premiers avec ι_p=1 : {sum(1 for i in iot if i==1)}/{len(iot)} ; ι_p≤2 : {sum(1 for i in iot if i<=2)}/{len(iot)}")

print("\n### EXP 2 : combien de PATRONS distincts ? (δ-set canonicalisé : orbites, tailles triées)")
patterns=Counter()
for (p,e,Mp,k,iota,dset,orbs) in rows:
    # signature : multiset des tailles d'orbite + présence du point fixe 0/e-0
    sig=tuple(sorted(len(o) for o in orbs))
    hasfix=any(len(o)==1 for o in orbs)
    patterns[(sig,)]+=1
for sig,ct in patterns.most_common():
    print(f"   patron tailles-orbites {sig[0]} : {ct} premiers")

print("\n### EXP 4 : la COEXISTENCE de ≥2 orbites — corrèle-t-elle avec ord_p(2) ?")
multi=[r for r in rows if r[4]>=2]; single=[r for r in rows if r[4]==1]
print(f"  ι_p=1 (une orbite) : {len(single)} premiers, e_p moy={sum(r[1] for r in single)/max(1,len(single)):.0f}")
print(f"  ι_p≥2 (multi)      : {len(multi)} premiers, e_p moy={sum(r[1] for r in multi)/max(1,len(multi)):.0f}")
print("  e_p des multi-orbites :", sorted(r[1] for r in multi))
# le point fixe 0 (δ≡0) présent ⟺ ? (0 = diagonale a=b, 2^{a+1})
print("  δ≡0 présent (paire a=b, i.e. 2·2^a) chez :", [r[0] for r in rows if 0 in r[5]])

print("\n### croissance de max ι_p (hors Wieferich) : plus stable que κ_p ?")
for LL in (80,120,160,200):
    mk=0; mi=0
    for p in primerange(LL+1, LL*LL+1):
        if p in (1093,3511): continue
        Mp,e,dset=max_fiber_deltas(p,LL)
        if Mp<4: continue
        orbs=involution_orbits(dset,e)
        mk=max(mk,len(dset)); mi=max(mi,len(orbs))
    print(f"  L={LL}: max κ_p={mk}, max ι_p={mi}")
