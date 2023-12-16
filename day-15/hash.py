#!/usr/bin/python3
import sys


def main(input_file):
    sum = 0
    with open(f"{input_file}") as file:
        while(True):
            line = file.readline()

            if not line:
                break

            for i in line.strip().split(","):
                sum += hash(i)

    print(f"sum of all hashes: {sum}")


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
