# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

limit=4_000_000
a, b = 1, 2
total = 0
while a <= limit:
    if a % 2 == 0:
        total += a
    a, b = b, a + b
print(total)