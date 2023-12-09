with open("input.txt") as infile:
    lines = infile.read().splitlines()

def get_prev(nums):
    all_zeroes = True
    diffs = []
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i-1]
        if diff != 0:
            all_zeroes = False
        diffs.append(diff)
    result = nums[0]
    if not all_zeroes:
        result -= get_prev(diffs)
    return result

sum = 0
for line in lines:
    nums = [int(i) for i in line.split()]
    prev = get_prev(nums)
    sum += prev
    print(line)
    print(f"{prev=} {sum=}")
print(sum)