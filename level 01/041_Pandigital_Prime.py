# What is the largest n-digit pandigital prime that exists?

from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def largest_pandigital_prime():
    for n in [7, 4]:
        digits = ''.join(str(d) for d in range(n, 0, -1))  
        for p in permutations(digits):
            num = int(''.join(p))
            if is_prime(num):
                return num
    return None

print(largest_pandigital_prime())