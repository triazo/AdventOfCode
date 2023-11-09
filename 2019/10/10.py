#!/usr/bin/python

import sys
import re
import math
import queue
import copy

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def mod(num, length):
    if num < 0:
        return num + length
    return num % length

def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1])

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def count_visible(asteroids, point):
    #print("--Evaluating %s"%str(point))
    asts = copy.deepcopy(asteroids)

    visible_count = 0
    for y in range(len(asteroids)):
        for x in range(len(asteroids[y])):
            if asts[y][x] == '.':
                continue
            #print("Looking at %s"%str((y, x)))
            if (y, x) == point:
                continue
            # Find differences - we will go *from point* *to the other*
            delta = (y - point[0], x - point[1])

            # Find GCD of the two points
            d = gcd(abs(delta[0]), abs(delta[1]))

            # Divide by GCD to find step
            step = (delta[0] / d, delta[1] / d)

            #print("From %s to %s, the step is %s, %d"%(str(point), str((y,x)), str(step), d))
            # Step from point to dest, check if there are asteroids in the way
            p = (point[0] + step[0], point[1] + step[1])
            while p != (y, x):
                #print("Trying: %s"%str(p))
                if asts[p[0]][p[1]] == '#':
                    break
                # check
                p = (p[0] + step[0], p[1] + step[1])

            # If no, increment counter
            if p == (y, x):
                visible_count += 1

    return visible_count


def find_angles(asteroids, point):
    asts = copy.deepcopy(asteroids)

    angles = []

    visible_count = 0
    for y in range(len(asteroids)):
        for x in range(len(asteroids[y])):
            if asts[y][x] == '.':
                continue
            #print("Looking at %s"%str((y, x)))
            if (y, x) == point:
                continue
            # Find differences - we will go *from point* *to the other*
            delta = (y - point[0], x - point[1])

            # Find GCD of the two points
            d = gcd(abs(delta[0]), abs(delta[1]))

            # Divide by GCD to find step
            step = (delta[0] / d, delta[1] / d)

            #print("From %s to %s, the step is %s, %d"%(str(point), str((y,x)), str(step), d))
            # Step from point to dest, check if there are asteroids in the way
            p = (point[0] + step[0], point[1] + step[1])
            while p != (y, x):
                #print("Trying: %s"%str(p))
                if asts[p[0]][p[1]] == '#':
                    break
                # check
                p = (p[0] + step[0], p[1] + step[1])

            # If no, find angle
            if p == (y, x):
                visible_count += 1
                angle = math.degrees(math.atan2(delta[1], -1 * delta[0]))
                if angle < 0:
                    angle += 360
                angles.append((angle, p))

    return angles

def main():
    sys.setrecursionlimit(2200)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]

    asteroids = []
    for y, line in enumerate(lines):
        asteroids.append([])
        for c in line:
            asteroids[y].append(c)

    max_point = (0, 0)
    max_visible = 0
    for y in range(len(asteroids)):
        for x in range(len(asteroids[y])):
            if asteroids[y][x] == ".":
                continue
            visible = count_visible(asteroids, (y, x))
            #print("%s produced %d"%(str((y,x)), visible))
            if visible > max_visible:
                max_visible = visible
                max_point = (y, x)

    print(max_point, max_visible)

    angles = sorted(find_angles(asteroids, max_point))
    print(angles)
    print(angles[199])
    print(len(angles))



if __name__ == "__main__":
    main()
