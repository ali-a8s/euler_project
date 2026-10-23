# What is the total of all the name scores in the file?
import string

path = r"C:\Users\LOQ\Code\euler\data\0022_names.txt"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

names = [n.strip('"') for n in content.split(",")]
names.sort()

alpahebt = list(string.ascii_uppercase)

def name_worth(name):
    count = 0
    for chr in name:
        count += alpahebt.index(chr) + 1
    return count

scores = []
for name in names:
    score = name_worth(name) * (names.index(name) + 1)
    scores.append(score)

print(sum(scores))