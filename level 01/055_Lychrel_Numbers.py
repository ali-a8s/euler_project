# How many Lychrel numbers are there below ten-thousand?

def reverse_number(n):
    return int(str(n)[::-1])

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_lychrel(n):
    for _ in range(50):
        n += reverse_number(n)

        if is_palindrome(n):
            return False
    return True

count = 0

for i in range(1, 10_000):
    if is_lychrel(i):
        count += 1

print(count)