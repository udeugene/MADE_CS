import math

def solve_square_eq(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    else:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)

assert solve_square_eq(4, 32, 48) == (-2, -6)
assert solve_square_eq(7, -1, 2) is None

assert math.isclose(solve_square_eq(4, -7, 0)[0], 7 / 4)
