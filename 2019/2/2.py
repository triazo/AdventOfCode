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

def run(o, n, v):
    ops = [x for x in o]
    ops[1] = n
    ops[2] = v
    i = 0
    while True:
        if ops[i] == 1:
            ops[ops[i+3]] = ops[ops[i+1]] + ops[ops[i+2]]
            i += 4
        elif ops[i] == 2:
            ops[ops[i+3]] = ops[ops[i+1]] * ops[ops[i+2]]
            i += 4
        elif ops[i] == 99:
            break

    return ops[0]

def main():

    sys.setrecursionlimit(2200)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split(',')
    ops = [int(x) for x in lines]

    for n in range(100):
        for v in range(100):
            result = run(ops, n, v)
            if result == 19690720:
                print(100 * n + v)


if __name__ == "__main__":
    main()
