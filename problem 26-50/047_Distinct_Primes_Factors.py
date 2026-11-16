from math import isqrt


def is_prime(num):
    if num < 2:
        return False

    if num % 2 == 0:
        return num == 2

    for i in range(3, isqrt(num) + 1, 2):
        if num % i == 0:
            return False

    return True


def prime_ls(num):
    return [i for i in range(2, isqrt(num) + 1) if is_prime(i)]


def solve(num):
    result = []

    for prime in prime_ls(num):
        if num % prime == 0:
            result.append(prime)

            while num % prime == 0:
                num //= prime

    if num > 1:
        result.append(num)

    return result


def find_consecutive_numbers():
    consecutive = 0
    num = 2

    while True:
        if len(solve(num)) == 4:
            consecutive += 1
        else:
            consecutive = 0

        if consecutive == 4:
            return num - 3

        num += 1


print(find_consecutive_numbers())