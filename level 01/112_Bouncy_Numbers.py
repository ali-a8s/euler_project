# Find the least number for which the proportion of bouncy numbers is exactly 99%

def is_bouncy(n):
    digits = str(n)

    increasing = False
    decreasing = False

    for i in range(len(digits) - 1):
        if digits[i] < digits[i + 1]:
            increasing = True

        elif digits[i] > digits[i + 1]:
            decreasing = True

        if increasing and decreasing:
            return True

    return False


bouncy_count = 0
n = 1

while True:
    if is_bouncy(n):
        bouncy_count += 1

    if 100 * bouncy_count == 99 * n:
        print(n)
        break

    n += 1