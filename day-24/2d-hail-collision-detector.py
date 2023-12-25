#!/usr/bin/python3
import sys
import re
from shapely import geometry


def main(input_file, minXY, maxXY):
    data = []
    with open(f"{input_file}") as file:
        data = parseFile(file)

    segments = getSegments(data, minXY, maxXY)

    testField = geometry.Polygon(geometry.LineString([
        (minXY, minXY), (minXY, maxXY), (maxXY, maxXY), (maxXY, minXY), (minXY, minXY)
    ]))
    max = len(data)
    outerLoop = 0
    innerLoop = 0
    crash = 0
    while outerLoop < max:
        innerLoop = outerLoop + 1
        while(innerLoop < max):
            # detect collision
            if segments[outerLoop][0].intersects(segments[innerLoop][0]):
                point = segments[outerLoop][0].intersection(segments[innerLoop][0])
                # print(f"detected collision {outerLoop} with {innerLoop} at {point}")
                # check if collision inside the field.
                if testField.contains(point):
                    # check if collision happen in the past?
                    d1x = point.x - data[outerLoop][0].x
                    d1y = point.y - data[outerLoop][0].y
                    if sameOrientation(d1x, d1y, data[outerLoop][1].x, data[outerLoop][1].y):
                        d1x = point.x - data[innerLoop][0].x
                        d1y = point.y - data[innerLoop][0].y
                        if sameOrientation(d1x, d1y, data[innerLoop][1].x, data[innerLoop][1].y):
                            # print(f"CRASH!")
                            crash += 1
                else:
                    # print("collision outside test Field")
            innerLoop += 1
        outerLoop += 1

    print(f"hail will crash {crash} times")

def sameOrientation(dx1, dy1, dx2, dy2):
    if dx1 * dx2 > 0 and dy1 * dy2 > 0:
        return True
    return False

def parseFile(file):
    data = []
    for line in file:
        data.append(parseLine(line))

    return data


def parseLine(line):
    m = re.search('(?P<x>[-0-9]+), +(?P<y>[-0-9]+), +(?P<z>[-0-9]+) +\@ +(?P<dx>[-0-9]+), +(?P<dy>[-0-9]+), +(?P<dz>[-0-9]+)', line.strip())

    p = geometry.Point(int(m.group("x")), int(m.group("y")))
    v = geometry.Point(int(m.group("dx")), int(m.group("dy")))

    return p, v


def getSegments(data, minXY, maxXY):
    segments = []
    for d in data:
        vector = d[1]
        point = d[0]

        a = vector.y/vector.x
        b = point.y - a * point.x
        fx = lambda x: (a * x) + b

        y1 = fx(minXY)
        y2 = fx(maxXY)

        segments.append((geometry.LineString([(minXY, y1), (maxXY, y2)]), a))

    return segments


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Missing input file name")
        exit

    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
