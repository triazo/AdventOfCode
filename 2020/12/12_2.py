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

    transforms = [
        lambda y, x: (y, x),
        lambda y, x: (-x, y),
        lambda y, x: (-y, -x),
        lambda y, x: (x, -y)
    ]


    position = (0, 0)
    way_position = (1, 10)

    for l in lines:
        c = l[0]
        arg = int(l[1:])
        print(l, position, way_position)
        if c == 'E':
            for i in range(arg):
                way_position = vadd(way_position, directions[0])
            continue
        if c == 'S':
            for i in range(arg):
                way_position = vadd(way_position, directions[1])
            continue
        if c == 'W':
            for i in range(arg):
                way_position = vadd(way_position, directions[2])
            continue
        if c == 'N':
            for i in range(arg):
                way_position = vadd(way_position, directions[3])
            continue


        if c == "F":
            for i in range(arg):
                position = vadd(position, way_position)
            continue

        if c == "R":
            way_position = transforms[arg//90](*way_position)
            continue
        if c == "L":
            way_position = transforms[4-(arg//90)](*way_position)
            continue


    print(position, way_position)
    print(abs(position[0]) + abs(position[1]))



if __name__ == "__main__":
    main()
