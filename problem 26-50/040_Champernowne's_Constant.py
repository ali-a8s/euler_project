# Champernowne's Constant

d = [1, 10, 100, 1_000, 10_000, 100_000]
result = 1

number = ''.join(str(i) for i in range(1, 1_000_000))

for i in d:
    print(f"d{d.index(i) + 1} ({i}) is {number[i - 1]}")
    result *= int(number[i - 1])

print(f'result is {result}')