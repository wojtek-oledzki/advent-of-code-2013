#!/usr/bin/python3
import sys
import re

def main(input_file):
    hashmap = {}
    with open(f"{input_file}") as file:
        while(True):
            line = file.readline()

            if not line:
                break

            for i in line.strip().split(","):
                h, label, op, focalLength  = operation(i)
                if op[0] == "-":
                    if h in hashmap:
                        if label in hashmap[h]:
                            del hashmap[h][label]
                else:
                    if not h in hashmap:
                        hashmap[h] = {}
                    hashmap[h][label] = focalLength

    print(focusingPower(hashmap))


def focusingPower(boxes):
    focusPower = 0
    for box, lenses in boxes.items():
        for i, (label, focus) in enumerate(lenses.items()):
            focusPower += ((box + 1) * (i+1) * focus)
    return focusPower


def operation(command):
    m = re.match(r"([a-z]+)(=|-)([0-9]*)", command)

    if m.group(3) != "":
        return hash(m.group(1)), m.group(1), m.group(2), int(m.group(3))

    return hash(m.group(1)), m.group(1), m.group(2), None


def hash(input) -> int:
    hash = 0
    for s in input:
        hash += ord(s)
        hash *= 17
        hash %= 256

    return hash


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing input file name")
        exit

    main(sys.argv[1])
