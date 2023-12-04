import re

regexp = re.compile(r"Card +(\d+):(.*)\|(.*)$")
with open("input.txt") as infile:
    lines = infile.read().splitlines()

    card_counts = [1] * len(lines)
    for line in lines:
        groups = re.match(regexp, line).groups()
        card_num = int(groups[0])
        winning_set = set(int(i) for i in groups[1].split())
        have_set = set(int(i) for i in groups[2].split())
        have_winners_set = winning_set.intersection(have_set)
        have_winners_ct = len(have_winners_set)
        for won_card in range(card_num, card_num + have_winners_ct):
            # card_counts is zero-indexed
            card_counts[won_card] += card_counts[card_num - 1]
    print(f"sum={sum(card_counts)}")