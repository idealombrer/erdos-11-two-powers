# CHANTIER F (Fable) — mini-test digits : les pires n (min de représentations) ont-ils un s_2(n) extrême ?
# R(n) = #{(l,m), 0<=l<=m : n-2^l-2^m > 0 et SANS FACTEUR CARRÉ}. Pire n = min R(n). s_2 = poids binaire.
# TABLE BRUTE, pas de verdict (comme Fable demande pour F).
import math

def squarefree_sieve(N):
    """sf[k]=True si k sans facteur carré, k<N."""
    sf=bytearray([1])*N
    i=2
    while i*i < N:
        sq=i*i
        for j in range(sq, N, sq): sf[j]=0
        i+=1
    return sf

print("### CHANTIER F — s_2(n) des pires n (min de représentations k+2^l+2^m, k sans facteur carré).")
print("### R(n)=#{paires (l,m): n-2^l-2^m>0 sans facteur carré}. TABLE BRUTE.\n")
print(f"  {'L':>3} {'#n testés':>10} {'minR':>5} {'s2 des ~10 pires n (poids binaire)':>36} {'s2 moy 5%pires':>15} {'s2 moy global':>14}")
for L in range(11, 21):
    lo, hi = 1<<L, 1<<(L+1)
    sf = squarefree_sieve(hi)
    pw = [1<<k for k in range(L+1)]
    best=[]  # (R(n), n, s2)
    s2sum=0; cnt=0
    Rvals=[]
    for n in range(lo|1, hi, 2):   # n impair
        R=0
        for i in range(L+1):
            a=pw[i]
            if a>=n: break
            for j in range(i, L+1):
                v=n-a-pw[j]
                if v<=0: break
                if sf[v]: R+=1
        s2=bin(n).count("1")
        s2sum+=s2; cnt+=1
        Rvals.append((R,s2,n))
    Rvals.sort()
    minR=Rvals[0][0]
    worst10=Rvals[:10]
    k5=max(1,cnt//20)
    s2_worst = sum(s for _,s,_ in Rvals[:k5])/k5
    s2_glob = s2sum/cnt
    s2list=",".join(str(s) for _,s,_ in worst10)
    print(f"  {L:>3} {cnt:>10} {minR:>5} {s2list:>36} {s2_worst:>15.2f} {s2_glob:>14.2f}")
print("\n[Comparer s2 moy des 5% pires vs global : si systématiquement < ou > => scission par s_2 justifiée.")
print(" minR = nb minimal de représentations ; s'il reste >0 partout, aucun contre-exemple à cette échelle.]")
