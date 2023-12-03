digits = [str(i) for i in range(10)]
print(digits)

def is_symbol(c):
    return c != '.' and not c in digits

with open("input.txt") as infile:
    lines = infile.read().splitlines()
    rows = len(lines)
    cols = len(lines[0])

    sum = 0
    for r_i in range(rows):
        part_num = 0
        adj = False
        for c_i in range(cols):
            c = lines[r_i][c_i]
            cur_adj = is_symbol(c) or r_i > 1 and is_symbol(lines[r_i - 1][c_i]) or r_i < rows - 1 and is_symbol(lines[r_i + 1][c_i])
            adj = adj or cur_adj

            if c in digits:
                part_num = 10 * part_num + int(c)

            if c_i == cols - 1 or not c in digits:
                # End of number
                if adj:
                    sum += part_num
                part_num = 0
                adj = cur_adj
print(f"{sum=}")