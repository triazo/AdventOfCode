#!/usr/bin/python

import sys
import re
import queue
import itertools

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Works better with negatives
def mod(num, length):
    if num < 0:
        return num + length
    return num % length

def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def run(o, inputs, state = None):
    i = 0
    if state == None:
        mem = [x for x in o]
    else:
        mem = state[1]
        i = state[0]
    input_index = 0
    output_value = None
    while True:
        op = mem[i]
        opcode = mem[i]%100
        modes = [int(m) for m in reversed(("00000"+str(op))[:-2])]
        #print(i, op, opcode, modes, mem[i:i+4])
        if opcode == 1:
            o1 = mem[i+1] if modes[0] == 1 else mem[mem[i+1]]
            o2 = mem[i+2] if modes[1] == 1 else mem[mem[i+2]]
            mem[mem[i+3]] = o1 + o2
            if modes[2] == 1:
                print("mode error")
            #print(o1, o2, mem[mem[i+3]])
            i += 4
        elif opcode == 2:
            o1 = mem[i+1] if modes[0] == 1 else mem[mem[i+1]]
            o2 = mem[i+2] if modes[1] == 1 else mem[mem[i+2]]
            mem[mem[i+3]] = o1 * o2
            if modes[2] == 1:
                print("mode error")
            i += 4
        elif opcode == 3:
            # input
            mem[mem[i+1]] = inputs[input_index]
            input_index += 1
            i += 2
        elif opcode == 4:
            # output
            o1 = mem[i+1] if modes[0] == 1 else mem[mem[i+1]]
            #print(o1)
            output_value = o1
            return((output_value, (i+2, mem)))
            #i += 2
        elif opcode == 5:
            o1 = mem[i+1] if modes[0] == 1 else mem[mem[i+1]]
            o2 = mem[i+2] if modes[1] == 1 else mem[mem[i+2]]
            if o1 != 0:
                i = o2
            else:
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
                mem[mem[i+3]] = 1
            else:
                mem[mem[i+3]] = 0
            i += 4
        elif op == 99:
            break
        else:
            sys.exit(1)
            print("bad op: %d"%op)


    return None

def main():

    sys.setrecursionlimit(2200)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split(',')

    ops = [int(x) for x in lines]

    max_output = 0
    max_permutation = []
    for permutation in itertools.permutations(range(5, 10)):
        # init
        amps = [None, None, None, None, None]
        signal = 0
        for i in range(5):
            output, state = run(ops, [permutation[i], signal])
            amps[i] = state
            signal = output

        # loop
        i = 0
        while True:
            out = run(ops, [signal], amps[i%5])
            if out == None:
                break
            output, state = out
            amps[i%5] = state
            signal = output
            i += 1

        output = signal
        print("perm %s resulted in output %d"%(permutation, signal))
        if output > max_output:
            max_output = output
            max_permutation = permutation

    print(max_output, max_permutation)


if __name__ == "__main__":
    main()
