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

def findfuel(mass):
    m = max((mass//3) - 2, 0)
    if m == 0:
        return 0

    return m + findfuel(m)

def main():

    sys.setrecursionlimit(2200)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]

    total = 0
    for line in lines:
        total += findfuel(int(line))

    print(total)

if __name__ == "__main__":
    main()
