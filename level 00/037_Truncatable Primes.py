# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def is_truncatable(num):
    if (num < 10) or (not is_prime(num)):
        return False

    num = str(num)
    for i in range(1, len(num)):
        left = int(num[i:])
        right = int(num[:-i])
        if (not is_prime(left)) or (not is_prime(right)):
            return False
    return True

result = []
n = 10
while True:
    if len(result) == 11:
        break

    n += 1

    if is_truncatable(n):
        result.append(n)

print(result)
print(sum(result))