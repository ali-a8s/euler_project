# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc
# a < b < c ==> a**2 + b**2 = c**2

for a in range(1000):
    for b in range(1000):
        for c in range(1000):
            if (a < b < c) and (a + b + c == 1000) and (a**2 + b**2 == c**2):
                print(f"{a} * {b} * {c} = {a * b * c}")