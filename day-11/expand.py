#!/usr/bin/python3
import sys
import copy


class Galaxy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __copy__(self):
        return Position(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Galaxy {self.x}, {self.y}"

    def distance(self, other):
        return abs(other.x - self.x) + abs(other.y - self.y)

    def moveX(self, delta):
        self.x += delta

    def moveY(self, delta):
        self.y += delta


def main(input_file):
    with open(f"{input_file}") as file:
        galaxies = getGalaxies(file)

    for g in galaxies:
        print(g)
    galaxiesPairs = pairUpGalaxies(galaxies)
    distances = getDistances(galaxiesPairs)

    print(f"sum of all distances {sum(distances)}")


def getGalaxies(file):
    galaxies = []

    fileContent = file.readlines()
    emptyColumns = [True for _ in range(len(fileContent[0].strip()))]
    emptyRows = [True for _ in range(len(fileContent))]

    y = 0
    file.seek(0, 0)
    for line in fileContent:
        for x, val in enumerate(line.strip()):
            if val == "#":
                galaxies.append(Galaxy(x, y))
                emptyColumns[x] = False
                emptyRows[y] = False
        y += 1

    print("original galaxies")
    for g in galaxies:
        print(g)
    print("- - -")

    return expandSpace(galaxies, emptyColumns, emptyRows)


def expandSpace(galaxies, emptyColumns, emptyRows):
    d = 0
    for row, isEmpty in enumerate(emptyRows):
        if isEmpty:
            for g in galaxies:
                if g.y > row + d:
                    g.moveY(1)
            d+=1

    d = 0
    for column, isEmpty in enumerate(emptyColumns):
        if isEmpty:
            for g in galaxies:
                if g.x > column + d:
                    g.moveX(1)
            d += 1

    return galaxies


def pairUpGalaxies(galaxies):
    pairs = []
    j = len(galaxies)

    for first in range(j):
        for second in range(first+1, j):
            pairs.append([galaxies[first], galaxies[second]])

    return pairs

def getDistances(pairs):
    distances = []
    for p in pairs:
        print(f"distance between {p[0]} and {p[1]} is {p[0].distance(p[1])}")
        distances.append(p[0].distance(p[1]))

    return distances


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing input file name")
        exit

    main(sys.argv[1])
