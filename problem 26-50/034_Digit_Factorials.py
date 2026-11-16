# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

def factorial(num):
    result = 1

    if (num == 0) or (num == 1):
        result = 1
    else:
        for i in range(1, num + 1):
            result *= i
    return result

def is_curious_number(num):
    ls = [int(i) for i in str(num)]
    total = 0
    for digit in ls:
        total += factorial(digit)
    if total == num:
        return True
    return False

result = 0
for i in range(3, 3_000_000):
    if is_curious_number(i):
        result += i

print(result)