#!/usr/bin/python

import sys
import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def mod(num, length):
    if num < 0:
        return num + length
    return num % length

def printmap(points):
    lowest = 9999999999
    lp = (0, 0)
    for p in points:
        if p[0] + p[1] < lowest:
            lowest = p[0] + p[1]
            lp = p

    for y in range(lp[1] - 20, lp[1] + 30):
        print(''.join(['#' if (x, y) in points else '-' for x in range(lp[0] - 20, lp[0] + 80)]))


def main():
    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]

    points = {}
    for line in lines:
        regex = r'position=<(.*), (.*)> velocity=<(.*), (.*)>'
        x, y, xp, yp = tuple(int(x.strip()) for x in re.search(regex, line).groups())
        #print(tuple(int(x.strip()) for x in re.search(regex, line).groups()))
        points[(x, y)] = (xp, yp)

    tick = 0
    while True:
        if tick % 1000 == 0:
            print(tick)

        # Move points
        newpoints = {}
        for point in points:
            dx, dy = points[point]
            newpoint = (point[0] + dx, point[1] + dy)
            newpoints[newpoint] = points[point]

        points = newpoints

        # Calculate average distance
        cx, cy = (0, 0)
        for point in points:
            cx += point[0]
            cy += point[1]
        cx = cx / len(points)
        cy = cy / len(points)

        dcx, dcy = (0, 0)
        for point in points:
            dcx += abs(cx - point[0])
            dcy += abs(cy - point[1])
        dcx = dcx / len(points)
        dcy = dcy / len(points)

        distance = dcx + dcy

        # Conditionally print
        if distance < 500:
            print("Distance is %d on tick %d" % (distance, tick))
            printmap(points)

        tick += 1



if __name__ == "__main__":
    main()
