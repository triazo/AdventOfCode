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

def distance(a, b):
    s = 0
    for i in range(len(a)):
        s += abs(a[i] - b[i])
    return s

def main():

    sys.setrecursionlimit(2200)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]

    bots = {}
    for line in lines:
        r = r'pos=<(.+),(.+),(.+)>, r=(.+)'
        x, y, z, r = re.search(r, line).groups()
        bots[(int(x),int(y),int(z))] = int(r)

    bestbot = (0,0,0)
    bestr = 0
    for b in bots:
        if bots[b] > bestr:
            bestbot = b
            bestr = bots[b]

    print(bestbot, bestr)

    inrange = 0
    for bot in bots:
        # if bot == bestbot:
        #     continue
        if distance(bot, bestbot) <= bestr:
            inrange += 1
            print("In range: %s" % str(bot))
        else:
            print("Not in range: %s" % str(bot))

    print(inrange)

if __name__ == "__main__":
    main()
