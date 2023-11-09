#!/usr/bin/python

import sys
import re
import queue
import math

from utils import *

def rotate_tile(tile, n):
    """rotates a tile 90 degrees, n times"""
    result = tile
    for rotation in range(n):
        newtile = []
        for i in range(len(tile)):
            newtile.append("".join(l[i] for l in reversed(result)))
        result = newtile
    return result

# class Tile:
#     def __init__(self, data, ident):
#         self.data = data
#         self.ident = ident

def sides(t):
    sides = []
    sides.append(t[0])
    # sides.append(rotate_tile(t, 1)[0])
    # sides.append(rotate_tile(t, 2)[0])
    # sides.append(rotate_tile(t, 3)[0])
    sides.append("".join(l[-1] for l in t))
    sides.append("".join(l[0] for l in reversed(t)))
    sides.append("".join(c for c in reversed(t[-1])))
    return sides

def checktiles(t1, t2):
    s2 = sides(t2)
    for i, s in enumerate(sides(t1)):
        if s[::-1] in s2:
            return (i, s2.index(s[::-1]), False)
        if s in s2:
            return (i, s2.index(s), True)
    return None

# Tile struct is (tile_number, (tile_rotation, tile_flipped))
def checktiles_fixed(tilestruct, t2):
    #print(tilestruct)
    tileno1, t1rot = tilestruct
    t1 = tiles[tileno1]
    s1 = sides(t1)[(t1rot[0] + 3) % 4]
    if t1rot[1]:
        s1 = s1[::-1]

    ### ASSUMING THERE IS ONLY ONE MATCH PER SET OF TILES
    s2 = sides(t2)
    if s1 in s2:
        return(s2.index(s1), True)
    if s1[::-1] in s2:
        return(s2.index(s1[::-1]), False)

def printtile(tile):
    for line in tile:
        print(" ".join(c for c in line))

def try_position(board, tilepool, index, trytile):
    if index >= 2:
        print(board, index, trytile, sidelen)
    x, y = (index%sidelen, index//sidelen)
    workingrot = None
    for rot, npos in enumerate(vadd((x, y), d) for d in four_directions_2d):
        if not npos in board:
            continue
        if index >= 2:
            print("Checking ", board[npos], trytile)
        tilerot = checktiles_fixed(board[npos], tiles[trytile])
        if not tilerot:
            continue
        if not workingrot:
            workingrot = tilerot
        if workingrot != tilerot:
            # Two different working rotations is still not valid
            return False

    if not workingrot and index != 0:
        return False
    # If it hasn't returned yet, assume it works here
    board[(x, y)] = (trytile, workingrot)
    tilepool.remove(trytile)

    possible = False

    for next_tile in tilepool:
        possible = possible or try_position(board, tilepool, index + 1, next_tile)
        if possible:
            break

    if len(tilepool) == 0:
        print("FOUND")
        print(board)
        return True

    if not possible:
        # Barked down the wrong tree, return
        tilepool.add(trytile)
        del board[(x, y)]
        return False

    print("How did it get here")
    return possible


tiles = {}
sidelen = 3

def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 20, s="sampleinput")

    titleregex=r"^Tile ([0-9]+):$"
    for line in lines:
        m = re.match(titleregex, line)
        if m:
            tileno = int(m.groups()[0])
            tile = []
            continue
        if line == "":
            tiles[tileno] = tile
            continue
        tile.append(line)

    sidelen = math.sqrt(len(tiles))
    print(len(tiles))

    # 12 by 12 matrix: recursively try building it:
    board = {}
    tilepool = {t for t in tiles}
    possible = False
    for t in tiles:
        if t != 1951:
            continue
        tilepool.remove(t)
        for flip in (False, True):
            for rotation in range(4):
                rotstruct = (rotation, flip)
                board[(0,0)] = (t, rotstruct)
                for t2 in tilepool:
                    possible = possible or  try_position(board, tilepool, 1, t2)
                    if possible:
                        break
                if possible:
                    break
            if possible:
                break
        tilepool.add(t)
        if possible:
            break
        tilepool.add(t)

    print(possible)
    print(board)




if __name__ == "__main__":
    main()
