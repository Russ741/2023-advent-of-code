def find_start():
    for i in range(len(lines)):
        s_pos = lines[i].find("S")
        if s_pos > -1:
            return (i, s_pos)

dirs = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0,  1)],
    ".": [],
    "S": [(-1, 0), (1, 0), (0, -1), (0, 1)],
}

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def char(coord):
    r, c = coord
    if r < 0 or r == len(lines) or c < 0 or c == len(lines[0]):
        return None
    return lines[r][c]

def get_next(prev, cur):
    cur_c = char(cur)
    for dir in dirs[cur_c]:
        next = add(cur, dir)
        if next == prev:
            continue
        next_c = char(next)
        if next_c is None:
            continue
        if next_c == "S":
            return next
        if next in coord_dists:
            # This check is basically redundant with the next == prev check
            continue
        for dir in dirs[next_c]:
            # This check is only really needed for the initial S square, but eh
            if add(next, dir) == cur:
                return next

with open("input.txt") as infile:
    lines = infile.read().splitlines()

start_r, start_c = find_start()
print(start_r, start_c)

coord_dists = {}

prev = (-1, -1)
next = (start_r, start_c)
dist = 0
while next not in coord_dists:
    coord_dists[next] = dist
    dist += 1
    prev, next = next, get_next(prev, next)
print(f"{next=} {dist=}")

print(dist / 2)