from pprint import pprint

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

def mul(a, x):
    return (a[0] * x, a[1] * x)

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

def add_pixel(coord, offset):
    zoom_coord = mul(coord, 3)
    zoom_coord = add(zoom_coord, (1, 1))
    zoom_coord = add(zoom_coord, offset)
    zoom_grid[zoom_coord[0]][zoom_coord[1]] = '+'

def add_to_zoom(cur):
    add_pixel(cur, (0, 0))
    cur_c = char(cur)
    if cur_c == 'S':
        return
    for dir in dirs[cur_c]:
        add_pixel(cur, dir)
        next = add(cur, dir)
        next_c = char(next)
        if next_c == 'S':
            add_pixel(cur, mul(dir, 2))

def zoom_inbounds(z_r, z_c):
    if z_r < 0 or z_r == zoom_rows or z_c < 0 or z_c == zoom_cols:
        return False
    return True

def flood(zoom_coord):
    r,c = zoom_coord
    if zoom_grid[r][c] != '.':
        return
    to_flood = set([zoom_coord])
    while to_flood:
        next_to_flood = set()
        for flood_coord in to_flood:
            r, c = flood_coord
            zoom_grid[r][c] = 'O'
            for next in [(r-1, c), (r, c-1), (r, c+1), (r+1, c)]:
                if not zoom_inbounds(*next):
                    continue
                if zoom_grid[next[0]][next[1]] != '.':
                    continue
                next_to_flood.add(next)
        to_flood = next_to_flood

def print_zoom_grid():
    for row in zoom_grid:
        for cell in row:
            print(cell, end = "")
        print()
    print()

def is_inside(row, col):
    z_r_min = 3 * row - 1
    z_r_max = 3 * row + 2
    z_c_min = 3 * col - 1
    z_c_max = 3 * col + 2
    for z_row in range(z_r_min, z_r_max):
        for z_col in range(z_c_min, z_c_max):
            if zoom_grid[z_row][z_col] != '.':
                return False
    return True

with open("input.txt") as infile:
    lines = infile.read().splitlines()

rows = len(lines)
cols = len(lines[0])

start_r, start_c = find_start()
print(start_r, start_c)

coord_dists = {}
zoom_rows = 3 * rows
zoom_cols = 3 * cols
zoom_grid = [ ["." for i in range(zoom_cols)] for j in range(zoom_rows) ]

prev = (-1, -1)
next = (start_r, start_c)
dist = 0
while next not in coord_dists:
    coord_dists[next] = dist
    add_to_zoom(next)
    dist += 1
    prev, next = next, get_next(prev, next)

print_zoom_grid()

import sys
sys.setrecursionlimit(10000)

for r in range(zoom_rows):
    flood((r, 0))
    flood((r, zoom_cols - 1))

for c in range(zoom_cols):
    flood((0, c))
    flood((zoom_rows - 1, c))

print_zoom_grid()

inside_cells = 0
for row in range(rows):
    for col in range(cols):
        inside_cells += is_inside(row, col)
print(f"{inside_cells=}")