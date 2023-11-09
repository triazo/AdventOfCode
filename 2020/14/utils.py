#!/usr/bin/python

import sys
import re
import queue
import requests

alphabet = 'abcdefghijklmnopqrstuvwxyz'

four_directions_2d = [(0, 1), (-1, 0), (0, -1), (1, 0)]
eight_directions_2d = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

two_d_transforms = [
        lambda y, x: (y, x),
        lambda y, x: (-x, y),
        lambda y, x: (-y, -x),
        lambda y, x: (x, -y)
    ]

def getlines(year, number, s=""):
    cookies = {"session": "53616c7465645f5f0457c13656d13ca45b713be2cacb74c62d445b7b3ce833ba3b936065906cc8f9d315600b22c25cf9"}
    try:
        filename = "input" if s == "" else s
        f = open(filename)
        lines = f.read().split('\n')[:-1]
        f.close()
        return lines
    except IOError:
        if s != "":
            print("s %s not found"%s)
            sys.exit(1)
        inlines = requests.get("https://adventofcode.com/%d/day/%d/input"%(year, number), cookies = cookies)
        if not inlines.ok:
            print("Request bad: %d"%inlines.status_code)
            sys.exit(1)
        with open("input", "w") as f:
            f.write(inlines.content.decode('utf-8'))
        return  inlines.content.decode('utf-8').split('\n')[:-1]

def lines_as_grid(lines):
    newlines = []
    for l in lines:
        newlines.append(list([c for c in l]))

def grid_bounds_check(grid, point):
    xmax = len(grid[0])
    ymax = len(grid)

    y = point[0]
    x = point[1]

    if y < 0 or x < 0:
        return False
    if y >= ymax or x >= xmax:
        return False
    return True


def mod(num, length):
    if num < 0:
        return num + length
    return num % length

def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1])

def vmul(a, b):
    return (a[0] * b[0], a[1] * b[1])
