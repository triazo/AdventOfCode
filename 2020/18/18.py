#!/usr/bin/python

import sys
import re
import queue

from utils import *

def parseterm(l, i):
    c = l[i]
    if c == "(":
        return myeval(l, i+1)
    elif c in "0123456789":
        return (int(c), i + 1)
    print(c)



ops = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
}

def myeval(l, i):
    a, i = parseterm(l, i)
    products = []
    while i < len(l):
        i += 1 # Always a space after the first term
        op = l[i]
        i += 1 # op
        i += 1 # space
        b, i = parseterm(l, i)
        #print(op, i, l[i])

        if op == "+":
            a = ops[op](a, b)
        else:
            products.append(a)
            a = b

        if i >=len(l) or l[i] == ")" :
            for p in products:
                a *= p
            return (a, i + 1)


def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 18)

    total = 0
    for line in lines:
        result, i = myeval(line, 0)
        total += result
        print(result)

    print(total)


if __name__ == "__main__":
    main()
