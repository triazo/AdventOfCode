#!/usr/bin/python

import sys
import re
import queue

from utils import *

# x, y
six_directions_hex = {"sw": (0, -1), "se": (1,-1), "e":(1, 0), "ne": (0,1), "nw":(-1, 1), "w": (-1, 0)}

def parse_directions(l):
    if len(l) == 0:
        return []
    directions = ["sw","se","ne","nw","e","w"]
    for d in directions:
        if l.startswith(d):
            return [d] + parse_directions(l[len(d):])


def simulate_day(tiles):
    newtiles = tiles.copy()
    for t in tiles:
        if tiles[t] == True:
            continue
        for d in list(six_directions_hex[s] for s in six_directions_hex) + [(0,0)]:
            current = vadd(t, d)
            black_tiles = 0
            for nd in list(six_directions_hex[s] for s in six_directions_hex):
                nc = vadd(current, nd)
                if nc in tiles and tiles[nc] == False:
                    black_tiles += 1

            if not current in tiles or tiles[current] == True:
                if black_tiles == 2:
                    newtiles[current] = False

            if current in tiles and tiles[current] == False:
                if black_tiles == 0 or black_tiles > 2:
                    newtiles[current] = True

    return newtiles


def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 24)

    tiles = {}
    for l in lines:
        directions = parse_directions(l)
        print(directions)
        current = (0,0)
        for d in directions:
            current = vadd(six_directions_hex[d], current)

        if not current in tiles:
            tiles[current] = False #False == black - it starts white, so first flip will make it black
        else:
            tiles[current] = not tiles[current]

    total = 0
    for t in tiles:
        if tiles[t] == False:
            total += 1
    print(total)


    for i in range(100):
        tiles = simulate_day(tiles)


    total = 0
    for t in tiles:
        if tiles[t] == False:
            total += 1
    print(total)


if __name__ == "__main__":
    main()
