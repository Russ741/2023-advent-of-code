import sys

sys.setrecursionlimit(5000)

from collections import defaultdict
from dataclasses import dataclass

ONE_WAYS = {
    (-1, 0): '^',
    (1, 0): 'v',
    (0, -1): '<',
    (0, 1): '>',
}

def next_steps(r, c):
    result = []
    for diff in ONE_WAYS.keys():
        nr, nc = r + diff[0], c + diff[1]
        if nr >= 0 and nr < rows and nc >= 0 and nc < cols and (lines[nr][nc] == '.' or lines[nr][nc] == ONE_WAYS[diff]) and not visited[nr][nc]:
            result.append((nr, nc))
    return result

def recurse(r, c):
    if (r, c) == end:
        return 0
    visited[r][c] = True
    max_dist = 0
    for nr, nc in next_steps(r, c):
        max_dist = max(max_dist, recurse(nr, nc))
    visited[r][c] = False
    return max_dist + 1

with open("input.txt") as infile:
    lines = infile.read().splitlines()

rows = len(lines)
cols = len(lines[0])

# Find the starting and ending points (they're in predictable locations, but not guaranteed by the problem statement)
for col in range(cols):
    if lines[0][col] == '.':
        start = (0, col)
    if lines[rows-1][col] == '.':
        end = (rows-1, col)

visited = [[False for _ in range(cols)] for _ in range(rows)]

print(recurse(*start))