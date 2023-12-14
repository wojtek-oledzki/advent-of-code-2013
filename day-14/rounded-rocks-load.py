#!/usr/bin/python3
import sys

def main(input_file):
    with open(f"{input_file}") as file:
        analyse(file)

    print(f"answer: ")


def analyse(file):
    columns = []

    line = file.readline().strip()
    file.seek(0,0)
    columns = [[] for _ in line]

    while(True):
        line = file.readline()

        if not line:
            break

        line = line.strip()

        for i, c in enumerate(line):
            columns[i] += c

    weights = 0
    maxWeight = len(columns[0])
    for column in columns:
        for i, el in enumerate(boubleStone(column)):
            if el == "O":
                weights += maxWeight - i
    print(weights)


def boubleStone(column):
    anyChange = True
    while(anyChange):
        anyChange = False
        ind = len(column) -1
        while(ind > 0):
            if needsSwapping(column[ind], column[ind-1]):
                column[ind], column[ind-1] = column[ind-1], column[ind]
                anyChange = True
            ind -= 1

    return column


def needsSwapping(first, second):
    if first == ".":
        return False
    if first == "O" and second == ".":
        return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing input file name")
        exit

    main(sys.argv[1])
