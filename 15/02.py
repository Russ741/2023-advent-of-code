import re

with open("input.txt") as infile:
    lines = infile.read().splitlines()
    steps = lines[0].split(',')

def hash(step):
    result = 0
    for c in step:
        result += ord(c)
        result *= 17
        result %= 256
    return result

def score_boxes(boxes):
    total = 0
    for i in range(len(boxes)):
        box_score = 0
        slot = 1
        for _, focal in boxes[i].items():
            slot_score = (i + 1) * slot * focal
            box_score += slot_score
            # print(f"{i} {slot=} {focal=} {slot_score=}")
            slot += 1
        total += box_score
    return total

# lens focusing power = (box number + 1) * slot number (one-indexed) * focal length

result = 0
boxes = [{} for _ in range(256)]
for step in steps:
    grps = re.match("^(.*)([=-])(.*)$", step).groups()
    label = grps[0]
    box = hash(label)
    op = grps[1]
    focal = None
    if op == '=':
        focal = int(grps[2])
        # print(f"Adding {label=} to {box=}")
        boxes[box][label] = focal
    else:
        boxes[box].pop(label, 0)

print(score_boxes(boxes))