#!/usr/bin/python

import sys
import re
import queue
import pulp
import itertools

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

    prob = pulp.LpProblem("problem", pulp.LpMaximize)
    counts = [pulp.LpVariable("c_%d"%i, lowBound=0, upBound=1, cat='Integer') for i in range(len(bots))]
    x,y,z = (pulp.LpVariable(c) for c in "xyz")
    totalCount = pulp.LpVariable("totalCount")

    prob += totalCount
    prob += totalCount == sum(counts)

    prob += totalCount == sum(counts)
    for i, (x_i, y_i, z_i) in enumerate(bots):
        r_i = bots[(x_i, y_i, z_i)]
        c_i = counts[i]
        for sign in itertools.product([-1, 1], repeat=3):
            prob += (
                sign[0] * (x - x_i) +
                sign[1] * (y - y_i) +
                sign[2] * (z - z_i)
            ) <= r_i + (1-c_i) * int(1e10)

    print(prob)
    status = prob.solve()
    print(pulp.LpStatus[status])
    print('x,y,z', pulp.value(x), pulp.value(y), pulp.value(z))
    print('distFromOrigin', abs(pulp.value(x)) + abs(pulp.value(y)) + abs(pulp.value(z)))
    print('totalCount', pulp.value(totalCount))




if __name__ == "__main__":
    main()
