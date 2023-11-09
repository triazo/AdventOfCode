#!/usr/bin/python

import sys
import re
import queue

from utils import *

four_directions_2d = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2015, 3)

    cardnals = ">v<^"
    delivered = {(0,0): 2}
    current = (0,0)
    current_ro = (0,0)
    for i, c in enumerate(lines[0]):
        if i%2 == 0:
            current = vadd(current, four_directions_2d[cardnals.index(c)])
            if not current in delivered:
                delivered[current] = 1
            else:
                delivered[current] += 1
        else:
            current_ro = vadd(current_ro, four_directions_2d[cardnals.index(c)])
            if not current_ro in delivered:
                delivered[current_ro] = 1
            else:
                delivered[current_ro] += 1


    print(len(delivered))





if __name__ == "__main__":
    main()
