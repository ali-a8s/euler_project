# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

def factorial(num):
    result = 1

    if (num == 0) or (num == 1):
        result = 1
    else:
        for i in range(1, num + 1):
            result *= i
    return result

def digit_factorial_sum(n):
    n_str = str(n)
    ls = [int(n_str[i]) for i in range(len(n_str))]

    result = 0
    for digit in ls:
        result += factorial(digit)

    return result

def chain_length(n):
    seen = set()

    while n not in seen:
        seen.add(n)
        n = digit_factorial_sum(n)

    return len(seen)

count = 0

for i in range(1, 1_000_000):
    if chain_length(i) == 60:
        count += 1

print(count)