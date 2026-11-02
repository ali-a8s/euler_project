# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc
# a < b < c ==> a**2 + b**2 = c**2

def find_pythagorean_triplet(target_sum=1000):
    for a in range(1, target_sum // 3):
        for b in range(a + 1, target_sum // 2):
            c = target_sum - a - b
            if a * a + b * b == c * c:
                return a * b * c

print(find_pythagorean_triplet())