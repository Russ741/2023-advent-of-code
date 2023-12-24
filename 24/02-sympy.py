from sympy import solve
from sympy.abc import a, b, c, d, e, f, g, h, i, j, k, l
from dataclasses import dataclass
import re

# a, b, c = rock's velocity in x, y, z
# d, e, f = rock's initial position in x, y, z
# g, h... = time of intersection with hail 0, 1, ...

@dataclass
class Hail:
    px: int
    py: int
    pz: int
    vx: int
    vy: int
    vz: int

with open("input.txt") as infile:
    lines = infile.read().splitlines()

stones = []
for line in lines:
    groups = re.match("^(.*), (.*), (.*) @ (.*), (.*), (.*)$", line).groups()
    nums = [int(n) for n in groups]
    stones.append(Hail(*nums))

system = []

for index, t in enumerate([g, h, i]):
    s = stones[index]
    system.append(t * s.vx + s.px - t * a - d)
    system.append(t * s.vy + s.py - t * b - e)
    system.append(t * s.vz + s.pz - t * c - f)

solution = solve(system, [a, b, c, d, e, f, g, h, i])
print(solution)
print(sum(solution[0][3:6]))