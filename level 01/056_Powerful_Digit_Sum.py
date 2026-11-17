# Considering natural numbers of the form, a**b , where a,b < 100 , what is the maximum digital sum?

def sum_of_digits(num):
    num_str = str(num)
    ls = [int(num_str[i]) for i in range(len(num_str))]
    return sum(ls)

max_number = -1
for a in range(1, 100):
    for b in range(1, 100):
        result = sum_of_digits(a**b)
        if result > max_number:
            max_number = result

print(max_number)