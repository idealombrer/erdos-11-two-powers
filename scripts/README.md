# scripts/ — numerical support

Each script prints the figures quoted in the paper to stdout. The authoritative index —
paper claim → script — is the **table in [`../README.md`](../README.md#numerical-claims--scripts)**.

Requirements: `python3` with `numpy` and `sympy`. All scripts are path-independent; run any of
them from inside this directory:

```bash
cd scripts
python3 orders.py               # pivot constant 0.3205..., order sum O(L^2/log L)
python3 chantierH_supnorm.py    # Bourgain-Chang sup-norm max|S|/(L+1) = 0.37, 0.31, 0.24
python3 chantierJ_k2.py         # k=2 inventory: every p^2|N double is a Mersenne square
```

Some scripts sweep a range of $L$ and take up to a couple of minutes (e.g.
`chantierA_moments.py`, `chantierJ_k2.py`, `chantierH_supnorm.py`); the rest run in seconds.
Each has a header docstring stating what it computes.
