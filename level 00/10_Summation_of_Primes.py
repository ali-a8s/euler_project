# Find the sum of all the primes below two million.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("primes below? "))
primes = [i for i in range(n) if is_prime(i)]

print(f"the sum of the primes below {n} is {sum(primes)}")