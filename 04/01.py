import re

regexp = re.compile(r"Card +(\d+):(.*)\|(.*)$")
with open("input.txt") as infile:
    lines = infile.read().splitlines()

    sum = 0
    for line in lines:
        groups = re.match(regexp, line).groups()
        card_num = groups[0]
        winning_set = set(int(i) for i in groups[1].split())
        have_set = set(int(i) for i in groups[2].split())
        have_winners_set = winning_set.intersection(have_set)
        have_winners_ct = len(have_winners_set)
        if have_winners_ct > 0:
            sum += 2 ** (have_winners_ct - 1)
    print(f"{sum=}")