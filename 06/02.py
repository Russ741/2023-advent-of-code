from math import sqrt, floor, ceil

with open("input.txt") as infile:
    lines = infile.read().splitlines()
    t = int("".join(lines[0].split()[1:]))
    d = int("".join(lines[1].split()[1:]))

# roots: 0 = c**2 - t*c + dist
# c = -(-t) +- sqrt(t**2 - 4 * 1 * dist) / 2
# c = (t +- sqrt(t**2 - 4 * dist)) / 2
def get_charge_roots(t, d):
    d += 1  # have to *beat* distance
    f = sqrt(t**2 - 4 * d)
    return (t - f) / 2, (t + f) / 2

min, max = get_charge_roots(t, d)
result = floor(max) - ceil(min) + 1
print(f"Result: {result}")