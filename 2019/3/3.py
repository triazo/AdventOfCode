#!/usr/bin/python3

import sys
import re
import queue

from shapely.geometry import LineString

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def mod(num, length):
    if num < 0:
        return num + length
    return num % length

def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1])

def pdiff(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def test_intersect(a1, a2, b1, b2):
    line1=LineString([a1, a2])
    line2=LineString([b1, b2])

    i = line1.intersection(line2)
    if i:
        return (i.x, i.y)
    return None

def main():

    sys.setrecursionlimit(2200)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]

    operations = {
        "U": lambda p, a: (p[0], p[1]+a),
        "D": lambda p, a: (p[0], p[1]-a),
        "L": lambda p, a: (p[0]-a, p[1]),
        "R": lambda p, a: (p[0]+a, p[1])
    }

    trails = []
    for line in lines:
        trail = [(0,0)]
        for op in line.split(','):
            f = op[0]
            a = int(op[1:])
            trail.append(operations[f](trail[-1], a))
        trails.append(trail)


    mindistance = 99999999999999
    one_intersect = 0
    two_intersect = 0
    for i in range(len(trails[0])-1):
        # for k in range(i):
        #     res = test_intersect(trails[0][i], trails[0][i+1], trails[0][k], trails[0][k+1])
        #     if res:
        #         one_intersect += 1
        for j in range(len(trails[1])-1):
            # for k in range(j):
            #     res = test_intersect(trails[1][j], trails[1][j+1], trails[1][k], trails[1][k+1])
            #     if res:
            #         two_intersect += 1

            res = test_intersect(trails[0][i], trails[0][i+1], trails[1][j], trails[1][j+1])
            if res:
                if res == (0, 0):
                    continue

                s1=sum(pdiff(trails[0][ii], trails[0][ii+1]) for ii in range(i)) + pdiff(res, trails[0][i])
                s2=sum(pdiff(trails[1][ii], trails[1][ii+1]) for ii in range(j)) + pdiff(res, trails[1][j])

                # Account for self intersections
                self_intersects = one_intersect + two_intersect
                self_intersects = 0

                print(res, s1 + s2 - self_intersects )
                d = s1 + s2 - self_intersects
                if d < mindistance:
                    mindistance = d

    print(mindistance)

if __name__ == "__main__":
    main()
