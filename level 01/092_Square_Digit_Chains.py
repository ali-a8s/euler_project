# https://projecteuler.net/problem=92

def digit_square_sum(n):
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** 2
        n //= 10

    return total


results = {}

for n in range(1, 568):
    current = n

    while current != 1 and current != 89:
        current = digit_square_sum(current)

    results[n] = current


count = 0

for n in range(1, 10_000_000):
    if results[digit_square_sum(n)] == 89:
        count += 1

print(count)