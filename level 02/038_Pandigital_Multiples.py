# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, … , n) where n > 1?

for i in range(9999, 1, -1):
    s = ""
    m = 1
    while len(s) < 9:
        s += str(i*m)
        m += 1

    if (len(s) == 9) and (sorted(s) == list('123456789')):
        print(int(s))