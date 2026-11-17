# Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?

import math

path = r"C:\Users\LOQ\Code\euler\data\0042_words.txt"

letter_values = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
    'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
    'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
    'Z': 26
}

def calculate_word(word):
    total = 0

    for ch in word:
        total += letter_values[ch]

    return total

def is_triangle_number(x):
    n = (math.sqrt(1 + 8 * x) - 1) / 2
    return n.is_integer()

with open(path, 'r', encoding='utf-8') as f:
    words = f.read().replace('"', '').split(',')

words_count = {}

for word in words:
    words_count[word] = calculate_word(word)

result = []
for key, value in words_count.items():
    if is_triangle_number(value):
        result.append(key)


print(len(result))
print("\n")
print(result)