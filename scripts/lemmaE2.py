"""
Verify the KERNEL CANCELLATION mechanism behind S(a)=0.

Claim: for p prime, p | a not, the complete-period subgroup sum
   S(a) = sum_{x in <2> mod p^2} e_{p^2}(a x)
vanishes  <=>  p | d_p  (d_p = ord_{p^2}(2)), i.e. p is NON-Wieferich (2^{p-1} != 1 mod p^2),
because then <2> contains the kernel K = {1+jp : j} of reduction mod p, and each K-coset
sums to 0.

Wieferich primes (1093, 3511): d_p = ord_p(2) (no factor p) => <2> misses K => S(a) != 0.
"""
import cmath, math

def ord_mod(p, mod):
    o = 1; v = 2 % mod
    while v != 1:
        v = (v*2) % mod; o += 1
    return o

def kernel_in_subgroup(p):
    """is the element 1+p (a generator of K) inside <2> mod p^2 ?"""
    m = p*p
    target = (1 + p) % m
    v = 1 % m
    for _ in range(ord_mod(p, m)):
        if v == target:
            return True
        v = (v*2) % m
    return False

def S_maxabs_coprime(p):
    """max_{a: p∤a} |sum_{x in <2>} e_{p^2}(a x)|, exact-ish via complex sum."""
    m = p*p
    xs = []; v = 1 % m
    for _ in range(ord_mod(p, m)):
        xs.append(v); v = (v*2) % m
    best = 0.0
    for a in range(1, m):
        if a % p == 0:
            continue
        s = sum(cmath.exp(2j*math.pi*(a*x % m)/m) for x in xs)
        best = max(best, abs(s))
    return best

if __name__ == "__main__":
    print("p | d_p (non-Wieferich) and kernel-containment and S(a)=0 should all agree:")
    print(f"{'p':>5} {'ord_p(2)':>8} {'d_p=ord_p2':>10} {'p|d_p?':>7} {'K in <2>?':>9} {'maxS(p∤a)':>10}")
    for p in (3,5,7,11,13,17,19,23,29,31,37,41,43,127):
        ep = ord_mod(p, p)
        dp = ord_mod(p, p*p)
        pdvd = (dp % p == 0)
        kin = kernel_in_subgroup(p)
        sm = S_maxabs_coprime(p)
        print(f"{p:>5} {ep:>8} {dp:>10} {str(pdvd):>7} {str(kin):>9} {sm:>10.4f}")

    print("\nWieferich primes: expect d_p = ord_p(2) (NO factor p), K NOT in <2>, S != 0:")
    for p in (1093, 3511):
        ep = ord_mod(p, p)
        dp = ord_mod(p, p*p)
        print(f"  p={p}: ord_p(2)={ep}, ord_p2(2)={dp}, d_p==ord_p? {dp==ep}, "
              f"p|d_p? {dp%p==0}, K in <2>? {kernel_in_subgroup(p)}")
