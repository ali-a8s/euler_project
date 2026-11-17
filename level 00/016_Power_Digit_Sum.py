# What is the sum of the digits of the number 2**1000?

num = 2**1000

ls = [int(i) for i in str(num)]
print(sum(ls))