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


def main():

    sys.setrecursionlimit(2200)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]

    #numbers = [1721,979,366,299,675,1456]
    numbers = [int(i) for i in lines]

    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == 2020:
                    print(i * j * k)


if __name__ == "__main__":
    main()
