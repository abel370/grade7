import numpy as np

def factor_trinomial(a, b, c):
    """Factor a trinomial of the form ax^2 + bx + c using NumPy."""
    if a == 0:
        return "Not a valid quadratic trinomial."

    # Compute a * c
    ac = a * c
    factors = []

    # Find integer pairs that multiply to ac
    for i in range(1, int(np.sqrt(abs(ac))) + 1):
        if ac % i == 0:
            j = ac // i
            factors.append((i, j))
            factors.append((-i, -j))

    # Find the pair that sums to b
    for (m, n) in factors:
        if m + n == b:
            break
    else:
        return "Cannot be factored using integers."

    # Find GCDs
    g1 = np.gcd(a, m)
    g2 = np.gcd(n, c)

    # Construct factorized form
    factor1 = f"{g1}x + {m//g1}" if g1 != 1 else f"x + {m}"
    factor2 = f"{g2}x + {n//g2}" if g2 != 1 else f"x + {n}"

    return f"({factor1})({factor2})"

# Example usage
a, b, c = map(int, input("Enter coefficients a, b, c separated by spaces: ").split())
print(f"Factored form: {factor_trinomial(a, b, c)}")
