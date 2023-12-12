def get_empty_rows():
    empty_rows = []
    for row in range(row_ct):
        if orig[row] == '.' * col_ct:
            empty_rows.append(row)
    return empty_rows

def get_empty_cols():
    empty_cols = []
    for col in range(col_ct):
        empty = True
        for row in range(row_ct):
            if orig[row][col] != '.':
                empty = False
                break
        if empty:
            empty_cols.append(col)
    return empty_cols

def get_map(count, empties):
    ADD_PER_EMPTY = 10**6 - 1
    empty_count = 0
    result = []
    for i in range(count):
        if i in empties:
            empty_count += 1
        result.append(i + ADD_PER_EMPTY * empty_count)
    return result

def get_galaxy_coords():
    coords = []
    for row in range(row_ct):
        for col in range(col_ct):
            if orig[row][col] == '#':
                coords.append((row_map[row], col_map[col]))
    return coords

with open("input.txt") as lines:
    orig = lines.read().splitlines()

row_ct = len(orig)
col_ct = len(orig[0])

row_map = get_map(row_ct, get_empty_rows())
col_map = get_map(col_ct, get_empty_cols())

coords = get_galaxy_coords()

sum_dists = 0
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        dr = abs(coords[j][0] - coords[i][0])
        dc = abs(coords[j][1] - coords[i][1])
        sum_dists += dr + dc
print(sum_dists)