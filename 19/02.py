import re

with open("input.txt") as infile:
    wf_str, _ = infile.read().split("\n\n")

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

def get_combos(type_ranges):
    result = 1
    for low, high in type_ranges.values():
        result *= max(high - low + 1, 0)
    return result

def split_ranges(type_ranges, type, sign, qty):
    tr1 = type_ranges.copy()
    tr2 = type_ranges.copy()
    if sign == '<':
        tr1[type] = (tr1[type][0], qty - 1)
        tr2[type] = (qty, tr2[type][1])
    else:
        tr1[type] = (qty + 1, tr1[type][1])
        tr2[type] = (tr2[type][0], qty)
    return tr1, tr2

start_tr = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
workflow_trs = [("in", start_tr)]

accepted = 0
rejected = 0
while workflow_trs:
    wf, tr = workflow_trs.pop()
    print(f"{tr=} {wf=}")
    if wf == 'A':
        accepted += get_combos(tr)
    elif wf == 'R':
        rejected += get_combos(tr)
    else:
        wf_rules = rules[wf]
        rem_tr = tr
        for type, sign, qty, new_flow in wf_rules:
            if not type:
                workflow_trs.append((new_flow, rem_tr))
            else:
                new_tr, rem_tr = split_ranges(rem_tr, type, sign, qty)
                if get_combos(new_tr) > 0:
                    workflow_trs.append((new_flow, new_tr))
                if get_combos(rem_tr) == 0:
                    break
print(f"{accepted=}")
