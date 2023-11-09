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


def co(o, obj):
    if obj == 'COM':
        return ['COM']
    return co(o, o[obj]) + [obj]

def main():

    sys.setrecursionlimit(2200)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]

    o = {}
    o['COM'] = None
    for line in lines:
        center = line.split(')')[0]
        outer = line.split(')')[1]
        o[outer] = center

    san = co(o, 'SAN')
    you = co(o, 'YOU')

    same = 0
    for i in range(len(san)):
        if san[i] == you[i]:
            same = i
        else:
            break

    print((len(san)-i) + (len(you)-i))


if __name__ == "__main__":
    main()
