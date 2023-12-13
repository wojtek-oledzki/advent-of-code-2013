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
            sum += analyseMap(list(map(mapDotAndHash, mapRows)), list(map(mapDotAndHash, mapCols)))
            break

        line = line.strip()

        if isMapsFirstLine:
            mapCols = ["" for _ in line]
            isMapsFirstLine = False

        if line == "":

            sum += analyseMap(list(map(mapDotAndHash, mapRows)), list(map(mapDotAndHash, mapCols)))
            mapRows = []
            isMapsFirstLine = True

        else:
            mapRows.append(line)
            for i, c in enumerate(line):
                mapCols[i] += c
    print(f"total sum: {sum}")

def mapDotAndHash(line):
    bLine = ""
    for c in line:
        if c == ".":
            bLine += "0"
        else:
            bLine += "1"

    return int(bLine, 2)

def analyseMap(rows, cols):
    smudges = 1

    mirrorPosition = findMirror(rows, smudges)
    if mirrorPosition == -1:
        mirrorPosition = findMirror(cols, smudges)
        return mirrorPosition
    else:
        return 100 * mirrorPosition


def findMirror(lines, smudges):
    i = 0
    size = len(lines)

    while(i < size - 1):
        if smudges > 0 and isPowerOf2(lines[i] ^ lines[i+1]):
            smudges -= 1
            if isMirror(lines, i, smudges):
                return i + 1
            else:
                smudges += 1
        if lines[i] == lines[i+1]:
            if isMirror(lines, i, smudges):
                return i + 1
        i += 1

    return -1

def isPowerOf2(number):
    return (number & (number - 1) == 0) and number != 0

def isMirror(lines, mirrorPosition, smudges):
    l = mirrorPosition - 1
    r = mirrorPosition + 2
    max = len(lines) - 1

    while(l >=0 and r <= max):
        if smudges > 0 and isPowerOf2(lines[l] ^ lines[r]):
            smudges -= 1
        elif lines[l] != lines[r]:
            return False
        l -= 1
        r += 1

    return True and smudges == 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing input file name")
        exit

    main(sys.argv[1])
