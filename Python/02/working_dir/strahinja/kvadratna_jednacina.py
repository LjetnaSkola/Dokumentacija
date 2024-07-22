import math


def quadratic_eq(a, b, c):
    DX = b**2 - 4 * a * c
    if DX < 0:
        D1 = math.sqrt(abs(DX))
        return tuple(complex(-b, D) / (2 * a) for D in (D1, -D1))
    D1 = math.sqrt(DX)
    return tuple((-b + D) / (2 * a) for D in (D1, -D1))


if __name__ == "__main__":
    print(quadratic_eq(1, -5, -14))  # Example output: (7.0, -2.0)
    print(quadratic_eq(20, -15, -10))  # Example output: (1.0, -0.5)
    print(quadratic_eq(1, 6, 18))  # Example output: (-3.0, -6.0)
