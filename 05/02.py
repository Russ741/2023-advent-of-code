from collections import defaultdict
from pprint import pprint

lines = None
with open("input.txt") as infile:
    lines = infile.read().splitlines()

# Return [unmapped], [mapped]
def apply_mapping_to_range(r_f, r_l, s_f, s_l, offset):
    o_f = max(r_f, s_f)
    o_l = min(r_l, s_l)
    if o_f > o_l:
        return [(r_f, r_l)], []
    mapped = [(o_f + offset, o_l + offset)]
    unmapped = []
    if r_f < o_f:
        unmapped.append((r_f, o_f - 1))
    if o_l < r_l:
        unmapped.append((o_l + 1, r_l))
    return unmapped, mapped

# return mapped_from and mapped_to
def apply_map_to_ranges(map, unmapped):
    next_unmapped = []
    mapped = []
    for (s_f, s_l, offset) in map:
        if not unmapped:
            break

        for r_f, r_l in unmapped:
            u, m = apply_mapping_to_range(r_f, r_l, s_f, s_l, offset)
            next_unmapped.extend(u)
            mapped.extend(m)
        unmapped = next_unmapped
        next_unmapped = []

    mapped.extend(unmapped)
    return mapped

# (range_first, range_last)
ranges = []
# (src_first, src_last, offset)
map = []

for line in lines:
    if line.startswith("seeds: "):
        print("Loading initial ranges.")
        s_and_l = [int(i) for i in line.split()[1:]]
        for i in range(0, len(s_and_l), 2):
            first = s_and_l[i]
            last = s_and_l[i] + s_and_l[i+1] - 1
            ranges.append((first, last))
    elif line == "":
        print("Applying map to ranges.")
        ranges = apply_map_to_ranges(map, ranges)
        map.clear()
    elif line.endswith("map:"):
        print(f"Next map: {line}")
        continue
    else:
        # Mapping line
        print(f"Adding {line} to map.")
        (dest_first, src_first, m_len) = [int(i) for i in line.split()]
        offset = dest_first - src_first
        src_last = src_first + m_len - 1
        map.append((src_first, src_last, offset))

ranges = sorted(ranges)
print(ranges[0])