# What is the largest prime factor of the number 600851475143

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 2
    if n > 1:
        factors.append(n)
    return factors

print(prime_factors(600851475143)[-1])