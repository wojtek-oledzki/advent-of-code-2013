#!/usr/bin/python3
import sys
import re
from functools import reduce
from operator import mul

def main(input_file):
    times = []
    timeFunctions = []
    with open(f"/app/{input_file}") as file:
        times = parse_times(file.readline().strip())
        timeFunctions = list(map(get_time_function, times))
        current_records = parse_distance(file.readline().strip())

    number_of_better_records = []
    for i, time in enumerate(times):
        print(f"round {i}")

        current_record = current_records[i]
        possible_better_records = 0
        for t in range(time):
            if timeFunctions[i](t) > current_record:
                possible_better_records += 1
        print(f"possible better {possible_better_records}")
        number_of_better_records.append(possible_better_records)

    print(reduce(mul, number_of_better_records))


def get_time_function(time):
    def func(wait):
        return (time - wait) * wait

    return func


def parse_times(time_line):
    m = re.match(r"Time: +([0-9 ]+)", time_line)
    return list(map(int, re.split(r' +', m.group(1).strip())))


def parse_distance(time_line):
    m = re.match(r"Distance: +([0-9 ]+)", time_line)
    return list(map(int, re.split(r' +', m.group(1).strip())))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing input file name")
        exit

    main(sys.argv[1])
