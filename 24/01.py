from dataclasses import dataclass
import re

@dataclass
class Hail:
    px: float
    py: float
    pz: float
    vx: float
    vy: float
    vz: float

    def slope(self):
        return self.vy / self.vx

    def y(self, x):
        slope = self.slope()
        y = self.py + slope * (x - self.px)
        return y

    def x_is_future(self, x):
        return (x - self.px) / self.vx > 0

def x_y_collision(h1, h2):
    yi1 = h1.y(0)
    yi2 = h2.y(0)

    dyi = yi2 - yi1
    ds = h2.slope() - h1.slope()
    if not ds:
        return None, None
    collide_x = - dyi / ds
    collide_y = h1.y(collide_x)
    return collide_x, collide_y

COORD_MIN = 200000000000000
COORD_MAX = 400000000000000

# COORD_MIN = 7
# COORD_MAX = 27

with open("input.txt") as infile:
    lines = infile.read().splitlines()

stones = []
for line in lines:
    groups = re.match("^(.*), (.*), (.*) @ (.*), (.*), (.*)$", line).groups()
    nums = [int(n) for n in groups]
    stones.append(Hail(*nums))

for stone in stones:
    print(stone, stone.y(0), stone.slope())

future_intersections = 0
for i in range(len(stones)):
    si = stones[i]
    for j in range(i + 1, len(stones)):
        sj = stones[j]
        x, y = x_y_collision(si, sj)
        if not x:
            # print(i, j, "Parallel")
            continue
        else:
            # print(i, j, si.x_is_future(x), sj.x_is_future(x), (x, y))

            if si.x_is_future(x) and sj.x_is_future(x) and x >= COORD_MIN and x <= COORD_MAX and y >= COORD_MIN and y <= COORD_MAX:
                future_intersections += 1
print(future_intersections)