from math import sqrt, floor, ceil

tds = []
with open("input.txt") as infile:
    lines = infile.read().splitlines()
    times = [int(i) for i in lines[0].split()[1:]]
    distances = [int(i) for i in lines[1].split()[1:]]
    tds = list(zip(times, distances))
print(tds)

# roots: 0 = c**2 - t*c + dist
# c = -(-t) +- sqrt(t**2 - 4 * 1 * dist) / 2
# c = (t +- sqrt(t**2 - 4 * dist)) / 2
def get_charge_roots(t, d):
    d += 1  # have to *beat* distance
    f = sqrt(t**2 - 4 * d)
    return (t - f) / 2, (t + f) / 2

result = 1
for t, d in tds:
    min, max = get_charge_roots(t, d)
    ways = floor(max) - ceil(min) + 1
    result *= ways
    print(f"{t=} {d=}: {min=} {max=} = {ways} -> {result}")
print(f"Result: {result}")