from enum import IntFlag

with open("input.txt") as infile:
    lines = infile.read().splitlines()

class Dir(IntFlag):
    U = 1
    D = 2
    L = 4
    R = 8

U = Dir.U
D = Dir.D
L = Dir.L
R = Dir.R

def next(r, c, dir):
    match dir:
        case Dir.U:
            return r-1, c
        case Dir.D:
            return r+1, c
        case Dir.L:
            return r, c-1
        case Dir.R:
            return r, c+1

rows = len(lines)
cols = len(lines[0])

def inbounds(r, c):
    return r >= 0 and r < rows and c >= 0 and c < cols

new_beams = [(0, -1, R)]  # source r, c, dir
beams = {} # (r, c) -> U | D | L | R

while new_beams:
    (r, c, dir) = new_beams.pop()
    dr, dc = next(r, c, dir)
    d = (dr, dc)
    if not inbounds(dr, dc):
        continue
    if d in beams and beams[d] & dir:
        continue
    beams[d] = beams.get(d, Dir(0)) | dir
    cell = lines[dr][dc]
    match dir:
        case Dir.U:
            if cell == '.' or cell == '|':
                new_beams.append((dr, dc, U))
            elif cell == '\\':
                new_beams.append((dr, dc, L))
            elif cell == '/':
                new_beams.append((dr, dc, R))
            elif cell == '-':
                new_beams.append((dr, dc, L))
                new_beams.append((dr, dc, R))
        case Dir.D:
            if cell == '.' or cell == '|':
                new_beams.append((dr, dc, D))
            elif cell == '\\':
                new_beams.append((dr, dc, R))
            elif cell == '/':
                new_beams.append((dr, dc, L))
            elif cell == '-':
                new_beams.append((dr, dc, L))
                new_beams.append((dr, dc, R))
        case Dir.L:
            if cell == '.' or cell == '-':
                new_beams.append((dr, dc, L))
            elif cell == '\\':
                new_beams.append((dr, dc, U))
            elif cell == '/':
                new_beams.append((dr, dc, D))
            elif cell == '|':
                new_beams.append((dr, dc, U))
                new_beams.append((dr, dc, D))
        case Dir.R:
            if cell == '.' or cell == '-':
                new_beams.append((dr, dc, R))
            elif cell == '\\':
                new_beams.append((dr, dc, D))
            elif cell == '/':
                new_beams.append((dr, dc, U))
            elif cell == '|':
                new_beams.append((dr, dc, U))
                new_beams.append((dr, dc, D))

print(len(beams))