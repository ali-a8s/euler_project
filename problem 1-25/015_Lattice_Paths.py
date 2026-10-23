def factorial(num):
    result = 1

    if (num == 0) or (num == 1):
        result = 1
    else:
        for i in range(1, num + 1):
            result *= i
    return result


n = 20

res = factorial(2 * n) / (factorial(n) * factorial(n))

print(res)