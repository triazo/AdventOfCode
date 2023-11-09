#!/usr/bin/python

import sys
import re
import queue

from utils import *

def test_terminate(lines):
    ip = 0
    accumulator = 0

    terminated = False

    executed_instructions = {}

    while ip < len(lines):
        l = lines[ip]
        inst = l.split(' ')[0]
        arg = int(l.split(' ')[1])

        if ip in executed_instructions:
            #print(accumulator)

            return 0

        executed_instructions[ip] = ""

        #print(inst, arg)

        if inst == "acc":
            accumulator += arg
        elif inst == "jmp":
            ip += arg
            continue
        elif inst == "nop":
            pass

        ip += 1

    if ip == len(lines):
        return accumulator
    return 0


def main():

    sys.setrecursionlimit(2200)

    lines = getlines(2020, 8)

    for i, l in enumerate(lines):
        # Create new line set with instructions replaced
        newlines = []
        for j, l2 in enumerate(lines):
            if i == j:
                newlines.append(l2.replace("jmp", "xxx").replace("nop", "jmp").replace("xxx", "nop"))
            else:
                newlines.append(l2)

        res = test_terminate(newlines)
        if res != 0:
            print(res)






if __name__ == "__main__":
    main()
