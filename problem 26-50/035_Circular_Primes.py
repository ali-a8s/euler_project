# How many circular primes are there below one million?

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def rotations(n):
    s = str(n)
    return [int(s[i:] + s[:i]) for i in range(len(s))]


def is_circular_prime(n):
    return all(is_prime(r) for r in rotations(n))

count = sum(1 for i in range(2, 1_000_000) if is_circular_prime(i))
print(count)  # 55