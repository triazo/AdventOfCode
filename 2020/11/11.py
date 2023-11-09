#!/usr/bin/python

import sys
import re
import queue

from utils import *

def bounds_check(coord, bounds):
    y, x = bounds
    if coord[0] < 0 or coord[1] < 0:
        return False
    if coord[0] >= y:
        return False
    if coord[1] >= x:
        return False
    return True

def printfloor(state):
    for i in range(len(state)):
        print(''.join(state[i]))

# def stateequals(a, b):
#     for i, l

def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 11)

    state = lines

    directions = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

    newstate = []

    bounds = (len(state), len(state[0]))

    for iteration in range(500):
        for y in range(len(state)):
            newline=[]
            for x in range(len(state[0])):
                cell = (y, x)
                current = state[y][x]
                occupied = 0
                for d in directions:
                    test = vadd(cell, d)
                    while bounds_check(test, bounds) and state[test[0]][test[1]] == '.':
                        test = vadd(test, d)
                    if bounds_check(test, bounds) and state[test[0]][test[1]] == '#':
                        occupied += 1

                nextone = current
                if current == "L" and occupied == 0:
                    nextone = "#"
                elif current == "#" and occupied >= 5:
                    nextone = "L"
                newline.append(nextone)
            newstate.append(newline)
        print(iteration)
        #printfloor(newstate)
        state = newstate
        newstate = []

    print(sum(l.count("#") for l in state))


if __name__ == "__main__":
    main()
