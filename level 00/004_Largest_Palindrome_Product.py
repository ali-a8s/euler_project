# Find the largest palindrome made from the product of two 3-digit numbers.

def is_pali(num):
    ls = [i for i in str(num)]
    ls_rev = list(reversed(ls))
    result = int(''.join(ls_rev))

    if num == result:
        return True
    return False

result = []
for i in range(100, 1000):
    for j in range(100, 1000):
        prod = i * j
        if is_pali(prod):
            print(f"{i} * {j} == {prod}")
            result.append(prod)

print(f"\nthe largest pali in the range is: {max(result)}")