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

    width = 6
    height = 25

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]

    img = lines[0]
    layer_size = width * height
    layers = []
    for l in range(len(img) / layer_size):
        layers.append([])
        for x in range(width):
            layers[l].append([])
            for y in range(height):
                layers[l][x].append(img[l * layer_size + x * height + y])

    # l0 = layer_size
    # l0_layer = []
    # for l in layers:
    #     zero_count = 0
    #     for row in l:
    #         for i in row:
    #             if i == '0':
    #                 zero_count += 1
    #     if zero_count < l0:
    #         l0 = zero_count
    #         l0_layer = l

    # print(l0_layer)
    # one_count = 0
    # two_count = 0
    # for row in l0_layer:
    #     for i in row:
    #         if i == '1':
    #             one_count += 1
    #         if i == '2':
    #     one_count += 1

    final_image = []
    for x in range(width):
        final_image.append([])
        for y in range(height):
            final_image[x].append('2')

    for l in layers:
        for x, row in enumerate(l):
            for y, c in enumerate(row):
                if final_image[x][y] == '2':
                    final_image[x][y] = c

    for row in final_image:
        for c in row:
            sys.stdout.write('#' if c == '1' else ' ')
        sys.stdout.write('\n')



if __name__ == "__main__":
    main()
