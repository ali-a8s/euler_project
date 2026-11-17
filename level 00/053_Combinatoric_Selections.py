# https://projecteuler.net/problem=53

def factorial(n):
    result = 1

    if n in [0, 1]:
        return 1
    else:
        for i in range(1, n + 1):
            result *= i

        return result

def comb_formule(n, r):
    return (factorial(n) / (factorial(r) * factorial(n - r)))

result = 0

for n in range(1, 101):
    for r in range(1, n):
        if comb_formule(n, r) > 1_000_000:
            result += 1

print(result)