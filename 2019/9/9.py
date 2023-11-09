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

def get_param(mem, i, mode, relative_base):
    addr = get_addr(mem, i, mode, relative_base)
    if not addr in mem:
        mem[addr] = 0
    return mem[addr]

def get_addr(mem, i, mode, relative_base):
    addr = {
        0: mem[i],
        1: i,
        2: mem[i] + relative_base
    }
    return addr[mode]

def run(o, inputs, state = None):
    i = 0
    if state == None:
        mem = dict(o)
    else:
        mem = state[1]
        i = state[0]
    input_index = 0
    output_value = None
    relative_base = 0
    while True:
        op = mem[i]
        opcode = mem[i]%100
        modes = [int(m) for m in reversed(("00000000000"+str(op))[:-2])]
        #print(i, op, opcode, modes, [mem[ii] for ii in range(i, i+4)])
        if opcode == 1: #add
            o1 = get_param(mem, i+1, modes[0], relative_base)
            o2 = get_param(mem, i+2, modes[1], relative_base)
            mem[get_addr(mem, i+3, modes[2], relative_base)] = o1 + o2
            if modes[2] == 1:
                print("mode error")
            #print(o1, o2, mem[mem[i+3]])
            i += 4
        elif opcode == 2: # mul
            o1 = get_param(mem, i+1, modes[0], relative_base)
            o2 = get_param(mem, i+2, modes[1], relative_base)
            mem[get_addr(mem, i+3, modes[2], relative_base)] = o1 * o2
            if modes[2] == 1:
                print("mode error")
            i += 4
        elif opcode == 3: #input
            addr = get_addr(mem, i+3, modes[2], relative_base)
            mem[addr] = inputs[input_index]
            input_index += 1
            i += 2
        elif opcode == 4: #output
            o1 = get_param(mem, i+1, modes[0], relative_base)
            #print(o1)
            output_value = o1
            print(output_value)
            #return((output_value, (i+2, mem), relative_base))
            i += 2
        elif opcode == 5: # jump if not zero
            o1 = get_param(mem, i+1, modes[0], relative_base)
            o2 = get_param(mem, i+2, modes[1], relative_base)
            if o1 != 0:
                i = o2
            else:
                i += 3
        elif opcode == 6: #jump if zero
            o1 = get_param(mem, i+1, modes[0], relative_base)
            o2 = get_param(mem, i+2, modes[1], relative_base)
            if o1 == 0:
                i = o2
            else:
                i += 3
        elif opcode == 7: # test less than
            o1 = get_param(mem, i+1, modes[0], relative_base)
            o2 = get_param(mem, i+2, modes[1], relative_base)
            addr = get_addr(mem, i+3, modes[2], relative_base)
            if o1 < o2:
                mem[addr] = 1
            else:
                mem[addr] = 0
            i += 4
        elif opcode == 8: # test equal
            o1 = get_param(mem, i+1, modes[0], relative_base)
            o2 = get_param(mem, i+2, modes[1], relative_base)
            if o1 == o2:
                mem[mem[i+3]] = 1
            else:
                mem[mem[i+3]] = 0
            i += 4
        elif opcode == 9: # set relative_base
            o1 = get_param(mem, i+1, modes[0], relative_base)
            relative_base += o1
            i += 2
        elif op == 99:
            break
        else:
            print("bad op: %d"%op)
            sys.exit(1)


    return None


def main():

    sys.setrecursionlimit(2200)

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split(',')

    ops = {i: int(x) for i, x in enumerate(lines)}

    output = run(ops, [2])
    # while output:
    #     print(output[0])
    #     output = run(ops, [], output[1])


if __name__ == "__main__":
    main()
