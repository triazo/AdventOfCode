#!/usr/bin/python

import sys
import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def mod(num, length):
    if num < 0:
        return num + length
    return num % length

def getgrid(grid, p):
    if p[0] < 0 or p[1] < 0:
        return ' '
    if p[0] >= len(grid):
        return ' '
    if p[1] >= len(grid[0]):
        return ' '
    return grid[p[0]][p[1]]

def mkhash(grid):
    return ''.join([''.join(row) for row in grid])

def adj(grid, p):
    l =  [getgrid(grid, (p[0]-1,p[1])), getgrid(grid, (p[0]-1,p[1]+1)),
          getgrid(grid, (p[0],p[1]+1)), getgrid(grid, (p[0]+1,p[1]+1)),
          getgrid(grid, (p[0]+1,p[1])), getgrid(grid, (p[0]+1,p[1]-1)),
          getgrid(grid, (p[0],p[1]-1)), getgrid(grid, (p[0]-1,p[1]-1))]
    l = [item for item in l if item != ' ']
    return l

def printgrid(grid):
    for row in grid:
        print(''.join(row))

def main():

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]

    grid = []
    for line in lines:
        t = []
        for c in line:
            t.append(c)
        grid.append(t)

    grids = {}

    i = 0
    while i < 1000000000:
        newgrid = []
        for y, row in enumerate(grid):
            ngrow = []
            for x, c in enumerate(row):
                nc = c
                # print(y,x)n
                # print(adj(grid, (y,x)))
                if c == '.' and adj(grid, (y,x)).count('|') >= 3:
                    nc = '|'
                if c == '|' and adj(grid, (y,x)).count('#') >= 3:
                    nc = '#'
                if c == '#' and adj(grid, (y,x)).count('#') >= 1 and adj(grid, (y,x)).count('|') >= 1:
                    nc = '#'
                elif c == '#':
                    nc = '.'
                #print(c,nc)
                ngrow.append(nc)

            newgrid.append(ngrow)
        #print(i)
        #printgrid(newgrid)
        #print('')

        # FAST FORWARD
        if i < 100000 and mkhash(newgrid) in grids and i < 100000:
            interval = i - grids[tuple(newgrid)]
            i += ((1000000000 - i) / interval) * interval
        elif i < 100000:
            grids[tuple(newgrid)] = i
        grid = newgrid
        i += 1

    tc = 0
    lc = 0
    for row in grid:
        for c in row:
            if c == '|':
                tc += 1
            elif c == '#':
                lc += 1
    print(tc * lc)



if __name__ == "__main__":
    main()
