# Find the sum of the digits in the number 100!

def factorial(num):
    result = 1

    if (num == 0) or (num == 1):
        result = 1
    else:
        for i in range(1, num + 1):
            result *= i
    return result

number = factorial(100)
ls = [int(i) for i in str(number)]
print(sum(ls))
