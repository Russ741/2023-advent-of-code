import re

with open("input.txt") as infile:
    lines = infile.read().splitlines()
    steps = lines[0].split(',')

def hash(step):
    result = 0
    for c in step:
        result += ord(c)
        result *= 17
        result %= 256
    return result

result = 0
for step in steps:
    result += hash(step)
print(result)