#!/usr/bin/python3
import sys

def main(input_file):
    with open(f"{input_file}") as file:
        analyse(file)

def analyse(file):
    mapRows = []
    mapCols = []
    isMapsFirstLine = True
    sum = 0

    while(True):
        line = file.readline()

        if not line:
            sum += analyseMap(mapRows, mapCols)
            break

        line = line.strip()

        if isMapsFirstLine:
            mapCols = ["" for _ in line]
            isMapsFirstLine = False

        if line == "":
            sum += analyseMap(mapRows, mapCols)
            mapRows = []
            isMapsFirstLine = True

        else:
            mapRows.append(line)
            for i, c in enumerate(line):
                mapCols[i] += c
    print(f"total sum: {sum}")


def analyseMap(rows, cols):
    mirrorPosition = findMirror(rows)
    if mirrorPosition == -1:
        mirrorPosition = findMirror(cols)
        return mirrorPosition
    else:
        return 100 * mirrorPosition


def findMirror(lines):
    i = 0
    size = len(lines)

    while(i < size - 1):
        if lines[i] == lines[i+1]:
            if isMirror(lines, i):
                return i + 1
        i += 1

    return -1


def isMirror(lines, mirrorPosition):
    l = mirrorPosition - 1
    r = mirrorPosition + 2
    max = len(lines) - 1

    while(l >=0 and r <= max):
        if lines[l] != lines[r]:
            return False
        l -= 1
        r += 1

    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing input file name")
        exit

    main(sys.argv[1])
