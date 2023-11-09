#!/usr/bin/python

import sys
import re
import queue

from utils import *

def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 9)

    preamble_length = 25

    data = []
    for l in lines:
        data.append(int(l))


    break_val = 0
    for i, d in enumerate(data):
        if i < preamble_length:
            continue
        match = False
        for j in range(preamble_length):
            for k in range(preamble_length):
                if i != k and data[i-(j+1)] + data[i-(k+1)] == d:
                    match = True
        if not match:
            print(i, d)
            break_val = d
            break


    for i, d in enumerate(data):
        j = 2
        while sum(data[i:i+j]) <= break_val:
            if sum(data[i:i+j]) == break_val:
                print(i, j)
                print(max(data[i:i+j]) + min(data[i:i+j]))
            j += 1



if __name__ == "__main__":
    main()
