#!/usr/bin/python

import sys
import re
import queue

from utils import *



def calc(lines, r, d):
    x = 0
    for i in range(0, len(lines), d):
        if lines[i][((i*r)//d)%len(lines[0])] == '#':
            x += 1

    return x

def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 3)


    l = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    x = 1
    for li in l:
        res = calc(lines, li[0], li[1])
        print(res)
        x = x * res
    print(x)




if __name__ == "__main__":
    main()
