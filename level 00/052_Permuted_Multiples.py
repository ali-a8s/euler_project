# https://projecteuler.net/problem=52

def same_digits(a, b):
    return sorted(str(a)) == sorted(str(b))

n = 1

while True:
    if all(same_digits(n, n * i) for i in range(2, 7)):
        print(n)
        break

    n += 1