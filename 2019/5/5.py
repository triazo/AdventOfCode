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

def run(o):
    mem = [x for x in o]
    i = 0
    while True:
        op = mem[i]
        opcode = mem[i]%100
        modes = [int(m) for m in reversed(("00000"+str(op))[:-2])]
        print(i, op, opcode, modes, mem[i:i+4])
        if opcode == 1:
            o1 = mem[i+1] if modes[0] == 1 else mem[mem[i+1]]
            o2 = mem[i+2] if modes[1] == 1 else mem[mem[i+2]]
            mem[mem[i+3]] = o1 + o2
            if modes[2] == 1:
                print("Mode error")
            #print(o1, o2, mem[mem[i+3]])
            i += 4
        elif opcode == 2:
            o1 = mem[i+1] if modes[0] == 1 else mem[mem[i+1]]
            o2 = mem[i+2] if modes[1] == 1 else mem[mem[i+2]]
            mem[mem[i+3]] = o1 * o2
            if modes[2] == 1:
                print("Mode error")
            i += 4
        elif opcode == 3:
            # input
            mem[mem[i+1]] = int(input())
            i += 2
        elif opcode == 4:
            # output
            o1 = mem[i+1] if modes[0] == 1 else mem[mem[i+1]]
            print(o1) # ignores mode but has no side effects
            i += 2
        elif opcode == 5:
            o1 = mem[i+1] if modes[0] == 1 else mem[mem[i+1]]
            o2 = mem[i+2] if modes[1] == 1 else mem[mem[i+2]]
            if o1 != 0:
                print("%d does not equal 0, jumping to %d"%(o1,o2))
                i = o2
            else:
                print("%d equals 0, not jumping to %d"%(o1,o2))
                i += 3
        elif opcode == 6:
            o1 = mem[i+1] if modes[0] == 1 else mem[mem[i+1]]
            o2 = mem[i+2] if modes[1] == 1 else mem[mem[i+2]]
            if o1 == 0:
                i = o2
            else:
                i += 3
        elif opcode == 7:
            o1 = mem[i+1] if modes[0] == 1 else mem[mem[i+1]]
            o2 = mem[i+2] if modes[1] == 1 else mem[mem[i+2]]
            if o1 < o2:
                mem[mem[i+3]] = 1
            else:
                mem[mem[i+3]] = 0
            i += 4
        elif opcode == 8:
            o1 = mem[i+1] if modes[0] == 1 else mem[mem[i+1]]
            o2 = mem[i+2] if modes[1] == 1 else mem[mem[i+2]]
            if o1 == o2:
                print("%d equals %d"%(o1,o2))
                mem[mem[i+3]] = 1
            else:
                print("%d does not equal %d"%(o1,o2))
                mem[mem[i+3]] = 0
            i += 4


        elif op == 99:
            break
        else:
            sys.exit(1)
            print("bad op: %d"%op)


    return mem[0]


def main():

    sys.setrecursionlimit(2200)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split(',')

    ops = [int(x) for x in lines]


    result = run(ops)


if __name__ == "__main__":
    main()
