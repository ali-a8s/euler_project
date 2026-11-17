# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from itertools import permutations

perms = permutations("0123456789")

target = 999_999 
result = next(p for i, p in enumerate(perms) if i == target)

print("".join(result))