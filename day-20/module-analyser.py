#!/usr/bin/python3
import sys
import re
import math


def main(input_file):
    modules = {}
    stack = []

    with open(f"{input_file}") as file:
        modules = getModules(file)

    # for m in modules:
    #     print(modules[m])

    loops = []
    low, high = pushTheButton(modules)
    loops.append((low, high))

    max = 999
    while((not allFlipFlopsBackToOff(modules)) and max > 0):
        print (f"{max} push the button")
        low, high = pushTheButton(modules)
        loops.append((low, high))
        max -= 1

    sumLow = sum([i[0] for i in loops])
    sumHigh = sum([i[1] for i in loops])
    extra = 1000 % len(loops)
    multiloops = math.floor(1000/len(loops))

    totalLow = multiloops * sumLow
    totalHigh = multiloops * sumHigh

    total = totalLow * totalHigh
    print(f"totalLow {totalLow} ({sumLow}), totalHigh {totalHigh} ({sumHigh} * {multiloops}), total {total}")


def allFlipFlopsBackToOff(modules) -> bool:
    allOff = 0
    for m in modules:
        if modules[m].type == Module.TYPE_FLIPFLOP:
            allOff = max(allOff, modules[m].state)

    return allOff == 0


def pushTheButton(modules):
    stack = []
    low = 1 # first button
    high = 0

    outputs, l, h = modules["broadcaster"].process()
    low += l
    high += h
    for o in outputs:
        stack.append(o)

    while(len(stack) > 0):
        m = stack.pop(0)

        out, l, h = m.process()
        low += l
        high += h
        for o in out:
            stack.insert(0, o)

    return low, high


def getModules(file) -> dict:
    modules = {}

    for line in file:
        m = parseLine(line.strip())
        m.addModulesLookup(modules)
        modules[m.name] = m

    for m in modules:
        for o in modules[m].outputs:
            if o in modules:
                modules[o].registerInput(modules[m])

    return modules


def parseLine(line):
    m = re.match(r"(.*) -> (.*)", line)
    modType = m.group(1)
    outputs = m.group(2).split(", ")

    if modType == "broadcaster":
        return Broadcaster("broadcaster", outputs)

    if modType[0] == "%":
        return FlipFlop(modType[1:], outputs)
    elif modType[0] == "&":
        return Conjunction(modType[1:], outputs)


class Module:
    TYPE_NONE = "none"
    TYPE_BROADCASTER = "broadcaster"
    TYPE_FLIPFLOP = "flip-flop"
    TYPE_CONJUNCTION = "conjunction"

    def __init__(self, name, outputs) -> None:
        self.type = -1
        self.state = 0
        self.name = name
        self.outputs = outputs
        self.inputs = {}

        self._setType()


    def _setType(self):
        self.type = Module.TYPE_NONE


    def __str__(self) -> str:
        return f"{self.type}  ({self.inputs}) -> {self.state} -> {self.outputs}"


    def addModulesLookup(self, modules):
        self.modules = modules


    def registerInput(self, inputModule):
        # print(f"registering input {inputModule}")
        self.inputs[inputModule.name] = 0


    def process(self):
        outputs = []
        low = 0
        high = 0
        for o in self.outputs:
            # print(f"out ({self.name}) - {self.state}")
            if self.state == 0:
                low += 1
            else:
                high += 1
            if o in self.modules and self.modules[o].sent(self):
                outputs.append(self.modules[o])

        return outputs, low, high

    def sent(self, inputModule) -> bool:
        raise NotImplementedError("you need to implement sent()")


class Broadcaster(Module):
    def _setType(self):
        self.type = Module.TYPE_BROADCASTER


class FlipFlop(Module):
    def _setType(self):
        self.type = Module.TYPE_FLIPFLOP


    def sent(self, inputModule) -> bool:
        if inputModule.state == 1:
            return False
        else:
            self.state = (self.state + 1) % 2
            return True


class Conjunction(Module):
    def _setType(self):
        return Module.TYPE_CONJUNCTION


    def sent(self, inputModule) -> bool:
        self.inputs[inputModule.name] = inputModule.state

        s = 1
        for i in self.inputs:
            s = min(s, self.inputs[i])
        self.state = (s + 1) % 2

        return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing input file name")
        exit

    main(sys.argv[1])
