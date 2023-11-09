#!/usr/bin/python

import sys
import re
import queue

from utils import *

def find_color(reqs, curcolor, destcolor):
    counter = 0
    for c in reqs[curcolor]:
        if c[0] == destcolor:
            print("found", c[1])
            counter += c[1]
        counter += find_color(reqs, c[0], destcolor)
    return counter

def count(reqs, rootcolor):
    counter = 1
    for c in reqs[rootcolor]:
        counter += c[1] * count(reqs, c[0])

    return(counter)

def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 7)

    lineregex = r"^(?P<root>([a-z]| )+) bags contain ([0-9]+ ([a-z]| )+ bags?,? ?)*\.$"
    startregex = r"^(?P<root>([a-z]| )+) bags contain .*$"
    eachregex = r"([0-9]+) (([a-z]| )+) bag"

    reqs = {}
    for l in lines:
        mstart = re.match(startregex, l)
        if not mstart:
            continue
        color = mstart.groupdict()["root"]
        reqs[color] = []

        rest = re.findall(eachregex, l)
        for r in rest:
            n = r[0]
            c = r[1]
            reqs[color].append((c, int(n)))


    rq = "shiny gold"

    x = 0
    for root in reqs:
        print(root, reqs[root])
        if find_color(reqs, root, rq) != 0:
            x += 1
    print(x)

    print(count(reqs, rq) - 1)


if __name__ == "__main__":
    main()
