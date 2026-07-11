# CHANTIER D1 (Fable) — vérifier la borne de Stepanov/Heath-Brown–Konyagin AVANT de l'écrire au papier.
# Claim: pour G=<2> mod p (|G|=e_p), N2(n)=#{(u,v)∈G²:u+v≡n mod p} vérifie max_n N2(n) <= 4 e_p^{2/3}
# (sous condition de taille |G|<=p^{2/3}). Test de cohérence de la lecture de Fable sur NOS premiers.
from sympy import primerange
from collections import Counter

def ord2(p):
    x=1
    for k in range(1,p):
        x=(2*x)%p
        if x==1: return k
    return p-1

def N2max(p, e):
    """max_{n≠0} #{(u,v)∈G²: u+v≡n mod p}, G=<2> mod p (reps ordonnées, DÉGÉNÉRÉ n=0 EXCLU)."""
    G=[pow(2,k,p) for k in range(e)]
    c=Counter()
    for u in G:
        for v in G:
            c[(u+v)%p]+=1
    c.pop(0, None)   # exclure n=0 (cas dégénéré -1∈<2>)
    return max(c.values()) if c else 0

print("### CHANTIER D1 — borne Stepanov max_n r_p(n) <= 4 e_p^{2/3} ?  (test de cohérence, sur nos premiers)")
print("### On filtre e_p <= p^{2/3} (condition du théorème). Ratio = N2max / e_p^{2/3}.\n")
worst=0.0; worst_p=None; nboth=0; nviol=0; maxratio_all=0.0
# balayage de premiers jusqu'à 30000 (couvre p<=L² pour L<=170) avec e_p pas trop grand
buckets={}  # tranche de e_p -> max ratio
for p in primerange(3, 30000):
    e=ord2(p)
    if e**3 > p*p:   # e > p^{2/3} : hors condition Stepanov
        continue
    if e < 4: continue        # trop petit, ratio explose trivialement (bord)
    m=N2max(p,e)
    r = m / (e**(2/3))
    nboth+=1
    if r>maxratio_all: maxratio_all=r; worst_p=(p,e,m,r)
    if m > 4*e**(2/3): nviol+=1
    b=(e//10)*10
    buckets[b]=max(buckets.get(b,0), r)

print(f"  #premiers testés (e_p<=p^{{2/3}}, e_p>=4) : {nboth}")
print(f"  #violations de max_n r_p <= 4 e_p^{{2/3}} : {nviol}")
print(f"  ratio max observé N2max/e_p^{{2/3}} : {maxratio_all:.3f}  (à p={worst_p[0]}, e_p={worst_p[1]}, N2max={worst_p[2]})")
print(f"  borne 4 : {'RESPECTÉE partout' if nviol==0 else 'VIOLÉE '+str(nviol)+' fois — lecture de Fable à revoir'}")
print("\n  Ratio max par tranche de e_p (pour voir si l'exposant 2/3 est le bon / si le ratio dérive) :")
for b in sorted(buckets):
    print(f"    e_p∈[{b},{b+9}] : ratio_max = {buckets[b]:.3f}")
print("\n[Si borne respectée et ratio borné ~<4 : lecture de Fable cohérente, on peut écrire la prop.")
print(" Si ratio dérive avec e_p : l'exposant 2/3 (ou la constante 4) est faux dans nos données.]")
