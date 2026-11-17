# For which value of  p <= 1000, is the number of solutions maximised?

from math import gcd

LIMIT = 1000
count = [0] * (LIMIT + 1)

m = 2
while 2 * m * (m + 1) <= LIMIT:
    for n in range(1, m):
        if (m - n) % 2 == 0:
            continue
        if gcd(m, n) != 1:
            continue
        p0 = 2 * m * (m + n)
        if p0 > LIMIT:
            break
        for k in range(1, LIMIT // p0 + 1):
            count[k * p0] += 1
    m += 1

best_p = 1
best_c = 0
for p in range(1, LIMIT + 1):
    if count[p] > best_c:
        best_c = count[p]
        best_p = p

print(f"p = {best_p}, number of answers= {best_c}")