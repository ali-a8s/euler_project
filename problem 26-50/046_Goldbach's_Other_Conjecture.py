# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from math import isqrt

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False

    return True

def is_composite(n):
    return n > 1 and not is_prime(n)

def check_conjecture(n):
    k = 1

    while 2 * k**2 < n:
        p = n - 2 * k**2

        if is_prime(p):
            return True

        k += 1

    return False

n = 9

while True:
    if is_composite(n) and not check_conjecture(n):
        print(n)
        break

    n += 2