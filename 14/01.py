with open("input.txt") as infile:
    lines = infile.read().splitlines()

rows = len(lines)
cols = len(lines[0])

load = 0
for col in range(cols):
    col_load = 0
    empty_row = 0
    for row in range(rows):
        chr = lines[row][col]
        if chr == "#":
            empty_row = row + 1
        elif chr == "O":
            col_load += rows - empty_row
            empty_row += 1
        elif chr == ".":
            pass
    load += col_load
    print(f"{col=} {col_load=} {load=}")