#!/usr/bin/python

import sys
import re
import queue
import requests

from utils import *

def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 2, samplefile="sampleinput")

    # lines = """1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# """.split("\n")[:-1]

    x = 0
    for l in lines:
        minl = int(l.split("-")[0])
        maxl = int(l.split("-")[1].split(" ")[0])
        letter = l.split(" ")[1].split(":")[0]
        pw = l.split(" ")[2]

        # if pw.count(letter) >= minl and pw.count(letter) <= maxl:
        #     x += 1
        if pw[minl-1] == letter or pw[maxl-1] == letter:
            if pw[minl-1] == letter and pw[maxl-1] == letter:
                continue
            x += 1


    print(x)

if __name__ == "__main__":
    main()
