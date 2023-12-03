from collections import defaultdict


digits = [str(i) for i in range(10)]
print(digits)

lines = []
rows = 0
cols = 0

def get_asts(r, c):
    result = []
    for r_n in (r - 1, r, r + 1):
        if r_n < 0 or r_n == rows:
            continue
        if lines[r_n][c] == '*':
            result.append((r_n, c))
    return result

with open("input.txt") as infile:
    lines = infile.read().splitlines()
    rows = len(lines)
    cols = len(lines[0])

    asts_to_part_nums = defaultdict(list)
    for r_i in range(rows):
        part_num = 0
        adj_asts = []
        for c_i in range(cols):
            c = lines[r_i][c_i]
            cur_adj_asts = get_asts(r_i, c_i)
            adj_asts.extend(cur_adj_asts)

            if c in digits:
                part_num = 10 * part_num + int(c)

            if c_i == cols - 1 or not c in digits:
                # End of number
                if part_num > 0:
                    for ast in adj_asts:
                        asts_to_part_nums[ast].append(part_num)
                part_num = 0
                adj_asts = cur_adj_asts

    sum = 0
    print(asts_to_part_nums)
    for part_nums in asts_to_part_nums.values():
        if len(part_nums) == 2:
            sum += part_nums[0] * part_nums[1]
print(f"{sum=}")