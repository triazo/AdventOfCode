#!/usr/bin/python

import sys
import math

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

width = 500
height = 500

def main():
    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]

    points = [(int(l.split()[0][:-1]),int(l.split()[1])) for l in lines]

    print(points)

    grid = []
    counter = 0
    for i in range(width):
        grid.append([])
        for j in range(height):
            counter += 1
            if counter % 100000 == 0:
                print(counter)
            grid[i].append((4001, (9999, 9999)))
            for point in points:
                distance = abs(i - point[0]) + abs(j - point[1])
                if distance < grid[i][j][0]:
                    grid[i][j] = (distance, (point))
            for point in points:
                distance = abs(i - point[0]) + abs(j - point[1])
                if distance == grid[i][j][0] and grid[i][j][1] != point:
                    grid[i][j] = (0, (0,0))

    # for i in range(height):
    #     print(''.join([alphabet[points.index(grid[j][i][1])] if grid[j][i][1] != (0,0) else '.' for j in range(width) ]))



    areas = {}
    for i in range(width):
        for j in range(height):
            if not grid[i][j][1] in areas:
                areas[grid[i][j][1]] = 0
            areas[grid[i][j][1]] += 1


    for i in range(width):
        if grid[i][height-1][1] in areas:
            del areas[grid[i][height-1][1]]
    for j in range(height):
        if grid[height-1][j][1] in areas:
            del areas[grid[height-1][j][1]]

    for i in range(width):
        if grid[i][0][1] in areas:
            del areas[grid[i][0][1]]
    for j in range(height):
        if grid[0][j][1] in areas:
            del areas[grid[0][j][1]]

    totals = sorted([(areas[k], k) for k in areas])


    print(totals)

if __name__ == "__main__":
    main()
