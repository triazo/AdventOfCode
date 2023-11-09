#!/usr/bin/python

import sys

lines = open(sys.argv[1],'r').read().split('\n')

left = 'ABC'
right = 'XYZ'

lookup = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}


total = 0
def score(l, r):
    return r + (((r - l) % 3 + 1) % 3) * 3

def hand(l, r):
    return ["", ((l - 1) - 1)%3 + 1, l, (((l + 1) - 1) % 3) + 1][r]

for match in lines:
    if match == "":
        continue
    sl = match.split(' ')
    l = lookup[sl[0]]
    r = hand(l, lookup[sl[1]])
    # if l == r:
    #     total += 3
    #     total += r
    # elif l == r-1:
    #     total += 6
    #     total += r
    # elif r == l-1:
    #     total += 0
    #     total += r
    # elif l == r-2:
    #     total += 0
    #     total += r
    # elif r == l-2:
    #     total += 6
    #     total += r
    # else:
    total += score(l, r)


print(total)
