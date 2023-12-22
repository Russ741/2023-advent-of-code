from sys import exit

STEPS = 131 * 30 + 65

with open("input.txt") as infile:
    rows = infile.read().splitlines()

row_ct = len(rows)
col_ct = len(rows[0])

def get_cell(r, c):
    nr = r % row_ct
    nc = c % col_ct
    return rows[nr][nc]

start_coords = None
for row in range(row_ct):
    for col in range(col_ct):
        if rows[row][col] == 'S':
            start_coords = (row, col)
            break
    if start_coords:
        break

prev = set()
cur = set([start_coords])
even = 1
odd = 0
for step in range(1, STEPS):
    next = set()
    for r, c in cur:
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if get_cell(nr, nc) == '#' or (nr, nc) in prev:
                continue
            next.add((nr, nc))
    if step % 2 == 0:
        even += len(next)
    else:
        odd += len(next)
    if step % 2 == 0 and step % 131 == 65:
        print(f"\t{step}\t{even}")
    prev = cur
    cur = next
print(f"{step=} {even=} {odd=}")