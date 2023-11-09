#!/usr/bin/python

import sys
import re
import queue

from utils import *

def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 15)

    starting_numbers = lines[0].split(',')

    history = {}
    turn = 1
    mrn = 0
    for sn in starting_numbers:
        n = int(sn)
        print(turn, n)
        if not mrn in history:
            history[mrn] = []
        history[mrn] = turn
        turn += 1
        print("adding %d to history at %d"%(turn-1, mrn))
        mrn = n

    while turn < 30000001:

        if not mrn in history:
            n = 0
        else:
            n = (turn) - history[mrn]
        if not mrn in history:
            history[mrn] = []
        history[mrn] = turn

        #print("turn, recent, said", turn, mrn, n)


        turn += 1
        mrn = n

        if turn % 1000 == 0:
            sys.stdout.write('%d\r'%turn)

    for i in range(12):
        print("stuff")
    print(mrn)


if __name__ == "__main__":
    main()
