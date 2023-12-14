#!/usr/bin/python3
import sys


def main(input_file):
    with open(f"{input_file}") as file:
        platform = getPlatform(file)

    hashes = []
    targetSpins = 1000000000
    while(targetSpins > 0):
        platform.spinCycle()
        targetSpins -= 1
        # look for cyclic loop
        hashes.append(hash(platform))

        foundCyclicLoop, cycleLength = lookForCyclicLoop(hashes)
        if foundCyclicLoop:
            break

    extraCycles = targetSpins % cycleLength
    while(extraCycles > 0):
        platform.spinCycle()
        extraCycles -= 1

    print(f"load on North beams after {targetSpins} cycles is: {platform.getNorthBeamsLoad()}")


def lookForCyclicLoop(list):
    if len(list) < 2:
        return False, 0

    last = list.pop()
    for i, m in enumerate(list):
        if m == last:
            list.append(last)
            return True, len(list) - i - 1
    list.append(last)
    return False, 0


class Platform:
    def __init__(self, x, y):
        self.rows = [["." for _ in range(x)] for _ in range(y)]
        self.rowsCount = y
        self.columnsCount = x
        self.bolders = []


    def __str__(self):
        m = ""
        for r in self.rows:
            m += "".join(r) + "\n"

        return m

    def __hash__(self):
        return hash((self.__str__()))


    def addRow(self):
        self.rows.append(["." for _ in range(self.columnsCount)])
        self.rowsCount = len(self.rows)


    def putBolder(self, x, y):
        self.bolders.append(Bolder(x, y, self))
        self.rows[y][x] = "O"


    def moveBolder(self, sx, sy, dx, dy):
        self.rows[sy][sx] = "."
        self.rows[dy][dx] = "O"


    def putBlock(self, x, y):
        self.rows[y][x] = "#"


    def getNorthBeamsLoad(self):
        load = 0
        maxWeight = self.rowsCount
        for b in self.bolders:
            load += maxWeight - b.y

        return load


    def isEmpty(self, x, y) -> bool:
        return self.rows[y][x] == "."


    def spinCycle(self) -> None:
        self.tiltNorth()
        self.tiltWest()
        self.tiltSouth()
        self.tiltEast()


    def tiltNorth(self) -> None:
        # order North
        self.bolders.sort(key=lambda el: el.y)
        for b in self.bolders:
            b.moveNorth()


    def tiltSouth(self) -> None:
        # order South
        self.bolders.sort(key=lambda el: el.y, reverse=True)
        for b in self.bolders:
            b.moveSouth()


    def tiltWest(self) -> None:
        # order East
        self.bolders.sort(key=lambda el: el.x)
        for b in self.bolders:
            b.moveWest()


    def tiltEast(self) -> None:
        self.bolders.sort(key=lambda el: el.x, reverse=True)
        for b in self.bolders:
            b.moveEast()


    def countEmptyNortOf(self, x, y) -> int:
        return self.countEmptyY(x, y, -1)


    def countEmptySouthOf(self, x, y) -> int:
        return self.countEmptyY(x, y, 1)


    def countEmptyWestOf(self, x, y) -> int:
        return self.countEmptyX(x, y, -1)


    def countEmptyEastOf(self, x, y) -> int:
        return self.countEmptyX(x, y, 1)


    def countEmptyY(self, x, y, step) -> int:
        c = 0
        while(y+step >= 0 and y+step < self.rowsCount and self.rows[y+step][x] == "."):
            c += 1
            y += step

        return c


    def countEmptyX(self, x, y, step) -> int:
        c = 0
        while(x+step >= 0 and x+step < self.columnsCount and self.rows[y][x+step] == "."):
            c += 1
            x += step

        return c


class Bolder:
    def __init__(self, x, y, platform) -> None:
        self.x = x
        self.y = y
        self.platform = platform


    def __str__(self) -> str:
        return "O"


    def moveNorth(self):
        d = self.platform.countEmptyNortOf(self.x, self.y)
        self.platform.moveBolder(self.x, self.y, self.x, self.y - d)
        self.y -= d


    def moveSouth(self):
        d = self.platform.countEmptySouthOf(self.x, self.y)
        self.platform.moveBolder(self.x, self.y, self.x, self.y + d)
        self.y += d


    def moveEast(self) -> None:
        d = self.platform.countEmptyEastOf(self.x, self.y)
        self.platform.moveBolder(self.x, self.y, self.x + d, self.y)
        self.x += d


    def moveWest(self) -> None:
        d = self.platform.countEmptyWestOf(self.x, self.y)
        self.platform.moveBolder(self.x, self.y, self.x - d, self.y)
        self.x -= d


def getPlatform(file):
    line = file.readline().strip()
    file.seek(0,0)
    platform = Platform(len(line), 0)

    row = 0
    while(True):
        line = file.readline()

        if not line:
            break

        line = line.strip()
        platform.addRow()

        for i, c in enumerate(line):
            if c == "#":
                platform.putBlock(i, row)
            elif c == "O":
                platform.putBolder(i, row)

        row += 1

    return platform


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
