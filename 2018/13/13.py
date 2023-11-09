#!/usr/bin/python

import sys
import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def mod(num, length):
    if num < 0:
        return num + length
    return num % length

def add(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def printtrack(track, carts):
    for y, line in enumerate(track):
        for x, c in enumerate(line):
            if not (y, x) in carts:
                sys.stdout.write(c)
            else:
                sys.stdout.write('^>v<'[directions.index(carts[(y, x)][0])])
        sys.stdout.write('\n')

def tick(carts, tracks):
    turns = [lambda (x, y):  (y * -1, x ), lambda (x, y): (x, y), lambda (x, y): (y, x * -1)]
    corners = {
        "/": lambda (x, y): (y * -1, x * -1),
        "\\": lambda (x, y): (y, x),
        }

    # Cart format is (direction, turn index)
    # Start running carts
    for c in sorted([c for c in carts]):
        if not c in carts:
            continue
        # first move the cart
        oldc = carts[c]
        nextpos = add(c, oldc[0])
        if nextpos in carts:
            print('found collision')
            print(nextpos)
            del carts[c]
            del carts[nextpos]

            continue


        # then turn the cart
        nt = tracks[nextpos[0]][nextpos[1]]
        if nt == '+':
            newdir = turns[oldc[1]](oldc[0])
            newturn = (oldc[1] + 1) % 3
            carts[nextpos] = (newdir, newturn)

        elif nt == '/' or nt == '\\':
            newdir = corners[nt](oldc[0])
            carts[nextpos] = (newdir, oldc[1])

        else:
            carts[nextpos] = (oldc[0], oldc[1])

        # Then change out the dict
        del carts[c]
    return (carts, tracks)

def main():
    # directions
    # ^ (-1, 0)
    # > (0, 1)
    # v (1, 0)
    # < (0, -1)


    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]

    tracks = [[c for c in line] for line in lines]
    carts = {}
    for y, row in enumerate(tracks):
        for x, c in enumerate(row):
            if c in '^>v<':
                carts[(y, x)] = (directions['^>v<'.index(c)], 0)
                tracks[y][x] = ('-','|')['^>v<'.index(c) % 2 == 0]

    i = 0
    while True:
        i += 1
        if i % 100 == 0:
            print(i)
        carts, tracks = tick(carts, tracks)
        if len(carts) == 1:
            print('one cart left')
            print(carts)
            sys.exit(0)
        #printtrack(tracks, carts)


    print(len(carts))

if __name__ == "__main__":
    main()
