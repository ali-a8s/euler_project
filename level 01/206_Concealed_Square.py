# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,

import math

minimum = math.isqrt(1020304050607080900)
maximum = math.isqrt(1929394959697989990)

start = minimum + (10 - minimum % 10) % 10

for n in range(start, maximum + 1, 10):
    square = n * n

    value = square // 100
    valid = True

    for expected in range(9, 0, -1):
        if value % 10 != expected:
            valid = False
            break

        value //= 100

    if valid and value == 0:
        print(n)
        break