def move(right, down, dir, dist):
    if dir == 'U':
        return right, down - dist
    elif dir == 'D':
        return right, down + dist
    elif dir == 'L':
        return right - dist, down
    elif dir == 'R':
        return right + dist, down

def row_col(right, down):
    return down - min_down, right - min_right

def flood(row, col):
    if board[row][col] != '.':
        return 0
    to_flood = set()
    to_flood.add((row, col))
    result = 0
    while to_flood:
        r, c = to_flood.pop()
        if board[r][c] != '.':
            continue
        board[r][c] = '-'
        result += 1
        for n_r, n_c in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c+1)]:
            if n_r < 0 or n_r >= rows or n_c < 0 or n_c >= cols:
                continue
            to_flood.add((n_r, n_c))
    return result

with open("input.txt") as infile:
    lines = infile.read().splitlines()
    segments = [line.split() for line in lines]

dir_dists = [(segment[0], int(segment[1])) for segment in segments]

max_right = 0
min_right = 0
max_down = 0
min_down = 0

right = 0
down = 0

for dir, dist in dir_dists:
    right, down = move(right, down, dir, dist)
    max_right = max(max_right, right)
    min_right = min(min_right, right)
    max_down = max(max_down, down)
    min_down = min(min_down, down)

rows, cols = row_col(max_right + 1, max_down + 1)
start_row, start_col = row_col(0, 0)

board = [['.' for _ in range(cols)] for _ in range(rows)]

right = 0
down = 0
for dir, dist in dir_dists:
    for step in range(dist):
        right, down = move(right, down, dir, 1)
        row, col = row_col(right, down)
        board[row][col] = '#'

non_excavated = 0
for row in [0, rows - 1]:
    for col in range(0, cols):
        non_excavated += flood(row, col)
for col in [0, cols - 1]:
    for row in range(0, rows):
        non_excavated += flood(row, col)
excavated = rows * cols - non_excavated
print(excavated)