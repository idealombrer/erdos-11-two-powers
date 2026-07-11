# CHANTIER A (Fable) — CORRIGÉ : moments du VRAI C(n) = Σ_p N_p(N_p−1) (compte de collisions, papier l.741).
# (v1 mesurait Σ N_p = mauvaise quantité.) Σ N_p <= π(L²)+C(n) (prop Qfree) ; densité exceptionnelle
# contrôlée par C(n). Markov donne C̄/(ηL²)=O(1/(L logL)). Chebyshev/2k-moment font-ils mieux ?
# C(n)=Σ X_p, X_p=N_p(N_p−1). Indép. CRT => Var[C]=Σ Var[X_p]. ATTENTION: X_p convexe amplifie grands N_p
# (queue potentiellement LOURDE, pas Poisson) — à vérifier, pas à supposer.
from collections import Counter
from sympy import primerange
import math

def moments_C(L):
    """E[C]=Σ Δ_p/p² ; Var[C]=Σ Var[X_p] ; + max X_p, sur p∈(L,L²], X_p=N_p(N_p−1)."""
    EC=0.0; VarC=0.0; maxXp=0.0; EC3=0.0
    for p in primerange(L+1, L*L+1):
        p2=p*p; pw=[1]*(L+1)
        for k in range(1,L+1): pw[k]=(pw[k-1]<<1)%p2
        c=Counter()
        for a in range(L+1):
            pa=pw[a]
            for b in range(a,L+1): c[(pa+pw[b])%p2]+=1
        # X_p prend la valeur x_r=count_r(count_r−1) sur la classe r ; E sur n mod p² :
        # E[X_p]=Σ_r x_r/p² = Δ_p/p² ; E[X_p²]=Σ_r x_r²/p²
        s1=0; s2=0
        for v in c.values():
            x=v*(v-1)
            if x: s1+=x; s2+=x*x
        eXp=s1/p2; eXp2=s2/p2
        EC += eXp; VarC += (eXp2 - eXp*eXp)
        # max de x_r sur ce p (pour voir la queue)
        mx=max((v*(v-1) for v in c.values()), default=0)
        maxXp=max(maxXp, mx)
    return EC, VarC, maxXp

print("### CHANTIER A CORRIGÉ — moments du VRAI C(n)=Σ N_p(N_p−1). Chebyshev bat-il Markov O(1/(L logL)) ?\n")
print(f"  {'L':>3} {'E[C]=C̄':>9} {'Var[C]':>10} {'Var/E':>7} {'maxX_p':>7} {'Markov':>12} {'Chebyshev':>12} {'gain?':>6}")
for L in (16,20,24,28,32,36):
    EC,VarC,maxXp = moments_C(L)
    eta=0.4; t=eta*L*L
    markov = EC/t                       # P(C>=t) <= C̄/t
    cheby  = VarC/((t-EC)**2) if t>EC else float('inf')   # P(|C-C̄|>=t-C̄) <= Var/(t-C̄)²
    gain = "OUI" if cheby<markov else "non"
    print(f"  {L:>3} {EC:>9.3f} {VarC:>10.3f} {VarC/EC if EC else 0:>7.2f} {maxXp:>7.0f} "
          f"{markov:>12.2e} {cheby:>12.2e} {gain:>6}")
print("""
  Lecture (HONNÊTE) :
  - E[C]=C̄ doit retrouver ~0.44..0.96 du papier (sanity check bonne quantité).
  - Si Var[C]/E[C] borné (~O(1)) : Chebyshev O(Var/(ηL²)²)=O(1/(L³logL)) bat Markov O(1/(L logL)) d'un
    facteur L². Si Var[C]/E[C] EXPLOSE (queue lourde via maxX_p) : Chebyshev ne gagne pas -> Fable a tort
    sur ce C(n), la convexité de N_p(N_p−1) tue la concentration. À LIRE dans les chiffres, pas supposer.
""")
