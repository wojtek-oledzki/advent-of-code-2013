#!/usr/bin/python3
import sys


def main(input_file):
    map = []
    with open(f"{input_file}") as file:
        map = readMap(file)

    beams = []
    energized = {}
    beams.append(BeamOnMap(map, energized))
    while(len(beams) > 0):
        print(f"{len(beams)} to analyse...")
        for i, b in enumerate(beams):
            del beams[i]
            for newBeam in b.go():
                beams.append(newBeam)

    print(f"{len(energized)} tiles end up being energized")


def readMap(file) -> list:
    map = []
    for l in file:
        map.append(l.strip())

    return map


class BeamOnMap:
    DIR_LEFT = -1, 0
    DIR_RIGHT = 1, 0
    DIR_UP = 0, -1
    DIR_DOWN = 0, 1

    def __init__(self, rows, energized, x = 0, y = 0, direction = DIR_RIGHT) -> None:
        self.newBeams = []
        self.rows = rows
        self.energized = energized
        self.position = x, y
        self.direction = direction

        self.maxX = len(self.rows[0]) - 1
        self.maxY = len(self.rows) - 1


    def go(self):
        self.energiseTile()
        while(self.move()):
            pass

        return self.newBeams


    def move(self):
        # prepare for next move
        newBeam = self.prepareForNextMove()
        if newBeam:
            self.newBeams.append(newBeam)

        # move
        self.position = (self.position[0] + self.direction[0], self.position[1] + self.direction[1])

        # check if finished
        if self.notOnMap():
            return False

        if self.alreadyVisited():
            return False

        self.energiseTile()

        return True


    def prepareForNextMove(self):
        if self.currentFiled() == ".":
            return None

        if self.currentFiled() == "\\":
            # update direction, no clone
            if self.direction == self.DIR_LEFT:
                self.direction = self.DIR_UP
            elif self.direction == self.DIR_RIGHT:
                self.direction = self.DIR_DOWN
            elif self.direction == self.DIR_UP:
                self.direction = self.DIR_LEFT
            elif self.direction == self.DIR_DOWN:
                self.direction = self.DIR_RIGHT
            return None

        if self.currentFiled() == "/":
            # update direction, no clone
            if self.direction == self.DIR_LEFT:
                self.direction = self.DIR_DOWN
            elif self.direction == self.DIR_RIGHT:
                self.direction = self.DIR_UP
            elif self.direction == self.DIR_UP:
                self.direction = self.DIR_RIGHT
            elif self.direction == self.DIR_DOWN:
                self.direction = self.DIR_LEFT
            return None

        if self.currentFiled() == "|":
            if self.direction == self.DIR_RIGHT:
                self.direction = self.DIR_DOWN
                return self.cloneInDirection(self.DIR_UP)
            elif  self.direction == self.DIR_LEFT:
                self.direction = self.DIR_DOWN
                return self.cloneInDirection(self.DIR_UP)
            elif self.direction == self.DIR_DOWN or self.direction == self.DIR_UP:
                return None

        if self.currentFiled() == "-":
            if self.direction == self.DIR_DOWN:
                self.direction = self.DIR_LEFT
                return self.cloneInDirection(self.DIR_RIGHT)
            elif  self.direction == self.DIR_UP:
                self.direction = self.DIR_LEFT
                return self.cloneInDirection(self.DIR_RIGHT)
            elif self.direction == self.DIR_LEFT or self.direction == self.DIR_RIGHT:
                return None


    def cloneInDirection(self, dir):
        nb = BeamOnMap(self.rows, self.energized, self.position[0] + dir[0], self.position[1] + dir[1], dir)

        if nb.alreadyVisited():
            return None

        if nb.notOnMap():
            return None

        return nb


    def notOnMap(self):
        return self.position[0] < 0 or self.position[0] > self.maxX or self.position[1] < 0 or self.position[1] > self.maxY


    def currentFiled(self):
        return self.rows[self.position[1]][self.position[0]]


    def energiseTile(self):
        if f"{self.position}" in self.energized:
            self.energized[f"{self.position}"][f"{self.direction}"] = True
        else:
            self.energized[f"{self.position}"] = {}
            self.energized[f"{self.position}"][f"{self.direction}"] = True


    def alreadyVisited(self):
        if f"{self.position}" in self.energized:
            if f"{self.direction}" in self.energized[f"{self.position}"]:
                return True
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing input file name")
        exit

    main(sys.argv[1])
