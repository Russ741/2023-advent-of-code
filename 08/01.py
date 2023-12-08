import re
from pprint import pprint

pairs = {}
with open("input.txt") as infile:
    lines = infile.read().splitlines()
    lr = lines[0]
    lines = lines[2:]
    for line in lines:
        match = re.match("^(.*) = \((.*), (.*)\)$", line)
        groups = match.groups()
        pairs[groups[0]] = (groups[1], groups[2])

pprint(pairs)

location = "AAA"
steps = 0
while location != "ZZZ":
    lr_i = lr[steps % len(lr)]
    location = pairs[location][0 if lr_i == "L" else 1]
    steps += 1
print(f"{steps=}")