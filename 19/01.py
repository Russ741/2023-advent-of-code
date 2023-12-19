import re

with open("input.txt") as infile:
    wf_str, parts_str = infile.read().split("\n\n")

rules = {}
for wf_line in wf_str.splitlines():
    line_match = re.match("(.*){(.*)}", wf_line)
    wf_name, wf_rules_str = line_match.groups()
    wf_rule_strs = wf_rules_str.split(',')
    wf_rules = []
    for wf_rule_str in wf_rule_strs:
        rule_match_groups = re.match(r"(:?(.+)([<>])(.+):)?(.*)", wf_rule_str).groups()
        rule = list(rule_match_groups[1:])
        if rule[2] is not None:
            rule[2] = int(rule[2])
        rule = tuple(rule)
        wf_rules.append(rule)
    rules[wf_name] = wf_rules

print(rules)

parts = []
for part_line in parts_str.splitlines():
    part = {}
    splits = part_line[1:-1].split(",")
    for split in splits:
        type, count = split.split("=")
        count = int(count)
        part[type] = count
    parts.append(part)
print(parts)

score = 0
for part in parts:
    flow_name = "in"
    while flow_name not in ("A", "R"):
        flow_rules = rules[flow_name]
        for cur_rule in flow_rules:
            type, sign, qty, new_flow = cur_rule
            if not type:
                flow_name = new_flow
                break
            if sign == "<" and part[type] < qty:
                flow_name = new_flow
                break
            if sign == ">" and part[type] > qty:
                flow_name = new_flow
                break
    if flow_name == "A":
        value = sum(part.values())
        score += sum(part.values())
        print(f"Added {value} to {score}")
print(score)