#!/usr/bin/python

import sys
import re
import queue

from utils import *


def printstate(s):
    return
    for z in range(min(p[2] for p in s), max(p[2] for p in s) +1):
        print("")
        print(z)
        for y in range(min(p[1] for p in s), max(p[1] for p in s) +1):
            for x in range(min(p[0] for p in s), max(p[0] for p in s) +1):
                if (x, y, z) in s:
                    sys.stdout.write("#")
                else:
                    sys.stdout.write(".")
            sys.stdout.write("\n")

def main():

    sys.setrecursionlimit(2200)

    neighbors_3d= list((x, y, z, w) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2) for w in range(-1,2))
    neighbors_3d.remove((0,0,0,0))

    lines = getlines(2020, 17)

    active_state = {}

    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == "#":
                active_state[(x, y, 0, 0)] = "#"


    next_state = {}
    for i in range(6):
        printstate(active_state)
        for cell in active_state:
            if not active_state[cell] == "#":
                continue
            for c in (vadd4(d, cell) for d in neighbors_3d):
                count = 0
                for d in neighbors_3d:
                    if vadd4(d, c) in active_state:
                        count += 1

                if c in active_state and active_state[c] == "#":
                    if count == 2 or count == 3:
                        next_state[c] = "#"
                else:
                    if count == 3:
                        next_state[c] = "#"

            count = 0
            for d in neighbors_3d:
                if vadd4(d, cell) in active_state:
                    count += 1
            if cell in active_state and active_state[cell] == "#":
                if count == 2 or count == 3:
                    next_state[cell] = "#"
            elif count == 3:
                next_state[cell] = "#"

        active_state = next_state.copy()
        next_state = {}




    print(len(active_state))


if __name__ == "__main__":
    main()
