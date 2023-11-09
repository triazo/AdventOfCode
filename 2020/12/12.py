#!/usr/bin/python

import sys
import re
import queue

from utils import *

def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 12)

    # y, x
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    direction_offset = 360 * 1000

    position = (-1, 10)

    for l in lines:
        c = l[0]
        arg = int(l[1:])
        d = direction_offset
        if c == 'E':
            d = 0
        if c == 'S':
            d = 1
        if c == 'W':
            d = 2
        if c == 'N':
            d = 3
        if c == "R":
            direction_offset += arg//90
            continue
        if c == "L":
            direction_offset -= arg//90
            continue
        for i in range(arg):
            position = vadd(position, directions[d%4])
        print(position)

    print(abs(position[0]) + abs(position[1]))



if __name__ == "__main__":
    main()
