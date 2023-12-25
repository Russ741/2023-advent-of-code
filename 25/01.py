import re
from collections import defaultdict

def print_adj_list_to_dotfile(adj_list):
    print("\n---\n")
    print("graph G {")
    visited = set()
    for src, adj in adj_list.items():
        visited.add(src)
        for dst in adj:
            if dst not in visited:
                print(f"  {src} -- {dst}")
    print("}")

# dot -Tsvg output.dot -o output.svg

with open("input.txt") as infile:
    lines = infile.read().splitlines()

adj_list = defaultdict(set)
for line in lines:
    groups = re.match("(.*): (.*)", line).groups()
    src = groups[0]
    dsts = groups[1].split()
    for dst in dsts:
        adj_list[src].add(dst)
        adj_list[dst].add(src)

print_adj_list_to_dotfile(adj_list)

# Relevant edges are btp-qxr vfx-bgl rxt-bqq

for src, dst in (("btp", "qxr"), ("vfx", "bgl"), ("rxt", "bqq")):
    adj_list[src].remove(dst)
    adj_list[dst].remove(src)

visited = set()
to_visit = set(["btp"])
while to_visit:
    visiting = to_visit.pop()
    visited.add(visiting)
    for next in adj_list[visiting]:
        if next not in visited:
            to_visit.add(next)

visit_ct = len(visited)
unvisit_ct = len(adj_list) - visit_ct

print(f"{visit_ct=} {unvisit_ct=} {visit_ct * unvisit_ct}")