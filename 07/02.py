from collections import defaultdict

hand_map = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 1,
    'T': 10,
}
hand_map.update({str(i):i for i in range(9, 1, -1)})
print(hand_map)

def hand_key(hand_and_bid):
    hand = hand_and_bid[0]
    key = 0
    counts = defaultdict(int)
    for card in hand:
        key = key * 100 + hand_map[card]
        counts[card] += 1
    jokers = counts['J']
    counts['J'] = 0
    sorted_counts = sorted(counts.values())
    sorted_counts.reverse()
    hand_value = (sorted_counts[0] + jokers) * 10
    if len(sorted_counts) > 1:
        hand_value += sorted_counts[1]
    key += 10 ** 10 * hand_value
    return key

hands_and_bids = []
with open("input.txt") as infile:
    for line in infile.read().splitlines():
        hand, bid = line.split()
        hands_and_bids.append((hand, int(bid)))
hands_and_bids.sort(key=hand_key)

winnings = 0
for i in range(len(hands_and_bids)):
    hand_winnings = hands_and_bids[i][1] * (i + 1)
    winnings += hand_winnings
    print(f"{i+1} ({hands_and_bids[i][0]}): {hands_and_bids} -> {hand_winnings}")
print(f"{winnings=}")