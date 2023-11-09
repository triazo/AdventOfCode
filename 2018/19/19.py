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

    ops = {
        # add
        "addr": lambda a, b, r: r[a] + r[b],
        "addi": lambda a, b, r: r[a] + b,

        # mul
        "mulr": lambda a, b, r: r[a] * r[b],
        "muli": lambda a, b, r: r[a] * b,

        # AND
        "banr": lambda a, b, r: r[a] & r[b],
        "bani": lambda a, b, r: r[a] & b,

        # OR
        "borr": lambda a, b, r: r[a] | r[b],
        "bori": lambda a, b, r: r[a] | b,

        # set
        "setr": lambda a, b, r: r[a],
        "seti": lambda a, b, r: a,

        # gt
        "gtir": lambda a, b, r: int(a > r[b]),
        "gtri": lambda a, b, r: int(r[a] > b),
        "gtrr": lambda a, b, r: int(r[a] > r[b]),

        # eq
        "eqir": lambda a, b, r: int(a == r[b]),
        "eqri": lambda a, b, r: int(r[a] == b),
        "eqrr": lambda a, b, r: int(r[a] == r[b]),
    }

    #ops = {names[i]: ops[i] for i in range(len(ops))}

    #registers


    program = []

    for line in lines[1:]:
        rx = r'(.+) (.+) (.+) (.+)'
        opcode, a, b, c = re.search(rx, line).groups()
        a = int(a)
        b = int(b)
        c = int(c)

        program.append((opcode, a, b, c))


    r = [1, 0, 0, 0, 0, 0]
    ip = 0
    ipr = 5

    clock = 0
    while True:
        clock += 1
        if clock % 1 == 0:
            print r
            print clock
        r[ipr] = ip
        if ip < 0 or ip >= len(program):
            break
        i = program[ip]
        #print(ip, i)
        #print(ops[i[0]](i[1], i[2], r))
        r[i[3]] = ops[i[0]](i[1], i[2], r)

        ip = r[ipr]
        ip += 1
        #print(r)

    print(r[0])


if __name__ == "__main__":
    main()
