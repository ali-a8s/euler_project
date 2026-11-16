# What is the sum of the numbers on the diagonals in a 1001 by 1001  spiral formed in the same way?

total = 1

for n in range(3, 1002, 2):
    total += 4 * n**2 - 6 * (n - 1)

print(total)
