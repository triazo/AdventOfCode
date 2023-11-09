#!/usr/bin/python

import sys
import re
import queue

from utils import *

def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2015, 2)

    total = 0
    ribbon = 0
    for l in lines:
        n = l.split("x")
        l = int(n[0])
        w = int(n[1])
        h = int(n[2])

        ss = min(l*w, w*h, h*l)

        rb = (2*l + 2*h + 2*w) - max(2*l,2*h,2*w)
        rb += l*w*h

        total += 2*l*w + 2*w*h + 2*h*l + ss
        ribbon += rb

    print(total)
    print(ribbon)

if __name__ == "__main__":
    main()
