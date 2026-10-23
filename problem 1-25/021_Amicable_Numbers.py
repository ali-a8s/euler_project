# Evaluate the sum of all the amicable numbers under 10000

def d(n):
    total = 1                      
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:       
                total += n // i
    return total

result = set()
for a in range(2, 10000):
    b = d(a)
    if b != a and d(b) == a:
        result.add(a)
        result.add(b)     

print(len(result))      
print(sorted(result))
print(sum(result))      