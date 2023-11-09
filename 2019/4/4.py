#!/usr/bin/python

import sys
import re
import queue

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def mod(num, length):
    if num < 0:
        return num + length
    return num % length

def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1])

def test(i):
    si = str(i)
    for ci in range(len(si)-1):
        if int(si[ci]) > int(si[ci+1]):
            return False
    mark = False
    for ci in range(len(si)-1):
        if si[ci] == si[ci+1]:
            if ci == 4 or si[ci+1] != si[ci+2]:
                if ci == 0 or si[ci-1] != si[ci]:
                    return True


    # for ci in range(len(si)-2):
    #     if si[ci] == si[ci+1] and si[ci+1] == si[ci+2]:
    #         mark = False

    return mark

def main():

    sys.setrecursionlimit(2200)

    # lines = []
    # with open(sys.argv[1], 'r') as f:
    #     lines = f.read().split('\n')[:-1]

    inpt=(134792,675810)
    count = 0
    for i in range(inpt[0],inpt[1]):
        if test(i):
            count += 1

    print(count)

if __name__ == "__main__":
    main()
