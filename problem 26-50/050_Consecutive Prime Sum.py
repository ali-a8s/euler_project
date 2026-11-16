# Which prime, below one-million, can be written as the sum of the most consecutive primes?

def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

limit = 1_000_000
primes = [i for i in range(limit) if is_prime(i)]

best_prime = None
best_length = 0

for start in range(len(primes)):
    total = 0
    for end in range(start, len(primes)):
        total += primes[end]

        if total >= limit:
            break

        length = end - start + 1

        if is_prime(total) and length > best_length:
            best_length = length
            best_prime = total

print(best_prime, best_length)