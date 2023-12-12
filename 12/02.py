with open("input.txt") as infile:
    lines = infile.read().splitlines()

def process_operational(cur_group_idx, run_length, ways):
    if cur_group_idx == len(groups):
        # current entry is complete -> valid
        return (cur_group_idx, 0), ways
    cur_group = groups[cur_group_idx]
    if run_length == 0:
        # current run hasn't started yet -> valid
        return (cur_group_idx, run_length), ways
    if run_length < cur_group:
        # current run is incomplete -> invalid
        return (cur_group_idx, run_length), 0
    if run_length == cur_group:
        # current run just completed -> valid
        return (cur_group_idx + 1, 0), ways

def process_damaged(cur_group_idx, run_length, ways):
    if cur_group_idx == len(groups):
        # current entry is complete -> invalid
        return (cur_group_idx, 0), 0
    cur_group = groups[cur_group_idx]
    if run_length < cur_group:
        # starting a new run -> valid
        return (cur_group_idx, run_length + 1), ways
    if run_length == cur_group:
        # continuing a completed run -> invalid
        return (cur_group_idx, run_length + 1), 0

sum = 0
for line in lines:
    springs, groups = line.split()
    springs = '?'.join([springs] * 5)
    groups = ','.join([groups] * 5)
    groups = [int(i) for i in groups.split(",")]

# Idea: map from (first incomplete group, length of current run) to ways
# How to differentiate between "last cell was damaged" vs. "last cell was fine"?
# Maybe reset the run at the first operational cell rather than last damaged?

    num_groups = len(groups)
    state_ways = {(0, 0): 1}
    for spring_pos in range(len(springs)):
        spring = springs[spring_pos]
        next_state_ways = {}
        for ((cur_group_idx, run_length), ways) in state_ways.items():
            if spring != '#':
                # operational or unknown
                next_state, next_ways = process_operational(
                    cur_group_idx, run_length, ways)
                if next_ways > 0:
                    next_state_ways[next_state] = next_state_ways.get(next_state, 0) + next_ways
            if spring != '.':
                # damaged or unknown
                next_state, next_ways = process_damaged(
                    cur_group_idx, run_length, ways)
                if next_ways > 0:
                    next_state_ways[next_state] = next_state_ways.get(next_state, 0) + next_ways
        state_ways = next_state_ways
    just_finished = state_ways.get((num_groups - 1, groups[-1]), 0)
    finished = state_ways.get((num_groups, 0), 0)
    sum += just_finished + finished
    print(f"{just_finished=} {finished=} {sum=}")
