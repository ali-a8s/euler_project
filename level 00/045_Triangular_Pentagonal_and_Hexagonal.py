
from math import isqrt


def is_pentagonal(num):
    discriminant = 1 + 24 * num
    root = isqrt(discriminant)

    if root * root != discriminant:
        return False

    return (1 + root) % 6 == 0


def solve():
    n = 144

    while True:
        hexagonal = n * (2 * n - 1)

        if is_pentagonal(hexagonal):
            return hexagonal

        n += 1


print(solve())