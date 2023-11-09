#!/usr/bin/python

import sys
import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'

HEIGHT, WIDTH = (300, 300)

def mod(num, length):
    if num < 0:
        return num + length
    return num % length

def power(x, y, serial):

    tmp = str(((x + 10) * y + serial) * (x + 10))[-3]
    return int(tmp) - 5

def main():
    serial = 4842

    grid = [[power(x, y, serial) for y in range(300)] for x in range(300)]

    highest = 0
    hc = (0, 0)
    for x in range(HEIGHT - 3):
        for y in range(WIDTH - 3):
            for size in range(max(x, y), 300)
            gp = 0
            for xi in range(x, x+3):
                for yi in range(y, y+3):
                    gp += grid[xi][yi]
            if gp > highest:
                highest = gp
                hc = (x, y)

    print(hc)

if __name__ == "__main__":
    main()
