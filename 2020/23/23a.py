#!/usr/bin/python

import sys
import re
import queue
import collections

from utils import *

def remove_cups(l, n, index):
    if index+3 >= len(l):
        end = index + 3 - len(l)
        return (l[end:index], l[index:] + l[:end])
    return (l[:index] + l[index+3:], l[index:index+3])

def get_dest_cup(l, current):
    ltl = list([i for i in l if i < current])
    if len(ltl) == 0:
        return max(l)
    return max(ltl)


def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 23)

    cups = list(int(c) for c in lines[0])
    print(cups)


    current_cup = cups[0]

    for round in range(100):
        cups, remaining = remove_cups(cups, 3, cups.index(current_cup)+1)
        dest_cup = get_dest_cup(cups, current_cup)

        dest_index = cups.index(dest_cup)
        for i in reversed(remaining):
            cups.insert(dest_index + 1, i)

        current_cup = cups[(cups.index(current_cup) + 1)%len(cups)]

        print(cups)

    finalindex = 0
    while cups[finalindex] != 1:
        finalindex += 1

    for i in range(len(cups)-1):
        sys.stdout.write(str(cups[(i + finalindex + 1)%len(cups)]))
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
