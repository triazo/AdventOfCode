#!/usr/bin/python

import sys
import re
import queue

from utils import *

def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2015, 1)

    l = lines[0]
    for i in range(len(l)):
        if l[:i].count('(') - l[:i].count(')') == -1:
            print(i)


if __name__ == "__main__":
    main()
