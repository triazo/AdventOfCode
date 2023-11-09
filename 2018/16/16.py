#!/usr/bin/python

import sys
import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def mod(num, length):
    if num < 0:
        return num + length
    return num % length



def main():

    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.read().split('\n')[:-1]

    names = ["addr", "addi", "mulr", "muli",
             "banr", "bani", "borr", "bori",
             "setr", "seti", "gtir", "gtri",
             "gtrr", "eqir", "eqri", "eqrr"]

    ops = [
        # add
        lambda a, b, r: r[a] + r[b],
        lambda a, b, r: r[a] + b,

        # mul
        lambda a, b, r: r[a] * r[b],
        lambda a, b, r: r[a] * b,

        # AND
        lambda a, b, r: r[a] & r[b],
        lambda a, b, r: r[a] & b,

        # OR
        lambda a, b, r: r[a] | r[b],
        lambda a, b, r: r[a] | b,

        # set
        lambda a, b, r: r[a],
        lambda a, b, r: a,

        # gt
        lambda a, b, r: int(a > r[b]),
        lambda a, b, r: int(r[a] > b),
        lambda a, b, r: int(r[a] > r[b]),

        # eq
        lambda a, b, r: int(a == r[b]),
        lambda a, b, r: int(r[a] == b),
        lambda a, b, r: int(r[a] == r[b]),
    ]

    opcodes = {}
    for i in range(len(ops)):
        opcodes[i] = {j for j in range(len(ops))}

    counter = 0
    for i in range(0, len(lines), 4):
        if len(lines[i]) == 0:
            break

        regexBefore = r'Before: \[(.*), (.*), (.*), (.*)\]'
        rb = [int(c) for c in re.search(regexBefore, lines[i]).groups()]

        regexAfter = r'After:  \[(.*), (.*), (.*), (.*)\]'
        ra = [int(c) for c in re.search(regexAfter, lines[i+2]).groups()]

        instruction = [int(c) for c in lines[i+1].split(' ')]

        workedas = set({})
        #print(instruction)
        for i, op in enumerate(ops):
            rtest = [v for v in rb]
            rtest[instruction[3]] = op(instruction[1], instruction[2], rb)
            #print(names[i], rb, rtest, ra)
            if rtest == ra:
                workedas.add(i)


        #print(instruction[0], workedas, workedas.intersection(opcodes[instruction[0]]))
        opcodes[instruction[0]] = workedas.intersection(opcodes[instruction[0]])


        #print("behaved as %d" % thiscount)
        # if thiscount == 1:
        #     opcodes[instruction[0]] = workedas

    for o in opcodes:
        print(o, opcodes[o])

    opcs = {}
    for i in range(len(ops)):
        for o in opcodes:
            if len(opcodes[o]) == 1:
                opcs[o] = opcodes[o].pop()
                del opcodes[o]
                for op in opcodes:
                    opcodes[op].discard(opcs[o])
                break

    print(opcs)

    #opcodes = {o: opcodes[o] for o in opcodes if len(opcodes[o]) == 1}

    plines = []
    with open(sys.argv[2], 'r') as f:
        plines = f.read().split('\n')[:-1]

    registers = [0, 0, 0, 0]
    for line in plines:
        instruction = [int(c) for c in line.split(' ')]
        print(instruction)
        registers[instruction[3]] = ops[opcs[instruction[0]]](instruction[1], instruction[2], registers)
    print(registers)


if __name__ == "__main__":
    main()
