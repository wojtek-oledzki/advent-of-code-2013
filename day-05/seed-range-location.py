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
        # 'humidity-to-location': [],
        # 'temperature-to-humidity': [],
        # 'light-to-temperature': [],
        # 'water-to-light': [],
        # 'fertilizer-to-water': [],
        # 'soil-to-fertilizer': [],
        # 'seed-to-soil': [],
    }
    seeds = []

    with open(f"/app/{input_file}") as file:
        seeds = parse_seeds(file.readline().strip())
        print("seeds parsed", flush=True)
        parse_mappings(file, map)

    print("starting the walk", flush=True)
    walk_seeds(seeds, map)


def parse_seeds(seeds_line):
    m = re.match(r"seeds: ([0-9 ]+)", seeds_line)
    ranges = map(int, m.group(1).strip().split(" "))
    seeds = []
    for x, y in zip(*[iter(ranges)]*2):
        seeds.append([x, x+y-1])

    return seeds


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
        "s": source_start,
        "e": source_start + length - 1,
        "t": dest_start - source_start,
    }


def walk_seeds(seeds, map):
    smallest_position = sys.maxsize

    for seed_range in seeds:
        meta_seed = seed_range[0]
        while (meta_seed <= seed_range[1]):
            position = meta_seed
            for mapping in map:
                position = transform(position, (map[mapping]))
            smallest_position = min(smallest_position, position)
            meta_seed += 1
        print(".", flush=True)
    print(f"smallest position: {smallest_position}")


def transform(number, trns):
    for tr in trns:
        if number >= tr['s'] and number <= tr['e']:
            return number + tr['t']

    return number


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing input file name")
        exit

    main(sys.argv[1])
