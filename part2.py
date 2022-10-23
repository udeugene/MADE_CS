import math

def solve_square_eq(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    else:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
