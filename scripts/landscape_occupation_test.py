# CHANTIER B (Fable) — RÉOUVERTURE propre du lead #1 (larger sieve), contre sa VRAIE formulation.
# Mesure : combien de classes mod q les ENTIERS M=1+2^β−2^γ−2^δ occupent-ils, pour q<=50 ?
# (Objet correct = les M(δ), PAS les premiers non-Sidon. STEP49 avait testé le mauvais objet.)
# SORTIE = TABLE BRUTE, PAS DE VERDICT (Fable veut valider l'adéquation avant fermeture).
from sympy import primerange
import math

def occupation(q, L):
    """#classes mod q occupées par {1+2^β−2^γ−2^δ mod q : β,γ,δ ∈ [0,L]}."""
    pw=[pow(2,k,q) for k in range(L+1)]
    H=set(pw)                      # {2^k mod q} = sous-groupe (complet si L>=ord_q(2))
    S=set()
    for a in H:
        for b in H:
            for c in H:
                S.add((1+a-b-c)%q)
    return len(S), len(H)          # (occupation, ord_q(2))

print("### CHANTIER B — occupation des classes mod q par M=1+2^β−2^γ−2^δ (objet correct du lead #1)")
print("### TABLE BRUTE, sans verdict. ν(q)=#classes occupées ; ord=ord_q(2) ; ν/q proche de 1 = saturation.\n")
# occupation stabilise dès L>=ord_q(2)<=q-1<=48 ; on prend L=60 (stable) + L=100 pour confirmer L-indep.
qs=list(primerange(3,51))
print(f"  {'q':>3} {'ord_q(2)':>9} | {'ν(q) [L=60]':>12} {'ν/q':>6} | {'ν(q) [L=100]':>13} {'ν/q':>6}")
rows=[]
for q in qs:
    n60,ordq = occupation(q,60)
    n100,_   = occupation(q,100)
    rows.append((q,ordq,n60,n100))
    print(f"  {q:>3} {ordq:>9} | {n60:>12} {n60/q:>6.2f} | {n100:>13} {n100/q:>6.2f}")

# Quantité pertinente pour le larger sieve : Σ_{q} log q / ν(q). Grande = sieve mordrait.
# (À comparer à log N où N = range des M ≈ 2^{L+1}, i.e. log N = (L+1)log2 — ÉNORME.)
print("\n### Quantité larger sieve Σ_{q<=Q} log q/ν(q)  (à comparer à log(range des M)=(L+1)ln2) :")
for Q in (10,20,50):
    Sdiv=sum(math.log(q)/n60 for (q,_,n60,_) in rows if q<=Q)
    Sfull=sum(math.log(q) for (q,_,_,_) in rows if q<=Q)   # Σ log q (cas ν=1, concentration max)
    print(f"  Q={Q:>3}: Σ log q/ν(q) = {Sdiv:.3f}   (vs Σ log q = {Sfull:.3f} si concentration parfaite ; "
          f"log(2^61)={61*math.log(2):.1f})")
print("\n[Table brute transmise pour réévaluation. ord_q(2) petit => ν(q) potentiellement <<q (Mersenne q|2^k−1).]")
