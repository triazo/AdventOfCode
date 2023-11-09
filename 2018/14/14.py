#!/usr/bin/python

import sys
import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def mod(num, length):
    if num < 0:
        return num + length
    return num % length

def main():

    # lines = []
    # with open(sys.argv[1], 'r') as f:
    #     lines = f.read().split('\n')[:-1]
    numrecipes = int(sys.argv[1])

    rs=[3, 7]
    elves = [0, 1]

    while True:
        #for t in xrange(10**(len(sys.argv[1])+2)):
        nr = 0
        for e in elves:
            nr += rs[e]

        for d in [int(c) for c in str(nr)]:
            rs.append(d)

        for i, e in enumerate(elves):
            elves[i] = (e + rs[e] + 1) % len(rs)

        if ''.join(chr(c) for c in rs[-6:]) == sys.argv[1]:
            print(len(rs) - 6)
            break

        # print(rs)
        # if len(rs) >= numrecipes:
        #     print("Reached the cutoff point")
    #print(''.join(str(c) for c in rs[numrecipes:numrecipes+10]))
    #print(''.join(str(c) for c in rs).index(sys.argv[1]))
if __name__ == "__main__":
    main()


# on tin:
#█▒triazo@tin▓▒░~/▓▒░% time /tmp/14.py 165061
#5992684592
#20181148
#/tmp/14.py 165061  161.75s user 0.46s system 99% cpu 2:42.23 total
