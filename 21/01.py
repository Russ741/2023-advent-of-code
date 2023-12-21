with open("input.txt") as infile:
    rows = infile.read().splitlines()

row_ct = len(rows)
col_ct = len(rows[0])

start_coords = None
for row in range(row_ct):
    for col in range(col_ct):
        if rows[row][col] == 'S':
            start_coords = (row, col)
            break
    if start_coords:
        break

reachable_by_step = []
reachable_by_step.append(set([start_coords]))
print(reachable_by_step)
for step in range(1, 65):
    reachable_by_step.append(set())
    reachable = reachable_by_step[step]
    last_reachable = reachable_by_step[step - 1]
    for lr, lc in last_reachable:
        for r, c in [(lr-1, lc), (lr+1, lc), (lr, lc-1), (lr, lc+1)]:
            if r < 0 or r >= row_ct or c < 0 or c >= col_ct:
                continue
            if rows[r][c] == '#':
                continue
            reachable.add((r, c))
    print(step, len(reachable))
