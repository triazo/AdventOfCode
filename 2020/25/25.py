#!/usr/bin/python

import sys
import re
import queue

from utils import *

def transform(subject, loop_size):
    s = subject
    for i in range(loop_size):
        s = (s*subject) % 20201227

    return s

def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 25)

    k1 = int(lines[0])
    k2 = int(lines[1])

    subject=7
    s=subject
    i = 0
    while s != k1:
        s = (s*subject) % 20201227
        #print(s, k1)
        i += 1
    sk1 = i

    s=7
    i = 0
    while s != k2:
        s = (s*subject) % 20201227
        #print(s, k2)
        i += 1
    sk2 = i

    print(transform(7, 11))
    print(transform(7, 8))

    print(transform(k1, sk2))
    print(transform(k2, sk1))




if __name__ == "__main__":
    main()
