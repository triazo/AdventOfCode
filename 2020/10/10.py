#!/usr/bin/python

import sys
import re
import queue

from utils import *

def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 10)

    adapters = list([int(i) for i in lines])

    # current = 0
    # differences = [0, 0, 0, 1]
    # while len(adapters) > 0:
    #     nexta = min(adapters)
    #     adapters.remove(nexta)
    #     print(nexta, nexta-current)
    #     differences[nexta-current] += 1
    #     current = nexta

    # print(current, nexta)
    # print(differences)
    # print(differences[1] * differences[3])


    number_of_ways = {0: 1}
    for a in sorted(adapters):
        total = 0
        for i in range(1,4):
            if a-i in number_of_ways:
                total += number_of_ways[a-i]
        number_of_ways[a] = total
        print(a, total)
    print(number_of_ways[max(adapters)])




if __name__ == "__main__":
    main()
