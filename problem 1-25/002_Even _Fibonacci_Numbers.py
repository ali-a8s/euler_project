# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

import itertools

def fibonacci(n) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fib_sum = 0
for i in itertools.count():
    fib_i = fibonacci(i)
    if fib_i % 2 == 0:
        fib_sum += fib_i
    if fib_i > 4_000_000:
        break

print(fib_sum)