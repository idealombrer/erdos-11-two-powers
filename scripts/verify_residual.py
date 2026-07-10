"""
Split the residual term of Lemma E' into R1 (boundary, primes with a complete period d_p<=L+1)
and R2 (large primes d_p>L+1, no complete period), for the WORST n at each dyadic scale.

KEY CLAIM (approach b, elementary): boundary-bearing primes have d_p<=L+1 => p<=L+1 (since
d_p=p*ord_p(2)>=p for non-Wieferich p). So R1 involves only ~pi(L+1)=O(L/log L) primes, each
bord_p<=3(L+1), giving R1 = O(L^2/log L) = o(L^2) ELEMENTARILY. We verify:
  (1) every prime with d_p<=L+1 satisfies p<=L+1,
  (2) R1 <= 3(L+1)*pi(L+1) and R1/L^2 -> 0,
  (3) R2 = sum_{d_p>L+1, p<=sqrt n} N_p(n), report size and growth (needs analytic input).
"""
import sys
from sympy import primerange

def ordm(p, mod):
    o = 1; v = 2 % mod
    while v != 1:
        v = (v * 2) % mod; o += 1
    return o

def Np(n, p, L):
    m = p * p
    res = [pow(2, l, m) for l in range(L + 1)]
    from collections import Counter
    c = Counter(res)
    tot = 0
    for x, cx in c.items():
        y = (n - x) % m
        tot += cx * c.get(y, 0)
    return tot  # ordered pairs

def r_p(n, p):
    ep = ordm(p, p)
    H = set(pow(2, l, p) for l in range(ep))
    return sum(1 for u in H for v in H if (u + v) % p == n % p)

def worst_n(top, win):
    """worst n in [top-2win, top): maximize (ordered) nonsquarefree fraction via small-prime proxy."""
    import math
    lo = top - 2 * win
    # cheap proxy: count pairs with k divisible by 9,25,49 (p=3,5,7) -- correlates with worst
    best = None
    for n in range(lo | 1, top, 2):
        L = n.bit_length() - 1
        bad = 0; tot = 0
        for l in range(L + 1):
            for mm in range(l, L + 1):
                k = n - (1 << l) - (1 << mm)
                if k < 1: continue
                tot += 1
                if k % 9 == 0 or k % 25 == 0 or k % 49 == 0: bad += 1
        f = bad / tot
        if best is None or f > best[0]:
            best = (f, n, L)
    return best[1], best[2]

if __name__ == "__main__":
    print(f"{'scale':>9} {'L':>3} {'worst-n':>9} {'pi(L+1)':>7} {'maxP(dp<=L+1)':>13} "
          f"{'R1':>5} {'3(L+1)piL':>9} {'R1/L^2':>7} | {'R2':>4} {'R2/L^2':>7}")
    for kk in range(13, 23):
        top = 1 << kk
        n, L = worst_n(top, 400)
        sq = int(n ** 0.5)
        R1 = 0; R2 = 0; maxP_small = 0
        for p in primerange(3, sq + 1):
            dp = ordm(p, p * p)
            npn = Np(n, p, L)  # ordered
            if dp <= L + 1:
                maxP_small = max(maxP_small, p)
                Q = (L + 1) // dp
                main = Q * Q * p * r_p(n, p)   # ordered complete-period main term
                bord = npn - main
                R1 += bord
            else:
                R2 += npn
        import sympy
        piL = int(sympy.primepi(L + 1))
        print(f"{top:>9} {L:>3} {n:>9} {piL:>7} {maxP_small:>13} {R1:>5} "
              f"{3*(L+1)*piL:>9} {R1/(L*L):>7.4f} | {R2:>4} {R2/(L*L):>7.4f}")
