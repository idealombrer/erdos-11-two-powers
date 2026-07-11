# Script rename map (old → new)

Scripts were renamed to descriptive English names before publication. This map exists so that
`../worklog/` — which references the old names throughout and is deliberately left unmodified
(it is the historical record) — stays decipherable.

| Old name (worklog) | New name (this repo) |
|---|---|
| `chantierA_moments.py` | `typeB_moments_conditional_check.py` |
| `chantierB_occupation.py` | `landscape_occupation_test.py` |
| `chantierD_stepanov.py` | `typeA_garcia_voloch_check.py` |
| `chantierF_digits.py` | `landscape_digit_weight_check.py` |
| `chantierG_band.py` | `typeA_exceptional_band.py` |
| `chantierH_supnorm.py` | `typeB_supnorm_check.py` |
| `chantierJ_k2.py` | `typeB_k2_inventory.py` |
| `checkB.py` | `typeB_wall_first_moment.py` |
| `geometric_decay.py`, `heath_brown_e2.py`, `kappa_structure.py`, `larger_sieve_test.py`, `lemmaE2.py`, `orders.py`, `sum_ord.py`, `universality.py`, `verify_residual.py`, `verify_structure.py` | *(unchanged — already descriptive)* |

None of these scripts import one another (verified before renaming), so no internal import
statements needed fixing.
