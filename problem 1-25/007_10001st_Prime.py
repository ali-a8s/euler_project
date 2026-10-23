# 10 001st Prime number 


def nst_prime(num):
    x = 2
    ls = []
    while len(ls) < num:
        is_prime = True
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            ls.append(x)
        x += 1

    return max(ls)

print(f"6st prime number is: {nst_prime(6)}")
print(f"10001st prime number is: {nst_prime(10001)}")