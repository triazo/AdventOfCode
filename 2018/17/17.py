#!/usr/bin/python

import sys
import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def mod(num, length):
    if num < 0:
        return num + length
    return num % length


def printgrid(g):
    print(printgrid.minx)
    for y in range(len(g)):
        print(''.join(g[y][printgrid.minx:]))

def makegrid(lines):
    rx = r'(.)=(.+), (.)=(.+)\.\.(.+)'
    # find bounds
    maxx = 0
    minx = 999999
    maxy = 0
    for line in lines:
        wall = re.search(rx, line).groups()
        if wall[0] == 'x':
            if int(wall[1]) > maxx:
                maxx = int(wall[1])
            if int(wall[1]) < minx:
                minx = int(wall[1])
            if int(wall[4]) > maxy:
                maxy = int(wall[4])
        elif wall[0] == 'y':
            if int(wall[1]) > maxy:
                maxy = int(wall[1])
            if int(wall[4]) > maxx:
                maxx = int(wall[4])

    printgrid.minx = minx - 40
    print(maxx, maxy)
    # make blank array (of sand?)
    # g = 'grid', 'ground', doesn't matter
    g = []
    for y in range(maxy + 1):
        g.append([])
        for x in range(maxx + 4):
            g[y].append('.')


    for line in lines:
        w = re.search(rx, line).groups()
        wall = (w[0], int(w[1]), w[2], int(w[3]), int(w[4]))
        filledin = 0
        if wall[0] == 'x':
            for y in range(wall[3], wall[4] + 1):
                #print(y, wall[1])
                filledin += 1
                g[y][wall[1]] = '#'
        elif wall[0] == 'y':
            for x in range(wall[3], wall[4] + 1):
                filledin += 1
                g[wall[1]][x] = '#'
        #print("line %s filled in %d tiles" %(line, filledin))
    return g

def waterdown(g, start):
    y = start[0]
    x = start[1]
    # keep adding active waters '|' until you hit an obsticle. recurse back up the chain
    while g[y][x] != '#' and g[y][x] != '~':
        g[y][x] = '|'
        y += 1
        if y >= len(g):
            return 0

    y -= 1
    # hit ground or a water table
    result = wateracross(g, (y, x))
    while g[y][x] == '~':
        y -= 1
        result += wateracross(g, (y, x))

    return result

def wateracross(g, start):

    y = start[0]
    # search left
    xl = start[1]
    while g[y][xl] != '#' and g[y+1][xl] != '.' and g[y+1][xl] != '|':
        g[y][xl] = '|'
        xl -= 1

    # search right
    xr = start[1]
    try:
        while g[y][xr] != '#' and g[y+1][xr] != '.' and g[y+1][xr] != '|':
            g[y][xr] = '|'
            xr += 1
            #print(len(g), len(g[0]),  y, xr)
    except Exception as e:
        printgrid(g)
        sys.exit(1)

    leftcount = 0
    if g[y+1][xl] == '.':
        leftcount = waterdown(g, (y, xl))

    rightcount = 0
    if g[y+1][xr] == '.':
        rightcount = waterdown(g, (y, xr))

    if g[y][xl] == '#' and g[y][xr] == '#':
        for x in range(xl + 1, xr):
            g[y][x] = '~'

        #print("made %d still"% ((xr - xl) - 1))
        return (xr - xl) - 1

    return rightcount + leftcount

def main():

    sys.setrecursionlimit(2000)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]

    g = makegrid(lines)
    printgrid(g)

    result = waterdown(g, (0, 500))
    print(result)

    result = 0
    hitone = False
    for l in g:
        if not '#' in l and not hitone:
            continue
        hitone = True
        result += l.count('|')
        result += l.count('~')
    printgrid(g)
    print(result)
    result2 = 0
    for l in g:
        result2 += l.count('~')

    print(result2)




if __name__ == "__main__":
    main()
