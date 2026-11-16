# Find the sum of 0 all 9 to  pandigital numbers with this property.

from itertools import permutations

def find_pandigital_numbers():
    divisors = [2, 3, 5, 7, 11, 13, 17]
    results = []

    for digits in permutations('0123456789'):
        if digits[0] == '0':
            continue

        number = ''.join(digits)

        valid = True

        for i, divisor in enumerate(divisors):
            sub_number = int(number[i + 1:i + 4])

            if sub_number % divisor != 0:
                valid = False
                break

        if valid:
            results.append(int(number))

    return results, sum(results)


numbers, total = find_pandigital_numbers()

print("Valid numbers:", numbers)
print("Sum:", total) 