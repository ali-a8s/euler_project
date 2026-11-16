# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def sum_of_pow(num, p):
    ls = [int(i) for i in str(num)]
    ls_pow = list(map(lambda x:x**p, ls))
    return sum(ls_pow)

result = []
for i in range(1000, 1_000_000):
    sop = sum_of_pow(i, 5)
    if sop == i:
        result.append(i)

print(sum(result))
print(result)