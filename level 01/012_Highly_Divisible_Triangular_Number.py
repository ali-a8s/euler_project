# What is the value of the first triangle number to have over five hundred divisors?

import math

def count_divisors(n):
    count = 0
    root = int(math.isqrt(n))
    for i in range(1, root + 1):
        if n % i == 0:
            if i == n // i:   
                count += 1
            else:
                count += 2    
    return count

def triangle_num(num):
    return num * (num + 1) // 2

num = 1
while True:
    res = count_divisors(triangle_num(num))
    if res > 500:
        print(triangle_num(num))
        break
    else:
        num += 1