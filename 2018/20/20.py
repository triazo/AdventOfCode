#!/usr/bin/python

import sys
import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def mod(num, length):
    if num < 0:
        return num + length
    return num % length

def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1])

def traverse(rooms, starts, rex, starti):
    dirs = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1)
    }

    i = starti
    ps = starts
    ends = set()
    while True:
        if rex[i] == '|':
            ends = ends.union(ps)
            ps = starts
            i += 1
            continue

        if rex[i] == '(':
            i += 1
            ps, i = traverse(rooms, ps, rex, i)
            continue

        if rex[i] == ')':
            return (ends.union(ps), i + 1)

        if rex[i] == '$':
            return (ends.union(ps), i + 1)


        nps = set()
        for p in ps:
            np = vadd(p, dirs[rex[i]])
            rooms[p].add(np)
            if not np in rooms:
                rooms[np] = set(p)
            else:
                rooms[np].add(p)
            nps.add(np)
        ps = nps
        i += 1

def dfs(rooms, start):
    distances = {start: 0}
    curd = 0
    while True:
        tostarts = {p for p in distances if distances[p] == curd}
        curd += 1
        if len(tostarts) == 0:
            break
        toadds = set()
        for s in tostarts:
            toadds = toadds.union(rooms[s])
        realadds = {p for p in toadds if p in rooms and not p in distances}
        for p in realadds:
            distances[p] = curd

    farthest = sorted([(distances[p], p) for p in distances])[-1]

    farrooms = [p for p in distances if distances[p] >= 1000]
    print(len(farrooms))

    return(farthest)

def main():

    sys.setrecursionlimit(2200)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]


    rex = lines[0]

    rooms = {(0, 0): set()}

    i = 1
    p = (0, 0)
    r = traverse(rooms, set([(0,0)]), rex, i)
    print(r)
    print(rooms)
    print(len(rooms))
    print(dfs(rooms, (0, 0)))


if __name__ == "__main__":
    main()
