#!/usr/bin/python3
import sys
import re

def main(input_file):
    listX = []
    listY = []
    with open(f"{input_file}") as file:
        listX, listY = getPolygonVertices(file)

    print (listX)
    print(listY)

    area = polygonArea(listX, listY)
    print(f"lava lake area: {area}")


def getPolygonVertices(file):
    listX = [0]
    listY = [0]
    # first step is L :D
    currentX = 0
    currentY = 0

    dir, len = parseLine(file.readline().strip())
    for l in file:
        nextDir, nextLen = parseLine(l.strip())

        dx, dy = getDirectionAndLength(dir, len, nextDir)
        currentX += dx
        currentY += dy
        listX.append(currentX)
        listY.append(currentY)

        if isClockwise(dir, nextDir):
            if nextDir == "D":
                currentY += 1
            if nextDir == "U":
                currentY -= 1
            if nextDir == "L":
                currentX -= 1
            if nextDir == "R":
                currentX += 1

        len = nextLen
        dir = nextDir

    return listX, listY


def parseLine(line):
    m = re.match(r"([RLUD]) ([0-9]+) \(#(.*)([0-3])\)", line)
    print(m.group(3), m.group(4))

    return numberToDir(m.group(4)), int(m.group(3), 16)


def numberToDir(number):
    if number == "0":
        return "R"
    if number == "1":
        return "D"
    if number == "2":
        return "L"
    if number == "3":
        return "U"


def getDirectionAndLength(dir, len, nextDir):
    if dir == "R":
        if isClockwise(dir, nextDir):
            return len, 0
        else:
            return len - 1, 0
    if dir == "L":
        if isClockwise(dir, nextDir):
            return -1 * len, 0
        else:
            return -1 * (len - 1), 0
    if dir == "D":
        if isClockwise(dir, nextDir):
            return 0, len
        else:
            return 0, len - 1
    if dir == "U":
        if isClockwise(dir, nextDir):
            return 0, -1 * len
        else:
            return 0, -1 * (len - 1)


def isClockwise(prev, next):
    return (prev == "U" and next == "R") \
        or \
        (prev == "R" and next == "D") \
        or \
        (prev == "D" and next == "L") \
        or \
        (prev == "L" and next == "U")


def polygonArea(listX, listY):
    area = 0
    previous = len(listX) - 1

    if previous < 2:
        return area

    for i in range(previous):
        area += (listX[previous] + listX[i]) * (listY[previous]-listY[i])
        previous = i

    return area/2


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing input file name")
        exit

    main(sys.argv[1])
