# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2

def is_pali(num):
    ls = [i for i in str(num)]
    ls_rev = list(reversed(ls))
    result = ''.join(ls_rev)

    if str(num) == result:
        return True
    return False

pali_10 = []
for i in range(1, 1_000_000):
    if is_pali(i):
        pali_10.append(i)

total = 0
result = {}
for i in pali_10:
    base_2 = bin(i)[2:]
    if is_pali(base_2):
        result[i] = base_2
        total += i

print(f"sum of the numbers is: {total}\n")
for key, value in result.items():
    print(f"{key} = {value}")