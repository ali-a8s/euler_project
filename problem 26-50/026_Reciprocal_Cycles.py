# Find the value of  d < 1000 for which 1/d  contains the longest recurring cycle in its decimal fraction part.

LIMIT = 1000

best_d = 0
best_len = 0

for d in range(2, LIMIT):
    first_seen = [-1] * d
    rem = 1
    step = 0

    while rem != 0 and first_seen[rem] == -1:
        first_seen[rem] = step
        rem = (rem * 10) % d
        step += 1

    if rem == 0:
        cycle_len = 0
    else:
        cycle_len = step - first_seen[rem]   

    if cycle_len > best_len:
        best_len = cycle_len
        best_d = d

print(f"d = {best_d}, len= {best_len}")