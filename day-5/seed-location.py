#!/usr/bin/python3
import sys
import re

def main(input_file):
    map = {
        'seed-to-soil': [],
        'soil-to-fertilizer': [],
        'fertilizer-to-water': [],
        'water-to-light': [],
        'light-to-temperature': [],
        'temperature-to-humidity': [],
        'humidity-to-location': [],
    }
    seeds = []

    with open(f"/app/{input_file}") as file:
        seeds = parse_seeds(file.readline().strip())
        parse_mappings(file, map)

    walk_seeds(seeds, map)


def parse_seeds(seeds_line):
    m = re.match(r"seeds: ([0-9 ]+)", seeds_line)

    return map(int, m.group(1).strip().split(" "))


def parse_mappings(file, map):
    current_map = ""
    for line in file:
        if line.strip() == "":
            continue

        m = re.match(r"([a-z-]+) map:", line.strip())
        if m:
            current_map = m.group(1)
            continue
        if current_map:
            n = line.strip().split(" ")
            map[current_map].append(getTransformationMap(int(n[0]), int(n[1]), int(n[2])))


def getTransformationMap(dest_start, source_start, length):
    return {
        "start": source_start,
        "end": source_start + length - 1,
        "transformation": dest_start - source_start,
    }


def walk_seeds(seeds, map):
    smallest_position = sys.maxsize
    for meta_seed in seeds:
        # print(f"seed {meta_seed}")
        for mapping in map:
            meta_seed = transform(meta_seed, (map[mapping]))
        # print(f"position: {meta_seed}")
        smallest_position = min(smallest_position, meta_seed)
    print(f"smallest position: {smallest_position}")


def transform(number, trns):
    for tr in trns:
        if number >= tr['start'] and number <= tr['end']:
            return number + tr['transformation']

    return number

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing input file name")
        exit

    main(sys.argv[1])
