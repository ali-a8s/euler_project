# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

def is_pandigital(num):
    ls = [i for i in range(1, 10)]
    num_ls = sorted(int(i) for i in num)
    if num_ls == ls:
        return True
    return False

# a len = 1 / b len = 4 / c len = 4
# a len = 2 / b len = 3 / c len = 4

result = set()

for a in range(1, 10):
    for b in range(1000, 10000):
        c = a * b
        if len(str(c)) == 4:
            num = str(a) + str(b) + str(c)
            if is_pandigital(num):
                result.add(c)

for a in range(10, 100):
    for b in range(100, 1000):
        c = a * b
        if len(str(c)) == 4:
            num = str(a) + str(b) + str(c)
            if is_pandigital(num):
                result.add(c)

print(sum(result))