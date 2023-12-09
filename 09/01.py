with open("input.txt") as infile:
    lines = infile.read().splitlines()

def get_next(nums):
    all_zeroes = True
    diffs = []
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i-1]
        if diff != 0:
            all_zeroes = False
        diffs.append(diff)
    result = nums[-1]
    if not all_zeroes:
        result += get_next(diffs)
    return result

sum = 0
for line in lines:
    nums = [int(i) for i in line.split()]
    next = get_next(nums)
    sum += next
    # print(line)
    # print(f"{next=} {sum=}")
print(sum)