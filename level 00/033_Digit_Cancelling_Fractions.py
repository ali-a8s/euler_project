# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

from math import prod
from fractions import Fraction

fractions = []

for numerator in range(10, 100):
    for denominator in range(numerator + 1, 100):

        n = str(numerator)
        d = str(denominator)

        for digit in n:
            if digit in d and digit != "0":

                new_n = n.replace(digit, "", 1)
                new_d = d.replace(digit, "", 1)

                if not new_n or not new_d:
                    continue

                new_n = int(new_n)
                new_d = int(new_d)

                if numerator * new_d == denominator * new_n:
                    fractions.append(Fraction(numerator, denominator))

result = prod(fractions, start=Fraction(1, 1))

print("Fractions:", fractions)
print("Result:", result)
print("Denominator:", result.denominator)