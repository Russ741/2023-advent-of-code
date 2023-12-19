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
    # mapping
    #  from first row number
    #  to a mapping
    #   from first column number
    #    to "trench/not trench"
    rows = {}

    def initialize_grid(self, col_list, row_list):
        col_list = sorted(col_list)
        cells = {}
        cells[col_list[0] - 1] = '.'
        for col in col_list:
            cells[col] = '.'
            cells[col + 1] = '.'
        row_list = sorted(row_list)

        rows = self.rows
        rows[row_list[0] - 1] = cells.copy()
        for row in row_list:
            rows[row] = cells.copy()
            rows[row + 1] = cells.copy()

    def print_grid(self):
        print(self.rows[0].keys())
        # for row_start, row in self.rows.items():
        #     print(f"{row_start}: {row.values()}")

    def add_horizontal_line(self, row, l_col, r_col):
        cells = self.rows[row]
        for col in cells.keys():
            if col >= l_col and col <= r_col:
                cells[col] = '#'

    def add_vertical_line(self, col, u_row, d_row):
        for row, cells in self.rows.items():
            if row >= u_row and row <= d_row:
                cells[col] = '#'

grid = Grid()
grid.initialize_grid(col_rr_pairs.keys(), row_cc_pairs.keys())
for row, cc_pairs in row_cc_pairs.items():
    for l_col, r_col in cc_pairs:
        grid.add_horizontal_line(row, l_col, r_col)
for col, rr_pairs in col_rr_pairs.items():
    for u_row, d_row in rr_pairs:
        grid.add_vertical_line(col, u_row, d_row)
grid.print_grid()







# row, col = row_col(0, 0)
# col_to_bounds = {}

# for row, cc_pairs in row_cc_pairs.items():
#     for min_col, max_col in cc_pairs:
#         col_to_bounds.setdefault(min_col, []).append(row)
#         col_to_bounds.setdefault(max_col, []).append(-row)

# col_to_bounds = {col: sorted(col_to_bounds[col]) for col in sorted(col_to_bounds.keys())}

# area = 0
# rows = set()
# last_col = 0
# height = 0
# removed_rows = set()
# for col in col_to_bounds.keys():
#     # Complete all the rectangles before this column
#     width = col - last_col - 1
#     rect_area = height * width
#     area += rect_area
#     print(f"col {last_col} to {col-1} ({width}): {height=} {rect_area=} -> {area}")

#     # Add new rows
#     added_rows = [row for row in col_to_bounds[col] if row > 0]
#     print(f"col {col}: {added_rows=}")
#     rows.update(added_rows)

#     # Calculate height at this column
#     height = 0
#     last_row = 0
#     counting = False
#     row_list = sorted(rows):
#     for idx, row in enumerate(row_list):
#         if counting:
#             height += row - last_row + 1
#             if row not in
#             counting = False
#         else:
#             counting = True
#         last_row = row
#     area += height
#     print(f"col {col}: added {height=} -> {area}")

#     # Remove rows
#     removed_rows = [-row for row in col_to_bounds[col] if row < 0]
#     print(f"col {col}: {removed_rows=}")
#     rows.difference_update(removed_rows)

#     last_col = col

# print(area)

# # last_col = None
# # cur_line_rows = set()

# # area = 0

# # for col in col_to_bounds.keys():
# #     print(f"{col} {col_rr_pairs[col]}")
# #     if last_col:
# #         prev_rows = sorted(cur_line_rows)
# #         width = col - last_col
# #         for top, bottom in zip(prev_rows[0::2], prev_rows[1::2]):
# #             height = bottom - top + 1
# #             rect_area = width * height
# #             print(f"Adding {rect_area=} ({width} x {height}) to {area}")
# #             area += rect_area

# #     starting_line_rows = [row for row in col_to_bounds[col] if row > 0]
# #     starting_rows = set(starting_line_rows)

# #     for top, bottom in col_rr_pairs[col]:
# #         if top in starting_line_rows or bottom in starting_line_rows:
# #             print(f"Adding linearea {bottom-top} ({bottom} - {top}) to {area}")
# #             area += bottom - top
# #         if top in starting_line_rows and bottom in starting_line_rows:
# #             print(f"Adding pixel to {area}")
# #             area += 1

# #     cur_line_rows.update(starting_line_rows)
# #     ending_line_rows = [-row for row in col_to_bounds[col] if row < 0]
# #     cur_line_rows.difference_update(ending_line_rows)

# #     last_col = col
# # print(area)