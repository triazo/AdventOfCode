#!/usr/bin/python

import sys
import re
import queue

from utils import *

def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 14)

    mask = "X"*36
    memory = {}

    for l in lines:
        command = l.split(' ')[0].split('[')[0]
        operand = l.split('=')[1].strip()
        arg = ""
        if command == "mem":
            arg = int(l.split('[')[1].split(']')[0])

        #print(command, arg, operand)

        if command == "mask":
            mask = operand
            print(mask.count("X"))
            continue

        if command == "mem":
            bitmask = int(mask.replace("0", "1").replace("X", "0"), 2)
            bitand = int(mask.replace("X", "0"), 2)

            bitshifts = list(reversed([(len(mask))-1 - i for i, x in enumerate(mask) if x == "X"]))
            print(mask, bitshifts)
            for i in range(2**len(bitshifts)):
                address = arg & bitmask | bitand
                mask2 = 0
                for j in range(len(bitshifts)):
                    bit = (i & (1<<j)) >> j
                    mask2 |= (bit << bitshifts[j])

                address |= mask2d
                memory[address] = int(operand)
                print("mask, address, result ", mask2, address, memory[address])

    print(sum(memory[i] for i in memory))

if __name__ == "__main__":
    main()
