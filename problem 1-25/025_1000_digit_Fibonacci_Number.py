# What is the index of the first term in the Fibonacci sequence to contain 1000 digits

def first_fib_with_n_digits(n):
    a, b = 1, 1      
    index = 2

    while len(str(b)) < n:
        a, b = b, a + b
        index += 1

    return index, b

index, value = first_fib_with_n_digits(1000)

print(f"Index: {index}")
print(f"Digits: {len(str(value))}")
print(f"Value: {value}")