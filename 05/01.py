from collections import defaultdict

lines = None
with open("input.txt") as infile:
    lines = infile.read().splitlines()

seeds = None
maps = {}
for line in lines:
    if line.startswith("seeds: "):
        seeds = [int(i) for i in line.split()[1:]]
    elif line == "":
        continue
    elif line.endswith("map:"):
        map_name = line.split()[0]
        maps[map_name] = {}
    else:
        (dest_start, src_start, len) = [int(i) for i in line.split()]
        maps[map_name][src_start] = (dest_start, len)
for map_name in maps.keys():
    maps[map_name] = dict(sorted(maps[map_name].items()))

def get_next(map, src_num):
    for (src_start, (dest_start, len)) in map.items():
        if src_start > src_num:
            break
        if src_start + len >= src_num:
            return dest_start + src_num - src_start
    return src_num

lowest_loc = None
for orig_seed in seeds:
    next = orig_seed
    for map in maps.values():
        next = get_next(map, next)
    print(f"location for {orig_seed=} \t= {next}")
    if not lowest_loc or lowest_loc > next:
        lowest_loc = next

print(f"{lowest_loc=}")