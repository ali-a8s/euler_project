# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

n=20
result = 1
for i in range(1, n + 1):
    result = result * i // math.gcd(result, i)
print(result)