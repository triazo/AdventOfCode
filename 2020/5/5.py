#!/usr/bin/python

import sys
import re
import queue

from utils import *

def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 5)

    ns = []
    for l in lines:
        r = int(l[:7].replace('F', '0').replace('B','1'),2)
        c = int(l[7:].replace('L', '0').replace('R','1'),2)
        print(r*8 + c)
        ns.append(r*8 + c)

    print(max(ns))

    for i in range(864):
        if not i in ns:
            print(i)


if __name__ == "__main__":
    main()
