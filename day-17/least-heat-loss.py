#!/usr/bin/python3
import sys


def main(input_file):
    minHeatLoss = 0

    print(f"least heat loss is {minHeatLoss}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing input file name")
        exit

    main(sys.argv[1])
