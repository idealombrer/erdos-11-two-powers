"""
Verify the exact per-period structure used in PROOF.md §3:
for non-Wieferich p, over a full double period [0,d_p)^2,
   #{(l,m): 2^l + 2^m ≡ n (mod p^2)} = p * r_p(n),   r_p(n)=#{(u,v) in H_p^2: u+v ≡ n (mod p)}.
This is the consequence of the kernel Lemma K and underlies the uniform-in-n bound
(complete-period term) <= (L+1)^2 / d_p.
"""
def ordm(p, mod):
    o = 1; v = 2 % mod
    while v != 1:
        v = (v * 2) % mod; o += 1
    return o


def check(p):
    m = p * p; dp = ordm(p, m); ep = ordm(p, p)
    sub = [pow(2, l, m) for l in range(dp)]
    Hp = set(pow(2, l, p) for l in range(ep))
    for n in range(m):
        cnt = sum(1 for x in sub for y in sub if (x + y) % m == n)
        rp = sum(1 for u in Hp for v in Hp if (u + v) % p == n % p)
        if cnt != p * rp:
            return False
    return True


if __name__ == "__main__":
    for p in (3, 5, 7, 11, 13, 17, 19, 23):
        print(f"p={p}: period-count == p*r_p(n) for all n mod p^2 : {check(p)}")
