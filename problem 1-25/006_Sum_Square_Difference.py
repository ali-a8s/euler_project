# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_the_square(num):
    ls = [i**2 for i in range(1, num + 1)]
    result = sum(ls)
    return result

def square_of_the_sum(num):
    ls = [i for i in range(1, num+1)]
    result = sum(ls) ** 2
    return result


print("for first ten")
print(f"{square_of_the_sum(10)} - {sum_of_the_square(10)} = {square_of_the_sum(10) - sum_of_the_square(10)}")

print("\nfor first hundred") 
print(f"{square_of_the_sum(100)} - {sum_of_the_square(100)} = {square_of_the_sum(100) - sum_of_the_square(100)}")
