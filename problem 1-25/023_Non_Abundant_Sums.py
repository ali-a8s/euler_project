# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

n = 28124

def is_abundant(num):
    if num < 12:
        return False
    s = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            s += i
            if i != num // i:
                s += num // i
        i += 1
    return s > num

abundants = [i for i in range(1, n) if is_abundant(i)]

all_adds = set()
for i in abundants:
    for j in abundants:
        s = i + j
        if s >= n:
            break
        all_adds.add(s)

total = 0
for i in range(1, n):
    if i not in all_adds:
        total += i

print(total)