# Which starting number, under one million, produces the longest chain?
# n is even --> n/2
# n is odd  --> 3n + 1

def collatz_length(num):
    count = 1
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        count += 1
    return count

max_length = 0
best_run = 0

for i in range(1, 1_000_000):
    length = collatz_length(i)
    if length > max_length:
        max_length = length
        best_run = i

print(f"starting number: {best_run}\nlength: {max_length}")