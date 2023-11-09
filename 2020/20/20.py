#!/usr/bin/python

import sys
import re
import queue
import math

from utils import *

class Connection:
    def __init__(self, fromtile, totile, fromside, toside, flip):
        self.fromtile = fromtile
        self.totile = totile
        self.fromside = fromside
        self.toside = toside
        self.flip = flip

    def __str__(self):
        s="%d:%d->%d:%d%s"%(self.fromtile.ident,  self.fromside, self.totile.ident, self.toside, ("", "F")[self.flip])
        return s


class Tile:
    def __init__(self, data, ident):
        self.data = data
        self.ident = ident

        self.setsides()

    def setsides(self):
        t = self.data
        sides = []
        sides.append(t[0]) # Top
        sides.append("".join(l[-1] for l in t)) # Right Side
        sides.append("".join(c for c in reversed(t[-1]))) # Left side from bottom
        sides.append("".join(l[0] for l in reversed(t))) # Bottom

        self.sides = sides
        self.connections = []

    def check_against(self, othertile):
        if othertile is self:
            return
        for i, s in enumerate(self.sides):
            for j, s2 in enumerate(othertile.sides):
                if s == s2:
                    self.connections.append(Connection(self, othertile, i, j, True))
                if s[::-1] == s2:
                    self.connections.append(Connection(self, othertile, i, j, False))

    def get_side(self, side, rotation, flip):
        # flipped bit means it's horizontally flipped before rotationn
        # First undo rotation
        ns = (8 + side - rotation)%4
        if flip:
            newside = (4 - ns)%4
        else:
            newside = ns

        print(side, rotation, flip, newside)
        for c in self.connections:
            if c.fromside == newside:
                return c


    def get_side_tile(self, tile):
        for c in self.connections:
            if c.totile == tile:
                return c

def flip_board(board):
    return list(l[::-1] for l in board)

def rotate_board(board, n):
    """rotates a tile 90 degrees, n times"""
    result = board
    for rotation in range(n):
        newtile = []
        for i in range(len(board)):
            newtile.append("".join(l[i] for l in reversed(result)))
        result = newtile
    return result

tiles = {}

def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 20, )

    titleregex=r"^Tile ([0-9]+):$"

    for line in lines:
        m = re.match(titleregex, line)
        if m:
            tileno = int(m.groups()[0])
            tile = []
            continue
        if line == "":
            tiles[tileno] = Tile(tile, tileno)
            continue
        tile.append(line)

    sidelen = int(math.sqrt(len(tiles)))
    #print(len(tiles))

    for t in tiles:
        for t2 in tiles:
            tiles[t].check_against(tiles[t2])

    starttile = 0
    total = 1
    for t in tiles:
        if len(tiles[t].connections) == 2:
            total *= t
            starttile = t

    print(total)
    #starttile = 1951
    print(starttile)

    for c in tiles[starttile].connections:
        print(c)

    # orient starting tile
    starting_rotation = ((3 + 4) - max(c.fromside for c in tiles[starttile].connections))%4
    print(starting_rotation)

    board = {}
    board[(0,0)] = (starttile, starting_rotation, True)

    for x in range(sidelen):
        for y in range(sidelen):
            # Only need to go right and down yay
            t = board[(x, y)][0]
            r = board[(x, y)][1]
            f = board[(x, y)][2]

            if y+1<sidelen:
                tile = tiles[t]
                # go down
                c = tile.get_side(2, r, f)
                if not c:
                    print("bad c, looking for side %d with rotation %s"%(2, (r, f)))
                    print(board)
                    for conn in tile.connections:
                        print(conn)
                print(c)

                # find new rotation
                newflip = f
                if c.flip:
                    newflip = not f
                # TODO: figure out normal case rotation and flip case rotation,
                # figure out how the dest tile should be rotated.
                # Rotate it to side 0

                new_rotation = (8 + (-1, 1)[newflip] * c.toside) % 4
                print(c, new_rotation, newflip)

                board[(x, y+1)] = (c.totile.ident, new_rotation, newflip)

            # go right
            if x+1 < sidelen:
                tile = tiles[t]
                c = tile.get_side(1, r, f)
                if not c:
                    print("bad c, looking for side %d with rotation %s"%(1, (r, f)))
                    print(board)
                    for conn in tile.connections:
                        print(conn)
                print(c)

                newflip = f
                if c.flip:
                    newflip = not f

                new_rotation = (8 + 3 +  (-1, 1)[newflip] * c.toside) % 4
                print(c, new_rotation, newflip)

                if (x+1, y) in board:
                    if board[(x+1, y)] != (c.totile.ident, new_rotation, newflip):
                        print("ERROR")
                board[(x+1, y)] = (c.totile.ident, new_rotation, newflip)


    print(board)
    # print(board[(0,0)], board[(11,0)], board[(0,11)], board[(11,11)])
    # total = 1
    # for to in [board[(0,0)], board[(11,0)], board[(0,11)], board[(11,11)]]:
    #     total *= to[0]
    #print(total)


    tilesize = len(tiles[starttile].data)
    finalboard = []
    for y in range(sidelen):
        for i in range(tilesize - 2):
            s = ""
            for x in range(sidelen):
                b = board[(x, y)]
                data = tiles[b[0]].data
                if b[2]:
                    data = flip_board(data)
                data = rotate_board(data, b[1])
                s = "".join([s, data[i+1][1:-1]])
            #s = "".join(tiles[board[(x, y)][0]].data[i+1][1:-1] for x in range(sidelen))
            finalboard.append(s)
            print(s)

    dragon ="""
                  #
#    ##    ##    ###
 #  #  #  #  #  #   """
    dragon = dragon.split("\n")[1:]
    dragonheight = 3
    dragonlen = len(dragon[0])
    dragonparts = set()
    dragonspots = set()
    for i, l in enumerate(dragon):
        for j, c in enumerate(l):
            if c == "#":
                dragonparts.add((j, i))
    print(dragonparts)
    for flip in (False, True):
        dragonboardf = finalboard
        if flip:
            dragonboardf = flip_board(finalboard)
        for rotation in range(4):
            dragonboard = rotate_board(dragonboardf, rotation)
            for x in range(len(finalboard[0])-dragonlen):
                for y in range(len(finalboard[0])-dragonheight):
                    dragonhere = True
                    for dp in dragonparts:
                        np = vadd(dp, (x, y))
                        dragonhere = dragonhere and dragonboard[np[0]][np[1]] == "#"
                        if not dragonhere:
                            break
                    if dragonhere:
                        print("Foun a dragon!", (x, y), flip, rotation)
                        for dp in dragonparts:
                            np = vadd(dp, (x, y))
                            dragonspots.add(np)

    print(len(dragonspots))

    full_rough = sum(l.count("#") for l in finalboard)
    print(full_rough - len(dragonspots))


if __name__ == "__main__":
    main()
