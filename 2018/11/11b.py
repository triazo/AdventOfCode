#!/usr/bin/python

import sys
import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'

HEIGHT, WIDTH = (300, 300)

def mod(num, length):
    if num < 0:
        return num + length
    return num % length


def main():
    serial = 4842

    grid = [[power(x, y, serial) for y in range(300)] for x in range(300)]

    highest = 0
    hc = (0, 0, 0)
    counter = 0
    for x in range(HEIGHT - 3):
        for y in range(WIDTH - 3):
            counter += 1
            if counter % 1000 == 0:
                print(counter)

            ts = grid[x][y]
            for size in range(2, 300 - max(x, y)):
                xi = x + size - 1
                for yi in range(y, y+size):
                    ts += grid[xi][yi]
                yi = y + size - 1
                for xi in range(x, x+size-1):
                    ts += grid[xi][yi]

                if ts > highest:
                    highest = ts
                    hc = (x, y, size)
                    print('new highest is %s at %d' %(str(hc, ts)))


    print(hc, highest)

if __name__ == "__main__":
    main()
