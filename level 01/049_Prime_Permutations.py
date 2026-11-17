# What 12-digit number do you form by concatenating the three terms in this sequence?


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def get_permutation_key(n):
    return ''.join(sorted(str(n)))


def find_sequences(numbers):
    numbers = sorted(numbers)
    sequences = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            a = numbers[i]
            b = numbers[j]

            c = 2 * b - a

            if c in numbers:
                sequences.append((a, b, c))

    return sequences


def solve():
    groups = {}

    for n in range(1000, 10000):
        if is_prime(n):
            key = get_permutation_key(n)

            if key not in groups:
                groups[key] = []

            groups[key].append(n)

    for numbers in groups.values():
        if len(numbers) >= 3:
            sequences = find_sequences(numbers)

            for sequence in sequences:
                print(sequence)
                print(''.join(map(str, sequence)))

solve()