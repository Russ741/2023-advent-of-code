# z is distance from the ground. z=1 is on the ground.

import re
from pprint import pprint
from collections import defaultdict

bricks = []
with open("input.txt") as infile:
    lines = infile.read().splitlines()
    for line in lines:
        groups = re.match(r"(.+),(.+),(.+)~(.+),(.+),(.+)", line).groups()
        ints = [int(i) for i in groups]
        low = ints[0:3]
        high = ints[3:6]
        if low[2] > high[2]:
            low, high = high, low
        bricks.append((low, high))

bricks.sort(key = lambda lh: lh[0][2])

stack = defaultdict(dict)
spofs = defaultdict(set)

for num, brick in enumerate(bricks):
    lx, ly, lz = brick[0]
    hx, hy, hz = brick[1]

    tallest_sup = 0
    sup_nums = set()
    for x in range(lx, hx + 1):
        for y in range(ly, hy + 1):
            if x in stack and y in stack[x]:
                stack_z = stack[x][y][0]
                if stack_z > tallest_sup:
                    tallest_sup = stack_z
                    sup_nums.clear()
                if stack_z == tallest_sup:
                    stack_num = stack[x][y][1]
                    sup_nums.add(stack_num)

    spofs[num] = set()
    if len(sup_nums) == 1:
        single_support_num = sup_nums.pop()
        spofs[num].update(spofs[single_support_num])
        spofs[num].add(single_support_num)
    elif sup_nums:
        spofs[num].update(spofs[sup_nums.pop()])
        for sup in sup_nums:
            spofs[num] = spofs[num].intersection(spofs[sup])

    lower = lz - (tallest_sup + 1)
    lz -= lower
    hz -= lower
    brick[0][2] = lz
    brick[1][2] = hz

    for x in range(lx, hx + 1):
        for y in range(ly, hy + 1):
            stack[x][y] = (hz, num)

print(sum([len(spof) for spof in spofs.values()]))