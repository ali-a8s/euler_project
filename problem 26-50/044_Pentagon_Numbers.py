# https://projecteuler.net/problem=44


from math import isqrt


def pentagonal(n):
    return n * (3 * n - 1) // 2


def is_pentagonal(x):
    if x < 1:
        return False

    root = isqrt(1 + 24 * x)

    return ( root * root == 1 + 24 * x and (1 + root) % 6 == 0)


def find_pair():
    pentagonals = []
    pentagonal_set = set()

    best_difference = float("inf")
    best_pair = None

    n = 1

    while True:
        current = pentagonal(n)

        for previous in reversed(pentagonals):
            difference = current - previous

            if difference >= best_difference:
                break

            if (is_pentagonal(difference) and is_pentagonal(current + previous)):
                best_difference = difference
                best_pair = (previous, current)

        pentagonals.append(current)
        pentagonal_set.add(current)

        if best_pair is not None:
            next_difference = pentagonal(n + 1) - current

            if next_difference >= best_difference:
                return best_difference, best_pair

        n += 1


difference, pair = find_pair()

print(f"P1 = {pair[0]}")
print(f"P2 = {pair[1]}")
print(f"Difference = {difference}")