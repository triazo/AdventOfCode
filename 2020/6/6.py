#!/usr/bin/python

import sys
import re
import queue

from utils import *

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 6)

    groups = []
    curgroup = []
    nextone = True
    for l in lines:
        if l == "":
            print(len(curgroup))
            groups.append(curgroup)
            curgroup = []
            nextone = True
            continue
        if nextone:
            curgroup = list([letter for letter in l])
            print(curgroup)
            nextone = False
        else:
            #curgroup = intersection(curgroup, list(l))
            #curgroup = list([letter for letter in l if letter in curgroup])
            newgroup = []
            for letter in l:
                if letter in curgroup:
                    newgroup.append(letter)
            curgroup = newgroup
        print(curgroup)

    groups.append(curgroup)

    print(sum(len(l) for l in groups))

if __name__ == "__main__":
    main()
