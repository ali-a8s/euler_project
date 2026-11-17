# Find the last ten digits of the series, 1**1 + ... + 1000**1000

ls = [i for i in range(1, 1001)]

result = 0
for i in ls:
    result += i**i

last_10 = result % 10**10

print(last_10)