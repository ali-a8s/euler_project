# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

numerator = 3
denominator = 2

count = 0

for _ in range(1000):
    if len(str(numerator)) > len(str(denominator)):
        count += 1

    numerator, denominator = (numerator + 2 * denominator,
                              numerator + denominator)

print(count)