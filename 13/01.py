with open("input.txt") as infile:
    lines = infile.read().splitlines()

puzzles = [[]]
for line in lines:
    if not line:
        puzzles.append([])
    else:
        puzzles[-1].append(line)

def check_mirror_lt_row(puzzle, mirror_lt_row):
    max_idx = len(puzzle)
    max_dist = min(mirror_lt_row, max_idx - mirror_lt_row)
    for dist in range(max_dist):
        row_a = mirror_lt_row - dist - 1
        row_b = mirror_lt_row + dist
        for col in range(len(puzzle[0])):
            if puzzle[row_a][col] != puzzle[row_b][col]:
                return False
    return True

def check_mirror_lt_col(puzzle, mirror_lt_col):
    max_idx = len(puzzle[0])
    max_dist = min(mirror_lt_col, max_idx - mirror_lt_col)
    for dist in range(max_dist):
        col_a = mirror_lt_col - dist - 1
        col_b = mirror_lt_col + dist
        for row in range(len(puzzle)):
            if puzzle[row][col_a] != puzzle[row][col_b]:
                return False
    return True

def score_puzzle(puzzle):
    for mirror_lt_row in range(1, len(puzzle)):
        if check_mirror_lt_row(puzzle, mirror_lt_row):
            return 100 * mirror_lt_row
    for mirror_lt_col in range(1, len(puzzle[0])):
        if check_mirror_lt_col(puzzle, mirror_lt_col):
            return mirror_lt_col

score = 0
for puzzle in puzzles:
    score += score_puzzle(puzzle)
print(f"{score=}")
