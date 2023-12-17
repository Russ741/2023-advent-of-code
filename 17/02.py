from dataclasses import dataclass
from enum import Enum, auto

class Dir(Enum):
    U = auto()
    D = auto()
    L = auto()
    R = auto()

U = Dir.U
D = Dir.D
L = Dir.L
R = Dir.R

@dataclass(frozen=True)
class Node:
    r: int
    c: int
    d: Dir

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
            result.add(next)
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

to_explore = set([
    Node(0, 0, R),
    Node(0, 0, D),
])

while to_explore:
    node = to_explore.pop()
    next_to_explore = explore(node)
    to_explore |= next_to_explore

print(min(node_costs[Node(rows - 1, cols - 1, R)],
          node_costs[Node(rows - 1, cols - 1, D)]))