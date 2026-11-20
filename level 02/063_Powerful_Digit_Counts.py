# How many n-digit positive integers exist which are also an n-th power?

count = 0

for i in range(1, 10):
    for j in range(1, 30):
        if len(str(i ** j)) == j:
            print(f"{i} ** {j} = {i ** j}")
            count += 1

print(f"\ncount = {count}")