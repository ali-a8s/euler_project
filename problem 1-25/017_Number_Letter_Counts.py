# If all the numbers from 1 to 1000 inclusive were written out in words, how many letters would be used?

def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "ten", "eleven", "twelve", "thirteen",
            "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty",
            "seventy", "eighty", "ninety"]

    if n == 1000:
        return "one thousand"
    if n >= 100:
        rest = n % 100
        s = ones[n // 100] + " hundred"
        if rest:
            s += " and " + number_to_words(rest)
        return s
    if n >= 20:
        rest = n % 10
        return tens[n // 10] + ("-" + ones[rest] if rest else "")
    return ones[n]

def letter_count(n):
    words = number_to_words(n)
    return sum(c.isalpha() for c in words)  

total = sum(letter_count(n) for n in range(1, 1001))
print(total)  