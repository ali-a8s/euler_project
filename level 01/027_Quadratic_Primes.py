def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# n**2 + a * n + b

# b must be prime 
b_ls = [i for i in range(1000) if is_prime(i)]

best_count = 0
best_a = 0
best_b = 0

for a in range(-999, 1000):
    for b in range(2, 1001):
        if not is_prime(b):
            continue

        n = 0

        while True:
            result = n**2 + a * n + b

            if not is_prime(result):
                break

            n += 1

        if n > best_count:
            best_count = n
            best_a = a
            best_b = b


print(best_a * best_b)