#!/usr/bin/python

import sys
import math

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

width = 700
height = 700

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
            sum = 0
            for point in points:
                sum += abs(i - point[0]) + abs(j - point[1])
            grid[i].append(sum)

    # for i in range(height):
    #     print(''.join([alphabet[points.index(grid[j][i][1])] if grid[j][i][1] != (0,0) else '.' for j in range(width) ]))

    total = 0
    for i in range(width):
        for j in range(height):
            if grid[i][j] < 10000:
                total += 1
    print(total)

if __name__ == "__main__":
    main()
