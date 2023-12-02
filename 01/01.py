import re

digit_regex_str = '(\d)'
print(f"{digit_regex_str=}")
digit_regex = re.compile(digit_regex_str, re.IGNORECASE)

last_digit_regex_str = '.*' + digit_regex_str
print(f"{last_digit_regex_str=}")
last_digit_regex = re.compile(last_digit_regex_str, re.IGNORECASE)

def to_int(match_str):
    return int(match_str)

def get_first_digit(input_line):
    match = re.search(digit_regex, input_line)
    return to_int(match.group(1))

def get_last_digit(input_line):
    match = re.search(last_digit_regex, input_line)
    return to_int(match.group(1))

sum = 0
line_num = 1
with open('input.txt') as input_file:
    for input_line in input_file:
        first = get_first_digit(input_line)
        last = get_last_digit(input_line)
        delta = 10 * first + last
        sum += delta
        print(f"{line_num} {input_line=} {first=} {last=} {delta=} {sum=}")
        line_num += 1
print(f"{sum=}")