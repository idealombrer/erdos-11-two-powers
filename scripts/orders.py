"""
The linchpin constant for the two-powers elementary sieve (Erdős #11 variant):
    S = sum_{p>=3} 1 / ord_{p^2}(2).
If S < 1/2, the small-prime bad-pair count is < (total candidate pairs)/... , leaving a
positive density of squarefree pairs n-2^l-2^m (the large-prime term being o(L^2)).
k = n-2^l-2^m is always ODD, so p=2 is excluded; sum starts at p=3.
Result: S ~ 0.3205 < 0.5, dominated by p=3 (1/6), p=5 (1/20), p=7 (1/21).
"""
from sympy import nextprime, divisors, primerange


def ord_p2(p):
    """ord of 2 mod p^2, via divisors of p(p-1) (the order divides p(p-1))."""
    m = p * p
    for d in sorted(divisors(p * (p - 1))):
        if pow(2, d, m) == 1:
            return d
    return p * (p - 1)


if __name__ == "__main__":
    p, S = 3, 0.0
    TAIL = 5000
    print("p, ord_{p^2}(2), 1/ord, running sum:")
    while p < TAIL:
        d = ord_p2(p)
        S += 1.0 / d
        if p < 60 or p in (97, 101):
            print(f"  p={p:4d}  ord={d:8d}  1/ord={1.0/d:.5f}  sum={S:.5f}")
        p = nextprime(p)
    tail = sum(1.0 / (q * (q - 1)) for q in primerange(TAIL, 2_000_000))
    print(f"sum 3<=p<{TAIL}: {S:.6f}   tail proxy sum 1/(p(p-1)), p>={TAIL}: {tail:.6f}")
    print(f"=> S_total ~ {S + tail:.4f}  < 0.5 ? {S + tail < 0.5}")
