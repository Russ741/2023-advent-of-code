import re

def get_max(input, search):
    search_regex_str = '(\d+) ' + search
    match_all = re.findall(search_regex_str, input)
    max = 0
    for match in match_all:
        match = int(match)
        if match > max:
            max = match
    return max

maxes = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

with open("./input.txt") as input_file:
    sum = 0
    for input_line in input_file:
        (s1, _, s2) = input_line.partition(":")
        s1 = int(s1[5:])
        s2 = s2[:-1]
        print(f"{s1} {s2}")
        valid = True
        for search in [r'red', r'green', r'blue']:
            max = get_max(s2, search)
            if max > maxes[search]:
                valid = False
        if valid:
            sum += s1
    print(f"{sum=}")