from collections import defaultdict

def next_steps(r, c):
    result = []
    for diff in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + diff[0], c + diff[1]
        if nr >= 0 and nr < rows and nc >= 0 and nc < cols and lines[nr][nc] != '#':
            result.append((nr, nc))
    return result

def build_adj_list():
    adj_list = defaultdict(dict)
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == '#':
                continue
            adj_list[(r, c)] = {(nr, nc): 1 for nr, nc in next_steps(r, c)}
    return adj_list

# Optimize out nodes with only two edges
def compress_adj_list(adj_list):
    for r in range(rows):
        for c in range(cols):
            rc = (r, c)
            if rc not in adj_list:
                continue
            adj = list(adj_list[rc].items())
            if len(adj) == 2:
                rc0, d0 = adj[0]
                rc1, d1 = adj[1]
                d01 = d0 + d1
                del adj_list[rc0][rc]
                adj_list[rc0][rc1] = d01
                del adj_list[rc1][rc]
                adj_list[rc1][rc0] = d01
                del adj_list[rc]

def recurse(r, c):
    rc = (r, c)
    # print(rc)
    if rc == end:
        return 0
    visited.add(rc)

    max_dist = 0
    for nrc, dist in adj_list[rc].items():
        if nrc in visited:
            continue
        max_dist = max(max_dist, recurse(*nrc) + dist)
    visited.remove(rc)
    return max_dist

def print_adj_list_to_dotfile(adj_list):
    print("\n---\n")
    print("graph G {")
    visited = set()
    for src, adj in adj_list.items():
        visited.add(src)
        for dst, dist in adj.items():
            if dst not in visited:
                print(f"  r{src[0]}c{src[1]} -- r{dst[0]}c{dst[1]}")
    print("}")

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

adj_list = build_adj_list()

for r in range(rows):
    for c in range(cols):
        if lines[r][c] == '#':
            continue
        adj_list[(r, c)] = {(nr, nc): 1 for nr, nc in next_steps(r, c)}

print(f"{len(adj_list)=} before compression")

compress_adj_list(adj_list)

print(f"{len(adj_list)=} after compression")
print(adj_list)

print_adj_list_to_dotfile(adj_list)

visited = set()

print(recurse(*start))
