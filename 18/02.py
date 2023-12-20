import re
from enum import IntEnum, global_enum

@global_enum
class Dir(IntEnum):
    R = 0,
    D = 1,
    L = 2,
    U = 3

def next(r, d, dist, dir):
    if dir == R:
        return r + dist, d
    elif dir == L:
        return r - dist, d
    elif dir == D:
        return r, d + dist
    elif dir == U:
        return r, d - dist

def row_col(right, down):
    return down - min_down, right - min_right

def add_rd_pair(r1, d1, r2, d2):
    if r1 == r2:
        right_to_ud_pairs.setdefault(r1, []).append((min(d1, d2), max(d1, d2)))
    else:
        down_to_lr_pairs.setdefault(d1, []).append((min(r1, r2), max(r1, r2)))

def dist_dirs_part1():
    with open("input.txt") as infile:
        lines = infile.read().splitlines()
        segments = [line.split() for line in lines]
        dist_dirs = [(int(segment[1]), Dir[segment[0]]) for segment in segments]
    return dist_dirs

def dist_dirs_part2():
    with open("input.txt") as infile:
        dist_dirs = []
        for line in infile.read().splitlines():
            match = re.match(r"^.*([0-9a-fA-F]{5})([0-3])\)$", line)
            dist = int(match.group(1), base=16)
            dir = Dir(int(match.group(2)))
            dist_dirs.append((dist, dir))
    return dist_dirs
dist_dirs = dist_dirs_part2()

min_right, max_right, min_down, max_down = 0, 0, 0, 0
right, down = 0, 0

right_to_ud_pairs = {}
down_to_lr_pairs = {}
for dist, dir in dist_dirs:
    nr, nd = next(right, down, dist, dir)
    add_rd_pair(right, down, nr, nd)
    min_right = min(min_right, nr)
    max_right = max(max_right, nr)
    min_down = min(min_down, nd)
    max_down = max(max_down, nd)
    right, down = nr, nd

# Add a blank row at the left and top so that no lines start at row or col 0
min_right -= 1
min_down -= 1

rows = max_right - min_right + 1
cols = max_down - min_down + 1

col_rr_pairs = {}
for right, ud_pairs in right_to_ud_pairs.items():
    col_rr_pairs[right - min_right] = [(u - min_down, d - min_down) for u, d in ud_pairs]
row_cc_pairs = {}
for down, cc_pairs in down_to_lr_pairs.items():
    row_cc_pairs[down - min_down] = [(l - min_right, r - min_right) for l, r in cc_pairs]

class Grid:
    # 2d grid
    board = []

    # from board col to coord
    row_idxes = []
    col_idxes = []

    FLOODED = '!'

    def initialize_grid(self, col_list, row_list):
        col_list = sorted(col_list)
        self.col_idxes.append(col_list[0] - 1)
        row_list = sorted(row_list)
        self.row_idxes.append(row_list[0] - 1)

        for list, idxes in [(col_list, self.col_idxes), (row_list, self.row_idxes)]:
            for col in list:
                if col != idxes[-1]:
                    idxes.append(col)
                idxes.append(col + 1)

        board = self.board
        col_ct = len(self.col_idxes)
        for _ in range(len(self.row_idxes)):
            board.append(['.'] * col_ct)

    def print_grid(self):
        print(self.col_idxes)
        for board_idx, first_row in enumerate(self.row_idxes):
            print(f"{first_row:8}: {self.board[board_idx]}")

    def add_horizontal_line(self, row, l_col, r_col):
        for board_row, first_row in enumerate(self.row_idxes):
            if first_row > row:
                board_row = self.board[board_row - 1]
                break
        for board_col, first_col in enumerate(self.col_idxes):
            if first_col > r_col:
                break
            if first_col >= l_col:
                board_row[board_col] = '#'

    def add_vertical_line(self, col, u_row, d_row):
        for board_col, first_col in enumerate(self.col_idxes):
            if first_col > col:
                board_col = board_col - 1
                break
        for board_row, first_row in enumerate(self.row_idxes):
            if first_row > d_row:
                break
            if first_row >= u_row:
                self.board[board_row][board_col] = '#'

    def flood_outside(self):
        to_explore = [(0, 0)]
        while to_explore:
            r, c = to_explore.pop()
            row_ct = len(self.row_idxes)
            col_ct = len(self.col_idxes)
            if self.board[r][c] != '.':
                continue
            self.board[r][c] = self.FLOODED
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if nr < 0 or nr >= row_ct or nc < 0 or nc >= col_ct:
                    continue
                if self.board[nr][nc] != '.':
                    continue
                to_explore.append((nr, nc))

    def get_non_flooded(self):
        area = 0
        for board_row, first_row in enumerate(self.row_idxes[:-1]):
            height = self.row_idxes[board_row + 1] - first_row
            for board_col, first_col in enumerate(self.col_idxes[:-1]):
                if self.board[board_row][board_col] == self.FLOODED:
                    continue
                width = self.col_idxes[board_col + 1] - first_col
                area += height * width
        return area

grid = Grid()
grid.initialize_grid(col_rr_pairs.keys(), row_cc_pairs.keys())
# grid.print_grid()
for row, cc_pairs in row_cc_pairs.items():
    for l_col, r_col in cc_pairs:
        grid.add_horizontal_line(row, l_col, r_col)
for col, rr_pairs in col_rr_pairs.items():
    for u_row, d_row in rr_pairs:
        grid.add_vertical_line(col, u_row, d_row)
# grid.print_grid()
grid.flood_outside()
# grid.print_grid()
print(grid.get_non_flooded())
