import time
from dataclasses import dataclass
from enum import Enum, auto, global_enum
from heapq import heappush, heappop

start_time = time.time()

@global_enum
class Dir(Enum):
    U = auto()
    D = auto()
    L = auto()
    R = auto()

@dataclass(frozen=True)
class Node:
    r: int
    c: int
    d: Dir

    def __lt__(a, b):
        return a.r < b.r or a.r == b.r and a.c < b.c

def inbounds(node):
    return node.r >= 0 and node.r < rows and node.c >= 0 and node.c < cols

def explore(cur):
    cost = node_costs[cur]
    if cur.d == U or cur.d == D:
        dirs = [L, R]
    else:
        dirs = [U, D]

    result = set()
    for dir in dirs:
        next_cost = cost
        for dist in range(1, 11):
            r = cur.r
            c = cur.c
            match Dir(dir):
                case Dir.U: r -= dist
                case Dir.D: r += dist
                case Dir.L: c -= dist
                case Dir.R: c += dist
            next = Node(r, c, dir)
            if not inbounds(next):
                break
            next_cost += board[next.r][next.c] # accumulate costs along the way
            if dist < 4:
                continue
            if next in node_costs and node_costs[next] <= next_cost:
                continue
            node_costs[next] = next_cost
            result.add((next_cost, next))
    return result

with open("input.txt") as infile:
    lines = infile.read().splitlines()

board = [ [int(c) for c in line] for line in lines]

rows = len(board)
cols = len(board[0])

node_costs = {
    Node(0, 0, R) : 0,
    Node(0, 0, D) : 0,
}

to_explore = []
heappush(to_explore, (0, Node(0, 0, R)))
heappush(to_explore, (0, Node(0, 0, D)))

while to_explore:
    node = heappop(to_explore)[1]
    next_to_explore = explore(node)
    for next in next_to_explore:
        heappush(to_explore, next)

print(f"Runtime: {time.time() - start_time} seconds.")

print(min(node_costs[Node(rows - 1, cols - 1, R)],
          node_costs[Node(rows - 1, cols - 1, D)]))
